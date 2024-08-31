"""Utility functions for the component docs page."""

import inspect
import os
import re
import textwrap
from typing import Any
from typing import Literal
from typing import Union
from typing import _GenericAlias
from typing import get_args
from typing import get_origin

import flexdown
import reflex as rx
from reflex.base import Base
from reflex.components.base.fragment import Fragment
from reflex.components.component import Component
from reflex.components.radix.primitives.base import RadixPrimitiveComponent
from reflex.components.radix.themes.base import RadixThemesComponent

from pcweb.flexdown import markdown
from pcweb.flexdown import xd
from pcweb.styles.colors import c_color
from pcweb.styles.fonts import base
from pcweb.styles.fonts import large
from pcweb.styles.fonts import small
from pcweb.styles.shadows import shadows
from pcweb.templates.docpage import docdemobox
from pcweb.templates.docpage import docpage
from pcweb.templates.docpage import get_toc
from pcweb.templates.docpage import h1_comp
from pcweb.templates.docpage import h2_comp


def get_code_style(color: str):
    return {
        "color": rx.color(color, 11),
        "border_radius": "4px",
        "border": f"1px solid {rx.color(color, 5)}",
        "background": rx.color(color, 3),
    }


class Prop(Base):
    """Hold information about a prop."""

    # The name of the prop.
    name: str

    # The type of the prop.
    type_: Any

    # The description of the prop.
    description: str

    # The default value of the prop.
    default_value: str


from reflex.components.el.elements.base import BaseHTML


def get_default_value(lines: list[str], start_index: int) -> str:
    """Process lines of code to get the value of a prop, handling multi-line values.

    Args:
        lines: The lines of code to process.
        start_index: The index of the line where the prop is defined.

    Returns:
        The default value of the prop.
    """
    # Check for the default value in the prop comment (Default: )
    # Need to update the components comments in order to get the default value
    if start_index > 0:
        comment_line = lines[start_index - 1].strip()
        if comment_line.startswith("#"):
            default_match = re.search(r'Default:\s*(["\']?\w+["\']?|\w+)', comment_line)
            if default_match:
                default_value = default_match.group(1)
                return default_value

    # Get the initial line
    line = lines[start_index]
    parts = line.split("=", 1)
    if len(parts) != 2:
        return ""
    value = parts[1].strip()

    # Check if the value is complete
    open_brackets = value.count("{") - value.count("}")
    open_parentheses = value.count("(") - value.count(")")

    # If brackets or parentheses are not balanced, collect more lines
    current_index = start_index + 1
    while (open_brackets > 0 or open_parentheses > 0) and current_index < len(lines):
        next_line = lines[current_index].strip()
        value += " " + next_line
        open_brackets += next_line.count("{") - next_line.count("}")
        open_parentheses += next_line.count("(") - next_line.count(")")
        current_index += 1

    # Remove any trailing comments
    value = re.split(r"\s+#", value)[0].strip()

    # Process Var.create_safe within dictionary
    def process_var_create_safe(match):
        content = match.group(1)
        # Extract only the first argument
        first_arg = re.split(r",", content)[0].strip()
        return first_arg

    value = re.sub(r"Var\.create_safe\((.*?)\)", process_var_create_safe, value)
    value = re.sub(r"\bColor\s*\(", "rx.color(", value)

    return value.strip()


class Source(Base):
    """Parse the source code of a component."""

    # The component to parse.
    component: type[Component]

    # The source code.
    code: list[str] = []

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the source code parser."""
        super().__init__(*args, **kwargs)

        # Get the source code.
        self.code = [
            line
            for line in inspect.getsource(self.component).splitlines()
            if len(line) > 0
        ]

    def get_docs(self) -> str:
        """Get the docstring of the component.

        Returns:
            The docstring of the component.
        """
        return self.component.__doc__

    def get_props(self) -> list[Prop]:
        """Get a dictionary of the props and their descriptions.

        Returns:
            A dictionary of the props and their descriptions.
        """
        props = self._get_props()

        parent_cls = self.component.__bases__[0]
        if parent_cls not in (rx.Component, BaseHTML):
            props += Source(component=parent_cls).get_props()

        return props

    def _get_props(self) -> list[Prop]:
        """Get a dictionary of the props and their descriptions.

        Returns:
            A dictionary of the props and their descriptions.
        """
        out = []
        props = self.component.get_props()
        comments = []

        for i, line in enumerate(self.code):
            line = self.code[i]

            if re.search("def ", line):
                break

            if line.strip().startswith("#"):
                comments.append(line)
                continue

            match = re.search(r"\w+:", line)
            if match is None:
                continue

            prop = match.group(0).strip(":")
            if prop not in props:
                continue

            default_value = get_default_value(self.code, i)

            if i > 0:
                comment_above = self.code[i - 1].strip()
                assert comment_above.startswith(
                    "#",
                ), f"Expected comment, got {comment_above}"

            comment = Source.get_comment(comments)
            comments.clear()

            type_ = self.component.get_fields()[prop].outer_type_

            out.append(
                Prop(
                    name=prop,
                    type_=type_,
                    default_value=default_value,
                    description=comment,
                ),
            )

        return out

    @staticmethod
    def get_comment(comments: list[str]):
        return "".join([comment.strip().strip("#") for comment in comments])


# Mapping from types to colors.
TYPE_COLORS = {
    "int": "red",
    "float": "orange",
    "str": "yellow",
    "bool": "teal",
    "Component": "purple",
    "List": "blue",
    "Dict": "blue",
    "Tuple": "blue",
    "None": "gray",
    "Figure": "green",
    "Literal": "gray",
    "Union": "gray",
}

count = 0

import hashlib


def get_id(s):
    global count
    count += 1
    s = str(count)
    hash_object = hashlib.sha256(s.encode())
    hex_dig = hash_object.hexdigest()
    return "a_" + hex_dig[:8]


class PropDocsState(rx.State):
    """Container for dynamic vars used by the prop docs."""


EXCLUDED_COMPONENTS = [
    "Theme",
    "ThemePanel",
    "DrawerRoot",
    "DrawerTrigger",
    "DrawerOverlay",
    "DrawerPortal",
    "DrawerContent",
    "DrawerClose",
]


def render_select(prop, component, prop_dict):
    if (
        not rx.utils.types._issubclass(
            component,
            (RadixThemesComponent, RadixPrimitiveComponent),
        )
        or component.__name__ in EXCLUDED_COMPONENTS
    ):
        return rx.fragment()
    try:
        type_ = rx.utils.types.get_args(prop.type_)[0]
    except:
        return rx.fragment()

    try:
        if issubclass(type_, bool) and prop.name not in [
            "open",
            "checked",
            "as_child",
            "default_open",
            "default_checked",
        ]:
            name = get_id(f"{component.__qualname__}_{prop.name}")
            PropDocsState.add_var(name, bool, False)
            var = getattr(PropDocsState, name)
            setter = getattr(PropDocsState, f"set_{name}")
            prop_dict[prop.name] = var
            return rx.checkbox(
                var,
                on_change=setter,
            )
    except TypeError:
        pass

    if not isinstance(type_, _GenericAlias) or (
        type_.__origin__ not in (Literal, Union)
    ):
        return rx.fragment()
    # For the Union[Literal, Breakpoints] type
    if type_.__origin__ is Union:
        if not all(
            arg.__name__ in ["Literal", "Breakpoints"] for arg in type_.__args__
        ):
            return rx.fragment()
        # Get the literal values
        literal_values = [
            str(lit_arg)
            for arg in type_.__args__
            if get_origin(arg) is Literal
            for lit_arg in arg.__args__
        ]
        option = literal_values[0]
        name = get_id(f"{component.__qualname__}_{prop.name}")
        PropDocsState.add_var(name, str, option)
        var = getattr(PropDocsState, name)
        setter = getattr(PropDocsState, f"set_{name}")
        prop_dict[prop.name] = var
        return rx.select.root(
            rx.select.trigger(width="8em", style=small, color=c_color("slate", 11)),
            rx.select.content(
                rx.select.group(
                    *[
                        rx.select.item(item, value=item, style=small)
                        for item in literal_values
                    ],
                ),
            ),
            value=var,
            on_change=setter,
        )
    # Get the first option.
    option = type_.__args__[0]
    name = get_id(f"{component.__qualname__}_{prop.name}")
    PropDocsState.add_var(name, str, option)
    var = getattr(PropDocsState, name)
    setter = getattr(PropDocsState, f"set_{name}")
    prop_dict[prop.name] = var

    if prop.name == "color_scheme":
        return rx.popover.root(
            rx.popover.trigger(
                rx.box(
                    rx.button(
                        rx.text(var, style=small),
                        # Match the select.trigger svg icon
                        rx.html(
                            """<svg width="9" height="9" viewBox="0 0 9 9" fill="currentcolor" xmlns="http://www.w3.org/2000/svg" class="rt-SelectIcon" aria-hidden="true"><path d="M0.135232 3.15803C0.324102 2.95657 0.640521 2.94637 0.841971 3.13523L4.5 6.56464L8.158 3.13523C8.3595 2.94637 8.6759 2.95657 8.8648 3.15803C9.0536 3.35949 9.0434 3.67591 8.842 3.86477L4.84197 7.6148C4.64964 7.7951 4.35036 7.7951 4.15803 7.6148L0.158031 3.86477C-0.0434285 3.67591 -0.0536285 3.35949 0.135232 3.15803Z"></path></svg>""",
                        ),
                        color_scheme=var,
                        width="8em",
                        variant="surface",
                        justify_content="space-between",
                    ),
                ),
            ),
            rx.popover.content(
                rx.grid(
                    *[
                        rx.box(
                            rx.icon(
                                "check",
                                color=rx.color("gray", 12),
                                size=15,
                                position="absolute",
                                top="50%",
                                left="50%",
                                transform="translate(-50%, -50%)",
                                display=rx.cond(var == color, "block", "none"),
                            ),
                            width="30px",
                            height="30px",
                            border_radius="max(var(--radius-2), var(--radius-full))",
                            bg=f"var(--{color}-9)",
                            cursor="pointer",
                            position="relative",
                            flex_shrink=0,
                            on_click=PropDocsState.setvar(f"{name}", color),
                            border=rx.cond(
                                var == color,
                                "2px solid var(--gray-12)",
                                "",
                            ),
                        )
                        for color in list(map(str, type_.__args__))
                    ],
                    columns="6",
                    spacing="3",
                ),
            ),
        )
    return rx.select.root(
        rx.select.trigger(width="8em", style=small, color=c_color("slate", 11)),
        rx.select.content(
            rx.select.group(
                *[
                    rx.select.item(
                        item,
                        value=item,
                        style=small,
                        _hover=(
                            {"background": f"var(--{item}-9)"}
                            if prop.name == "color_scheme"
                            else None
                        ),
                    )
                    for item in list(map(str, type_.__args__))
                ],
            ),
        ),
        value=var,
        on_change=setter,
    )


def hovercard(trigger: rx.Component, content: rx.Component) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(
            trigger,
        ),
        rx.hover_card.content(
            content,
            side="top",
            align="center",
            color=c_color("slate", 9),
            style=small,
        ),
    )


def color_scheme_hovercard(literal_values: list[str]) -> rx.Component:
    return hovercard(
        rx.icon(tag="palette", size=15, color=c_color("slate", 9), flex_shrink=0),
        rx.grid(
            *[
                rx.tooltip(
                    rx.box(
                        width="30px",
                        height="30px",
                        border_radius="max(var(--radius-2), var(--radius-full))",
                        flex_shrink=0,
                        bg=f"var(--{color}-9)",
                    ),
                    content=color,
                    delay_duration=0,
                )
                for color in literal_values
            ],
            columns="6",
            spacing="3",
        ),
    )


def prop_docs(
    prop: Prop,
    prop_dict,
    component,
    is_interactive: bool,
) -> list[rx.Component]:
    """Generate the docs for a prop."""
    # Get the type of the prop.
    type_ = prop.type_
    if rx.utils.types._issubclass(prop.type_, rx.Var):
        # For vars, get the type of the var.
        type_ = rx.utils.types.get_args(type_)[0]

    origin = get_origin(type_)
    args = get_args(type_)

    literal_values = []  # Literal values of the prop
    all_types = []  # List for all the prop types
    MAX_PROP_VALUES = 3

    COMMON_TYPES = {}  # Used to exclude common types from the MAX_PROP_VALUES
    if origin is Union:
        non_literal_types = []  # List for all the non-literal types

        for arg in args:
            all_types.append(arg.__name__)
            if get_origin(arg) is Literal:
                literal_values.extend(str(lit_arg) for lit_arg in arg.__args__)
            elif arg.__name__ != "Breakpoints":  # Don't include Breakpoints
                non_literal_types.append(arg.__name__)

        if len(literal_values) < 10:
            literal_str = " | ".join(f'"{value}"' for value in literal_values)
            type_components = ([literal_str] if literal_str else []) + non_literal_types
            type_name = (
                " | ".join(type_components)
                if len(type_components) == 1
                else f"Union[{', '.join(type_components)}]"
            )
        else:
            type_name = (
                "Literal"
                if not non_literal_types
                else f"Union[Literal, {', '.join(non_literal_types)}]"
            )

    elif origin is dict:
        key_type = args[0].__name__ if args else "Any"
        value_type = args[1].__name__ if len(args) > 1 else "Any"
        type_name = f"Dict[{key_type}, {value_type}]"

    elif origin is Literal:
        literal_values = list(map(str, args))
        if len(literal_values) > MAX_PROP_VALUES and prop.name not in COMMON_TYPES:
            type_name = "Literal"
        else:
            type_name = " | ".join([f'"{value}"' for value in literal_values])

    else:
        type_name = type_.__name__

    # Get the default value.
    default_value = prop.default_value if prop.default_value is not None else "-"
    # Get the color of the prop.
    color = TYPE_COLORS.get(type_.__name__, "gray")
    # Return the docs for the prop.
    return [
        rx.table.cell(
            rx.hstack(
                rx.code(prop.name, text_wrap="nowrap", style=get_code_style("violet")),
                hovercard(
                    rx.icon(
                        tag="info",
                        size=15,
                        color=c_color("slate", 9),
                        flex_shrink=0,
                    ),
                    rx.text(prop.description, size="2"),
                ),
                spacing="2",
                align="center",
            ),
            padding_left="1em",
            justify="start",
        ),
        rx.table.cell(
            rx.hstack(
                rx.cond(
                    (len(literal_values) > 0) & (prop.name not in COMMON_TYPES),
                    rx.code(
                        (
                            " | ".join(
                                [f'"{v}"' for v in literal_values[:MAX_PROP_VALUES]]
                                + ["..."],
                            )
                            if len(literal_values) > MAX_PROP_VALUES
                            else type_name
                        ),
                        style=get_code_style(color),
                        text_wrap="nowrap",
                    ),
                    rx.code(
                        type_name,
                        style=get_code_style(color),
                        text_wrap="nowrap",
                    ),
                ),
                rx.cond(
                    len(literal_values) > MAX_PROP_VALUES
                    and prop.name not in COMMON_TYPES,
                    hovercard(
                        rx.icon(
                            tag="circle-ellipsis",
                            size=15,
                            color=c_color("slate", 9),
                            flex_shrink=0,
                        ),
                        rx.text(
                            " | ".join([f'"{v}"' for v in literal_values]),
                            size="2",
                        ),
                    ),
                ),
                rx.cond(
                    (origin == Union)
                    & (
                        "Breakpoints" in all_types
                    ),  # Display that the type is Union with Breakpoints
                    hovercard(
                        rx.icon(
                            tag="info",
                            size=15,
                            color=c_color("slate", 9),
                            flex_shrink=0,
                        ),
                        rx.text(f"Union[{', '.join(all_types)}]", size="2"),
                    ),
                ),
                rx.cond(
                    (prop.name == "color_scheme") | (prop.name == "accent_color"),
                    color_scheme_hovercard(literal_values),
                ),
                spacing="2",
                align="center",
            ),
            padding_left="1em",
            justify="start",
        ),
        rx.table.cell(
            rx.flex(
                rx.code(
                    default_value,
                    style=get_code_style(
                        (
                            "red"
                            if default_value == "False"
                            else "green" if default_value == "True" else "gray"
                        ),
                    ),
                    text_wrap="nowrap",
                ),
            ),
            padding_left="1em",
            justify="start",
        ),
        rx.cond(
            is_interactive,
            rx.table.cell(
                render_select(prop, component, prop_dict),
                padding_left="1em",
                justify="start",
            ),
            rx.fragment(),
        ),
    ]


EVENTS = {
    "on_focus": {
        "description": "Function or event handler called when the element (or some element inside of it) receives focus. For example, it is called when the user clicks on a text input.",
    },
    "on_blur": {
        "description": "Function or event handler called when focus has left the element (or left some element inside of it). For example, it is called when the user clicks outside of a focused text input.",
    },
    "on_change": {
        "description": "Function or event handler called when the value of an element has changed. For example, it is called when the user types into a text input each keystoke triggers the on change.",
    },
    "on_click": {
        "description": "Function or event handler called when the user clicks on an element. For example, it’s called when the user clicks on a button.",
    },
    "on_context_menu": {
        "description": "Function or event handler called when the user right-clicks on an element. For example, it is called when the user right-clicks on a button.",
    },
    "on_double_click": {
        "description": "Function or event handler called when the user double-clicks on an element. For example, it is called when the user double-clicks on a button.",
    },
    "on_mouse_up": {
        "description": "Function or event handler called when the user releases a mouse button on an element. For example, it is called when the user releases the left mouse button on a button.",
    },
    "on_mouse_down": {
        "description": "Function or event handler called when the user presses a mouse button on an element. For example, it is called when the user presses the left mouse button on a button.",
    },
    "on_mouse_enter": {
        "description": "Function or event handler called when the user’s mouse enters an element. For example, it is called when the user’s mouse enters a button.",
    },
    "on_mouse_leave": {
        "description": "Function or event handler called when the user’s mouse leaves an element. For example, it is called when the user’s mouse leaves a button.",
    },
    "on_mouse_move": {
        "description": "Function or event handler called when the user moves the mouse over an element. For example, it’s called when the user moves the mouse over a button.",
    },
    "on_mouse_out": {
        "description": "Function or event handler called when the user’s mouse leaves an element. For example, it is called when the user’s mouse leaves a button.",
    },
    "on_mouse_over": {
        "description": "Function or event handler called when the user’s mouse enters an element. For example, it is called when the user’s mouse enters a button.",
    },
    "on_scroll": {
        "description": "Function or event handler called when the user scrolls the page. For example, it is called when the user scrolls the page down.",
    },
    "on_submit": {
        "description": "Function or event handler called when the user submits a form. For example, it is called when the user clicks on a submit button.",
    },
    "on_cancel": {
        "description": "Function or event handler called when the user cancels a form. For example, it is called when the user clicks on a cancel button.",
    },
    "on_edit": {
        "description": "Function or event handler called when the user edits a form. For example, it is called when the user clicks on a edit button.",
    },
    "on_change_start": {
        "description": "Function or event handler called when the user starts selecting a new value(By dragging or clicking).",
    },
    "on_change_end": {
        "description": "Function or event handler called when the user is done selecting a new value(By dragging or clicking).",
    },
    "on_complete": {
        "description": "Called when the user completes a form. For example, it’s called when the user clicks on a complete button.",
    },
    "on_error": {
        "description": "The on_error event handler is called when the user encounters an error in a form. For example, it’s called when the user clicks on a error button.",
    },
    "on_load": {
        "description": "The on_load event handler is called when the user loads a form. For example, it is called when the user clicks on a load button.",
    },
    "on_esc": {
        "description": "The on_esc event handler is called when the user presses the escape key. For example, it is called when the user presses the escape key.",
    },
    "on_open": {
        "description": "The on_open event handler is called when the user opens a form. For example, it is called when the user clicks on a open button.",
    },
    "on_close": {
        "description": "The on_close event handler is called when the user closes a form. For example, it is called when the user clicks on a close button.",
    },
    "on_close_complete": {
        "description": "The on_close_complete event handler is called when the user closes a form. For example, it is called when the user clicks on a close complete button.",
    },
    "on_overlay_click": {
        "description": "The on_overlay_click event handler is called when the user clicks on an overlay. For example, it is called when the user clicks on a overlay button.",
    },
    "on_key_down": {
        "description": "The on_key_down event handler is called when the user presses a key.",
    },
    "on_key_up": {
        "description": "The on_key_up event handler is called when the user releases a key.",
    },
    "on_ready": {
        "description": "The on_ready event handler is called when the script is ready to be executed.",
    },
    "on_mount": {
        "description": "The on_mount event handler is called when the component is loaded on the page.",
    },
    "on_unmount": {
        "description": "The on_unmount event handler is called when the component is removed from the page. This handler is only called during navigation, not when the page is refreshed.",
    },
    "on_input": {
        "description": "The on_input event handler is called when the editor receives input from the user. It receives the raw browser event as an argument.",
    },
    "on_resize_editor": {
        "description": "The on_resize_editor event handler is called when the editor is resized. It receives the height and previous height as arguments.",
    },
    "on_copy": {
        "description": "The on_copy event handler is called when the user copies text from the editor. It receives the clipboard data as an argument.",
    },
    "on_cut": {
        "description": "The on_cut event handler is called when the user cuts text from the editor. It receives the clipboard data as an argument.",
    },
    "on_paste": {
        "description": "The on_paste event handler is called when the user pastes text into the editor. It receives the clipboard data and max character count as arguments.",
    },
    "toggle_code_view": {
        "description": "The toggle_code_view event handler is called when the user toggles code view. It receives a boolean whether code view is active.",
    },
    "toggle_full_screen": {
        "description": "The toggle_full_screen event handler is called when the user toggles full screen. It receives a boolean whether full screen is active.",
    },
    "on_cell_activated": {
        "description": "The on_cell_activated event handler is called when the user activate a cell from the data editor. It receive the coordinates of the cell.",
    },
    "on_cell_clicked": {
        "description": "The on_cell_clicked event handler is called when the user click on a cell of the data editor. It receive the coordinates of the cell.",
    },
    "on_cell_context_menu": {
        "description": "The on_cell_context_menu event handler is called when the user right-click on a cell of the data editor. It receives the coordinates of the cell.",
    },
    "on_cell_edited": {
        "description": "The on_cell_edited event handler is called when the user modify the content of a cell. It receives the coordinates of the cell and the modified content.",
    },
    "on_group_header_clicked": {
        "description": "The on_group_header_clicked event handler is called when the user left-click on a group header of the data editor. It receive the index and the data of the group header.",
    },
    "on_group_header_context_menu": {
        "description": "The on_group_header_context_menu event handler is called when the user right-click on a group header of the data editor. It receive the index and the data of the group header.",
    },
    "on_group_header_renamed": {
        "description": "The on_group_header_context_menu event handler is called when the user rename a group header of the data editor. It receive the index and the modified content of the group header.",
    },
    "on_header_clicked": {
        "description": "The on_header_clicked event handler is called when the user left-click a header of the data editor. It receive the index and the content of the header.",
    },
    "on_header_context_menu": {
        "description": "The on_header_context_menu event handler is called when the user right-click a header of the data editor. It receives the index and the content of the header. ",
    },
    "on_header_menu_click": {
        "description": "The on_header_menu_click event handler is called when the user click on the menu button of the header. (menu header not implemented yet)",
    },
    "on_item_hovered": {
        "description": "The on_item_hovered event handler is called when the user hover on an item of the data editor.",
    },
    "on_delete": {
        "description": "The on_delete event handler is called when the user delete a cell of the data editor.",
    },
    "on_finished_editing": {
        "description": "The on_finished_editing event handler is called when the user finish an editing, regardless of if the value changed or not.",
    },
    "on_row_appended": {
        "description": "The on_row_appended event handler is called when the user add a row to the data editor.",
    },
    "on_selection_cleared": {
        "description": "The on_selection_cleared event handler is called when the user unselect a region of the data editor.",
    },
    "on_column_resize": {
        "description": "The on_column_resize event handler is called when the user try to resize a column from the data editor.",
    },
    "on_open_change": {
        "description": "The on_open_change event handler is called when the open state of the component changes.",
    },
    "on_focus_outside": {
        "description": "The on_focus_outside event handler is called when the user focuses outside the component.",
    },
    "on_interact_outside": {
        "description": "The on_interact_outside event handler is called when the user interacts outside the component.",
    },
    "on_open_auto_focus": {
        "description": "The on_open_auto_focus event handler is called when the component opens and the focus is returned to the first item.",
    },
    "on_change": {
        "description": "The on_change event handler is called when the value or checked state of the component changes.",
    },
    "on_value_change": {
        "description": "The on_change event handler is called when the value state of the component changes.",
    },
    "on_close_auto_focus": {
        "description": "The on_close_auto_focus event handler is called when focus moves to the trigger after closing. It can be prevented by calling event.preventDefault.",
    },
    "on_escape_key_down": {
        "description": "The on_escape_key_down event handler is called when the escape key is down. It can be prevented by calling event.preventDefault.",
    },
    "on_pointer_down_outside": {
        "description": "The on_pointer_down_outside event handler is called when a pointer event occurs outside the bounds of the component. It can be prevented by calling event.preventDefault.",
    },
    "on_value_commit": {
        "description": "The on_value_commit event handler is called when the value changes at the end of an interaction. Useful when you only need to capture a final value e.g. to update a backend service.",
    },
    "on_clear_server_errors": {
        "description": "The on_clear_server_errors event handler is called when the form is submitted or reset and the server errors need to be cleared.",
    },
    "on_select": {
        "description": "The on_select event handler is called when the user selects an item.",
    },
    "on_drop": {
        "description": "The on_drop event handler is called when the user drops an item.",
    },
}


def generate_props(src, component, comp):
    if len(src.get_props()) == 0:
        return rx.vstack(
            rx.heading("Props", as_="h3", style=large),
            rx.text("No component specific props"),
            width="100%",
            overflow_x="auto",
            align_items="start",
            padding_y=".5em",
        )

    padding_left = "1em"

    prop_dict = {}

    is_interactive = True
    if not rx.utils.types._issubclass(
        component,
        (RadixThemesComponent, RadixPrimitiveComponent),
    ) or component.__name__ in [
        "Theme",
        "ThemePanel",
        "DrawerRoot",
        "DrawerTrigger",
        "DrawerOverlay",
        "DrawerPortal",
        "DrawerContent",
        "DrawerClose",
    ]:
        is_interactive = False

    body = rx.table.body(
        *[
            rx.table.row(
                *prop_docs(prop, prop_dict, component, is_interactive),
                align="center",
            )
            for prop in src.get_props()
            if not prop.name.startswith("on_")  # ignore event trigger props
        ],
        background=c_color("slate", 2),
    )

    def is_ineligble_data_component(
        component,
    ) -> bool:
        component_name: str = component.__name__.lower()
        match component_name:
            case "datalistroot":
                return False

            case component_name if "data" in component_name:
                return True

            case _:
                return False

    try:
        if f"{component.__name__}" in comp.metadata:
            comp = eval(comp.metadata[component.__name__])(**prop_dict)

        elif not is_interactive:
            comp = rx.fragment()

        else:
            try:
                comp = rx.vstack(component.create("Test", **prop_dict))

            except:
                comp = rx.fragment()

            if is_ineligble_data_component(component):
                raise Exception("Data components cannot be created")

    except Exception as e:
        print(f"Failed to create component {component.__name__}, error: {e}")
        comp = rx.fragment()

    return rx.vstack(
        docdemobox(comp) if not isinstance(comp, Fragment) else "",
        rx.scroll_area(
            rx.table.root(
                rx.el.style(
                    """
                    .rt-TableRoot:where(.rt-variant-surface) :where(.rt-TableRootTable) :where(.rt-TableHeader) {
                    --table-row-background-color: "transparent"
                    }
                    """,
                ),
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell(
                            "Prop",
                            padding_left=padding_left,
                            justify="start",
                            text_wrap="nowrap",
                            width="auto",
                        ),
                        rx.table.column_header_cell(
                            "Type | Values",
                            padding_left=padding_left,
                            justify="start",
                            text_wrap="nowrap",
                            width="auto",
                        ),
                        rx.table.column_header_cell(
                            "Default",
                            padding_left=padding_left,
                            justify="start",
                            text_wrap="nowrap",
                            width="auto",
                        ),
                        rx.cond(
                            is_interactive,
                            rx.table.column_header_cell(
                                "Interactive",
                                padding_left=padding_left,
                                justify="start",
                                text_wrap="nowrap",
                                width="auto",
                            ),
                            rx.fragment(),
                        ),
                    ),
                    background=c_color("slate", 3),
                ),
                body,
                width="100%",
                padding_x="0",
                variant="surface",
                size="1",
                border=f"1px solid {c_color('slate', 4)}",
            ),
            max_height="25em",
            margin_bottom="16px",
        ),
    )


# Default event triggers.
default_triggers = rx.Component.create().get_event_triggers()


def same_trigger(t1, t2):
    if t1 is None or t2 is None:
        return False
    args1 = inspect.getfullargspec(t1).args
    args2 = inspect.getfullargspec(t2).args
    return args1 == args2


def generate_event_triggers(comp, src):
    prop_name_to_description = {
        prop.name: prop.description
        for prop in src.get_props()
        if prop.name.startswith("on_")
    }
    triggers = comp().get_event_triggers()
    custom_events = [
        event
        for event in triggers
        if not same_trigger(triggers.get(event), default_triggers.get(event))
    ]

    if not custom_events:
        return rx.vstack(
            rx.heading("Event Triggers", as_="h3", style=large),
            rx.link(
                "See the full list of default event triggers",
                href="https://reflex.dev/docs/api-reference/event-triggers/",
                color=c_color("violet", 11),
                style=base,
                is_external=True,
            ),
            width="100%",
            overflow_x="auto",
            align_items="start",
            padding_y=".5em",
        )
    padding_left = "1em"

    return rx.vstack(
        rx.heading("Event Triggers", as_="h3", style=large),
        rx.link(
            "See the full list of default event triggers",
            href="https://reflex.dev/docs/api-reference/event-triggers/",
            color=c_color("violet", 11),
            style=base,
            is_external=True,
        ),
        rx.scroll_area(
            rx.table.root(
                rx.el.style(
                    """
                    .rt-TableRoot:where(.rt-variant-surface) :where(.rt-TableRootTable) :where(.rt-TableHeader) {
                        --table-row-background-color: "transparent"
                    }
                """,
                ),
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell(
                            "Trigger",
                            padding_left=padding_left,
                            justify="start",
                        ),
                        rx.table.column_header_cell(
                            "Description",
                            padding_left=padding_left,
                            justify="start",
                        ),
                    ),
                    background_color=c_color("slate", 3),
                ),
                rx.table.body(
                    *[
                        rx.table.row(
                            rx.table.cell(
                                rx.code(event, style=get_code_style("violet")),
                                padding_left=padding_left,
                                justify="start",
                            ),
                            rx.table.cell(
                                prop_name_to_description.get(event)
                                or EVENTS[event]["description"],
                                color=c_color("slate", 11),
                                style=small,
                                padding_left=padding_left,
                                justify="start",
                            ),
                        )
                        for event in custom_events
                    ],
                    background_color=c_color("slate", 2),
                ),
                width="100%",
                variant="surface",
                size="1",
                border=f"1px solid {c_color('slate', 4)}",
            ),
            width="100%",
            overflow="hidden",
            align_items="start",
        ),
        gap="24px",
        max_height="40em",
        align_items="start",
    )


def generate_valid_children(comp):
    if not comp._valid_children:
        return rx.text("")

    valid_children = [
        rx.chakra.wrap_item(rx.code(child, style=get_code_style("violet")))
        for child in comp._valid_children
    ]
    return rx.vstack(
        rx.heading("Valid Children", as_="h3", style=large),
        rx.chakra.wrap(*valid_children),
        width="100%",
        align_items="start",
        padding_bottom="24px",
    )


def component_docs(component_tuple, comp):
    """Generates documentation for a given component."""
    component = component_tuple[0]
    src = Source(component=component)
    props = generate_props(src, component, comp)
    triggers = generate_event_triggers(component, src)
    children = generate_valid_children(component)

    return rx.box(
        h2_comp(text=component_tuple[1].lower()),
        rx.box(markdown(textwrap.dedent(src.get_docs())), padding_bottom=".5em"),
        props,
        children,
        triggers,
        text_align="left",
        width="100%",
        padding_bottom="2em",
    )


tab_style = {
    "font_size": "1em",
    "font_weight": "500",
    "padding_x": ".5em",
    "color": "#696287",
}
tab_selected_style = {
    "color": "#5646ED",
    "bg": "#F5EFFE",
    "font_size": "1em",
    "font_weight": "500",
    "padding_x": ".5em",
    "padding_y": ".10em",
    "border_radius": "8px",
}


def multi_docs(path, comp, component_list, title):
    components = [
        component_docs(component_tuple, comp) for component_tuple in component_list[1:]
    ]
    fname = path.strip("/") + ".md"
    ll_doc_exists = os.path.exists(fname.replace(".md", "-ll.md"))

    non_active_style = {
        "padding": "8px",
        "color": c_color("slate", 9),
        "width": "7em",
        "transition": "color 0.035s ease-out",
        "_hover": {
            "color": c_color("slate", 11),
        },
        **small,
    }

    active_style = {
        "padding": "8px",
        "background": c_color("slate", 2),
        "color": c_color("slate", 11),
        "box_shadow": shadows["large"],
        "border_radius": "8px",
        "width": "7em",
        "cursor": "default",
        "border": f"1px solid {c_color('slate', 4)}",
        **small,
    }

    def links(current_page, ll_doc_exists, path):
        if ll_doc_exists:
            if current_page == "hl":
                return rx.flex(
                    rx.box(flex_grow="1"),
                    rx.flex(
                        rx.link(
                            rx.center(rx.text("High Level"), style=active_style),
                            underline="none",
                        ),
                        rx.link(
                            rx.center(rx.text("Low Level"), style=non_active_style),
                            href=path + "/low",
                            underline="none",
                        ),
                        spacing="2",
                        padding="8px",
                        background=c_color("slate", 3),
                        border_radius="16px",
                        align_items="center",
                        justify_items="center",
                    ),
                    margin_bottom=".5em",
                )
            return rx.flex(
                rx.box(flex_grow="1"),
                rx.flex(
                    rx.link(
                        rx.center(rx.text("High Level"), style=non_active_style),
                        href=path,
                        underline="none",
                    ),
                    rx.link(
                        rx.center(rx.text("Low Level"), style=active_style),
                        href=path + "/low",
                        underline="none",
                    ),
                    spacing="2",
                    padding="8px",
                    background=c_color("slate", 3),
                    border_radius="16px",
                    align_items="center",
                    justify_items="center",
                ),
                margin_bottom=".5em",
            )
        return rx.fragment()

    @docpage(set_path=path, t=title)
    def out():
        toc = get_toc(comp, fname, component_list)
        return toc, rx.flex(
            links("hl", ll_doc_exists, path),
            xd.render(comp, filename=fname),
            h1_comp(text="API Reference"),
            rx.vstack(*components),
            direction="column",
            width="100%",
        )

    @docpage(set_path=path + "low/", t=title + " (Low Level)")
    def ll():
        nonlocal fname
        fname = fname.replace(".md", "-ll.md")
        d2 = flexdown.parse_file(fname)
        toc = get_toc(d2, fname, component_list)
        return toc, rx.flex(
            links("ll", ll_doc_exists, path),
            xd.render_file(fname),
            h1_comp(text="API Reference"),
            rx.vstack(*components),
            direction="column",
            width="100%",
        )

    if ll_doc_exists:
        return (out, ll)
    return out

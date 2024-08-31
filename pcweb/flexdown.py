import flexdown
import reflex as rx

from pcweb.styles.colors import c_color
from pcweb.styles.fonts import base
from pcweb.styles.fonts import code
from pcweb.templates.docpage import code_block_markdown
from pcweb.templates.docpage import code_block_markdown_dark
from pcweb.templates.docpage import code_comp
from pcweb.templates.docpage import definition
from pcweb.templates.docpage import docdemo
from pcweb.templates.docpage import docdemobox
from pcweb.templates.docpage import docgraphing
from pcweb.templates.docpage import doclink2
from pcweb.templates.docpage import h1_comp_xd
from pcweb.templates.docpage import h2_comp_xd
from pcweb.templates.docpage import h3_comp_xd
from pcweb.templates.docpage import h4_comp_xd
from pcweb.templates.docpage import list_comp
from pcweb.templates.docpage import text_comp


def get_code_style(color: str):
    return {
        "p": {"margin_y": "0px"},
        "code": {
            "color": rx.color(color, 11),
            "border_radius": "4px",
            "border": f"1px solid {rx.color(color, 5)}",
            "background": rx.color(color, 4),
            **code,
        },
        **base,
    }


class AlertBlock(flexdown.blocks.MarkdownBlock):
    """A block that displays a component along with its code."""

    starting_indicator = "```md alert"
    ending_indicator = "```"

    include_indicators = True

    def render(
        self,
        env,
    ) -> rx.Component:
        lines = self.get_lines(env)

        args = lines[0].removeprefix(self.starting_indicator).split()

        if len(args) == 0:
            args = ["info"]
        status = args[0]

        if lines[1].startswith("#"):
            title = lines[1].strip("#").strip()
            content = "\n".join(lines[2:-1])
        else:
            title = ""
            content = "\n".join(lines[1:-1])

        colors = {
            "info": "accent",
            "success": "grass",
            "warning": "amber",
            "error": "red",
        }

        color = colors.get(status, "blue")

        has_content = bool(content.strip())

        if has_content:
            return rx.chakra.accordion(
                rx.chakra.accordion_item(
                    rx.chakra.accordion_button(
                        rx.hstack(
                            rx.box(
                                rx.match(
                                    status,
                                    (
                                        "info",
                                        rx.icon(
                                            tag="info",
                                            size=18,
                                            margin_right=".5em",
                                        ),
                                    ),
                                    (
                                        "success",
                                        rx.icon(
                                            tag="circle_check",
                                            size=18,
                                            margin_right=".5em",
                                        ),
                                    ),
                                    (
                                        "warning",
                                        rx.icon(
                                            tag="triangle_alert",
                                            size=18,
                                            margin_right=".5em",
                                        ),
                                    ),
                                    (
                                        "error",
                                        rx.icon(
                                            tag="ban",
                                            size=18,
                                            margin_right=".5em",
                                        ),
                                    ),
                                ),
                                color=f"{rx.color(color, 11)}",
                            ),
                            (
                                rx.markdown(
                                    title,
                                    margin_y="0px",
                                    style=get_code_style(color),
                                )
                                if title
                                else self.render_fn(content=content)
                            ),
                            rx.spacer(),
                            rx.chakra.accordion_icon(color=f"{rx.color(color, 11)}"),
                            align_items="center",
                            justify_content="left",
                            text_align="left",
                            spacing="2",
                            width="100%",
                        ),
                        padding="0px",
                        color=f"{rx.color(color, 11)}",
                        border_radius="12px",
                        _hover={},
                    ),
                    (
                        rx.chakra.accordion_panel(
                            markdown(content),
                            padding="0px",
                            margin_top="16px",
                        )
                        if title
                        else rx.fragment()
                    ),
                    border_radius="12px",
                    padding=["16px", "24px"],
                    background_color=f"{rx.color(color, 3)}",
                    border=f"1px solid {rx.color(color, 4)}",
                    allow_toggle=True,
                ),
                is_disabled=True,
                allow_toggle=True,
                width="100%",
                margin_bottom="16px",
            )
        return rx.vstack(
            rx.hstack(
                rx.box(
                    rx.match(
                        status,
                        ("info", rx.icon(tag="info", size=18, margin_right=".5em")),
                        (
                            "success",
                            rx.icon(tag="circle_check", size=18, margin_right=".5em"),
                        ),
                        (
                            "warning",
                            rx.icon(tag="triangle_alert", size=18, margin_right=".5em"),
                        ),
                        ("error", rx.icon(tag="ban", size=18, margin_right=".5em")),
                    ),
                    color=f"{rx.color(color, 11)}",
                ),
                rx.markdown(
                    title,
                    color=f"{rx.color(color, 11)}",
                    margin_y="0px",
                    style=get_code_style(color),
                ),
                align_items="center",
                width="100%",
                spacing="1",
                padding=["16px", "24px"],
            ),
            border=f"1px solid {rx.color(color, 4)}",
            background_color=f"{rx.color(color, 3)}",
            border_radius="12px",
            margin_bottom="16px",
        )


class SectionBlock(flexdown.blocks.Block):
    """A block that displays a component along with its code."""

    starting_indicator = "```md section"
    ending_indicator = "```"

    def render(
        self,
        env,
    ) -> rx.Component:
        lines = self.get_lines(env)

        # Split up content into sections based on markdown headers.
        header_indices = [i for i, line in enumerate(lines) if line.startswith("#")]
        header_indices.append(len(lines))
        sections = [
            (
                lines[header_indices[i]].strip("#"),
                "\n".join(lines[header_indices[i] + 1 : header_indices[i + 1]]),
            )
            for i in range(len(header_indices) - 1)
        ]

        return rx.box(
            rx.vstack(
                *[
                    rx.fragment(
                        rx.text(
                            rx.chakra.span(
                                header,
                                font_weight="bold",
                            ),
                            width="100%",
                        ),
                        rx.box(
                            markdown(section),
                            width="100%",
                        ),
                    )
                    for header, section in sections
                ],
                text_align="left",
                margin_y="1em",
                width="100%",
            ),
            border_left=f"1.5px {c_color('slate', 4)} solid",
            padding_left="1em",
            width="100%",
            align_items="center",
        )


class DefinitionBlock(flexdown.blocks.Block):
    starting_indicator = "```md definition"
    ending_indicator = "```"

    def render(
        self,
        env,
    ) -> rx.Component:
        lines = self.get_lines(env)

        # Split up content into sections based on markdown headers.
        header_indices = [i for i, line in enumerate(lines) if line.startswith("#")]
        header_indices.append(len(lines))
        sections = [
            (
                lines[header_indices[i]].removeprefix("#"),
                "\n".join(lines[header_indices[i] + 1 : header_indices[i + 1]]),
            )
            for i in range(len(header_indices) - 1)
        ]

        defs = [definition(title, content) for title, content in sections]

        return rx.fragment(
            rx.mobile_only(rx.chakra.vstack(*defs)),
            rx.tablet_and_desktop(
                rx.chakra.grid(
                    *[
                        rx.chakra.grid_item(d, row_span=1, col_span=1, width="100%")
                        for d in defs
                    ],
                    template_columns="repeat(2, 1fr)",
                    h="10em",
                    width="100%",
                    gap=4,
                    margin_bottom="1em",
                ),
            ),
        )


class DemoBlock(flexdown.blocks.Block):
    """A block that displays a component along with its code."""

    starting_indicator = "```python demo"
    ending_indicator = "```"
    include_indicators = True
    theme: str = None

    def render(
        self,
        env,
    ) -> rx.Component:
        lines = self.get_lines(env)
        code = "\n".join(lines[1:-1])

        args = lines[0].removeprefix(self.starting_indicator).split()

        exec_mode = env.get("__exec", False)
        comp = ""

        for arg in args:
            if arg.startswith("id="):
                comp_id = arg.rsplit("id=")[-1]
                break
        else:
            comp_id = None

        if "exec" in args:
            env["__xd"].exec(code, env, self.filename)
            if not exec_mode:
                comp = env[list(env.keys())[-1]]()
        elif "graphing" in args:
            env["__xd"].exec(code, env, self.filename)
            if not exec_mode:
                comp = env[list(env.keys())[-1]]()
                # Get all the code before the final "def".
                parts = code.rpartition("def")
                data, code = parts[0], parts[1] + parts[2]
                comp = docgraphing(code, comp=comp, data=data)
                return comp
        elif exec_mode:
            return comp
        elif "box" in args:
            comp = eval(code, env, env)
            return rx.box(docdemobox(comp), margin_bottom="1em", id=comp_id)
        else:
            comp = eval(code, env, env)

        # Sweep up additional CSS-like props to apply to the demobox itself
        demobox_props = {}
        for arg in args:
            prop, equals, value = arg.partition("=")
            if equals:
                demobox_props[prop] = value

        if "toggle" in args:
            demobox_props["toggle"] = True

        return docdemo(
            code,
            comp=comp,
            demobox_props=demobox_props,
            theme=self.theme,
            id=comp_id,
        )


class DemoBlockDark(DemoBlock):
    theme = "dark"


class VideoBlock(flexdown.blocks.MarkdownBlock):
    """A block that displays a video."""

    starting_indicator = "```md video"
    ending_indicator = "```"

    include_indicators = True

    def render(
        self,
        env,
    ) -> rx.Component:
        lines = self.get_lines(env)

        args = lines[0].removeprefix(self.starting_indicator).split()

        if len(args) == 0:
            args = ["info"]
        url = args[0]

        title = lines[1].strip("#").strip() if lines[1].startswith("#") else ""

        color = "blue"

        return rx.chakra.accordion(
            rx.chakra.accordion_item(
                rx.chakra.accordion_button(
                    rx.hstack(
                        (
                            rx.markdown(
                                title,
                                margin_y="0px",
                                style=get_code_style(color),
                            )
                            if title
                            else rx.markdown("Video Description")
                        ),
                        rx.spacer(),
                        rx.chakra.accordion_icon(color=f"{rx.color(color, 11)}"),
                        align_items="center",
                        justify_content="left",
                        text_align="left",
                        spacing="2",
                        width="100%",
                    ),
                    padding="0px",
                    color=f"{rx.color(color, 11)}",
                    _hover={},
                ),
                rx.chakra.accordion_panel(
                    rx.video(
                        url=url,
                        width="100%",
                        height="500px",
                        border_radius="10px",
                        overflow="hidden",
                    ),
                    margin_top="16px",
                    padding="0px",
                ),
                border_radius="12px",
                border=f"1px solid {rx.color(color, 4)}",
                background_color=f"{rx.color(color, 3)}",
                allow_toggle=True,
                padding=["16px", "24px"],
            ),
            margin_bottom="16px",
            is_disabled=True,
            allow_toggle=True,
            width="100%",
        )


component_map = {
    "h1": lambda text: h1_comp_xd(text=text),
    "h2": lambda text: h2_comp_xd(text=text),
    "h3": lambda text: h3_comp_xd(text=text),
    "h4": lambda text: h4_comp_xd(text=text),
    "p": lambda text: text_comp(text=text),
    "li": lambda text: list_comp(text=text),
    "a": doclink2,
    "code": lambda text: code_comp(text=text),
    "codeblock": code_block_markdown,
}
comp2 = component_map.copy()
comp2["codeblock"] = code_block_markdown_dark

xd = flexdown.Flexdown(
    block_types=[DemoBlock, AlertBlock, DefinitionBlock, SectionBlock, VideoBlock],
    component_map=component_map,
)
xd.clear_modules()
xd2 = flexdown.Flexdown(
    block_types=[DemoBlockDark, AlertBlock, DefinitionBlock, SectionBlock, VideoBlock],
    component_map=comp2,
)
xd2.clear_modules()


def markdown(text):
    return xd.get_default_block().render_fn(content=text)

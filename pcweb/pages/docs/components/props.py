import pynecone as pc

from pcweb.base_state import State
from pcweb.templates.docpage import (
    docdemo,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader,
)

code1 = """pc.avatar(
    name="John Doe",
)"""

code2 = """pc.button(
    "Fancy Button",
    border_radius="1em",
    box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
    background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
    box_sizing="border-box",
    color="white",
    _hover={
        "opacity": 0.85,
    }
)"""

code3 = """
class PropExampleState(State):
    text: str = "Hello World"
    color: str = "red"

    def flip_color(self):
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"

"""
exec(code3)
code4 = """pc.badge(
    PropExampleState.text,
    color_scheme=PropExampleState.color,
    on_click=PropExampleState.flip_color,
    font_size="1.5em",
    _hover={
        "cursor": "pointer",
    }
)
"""
code5 = """
class PropCondState(State):
    value: int
"""
exec(code5)
code6 = """pc.slider(
    on_change_end=PropCondState.set_value,
    color_scheme=pc.cond(PropCondState.value > 50, "green", "pink"),
)
"""

code7 = """pc.box(
    id="box-id",
    class_name=["class-name-1", "class-name-2",],
)
"""


@docpage()
def props():
    from pcweb.pages.docs.components.overview import components_overview
    from pcweb.pages.docs.library import library
    from pcweb.pages.docs.state.overview import state_overview
    from pcweb.pages.docs.state.vars import vars
    from pcweb.pages.docs.styling.overview import styling_overview

    return pc.box(
        docheader("Props", first=True),
        doctext(
            "Props modify the behavior and appearance of a component. ",
            "They are passed in as keyword arguments to the component function.",
        ),
        subheader("Component Props"),
        doctext(
            "Each component has props that are specific to that component. ",
            "For example, the ",
            pc.code("pc.avatar"),
            " component has a ",
            pc.code("name"),
            " prop that sets the name of the avatar. ",
        ),
        docdemo(code1),
        doctext(
            "Check the docs for the component you are using to see what props are available. ",
        ),
        doctext(
            pc.alert(
                pc.alert_icon(),
                pc.alert_title(
                    "Pynecone has several ",
                    doclink("built-in components", href=library.path),
                    " to get you started quickly.",
                ),
                status="success",
            ),
        ),
        subheader("HTML Props"),
        doctext(
            "Each component has basic HTML props. ",
            "You can set ",
            pc.code("id"),
            ", which type is a ",
            pc.code("str"),
            " to show specific content to the top of view with hash in URL. ",
            "You can also add ",
            pc.code("class_name"),
            ", which type can be a ",
            pc.code("str"),
            " or a ",
            pc.code("List[str]"),
            " to attach style. ",
        ),
        docdemo(code7),
        subheader("Style Props"),
        doctext(
            "In addition to component-specific props, most built-in components support a full range of style props. "
            "You can use any CSS property to style a component. ",
        ),
        docdemo(code2),
        doctext(
            "See the ",
            doclink("styling docs", href=styling_overview.path),
            " to learn more about customizing the appearance of your app.",
        ),
        subheader("Binding Props to State"),
        doctext(
            pc.alert(
                pc.alert_icon(),
                pc.box(
                    pc.alert_title(
                        "We recommend reading the ",
                        doclink("state docs", href=state_overview.path),
                        " for this section.",
                    ),
                    pc.alert_description(
                        "The rest of this page discusses how props interact with your app state. ",
                        "Feel free to continue with the component docs, and come back to this later. ",
                    ),
                ),
                status="warning",
            ),
        ),
        doctext(
            "You can set the value of a prop to a ",
            doclink("state var", href=vars.path),
            " to make the component update when the var changes. ",
        ),
        doctext(
            "Try clicking the badge below to change its color. ",
        ),
        docdemo(code4, code3, eval(code4), context=True),
        doctext(
            "In this example, the ",
            pc.code("color_scheme"),
            " prop is bound to the ",
            pc.code("color"),
            " state var. ",
        ),
        doctext(
            "When the ",
            pc.code("flip_color"),
            " event handler is called, the ",
            pc.code("color"),
            " var is updated, and the ",
            pc.code("color_scheme"),
            " prop is updated to match. ",
        ),
        subheader("Conditional Props"),
        doctext(
            "Sometimes you want to set a prop based on a condition. ",
            "You can use the ",
            pc.code("pc.cond"),
            " function to do this. ",
        ),
        docdemo(code6, code5, eval(code6), context=True),
    )

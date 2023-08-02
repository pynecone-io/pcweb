import reflex as rx
from pcweb import styles
from pcweb.base_state import State
from pcweb.templates.docpage import (
    doc_section,
    doccode,
    docdemobox,
    docheader,
    doclink,
    docpage,
    doctext,
    subheader_comp,
    text_comp,
    definition,
    docalert,
)
from pcweb.pages.docs.tutorial import intro
from pcweb.pages.docs.getting_started import installation

definitions = [
    definition(
        "Quickstart",
        rx.text(
            "Learn how to use Reflex in few minutes through an interactive chat app tutorial.",
        ),
    ),
    definition(
        "Gallery",
        rx.text(
            "Check out the gallery to see what types of apps you can build with Reflex.",
        ),
    ),
]

render_code = """rx.hstack(
    rx.button("Decrement", color_scheme = "red", border_radius="1em", on_click = State.decrement),
    rx.heading(State.count, font_size="2em"),
    rx.button("Increment", color_scheme = "green", border_radius="1em", on_click = State.increment),
)"""

counter_code = f"""
import reflex as rx

class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index():
    return {render_code} 


app = rx.App()
app.add_page(index)
app.compile()
"""


class CounterExampleState(State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def get_started() -> rx.Component:
    return rx.fragment(
        subheader_comp(text="Get Started"),
        doctext(
            "Below is a quick example of a counter app to get a feel for how Reflex works. ",
        ),
        doctext(
            "For a more in depth example, we recommend going through the ",
            doclink("tutorial", href=intro.path),
            " tutorial or go straight to the ",
            doclink("installation", href=installation.path),
            " to start building your own app.",
        ),
    )


def motivation() -> rx.Component:
    return rx.fragment(
        subheader_comp(text="Motivation"),
        text_comp(text="Reflex was created with the following goals:"),
        doc_section(
            rx.vstack(
                rx.text(
                    rx.span(
                        "Pure Python",
                        font_weight="bold",
                    ),
                    width="100%",
                ),
                rx.text(
                    "Use Python for everything. Don't worry about learning a new language.",
                    width="100%",
                ),
                rx.text(
                    rx.span(
                        "Easy to Learn",
                        font_weight="bold",
                    ),
                    width="100%",
                ),
                rx.text(
                    "Build and share your first app in minutes. No webdev experience required.",
                    width="100%",
                ),
                rx.text(
                    rx.span(
                        "Full Flexibility",
                        font_weight="bold",
                    ),
                    width="100%",
                ),
                rx.text(
                    "Remain as flexible as traditional web frameworks. ",
                    "Reflex is easy to get started with, but powerful enough for advanced use cases.",
                    width="100%",
                ),
                rx.text(
                    "Build anything from small data science apps to large, multi-page websites. ",
                    width="100%",
                ),
                rx.text(
                    "This entire site was built and deployed with Reflex!",
                    color=styles.ACCENT_COLOR,
                    width="100%",
                ),
                rx.text(
                    rx.span(
                        "Batteries Included",
                        font_weight="bold",
                    ),
                    width="100%",
                ),
                rx.text(
                    "No need to reach for a bunch of different tools. Reflex handles the frontend, backend, and deployment of your app.",
                    width="100%",
                ),
                text_align="left",
            ),
        ),
        margin_bottom="1em",
    )


def counter_example() -> rx.Component:
    from pcweb.pages.docs.advanced_guide.wrapping_react import wrapping_react
    from pcweb.pages.docs.library import library

    return rx.box(
        subheader_comp(text="Quickstart"),
        text_comp(
            text="Let's go over a simple counter app to explore the basics of Reflex. "
        ),
        docdemobox(
            rx.hstack(
                rx.button(
                    "Decrement",
                    bg="#fef2f2",
                    color="#b91c1c",
                    border_radius="lg",
                    on_click=CounterExampleState.decrement,
                ),
                rx.heading(
                    CounterExampleState.count, font_size="2em", padding_x="0.5em"
                ),
                rx.button(
                    "Increment",
                    bg="#ecfdf5",
                    color="#047857",
                    border_radius="lg",
                    on_click=CounterExampleState.increment,
                ),
            ),
        ),
        doc_section(
            text_comp(text="Here is the complete code to create this. "),
            doccode(counter_code),
        ),
        subheader_comp(text="The Structure of a Reflex App"),
        text_comp(text="Let's break this counter example down."),
        subheader_comp(text="Import"),
        doccode(counter_code, lines=(0, 1)),
        rx.text(
            "We begin by importing the library. ",
            "All Reflex functions and classes begin with the ",
            rx.code("rx."),
            " prefix.",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        subheader_comp(text="State"),
        doccode(counter_code, lines=(2, 5)),
        rx.text(
            "The state defines all the variables (called ",
            rx.span("vars", font_weight="bold"),
            ") in an app that can change, as well as the functions that change them. ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        rx.text(
            "Here our state has a single var, ",
            rx.code(
                "count",
            ),
            ", which holds the current value of the counter. ",
            " We initialize it to ",
            rx.code(
                "0",
            ),
            ". ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        subheader_comp(text="Event Handlers"),
        doccode(counter_code, lines=(5, 13)),
        rx.text(
            "Within the state, we define functions, called ",
            rx.span("event handlers", font_weight="bold"),
            ", that change the state vars. ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        rx.text(
            "Event handlers are the only way that we can modify the state in Reflex. ",
            "They can be called in response to user actions, such as clicking a button or typing in a text box. ",
            "These actions are called ",
            rx.span("events", font_weight="bold"),
            ".",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        rx.text(
            "Our counter app has two event handlers, ",
            rx.code(
                "increment",
            ),
            " and ",
            rx.code(
                "decrement",
            ),
            ".",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        subheader_comp(text="Frontend"),
        doccode(counter_code, lines=(13, 30)),
        text_comp(
            text="This function defines the frontend of the app. ",
        ),
        rx.text(
            "We use different components such as ",
            rx.code(
                "rx.hstack",
            ),
            ", ",
            rx.code(
                "rx.button",
            ),
            ", and ",
            rx.code(
                "rx.heading",
            ),
            " to build the frontend. ",
            "Components can be nested to create complex layouts, ",
            " and can be styled using the full power of CSS. ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        rx.text(
            "Reflex comes with ",
            doclink("50+ built-in components", href=library.path),
            " to help you get started. "
            "We are actively adding more components,  "
            "plus it's easy to ",
            doclink("wrap your own React components", href=wrapping_react.path),
            ". ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        doccode(counter_code, lines=(21, 22)),
        rx.text(
            "Components can reference the app's state vars. " "The ",
            rx.code(
                "rx.heading",
            ),
            " component displays the current value of the counter by referencing ",
            rx.code(
                "State.count",
            ),
            ". ",
            "All components that reference state will reactively update whenever the state changes.",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        doccode(counter_code, lines=(15, 21)),
        rx.text(
            "Components interact with the state by binding events triggers to event handlers. ",
            "For example, ",
            rx.code(
                "on_click",
            ),
            " is an event that is triggered when a user clicks a component. ",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        rx.text(
            "The first button in our app binds its ",
            rx.code(
                "on_click",
            ),
            " event to the ",
            rx.code(
                "State.decrement",
            ),
            " event handler, ",
            " and the second button binds its to the ",
            rx.code(
                "State.increment",
            ),
            " handler.",
            margin_bottom="1em",
            font_size=styles.TEXT_FONT_SIZE,
        ),
        subheader_comp(text="Routing"),
        doccode(counter_code, lines=(31, 33)),
        text_comp(text="Next we define our app and add the counter component to the base route."),
        subheader_comp(text="Compiling"),
        doccode(counter_code, lines=(33, 34)),
        text_comp(text="Finally, we compile our app, and we are ready to run it."),
        subheader_comp(text="Next Steps"),
        text_comp(
            text="And that's it! "
            "We've created an entire frontend and backend in less than 30 lines of code. "
            "From here we can continue developing or deploy it to the web in a single command. "
        ),
        doctext("Keep reading the docs to learn how to try Reflex yourself!"),
        padding_top="1em",
    )


@docpage()
def introduction():
    return rx.box(
        docheader("Reflex Docs"),
        rx.center(
            rx.span(
                "Looking for Pynecone? You are in the right place, Pynecone is now Reflex!",
                color="#494369",
            ),
            bg="#FAF8FB",
            font_family=styles.MONO,
            padding=4,
            margin_bottom="1em",
            border="1px solid #EAE4FD",
            border_radius=styles.DOC_BORDER_RADIUS,
            font_size=".8em",
        ),
        doctext(
            rx.span("Reflex", font_weight="bold"),
            rx.span(
                """
            is an open-source, full-stack Python framework that makes it easy to build and deploy web apps in minutes.
            """
            ),
        ),
        motivation(),
        get_started(),
        counter_example(),
    )

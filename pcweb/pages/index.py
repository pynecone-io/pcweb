import reflex as rx
from pcweb import styles
from pcweb.templates import webpage

from .demos_on_landing_page.auth.auth import auth
from .demos_on_landing_page.forms.forms import forms
from .demos_on_landing_page.dashboard.dashboard import dashboard

link_style = {
    "color": "black",
    "font_weight": styles.BOLD_WEIGHT,
    "_hover": {"color": rx.color("accent")},
}

button_style_landing= {
    "border_radius": "50px;",
    "border": "1px solid rgba(186, 199, 247, 0.12);",
    "background": "rgba(161, 157, 213, 0.03);",
    "backdrop_filter": "blur(2px);",
    "padding": "7px 12px;",
    "align_items": "center;",
    "color": "#848496;"
}


features_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen"
contribution_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22"
github_url = "https://github.com/reflex-dev/reflex"
bugs_url="https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue"



def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs, 
    )

class DemoState(rx.State):

    demo = "Chat"

    def set_demo(self, demo):
        self.demo = demo

def image_gen():
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            rx.icon("ellipsis"),
                            variant="soft"
                        ),
                    ),
                    rx.menu.content(
                        rx.menu.item("Share", shortcut="⌘ E"),
                        rx.menu.item("Duplicate", shortcut="⌘ D"),
                        rx.menu.separator(),
                        rx.menu.item("Archive", shortcut="⌘ N"),
                        rx.menu.sub(
                            rx.menu.sub_trigger("More"),
                            rx.menu.sub_content(
                                rx.menu.item("Move to project…"),
                                rx.menu.item("Move to folder…"),
                                rx.menu.separator(),
                                rx.menu.item("Advanced options…"),
                            ),
                        ),
                        rx.menu.separator(),
                        rx.menu.item("Add to favorites"),
                        rx.menu.separator(),
                        rx.menu.item("Delete", shortcut="⌘ ⌫", color="red"),
                    ),
                ),
                width="100%", 
                justify_content="space-between",    
            ),
            rx.center(
                rx.vstack(
                    rx.input(placeholder="Enter description", width="100%"),
                    rx.button("Generate Image ->", width="100%"),
                    align_items="center",
                ),
                width="100%",
                height="100%",
            ),
            width="60%",
            height="100%",
            padding_top="1em",
        ),
        rx.vstack(
            "Settings",
            rx.radix.input.root(
                rx.input(placeholder="Seed"),
                width="100%"
            ),
            rx.select(["Model 1", "Model 2", "Model 3"], default_value="Model 1", width="100%"),
            rx.text("Temperature"),
            rx.slider(default_value=25, width="100%"),
            rx.text("Width"),
            rx.slider(default_value=50, width="100%"),
            rx.text("Height"),
            rx.slider(default_value=75, width="100%"),
            rx.text("Share Results"),
            rx.switch(),
            rx.button("Save", width="100%", variant="outline"),
            width="40%",
            height="100%",
            border_left="1px solid #2F2B37;",
            padding_left="1em",
            align_items="start",
            justify_content="center"
        ),
        padding_x="1em",
        height="100%",
    )

def example_button(text):
    return rx.button(
    text,
    border_radius="8px;",
    border="1px solid rgba(186, 199, 247, 0.12);",
    background= "rgba(161, 157, 213, 0.03);",
    backdrop_filter= "blur(2px);",
    on_click= lambda: DemoState.set_demo(text)
)


def demos():
    return rx.vstack(
        rx.vstack(
            rx.text(
                "Build web apps, faster.",
                font_size="54px;",
                text_align="left",
                color="#D6D6ED",
                font_weight="bold",
                line_height="1",
            ),
            rx.text("Create your whole app in a single language. Don't worry about writing APIs to connect your frontend and backend.", color="#6C6C81"),
            padding_y="2em",
        ),
        rx.hstack(
            # example_button("Chat"),
            # example_button("Image Gen"),
            example_button("Forms"),
            example_button("Dashboard"),
            example_button("Auth"),
            rx.spacer(),
            rx.button(
                "View Code",
                border_radius="8px;",
                border="1px solid rgba(186, 199, 247, 0.12);",
                background= "rgba(161, 157, 213, 0.03);",
                backdrop_filter= "blur(2px);"
            ),
            width="70em",
            align_items="left"
        ),
        rx.box(
            rx.match(
                DemoState.demo,
                # ("Chat", forms()),
                # ("Image Gen", image_gen()),
                ("Forms", forms()),
                ("Dashboard", dashboard()),
                ("Auth", auth()),
                forms()
            ),
            height="30em",
            width="70em",
            border_radius= "10px;",
            border= "1px solid #2F2B37;",
            background= "linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
            
        ),
        padding_top="8em",
        padding_buttom= "20em",
        width="100%",
    )

def user_count_item(count, platform) -> rx.Component:
    return rx.flex(
        rx.text(f"{count}+", color="#E8E8F4", font_size="32px"),
        rx.text(platform, color="#6C6C81"),
        direction="column",
        align="center",
    )

def user_count_comp() -> rx.Component:
    return rx.center(
        user_count_item(110, "Contributors"),
        rx.divider(size="4", orientation="vertical"),
        user_count_item(5000, "Project created per month"),
        rx.divider(size="4", orientation="vertical"),
        user_count_item(3700, "Discord Members"),
        spacing="5",
        padding="1em",
    )

def open_source_badge() -> rx.Component:
    return rx.button(
        rx.flex(
            rx.text(
                "Open Source",
                color="transparent",
                font_size="14px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.28px",
                background="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                background_clip="text",
                _webkit_background_clip="text",
            ),
            height="31px",
            padding="0px 10px",
            justify="center",
            align="center",
            gap="10px",
            border_radius="15px",
            border="1px solid #4435D4",
            background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
            box_shadow="0px 0px 4px -1px rgba(27, 21, 90, 0.40), 0px 3px 6px -3px rgba(34, 25, 121, 0.60);",
        ),
        background="transparent",
        on_click=rx.redirect(
            github_url,
            external=True,
        ),
        _hover={
            "cursor": "pointer",
        },
    )

def github_button() -> rx.Component:
    return rx.button(
        rx.flex(
            rx.image(src="/companies/light/github.svg", height="20px", width="20px"),
            rx.center(
                "Github",
                color="#FFFFFF",
                font_size="14px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.28px",
            ),
            rx.center(
                "15.7k",
                color="#6151F3",
                font_size="12px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.24px",
            ),
            spacing="2",
        ),

        position="relative",
        top="32px",
        right="-140px",
        z_index="999",
        padding="var(--Space-4, 16px);",
        align="center",
        width="151px",
        height="42px",
        border_radius="70px",
        border="1px solid #3C3646",
        background="linear-gradient(243deg, #16141A -74.32%, #222029 69.37%);",
        box_shadow="0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
        on_click=rx.redirect(
            github_url,
            external=True,
        ),
        _hover={
            "cursor": "pointer",
        },
    )

def invite_message() -> rx.Component:
    return rx.box(
        rx.text(
            "Contribute to our open-source community.",
            color="#D6D6ED",
            font_size="38px",
            weight="bold",
            align="center",
            line_height="1",
        ),
        width="30em",
    )

def request_buttons() -> rx.Component:
    return rx.hstack(
        rx.button(
            "Bugs",
            color="#2BCEEA",
            weight="Medium",
            height="22px",
            width="138px",
            border="1px solid #2BCEEA",
            background_color="rgba(43, 206, 234, 0.25)",
            on_click=rx.redirect(
                bugs_url,
                external=True,
            ),
            _hover={
                "cursor": "pointer",
            },
        ),
        rx.button(
            "Good First Issues",
            color="#2BEA8E",
            weight="Medium",
            height="24px",
            width="138px",
            border="1px solid #2BEA8E",
            background_color="rgba(43, 234, 142, 0.25)",
            on_click=rx.redirect(
                contribution_url,
                external=True,
            ),
            _hover={
                "cursor": "pointer",
            },
        ),
    )

def invite_card_comp() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text(
                "Contribute to Reflex!", 
                color="#D6D6ED",
                weight="medium",
            ),
            request_buttons(),
            rx.text(
                "Start contributing today, checkout our Github for Details",
                color="#6C6C81",
                weight="medium",
            ),
            justify="start",
            direction="column",
            spacing="2",
        ),
        border_radius="10px",
        padding="1em",
        width="30em",
        border="1px solid #3C3646;",
        background="linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
        box_shadow= "0px 27px 44px -13px rgba(214, 214, 237, 0.10) inset, 0px 0px 27px -4px rgba(0, 0, 0, 0.30);",
    )

def stats() -> rx.Component:
    return rx.vstack(
        open_source_badge(),
        invite_message(),
        github_button(),
        invite_card_comp(),
        user_count_comp(),
        padding_top="25px",
        padding_bottom="25px",
        padding_left="25px",
        padding_right="25px",
    )


def landing():
    return rx.html("""
                   <svg width="837" height="250" viewBox="0 0 837 250" fill="none" xmlns="http://www.w3.org/2000/svg">
<g filter="url(#filter0_b_5217_1511)">
<path d="M553.48 199C552.375 199 551.48 198.105 551.48 197V53C551.48 51.8954 552.375 51 553.48 51H637.8C638.904 51 639.8 51.8954 639.8 53V78.6C639.8 79.7046 638.904 80.6 637.8 80.6H582.92C581.815 80.6 580.92 81.4954 580.92 82.6V108.2C580.92 109.305 581.815 110.2 582.92 110.2H637.8C638.904 110.2 639.8 111.096 639.8 112.2V137.8C639.8 138.905 638.904 139.8 637.8 139.8H582.92C581.815 139.8 580.92 140.696 580.92 141.8V167.4C580.92 168.505 581.815 169.4 582.92 169.4H637.8C638.904 169.4 639.8 170.296 639.8 171.4V197C639.8 198.105 638.904 199 637.8 199H553.48Z" fill="#BDB4E1" fill-opacity="0.03"/>
<path d="M553.48 198.5C552.652 198.5 551.98 197.828 551.98 197V53C551.98 52.1716 552.652 51.5 553.48 51.5H637.8C638.628 51.5 639.3 52.1716 639.3 53V78.6C639.3 79.4284 638.628 80.1 637.8 80.1H582.92C581.539 80.1 580.42 81.2193 580.42 82.6V108.2C580.42 109.581 581.539 110.7 582.92 110.7H637.8C638.628 110.7 639.3 111.372 639.3 112.2V137.8C639.3 138.629 638.628 139.3 637.8 139.3H582.92C581.539 139.3 580.42 140.419 580.42 141.8V167.4C580.42 168.781 581.539 169.9 582.92 169.9H637.8C638.628 169.9 639.3 170.572 639.3 171.4V197C639.3 197.828 638.628 198.5 637.8 198.5H553.48Z" stroke="#BAC7F7" stroke-opacity="0.32"/>
<path d="M553.48 198.5C552.652 198.5 551.98 197.828 551.98 197V53C551.98 52.1716 552.652 51.5 553.48 51.5H637.8C638.628 51.5 639.3 52.1716 639.3 53V78.6C639.3 79.4284 638.628 80.1 637.8 80.1H582.92C581.539 80.1 580.42 81.2193 580.42 82.6V108.2C580.42 109.581 581.539 110.7 582.92 110.7H637.8C638.628 110.7 639.3 111.372 639.3 112.2V137.8C639.3 138.629 638.628 139.3 637.8 139.3H582.92C581.539 139.3 580.42 140.419 580.42 141.8V167.4C580.42 168.781 581.539 169.9 582.92 169.9H637.8C638.628 169.9 639.3 170.572 639.3 171.4V197C639.3 197.828 638.628 198.5 637.8 198.5H553.48Z" stroke="url(#paint0_diamond_5217_1511)"/>
</g>
<g style="mix-blend-mode:plus-lighter">
<path d="M556.834 196C555.821 196 555 195.177 555 194.162V55.8378C555 54.8228 555.821 54 556.834 54H634.166C635.179 54 636 54.8228 636 55.8378V76.3622C636 77.3772 635.179 78.2 634.166 78.2H579.834C578.821 78.2 578 79.0228 578 80.0378V111.562C578 112.577 578.821 113.4 579.834 113.4H634.166C635.179 113.4 636 114.223 636 115.238V134.762C636 135.777 635.179 136.6 634.166 136.6H579.834C578.821 136.6 578 137.423 578 138.438V169.962C578 170.977 578.821 171.8 579.834 171.8H635.166C636.179 171.8 637 172.623 637 173.638V194.162C637 195.177 636.179 196 635.166 196H556.834Z" fill="url(#paint1_linear_5217_1511)" fill-opacity="0.8"/>
</g>
<g filter="url(#filter1_b_5217_1511)">
<path d="M671.24 110.2C670.136 110.2 669.24 109.305 669.24 108.2V53C669.24 51.8954 670.136 51 671.24 51H696.68C697.785 51 698.68 51.8954 698.68 53V110.2H671.24ZM757.56 110.2V53C757.56 51.8954 758.456 51 759.56 51H785C786.105 51 787 51.8954 787 53V108.2C787 109.305 786.105 110.2 785 110.2H757.56ZM698.68 139.8V110.2H757.56V139.8H698.68ZM671.24 199C670.136 199 669.24 198.105 669.24 197V141.8C669.24 140.696 670.136 139.8 671.24 139.8H698.68V197C698.68 198.105 697.785 199 696.68 199H671.24ZM759.56 199C758.456 199 757.56 198.105 757.56 197V139.8H785C786.105 139.8 787 140.696 787 141.8V197C787 198.105 786.105 199 785 199H759.56Z" fill="#BDB4E1" fill-opacity="0.03"/>
<path d="M671.24 109.7C670.412 109.7 669.74 109.029 669.74 108.2V53C669.74 52.1716 670.412 51.5 671.24 51.5H696.68C697.509 51.5 698.18 52.1716 698.18 53V109.7H671.24ZM699.18 110.7H757.06V139.3H699.18V110.7ZM671.24 140.3H698.18V197C698.18 197.828 697.509 198.5 696.68 198.5H671.24C670.412 198.5 669.74 197.828 669.74 197V141.8C669.74 140.972 670.412 140.3 671.24 140.3ZM758.06 197V140.3H785C785.829 140.3 786.5 140.972 786.5 141.8V197C786.5 197.828 785.829 198.5 785 198.5H759.56C758.732 198.5 758.06 197.828 758.06 197ZM758.06 109.7V53C758.06 52.1716 758.732 51.5 759.56 51.5H785C785.829 51.5 786.5 52.1716 786.5 53V108.2C786.5 109.029 785.829 109.7 785 109.7H758.06Z" stroke="#BAC7F7" stroke-opacity="0.32"/>
<path d="M671.24 109.7C670.412 109.7 669.74 109.029 669.74 108.2V53C669.74 52.1716 670.412 51.5 671.24 51.5H696.68C697.509 51.5 698.18 52.1716 698.18 53V109.7H671.24ZM699.18 110.7H757.06V139.3H699.18V110.7ZM671.24 140.3H698.18V197C698.18 197.828 697.509 198.5 696.68 198.5H671.24C670.412 198.5 669.74 197.828 669.74 197V141.8C669.74 140.972 670.412 140.3 671.24 140.3ZM758.06 197V140.3H785C785.829 140.3 786.5 140.972 786.5 141.8V197C786.5 197.828 785.829 198.5 785 198.5H759.56C758.732 198.5 758.06 197.828 758.06 197ZM758.06 109.7V53C758.06 52.1716 758.732 51.5 759.56 51.5H785C785.829 51.5 786.5 52.1716 786.5 53V108.2C786.5 109.029 785.829 109.7 785 109.7H758.06Z" stroke="url(#paint2_diamond_5217_1511)"/>
</g>
<g style="mix-blend-mode:plus-lighter">
<path d="M674.834 111.4C673.821 111.4 673 110.577 673 109.562V55.8378C673 54.8228 673.821 54 674.834 54H693.166C694.179 54 695 54.8228 695 55.8378V111.4H674.834ZM761 111.4V55.8378C761 54.8228 761.821 54 762.834 54H781.166C782.179 54 783 54.8228 783 55.8378V109.562C783 110.577 782.179 111.4 781.166 111.4H761ZM695 142.6V111.4H761V142.6H695ZM674.834 196C673.821 196 673 195.177 673 194.162V144.438C673 143.423 673.821 142.6 674.834 142.6H695V194.162C695 195.177 694.179 196 693.166 196H674.834ZM762.834 196C761.821 196 761 195.177 761 194.162V142.6H781.166C782.179 142.6 783 143.423 783 144.438V194.162C783 195.177 782.179 196 781.166 196H762.834Z" fill="url(#paint3_linear_5217_1511)" fill-opacity="0.8"/>
</g>
<g filter="url(#filter2_b_5217_1511)">
<path d="M200.2 199C199.096 199 198.2 198.105 198.2 197V53C198.2 51.8954 199.096 51 200.2 51H284.52C285.625 51 286.52 51.8954 286.52 53V78.6C286.52 79.7046 285.625 80.6 284.52 80.6H229.64C228.536 80.6 227.64 81.4954 227.64 82.6V108.2C227.64 109.305 228.536 110.2 229.64 110.2H284.52C285.625 110.2 286.52 111.096 286.52 112.2V137.8C286.52 138.905 285.625 139.8 284.52 139.8H229.64C228.536 139.8 227.64 140.696 227.64 141.8V167.4C227.64 168.505 228.536 169.4 229.64 169.4H284.52C285.625 169.4 286.52 170.296 286.52 171.4V197C286.52 198.105 285.625 199 284.52 199H200.2Z" fill="#BDB4E1" fill-opacity="0.03"/>
<path d="M200.2 198.5C199.372 198.5 198.7 197.828 198.7 197V53C198.7 52.1716 199.372 51.5 200.2 51.5H284.52C285.349 51.5 286.02 52.1716 286.02 53V78.6C286.02 79.4284 285.349 80.1 284.52 80.1H229.64C228.259 80.1 227.14 81.2193 227.14 82.6V108.2C227.14 109.581 228.259 110.7 229.64 110.7H284.52C285.349 110.7 286.02 111.372 286.02 112.2V137.8C286.02 138.629 285.349 139.3 284.52 139.3H229.64C228.259 139.3 227.14 140.419 227.14 141.8V167.4C227.14 168.781 228.259 169.9 229.64 169.9H284.52C285.349 169.9 286.02 170.572 286.02 171.4V197C286.02 197.828 285.349 198.5 284.52 198.5H200.2Z" stroke="#BAC7F7" stroke-opacity="0.32"/>
<path d="M200.2 198.5C199.372 198.5 198.7 197.828 198.7 197V53C198.7 52.1716 199.372 51.5 200.2 51.5H284.52C285.349 51.5 286.02 52.1716 286.02 53V78.6C286.02 79.4284 285.349 80.1 284.52 80.1H229.64C228.259 80.1 227.14 81.2193 227.14 82.6V108.2C227.14 109.581 228.259 110.7 229.64 110.7H284.52C285.349 110.7 286.02 111.372 286.02 112.2V137.8C286.02 138.629 285.349 139.3 284.52 139.3H229.64C228.259 139.3 227.14 140.419 227.14 141.8V167.4C227.14 168.781 228.259 169.9 229.64 169.9H284.52C285.349 169.9 286.02 170.572 286.02 171.4V197C286.02 197.828 285.349 198.5 284.52 198.5H200.2Z" stroke="url(#paint4_diamond_5217_1511)"/>
</g>
<g style="mix-blend-mode:plus-lighter">
<path d="M203 196C201.895 196 201 195.105 201 194V56C201 54.8954 201.895 54 203 54H282C283.105 54 284 54.8954 284 56V76.4C284 77.5046 283.105 78.4 282 78.4H226.333C225.229 78.4 224.333 79.2954 224.333 80.4V110.8C224.333 111.905 225.229 112.8 226.333 112.8H282C283.105 112.8 284 113.696 284 114.8V135.2C284 136.305 283.105 137.2 282 137.2H226.333C225.229 137.2 224.333 138.096 224.333 139.2V169.6C224.333 170.705 225.229 171.6 226.333 171.6H282C283.105 171.6 284 172.496 284 173.6V194C284 195.105 283.105 196 282 196H203Z" fill="url(#paint5_linear_5217_1511)" fill-opacity="0.8"/>
</g>
<g filter="url(#filter3_b_5217_1511)">
<path d="M317.96 199C316.855 199 315.96 198.105 315.96 197V53C315.96 51.8954 316.855 51 317.96 51H402.28C403.385 51 404.28 51.8954 404.28 53V78.6C404.28 79.7046 403.385 80.6 402.28 80.6H347.4C346.295 80.6 345.4 81.4954 345.4 82.6V108.2C345.4 109.305 346.295 110.2 347.4 110.2H402.28C403.385 110.2 404.28 111.096 404.28 112.2V137.8C404.28 138.905 403.385 139.8 402.28 139.8H347.4C346.295 139.8 345.4 140.696 345.4 141.8V197C345.4 198.105 344.505 199 343.4 199H317.96Z" fill="#BDB4E1" fill-opacity="0.03"/>
<path d="M317.96 198.5C317.132 198.5 316.46 197.828 316.46 197V53C316.46 52.1716 317.132 51.5 317.96 51.5H402.28C403.108 51.5 403.78 52.1716 403.78 53V78.6C403.78 79.4284 403.108 80.1 402.28 80.1H347.4C346.019 80.1 344.9 81.2193 344.9 82.6V108.2C344.9 109.581 346.019 110.7 347.4 110.7H402.28C403.108 110.7 403.78 111.372 403.78 112.2V137.8C403.78 138.629 403.108 139.3 402.28 139.3H347.4C346.019 139.3 344.9 140.419 344.9 141.8V197C344.9 197.828 344.228 198.5 343.4 198.5H317.96Z" stroke="#BAC7F7" stroke-opacity="0.32"/>
<path d="M317.96 198.5C317.132 198.5 316.46 197.828 316.46 197V53C316.46 52.1716 317.132 51.5 317.96 51.5H402.28C403.108 51.5 403.78 52.1716 403.78 53V78.6C403.78 79.4284 403.108 80.1 402.28 80.1H347.4C346.019 80.1 344.9 81.2193 344.9 82.6V108.2C344.9 109.581 346.019 110.7 347.4 110.7H402.28C403.108 110.7 403.78 111.372 403.78 112.2V137.8C403.78 138.629 403.108 139.3 402.28 139.3H347.4C346.019 139.3 344.9 140.419 344.9 141.8V197C344.9 197.828 344.228 198.5 343.4 198.5H317.96Z" stroke="url(#paint6_diamond_5217_1511)"/>
</g>
<g style="mix-blend-mode:plus-lighter">
<path d="M321 196C319.895 196 319 195.105 319 194V56C319 54.8954 319.895 54 321 54H398C399.105 54 400 54.8954 400 56V75.6C400 76.7046 399.105 77.6 398 77.6H344.333C343.229 77.6 342.333 78.4954 342.333 79.6V111.2C342.333 112.305 343.229 113.2 344.333 113.2H398C399.105 113.2 400 114.096 400 115.2V134.8C400 135.905 399.105 136.8 398 136.8H344.333C343.229 136.8 342.333 137.696 342.333 138.8V194C342.333 195.105 341.438 196 340.333 196H321Z" fill="url(#paint7_linear_5217_1511)" fill-opacity="0.8"/>
</g>
<g filter="url(#filter4_b_5217_1511)">
<path d="M435.72 199C434.615 199 433.72 198.105 433.72 197V53C433.72 51.8954 434.615 51 435.72 51H461.16C462.264 51 463.16 51.8954 463.16 53V167.4C463.16 168.505 464.055 169.4 465.16 169.4H520.04C521.144 169.4 522.04 170.296 522.04 171.4V197C522.04 198.105 521.144 199 520.04 199H435.72Z" fill="#BDB4E1" fill-opacity="0.03"/>
<path d="M435.72 198.5C434.891 198.5 434.22 197.828 434.22 197V53C434.22 52.1716 434.891 51.5 435.72 51.5H461.16C461.988 51.5 462.66 52.1716 462.66 53V167.4C462.66 168.781 463.779 169.9 465.16 169.9H520.04C520.868 169.9 521.54 170.572 521.54 171.4V197C521.54 197.828 520.868 198.5 520.04 198.5H435.72Z" stroke="#BAC7F7" stroke-opacity="0.32"/>
<path d="M435.72 198.5C434.891 198.5 434.22 197.828 434.22 197V53C434.22 52.1716 434.891 51.5 435.72 51.5H461.16C461.988 51.5 462.66 52.1716 462.66 53V167.4C462.66 168.781 463.779 169.9 465.16 169.9H520.04C520.868 169.9 521.54 170.572 521.54 171.4V197C521.54 197.828 520.868 198.5 520.04 198.5H435.72Z" stroke="url(#paint8_diamond_5217_1511)"/>
</g>
<g style="mix-blend-mode:plus-lighter">
<path d="M438.857 196C437.831 196 437 195.165 437 194.135V55.8649C437 54.8349 437.831 54 438.857 54H457.476C458.502 54 459.333 54.8349 459.333 55.8649V170.535C459.333 171.565 460.165 172.4 461.19 172.4H518.143C519.169 172.4 520 173.235 520 174.265V194.135C520 195.165 519.169 196 518.143 196H438.857Z" fill="url(#paint9_linear_5217_1511)" fill-opacity="0.8"/>
</g>
<g filter="url(#filter5_b_5217_1511)">
<path d="M53 199C51.8954 199 51 198.105 51 197V53C51 51.8954 51.8954 51 53 51H166.76C167.865 51 168.76 51.8954 168.76 53V108.2C168.76 109.305 167.865 110.2 166.76 110.2H139.32V82.6C139.32 81.4954 138.425 80.6 137.32 80.6H82.44C81.3354 80.6 80.44 81.4954 80.44 82.6V108.2C80.44 109.305 81.3354 110.2 82.44 110.2H139.32V139.8H82.44C81.3354 139.8 80.44 140.696 80.44 141.8V197C80.44 198.105 79.5446 199 78.44 199H53ZM141.32 199C140.215 199 139.32 198.105 139.32 197V139.8H166.76C167.865 139.8 168.76 140.696 168.76 141.8V197C168.76 198.105 167.865 199 166.76 199H141.32Z" fill="#BDB4E1" fill-opacity="0.03"/>
<path d="M53 198.5C52.1716 198.5 51.5 197.828 51.5 197V53C51.5 52.1716 52.1716 51.5 53 51.5H166.76C167.588 51.5 168.26 52.1716 168.26 53V108.2C168.26 109.029 167.588 109.7 166.76 109.7H139.82V82.6C139.82 81.2193 138.701 80.1 137.32 80.1H82.44C81.0593 80.1 79.94 81.2193 79.94 82.6V108.2C79.94 109.581 81.0593 110.7 82.44 110.7H138.82V139.3H82.44C81.0593 139.3 79.94 140.419 79.94 141.8V197C79.94 197.828 79.2684 198.5 78.44 198.5H53ZM139.82 140.3H166.76C167.588 140.3 168.26 140.972 168.26 141.8V197C168.26 197.828 167.588 198.5 166.76 198.5H141.32C140.492 198.5 139.82 197.828 139.82 197V140.3Z" stroke="#BAC7F7" stroke-opacity="0.32"/>
<path d="M53 198.5C52.1716 198.5 51.5 197.828 51.5 197V53C51.5 52.1716 52.1716 51.5 53 51.5H166.76C167.588 51.5 168.26 52.1716 168.26 53V108.2C168.26 109.029 167.588 109.7 166.76 109.7H139.82V82.6C139.82 81.2193 138.701 80.1 137.32 80.1H82.44C81.0593 80.1 79.94 81.2193 79.94 82.6V108.2C79.94 109.581 81.0593 110.7 82.44 110.7H138.82V139.3H82.44C81.0593 139.3 79.94 140.419 79.94 141.8V197C79.94 197.828 79.2684 198.5 78.44 198.5H53ZM139.82 140.3H166.76C167.588 140.3 168.26 140.972 168.26 141.8V197C168.26 197.828 167.588 198.5 166.76 198.5H141.32C140.492 198.5 139.82 197.828 139.82 197V140.3Z" stroke="url(#paint10_diamond_5217_1511)"/>
</g>
<g filter="url(#filter6_bdi_5217_1511)">
<path d="M556.834 196C555.821 196 555 195.177 555 194.162V55.8378C555 54.8228 555.821 54 556.834 54H634.166C635.179 54 636 54.8228 636 55.8378V76.3622C636 77.3772 635.179 78.2 634.166 78.2H579.834C578.821 78.2 578 79.0228 578 80.0378V111.562C578 112.577 578.821 113.4 579.834 113.4H634.166C635.179 113.4 636 114.223 636 115.238V134.762C636 135.777 635.179 136.6 634.166 136.6H579.834C578.821 136.6 578 137.423 578 138.438V169.962C578 170.977 578.821 171.8 579.834 171.8H635.166C636.179 171.8 637 172.623 637 173.638V194.162C637 195.177 636.179 196 635.166 196H556.834Z" fill="url(#paint11_linear_5217_1511)" fill-opacity="0.8" shape-rendering="crispEdges"/>
<path d="M674.834 111.4C673.821 111.4 673 110.577 673 109.562V55.8378C673 54.8228 673.821 54 674.834 54H693.166C694.179 54 695 54.8228 695 55.8378V111.4H674.834ZM761 111.4V55.8378C761 54.8228 761.821 54 762.834 54H781.166C782.179 54 783 54.8228 783 55.8378V109.562C783 110.577 782.179 111.4 781.166 111.4H761ZM695 142.6V111.4H761V142.6H695ZM674.834 196C673.821 196 673 195.177 673 194.162V144.438C673 143.423 673.821 142.6 674.834 142.6H695V194.162C695 195.177 694.179 196 693.166 196H674.834ZM762.834 196C761.821 196 761 195.177 761 194.162V142.6H781.166C782.179 142.6 783 143.423 783 144.438V194.162C783 195.177 782.179 196 781.166 196H762.834Z" fill="url(#paint12_linear_5217_1511)" fill-opacity="0.8" shape-rendering="crispEdges"/>
<path d="M203 196C201.895 196 201 195.105 201 194V56C201 54.8954 201.895 54 203 54H282C283.105 54 284 54.8954 284 56V76.4C284 77.5046 283.105 78.4 282 78.4H226.333C225.229 78.4 224.333 79.2954 224.333 80.4V110.8C224.333 111.905 225.229 112.8 226.333 112.8H282C283.105 112.8 284 113.696 284 114.8V135.2C284 136.305 283.105 137.2 282 137.2H226.333C225.229 137.2 224.333 138.096 224.333 139.2V169.6C224.333 170.705 225.229 171.6 226.333 171.6H282C283.105 171.6 284 172.496 284 173.6V194C284 195.105 283.105 196 282 196H203Z" fill="url(#paint13_linear_5217_1511)" fill-opacity="0.8" shape-rendering="crispEdges"/>
<path d="M321 196C319.895 196 319 195.105 319 194V56C319 54.8954 319.895 54 321 54H398C399.105 54 400 54.8954 400 56V75.6C400 76.7046 399.105 77.6 398 77.6H344.333C343.229 77.6 342.333 78.4954 342.333 79.6V111.2C342.333 112.305 343.229 113.2 344.333 113.2H398C399.105 113.2 400 114.096 400 115.2V134.8C400 135.905 399.105 136.8 398 136.8H344.333C343.229 136.8 342.333 137.696 342.333 138.8V194C342.333 195.105 341.438 196 340.333 196H321Z" fill="url(#paint14_linear_5217_1511)" fill-opacity="0.8" shape-rendering="crispEdges"/>
<path d="M438.857 196C437.831 196 437 195.165 437 194.135V55.8649C437 54.8349 437.831 54 438.857 54H457.476C458.502 54 459.333 54.8349 459.333 55.8649V170.535C459.333 171.565 460.165 172.4 461.19 172.4H518.143C519.169 172.4 520 173.235 520 174.265V194.135C520 195.165 519.169 196 518.143 196H438.857Z" fill="url(#paint15_linear_5217_1511)" fill-opacity="0.8" shape-rendering="crispEdges"/>
<path d="M56 196C54.8954 196 54 195.105 54 194V56C54 54.8954 54.8954 54 56 54H163C164.105 54 165 54.8954 165 56V112C165 113.105 164.105 114 163 114H143V78C143 76.8954 142.105 76 141 76H78C76.8954 76 76 76.8954 76 78V112C76 113.105 76.8954 114 78 114H143V136H78C76.8954 136 76 136.896 76 138V194C76 195.105 75.1046 196 74 196H56ZM145 196C143.895 196 143 195.105 143 194V136H163C164.105 136 165 136.896 165 138V194C165 195.105 164.105 196 163 196H145Z" fill="url(#paint16_linear_5217_1511)" fill-opacity="0.8" shape-rendering="crispEdges"/>
</g>
<g style="mix-blend-mode:plus-lighter" filter="url(#filter7_f_5217_1511)">
<path d="M556.834 196C555.821 196 555 195.177 555 194.162V55.8378C555 54.8228 555.821 54 556.834 54H634.166C635.179 54 636 54.8228 636 55.8378V76.3622C636 77.3772 635.179 78.2 634.166 78.2H579.834C578.821 78.2 578 79.0228 578 80.0378V111.562C578 112.577 578.821 113.4 579.834 113.4H634.166C635.179 113.4 636 114.223 636 115.238V134.762C636 135.777 635.179 136.6 634.166 136.6H579.834C578.821 136.6 578 137.423 578 138.438V169.962C578 170.977 578.821 171.8 579.834 171.8H635.166C636.179 171.8 637 172.623 637 173.638V194.162C637 195.177 636.179 196 635.166 196H556.834Z" fill="url(#paint17_linear_5217_1511)" fill-opacity="0.8"/>
<path d="M674.834 111.4C673.821 111.4 673 110.577 673 109.562V55.8378C673 54.8228 673.821 54 674.834 54H693.166C694.179 54 695 54.8228 695 55.8378V111.4H674.834ZM761 111.4V55.8378C761 54.8228 761.821 54 762.834 54H781.166C782.179 54 783 54.8228 783 55.8378V109.562C783 110.577 782.179 111.4 781.166 111.4H761ZM695 142.6V111.4H761V142.6H695ZM674.834 196C673.821 196 673 195.177 673 194.162V144.438C673 143.423 673.821 142.6 674.834 142.6H695V194.162C695 195.177 694.179 196 693.166 196H674.834ZM762.834 196C761.821 196 761 195.177 761 194.162V142.6H781.166C782.179 142.6 783 143.423 783 144.438V194.162C783 195.177 782.179 196 781.166 196H762.834Z" fill="url(#paint18_linear_5217_1511)" fill-opacity="0.8"/>
<path d="M203 196C201.895 196 201 195.105 201 194V56C201 54.8954 201.895 54 203 54H282C283.105 54 284 54.8954 284 56V76.4C284 77.5046 283.105 78.4 282 78.4H226.333C225.229 78.4 224.333 79.2954 224.333 80.4V110.8C224.333 111.905 225.229 112.8 226.333 112.8H282C283.105 112.8 284 113.696 284 114.8V135.2C284 136.305 283.105 137.2 282 137.2H226.333C225.229 137.2 224.333 138.096 224.333 139.2V169.6C224.333 170.705 225.229 171.6 226.333 171.6H282C283.105 171.6 284 172.496 284 173.6V194C284 195.105 283.105 196 282 196H203Z" fill="url(#paint19_linear_5217_1511)" fill-opacity="0.8"/>
<path d="M321 196C319.895 196 319 195.105 319 194V56C319 54.8954 319.895 54 321 54H398C399.105 54 400 54.8954 400 56V75.6C400 76.7046 399.105 77.6 398 77.6H344.333C343.229 77.6 342.333 78.4954 342.333 79.6V111.2C342.333 112.305 343.229 113.2 344.333 113.2H398C399.105 113.2 400 114.096 400 115.2V134.8C400 135.905 399.105 136.8 398 136.8H344.333C343.229 136.8 342.333 137.696 342.333 138.8V194C342.333 195.105 341.438 196 340.333 196H321Z" fill="url(#paint20_linear_5217_1511)" fill-opacity="0.8"/>
<path d="M438.857 196C437.831 196 437 195.165 437 194.135V55.8649C437 54.8349 437.831 54 438.857 54H457.476C458.502 54 459.333 54.8349 459.333 55.8649V170.535C459.333 171.565 460.165 172.4 461.19 172.4H518.143C519.169 172.4 520 173.235 520 174.265V194.135C520 195.165 519.169 196 518.143 196H438.857Z" fill="url(#paint21_linear_5217_1511)" fill-opacity="0.8"/>
<path d="M56 196C54.8954 196 54 195.105 54 194V56C54 54.8954 54.8954 54 56 54H163C164.105 54 165 54.8954 165 56V112C165 113.105 164.105 114 163 114H143V78C143 76.8954 142.105 76 141 76H78C76.8954 76 76 76.8954 76 78V112C76 113.105 76.8954 114 78 114H143V136H78C76.8954 136 76 136.896 76 138V194C76 195.105 75.1046 196 74 196H56ZM145 196C143.895 196 143 195.105 143 194V136H163C164.105 136 165 136.896 165 138V194C165 195.105 164.105 196 163 196H145Z" fill="url(#paint22_linear_5217_1511)" fill-opacity="0.8"/>
</g>
<g style="mix-blend-mode:plus-lighter">
<path d="M56 196C54.8954 196 54 195.105 54 194V56C54 54.8954 54.8954 54 56 54H163C164.105 54 165 54.8954 165 56V112C165 113.105 164.105 114 163 114H143V78C143 76.8954 142.105 76 141 76H78C76.8954 76 76 76.8954 76 78V112C76 113.105 76.8954 114 78 114H143V136H109.5H78C76.8954 136 76 136.896 76 138V194C76 195.105 75.1046 196 74 196H56ZM145 196C143.895 196 143 195.105 143 194V136H163C164.105 136 165 136.896 165 138V194C165 195.105 164.105 196 163 196H145Z" fill="url(#paint23_linear_5217_1511)" fill-opacity="0.8"/>
</g>
<defs>
<filter id="filter0_b_5217_1511" x="547.48" y="47" width="96.3198" height="156" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feGaussianBlur in="BackgroundImageFix" stdDeviation="2"/>
<feComposite in2="SourceAlpha" operator="in" result="effect1_backgroundBlur_5217_1511"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect1_backgroundBlur_5217_1511" result="shape"/>
</filter>
<filter id="filter1_b_5217_1511" x="665.24" y="47" width="125.76" height="156" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feGaussianBlur in="BackgroundImageFix" stdDeviation="2"/>
<feComposite in2="SourceAlpha" operator="in" result="effect1_backgroundBlur_5217_1511"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect1_backgroundBlur_5217_1511" result="shape"/>
</filter>
<filter id="filter2_b_5217_1511" x="194.2" y="47" width="96.3198" height="156" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feGaussianBlur in="BackgroundImageFix" stdDeviation="2"/>
<feComposite in2="SourceAlpha" operator="in" result="effect1_backgroundBlur_5217_1511"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect1_backgroundBlur_5217_1511" result="shape"/>
</filter>
<filter id="filter3_b_5217_1511" x="311.96" y="47" width="96.3198" height="156" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feGaussianBlur in="BackgroundImageFix" stdDeviation="2"/>
<feComposite in2="SourceAlpha" operator="in" result="effect1_backgroundBlur_5217_1511"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect1_backgroundBlur_5217_1511" result="shape"/>
</filter>
<filter id="filter4_b_5217_1511" x="429.72" y="47" width="96.3198" height="156" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feGaussianBlur in="BackgroundImageFix" stdDeviation="2"/>
<feComposite in2="SourceAlpha" operator="in" result="effect1_backgroundBlur_5217_1511"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect1_backgroundBlur_5217_1511" result="shape"/>
</filter>
<filter id="filter5_b_5217_1511" x="47" y="47" width="125.76" height="156" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feGaussianBlur in="BackgroundImageFix" stdDeviation="2"/>
<feComposite in2="SourceAlpha" operator="in" result="effect1_backgroundBlur_5217_1511"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect1_backgroundBlur_5217_1511" result="shape"/>
</filter>
<filter id="filter6_bdi_5217_1511" x="48" y="50" width="743" height="159" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feGaussianBlur in="BackgroundImageFix" stdDeviation="2"/>
<feComposite in2="SourceAlpha" operator="in" result="effect1_backgroundBlur_5217_1511"/>
<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
<feOffset dx="1" dy="6"/>
<feGaussianBlur stdDeviation="3.5"/>
<feComposite in2="hardAlpha" operator="out"/>
<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
<feBlend mode="normal" in2="effect1_backgroundBlur_5217_1511" result="effect2_dropShadow_5217_1511"/>
<feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_5217_1511" result="shape"/>
<feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
<feOffset dy="3"/>
<feGaussianBlur stdDeviation="2.5"/>
<feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
<feColorMatrix type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.14 0"/>
<feBlend mode="normal" in2="shape" result="effect3_innerShadow_5217_1511"/>
</filter>
<filter id="filter7_f_5217_1511" x="0" y="0" width="837" height="250" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
<feFlood flood-opacity="0" result="BackgroundImageFix"/>
<feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
<feGaussianBlur stdDeviation="27" result="effect1_foregroundBlur_5217_1511"/>
</filter>
<radialGradient id="paint0_diamond_5217_1511" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(576.98 45.5) rotate(2.41334) scale(130.616 104.678)">
<stop stop-color="#8F93BC"/>
<stop offset="0.32983" stop-color="#656484"/>
<stop offset="0.80622" stop-color="#232329" stop-opacity="0.08"/>
<stop offset="1" stop-color="#131217" stop-opacity="0"/>
</radialGradient>
<linearGradient id="paint1_linear_5217_1511" x1="540.595" y1="23.5" x2="633.267" y2="108.136" gradientUnits="userSpaceOnUse">
<stop stop-color="white"/>
<stop offset="1" stop-color="#5D4EF1" stop-opacity="0.2"/>
</linearGradient>
<radialGradient id="paint2_diamond_5217_1511" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(703.24 45.5) rotate(1.81047) scale(174.087 104.719)">
<stop stop-color="#8F93BC"/>
<stop offset="0.32983" stop-color="#656484"/>
<stop offset="0.80622" stop-color="#232329" stop-opacity="0.08"/>
<stop offset="1" stop-color="#131217" stop-opacity="0"/>
</radialGradient>
<linearGradient id="paint3_linear_5217_1511" x1="653.676" y1="23.5" x2="744.844" y2="135.193" gradientUnits="userSpaceOnUse">
<stop stop-color="white"/>
<stop offset="1" stop-color="#5D4EF1" stop-opacity="0.2"/>
</linearGradient>
<radialGradient id="paint4_diamond_5217_1511" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(223.7 45.5) rotate(2.41334) scale(130.616 104.678)">
<stop stop-color="#8F93BC"/>
<stop offset="0.32983" stop-color="#656484"/>
<stop offset="0.80622" stop-color="#232329" stop-opacity="0.08"/>
<stop offset="1" stop-color="#131217" stop-opacity="0"/>
</radialGradient>
<linearGradient id="paint5_linear_5217_1511" x1="186.419" y1="23.5" x2="279.187" y2="109.256" gradientUnits="userSpaceOnUse">
<stop stop-color="white"/>
<stop offset="1" stop-color="#5D4EF1" stop-opacity="0.2"/>
</linearGradient>
<radialGradient id="paint6_diamond_5217_1511" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(341.46 45.5) rotate(2.41334) scale(130.616 104.678)">
<stop stop-color="#8F93BC"/>
<stop offset="0.32983" stop-color="#656484"/>
<stop offset="0.80622" stop-color="#232329" stop-opacity="0.08"/>
<stop offset="1" stop-color="#131217" stop-opacity="0"/>
</radialGradient>
<linearGradient id="paint7_linear_5217_1511" x1="304.77" y1="23.5" x2="397.333" y2="107.005" gradientUnits="userSpaceOnUse">
<stop stop-color="white"/>
<stop offset="1" stop-color="#5D4EF1" stop-opacity="0.2"/>
</linearGradient>
<radialGradient id="paint8_diamond_5217_1511" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(459.22 45.5) rotate(2.41334) scale(130.616 104.678)">
<stop stop-color="#8F93BC"/>
<stop offset="0.32983" stop-color="#656484"/>
<stop offset="0.80622" stop-color="#232329" stop-opacity="0.08"/>
<stop offset="1" stop-color="#131217" stop-opacity="0"/>
</radialGradient>
<linearGradient id="paint9_linear_5217_1511" x1="422.419" y1="23.5" x2="515.187" y2="109.256" gradientUnits="userSpaceOnUse">
<stop stop-color="white"/>
<stop offset="1" stop-color="#5D4EF1" stop-opacity="0.2"/>
</linearGradient>
<radialGradient id="paint10_diamond_5217_1511" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(85 45.5) rotate(1.81047) scale(174.087 104.719)">
<stop stop-color="#8F93BC"/>
<stop offset="0.32983" stop-color="#656484"/>
<stop offset="0.80622" stop-color="#232329" stop-opacity="0.08"/>
<stop offset="1" stop-color="#131217" stop-opacity="0"/>
</radialGradient>
<linearGradient id="paint11_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint12_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint13_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint14_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint15_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint16_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint17_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint18_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint19_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint20_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint21_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint22_linear_5217_1511" x1="275.5" y1="-21.5" x2="554.113" y2="292.876" gradientUnits="userSpaceOnUse">
<stop stop-color="#5D4EF1"/>
<stop offset="1" stop-color="#FF8C23"/>
</linearGradient>
<linearGradient id="paint23_linear_5217_1511" x1="34.5" y1="23.5" x2="154.5" y2="130.5" gradientUnits="userSpaceOnUse">
<stop stop-color="white"/>
<stop offset="1" stop-color="#F1894E" stop-opacity="0.2"/>
</linearGradient>
</defs>
</svg>
"""
                   )

def spacer_box_will_fix_later():
    return rx.box(height="60px")

@webpage(path="/", title="Reflex · Web apps in Pure Python")
def index() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.vstack(
        rx.vstack(
            landing(),
            rx.vstack(
                rx.hstack(
                    rx.button(
                        "Frontend",
                        color="848496",
                        border_radius="50px;",
                        border="1px solid rgba(186, 199, 247, 0.12);",
                        background= "rgba(161, 157, 213, 0.03);",
                        backdrop_filter= "blur(2px);"
                    ),
                    rx.button(
                        "Backend",
                        color="848496",
                        border_radius="50px;",
                        border="1px solid rgba(186, 199, 247, 0.12);",
                        background= "rgba(161, 157, 213, 0.03);",
                        backdrop_filter= "blur(2px);"
                    ),
                    rx.button(
                        "Hosting",
                        color="848496",
                        border_radius="50px;",
                        border="1px solid rgba(186, 199, 247, 0.12);",
                        background= "rgba(161, 157, 213, 0.03);",
                        backdrop_filter= "blur(2px);"
                    ),
                ),
                rx.chakra.text(
                    "Web apps in Pure Python.",
                    font_size="54px;",
                    background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%);",
                    text_align="left",
                    background_clip="text",
                    font_weight="bold",
                    line_height="1",
                ),
                rx.chakra.text(
                        "Deploy with a single command.",
                        font_size="54px;",
                        max_width="650px",
                        color="#6C6C81",
                        text_align="left",
                        font_weight="bold",
                        line_height="1",
                ),
                rx.hstack(
                    rx.button(
                        "Get Started", 
                        border_radius= "8px",
                        padding_x="2em",
                        background="linear-gradient(180deg, #6151F3 0%, #5646ED 100%);",
                        box_shadow="0px 2px 9px -4px rgba(64, 51, 192, 0.70), 0px 0px 6px 2px rgba(255, 255, 255, 0.12) inset, 0px 0px 0px 1px rgba(255, 255, 255, 0.09) inset;",
                        _hover={}
                    ),
                    rx.button(
                        rx.link(
                            "Get a demo",
                            href="https://5dha7vttyp3.typeform.com/to/hQDMLKdX",
                            color="white"
                        ),
                        border_radius="8px;",
                        border="1px solid rgba(186, 199, 247, 0.12);",
                        background= "rgba(161, 157, 213, 0.03);",
                        backdrop_filter= "blur(2px);"
                    ),
                    padding_top="1em",
                ),
                padding_left="3em",
                align_items="left",
            ),
            align_items="left",
            padding_top="5em",
            padding_bottom="5em",
        ),
        demos(),
        spacer_box_will_fix_later(),
        stats(),

        width="100%",
    )






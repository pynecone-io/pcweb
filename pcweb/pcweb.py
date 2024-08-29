"""The main Reflex website."""

import os
import sys

import reflex as rx
from pcweb import styles
from pcweb.pages import page404, routes
from pcweb.pages.docs import outblocks, exec_blocks
from pcweb.whitelist import _check_whitelisted_path
from pcweb.scripts import get_pixel_website_trackers

# This number discovered by trial and error on Windows 11 w/ Node 18, any
# higher and the prod build fails with EMFILE error.
WINDOWS_MAX_ROUTES = 125


# Execute all the exec blocks in the documents.
for doc, href in outblocks:
    exec_blocks(doc, href)

# Create the app.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
    theme=rx.theme(
        has_background=True,
        radius="large",
        accent_color="violet",
    ),
    head_components=get_pixel_website_trackers(),
)


# XXX: The app is TOO BIG to build on Windows, so explicitly disallow it except for testing
if sys.platform == "win32":
    if not os.environ.get("REFLEX_WEB_WINDOWS_OVERRIDE"):
        raise RuntimeError(
            "reflex-web cannot be built on Windows due to EMFILE error. To build a "
            "subset of pages for testing, set environment variable REFLEX_WEB_WINDOWS_OVERRIDE."
        )
    routes = routes[:WINDOWS_MAX_ROUTES]


# Add the pages to the app.
for route in routes:
    if _check_whitelisted_path(route.path):
        app.add_page(
            route.component,
            route.path,
            route.title,
            image="/previews/index_preview.png",
            meta=[
                {"name": "theme-color", "content": route.background_color},
            ],
        )

# Add redirects
redirects = [
    ("/docs", "/docs/getting-started/introduction"),
    ("/docs/getting-started", "/docs/getting-started/introduction"),
    ("/docs/components", "/docs/components/overview"),
    ("/docs/state", "/docs/state/overview"),
    ("/docs/styling", "/docs/styling/overview"),
    ("/docs/database", "/docs/database/overview"),
    ("/docs/hosting", "/docs/hosting/self-hosting"),
    ("/docs/advanced-guide", "/docs/advanced-guide/custom-vars"),
    ("/docs/library/typography", "/docs/library/typography/text"),
    ("/docs/library/forms", "/docs/library/forms/form"),
    ("/docs/library/layout", "/docs/library/layout/box"),
    ("/docs/library/navigation", "/docs/library/navigation/link"),
    ("/docs/library/datadisplay", "/docs/library/datadisplay/badge"),
    ("/docs/library/graphing", "/docs/library/graphing/chart"),
    ("/docs/library/disclosure", "/docs/library/disclosure/accordion"),
    ("/docs/library/feedback", "/docs/library/feedback/alert"),
    ("/docs/library/media", "/docs/library/media/image"),
    ("/docs/library/overlay", "/docs/library/overlay/alertdialog"),
    ("/docs/library/other", "/docs/library/other/html"),
    ("/docs/library/theming/theme", "/docs/library/other/theme"),
    ("/docs/library/theming/theme-panel", "/docs/library/other/theme"),
    ("/docs/library/layout/foreach", "/docs/library/dynamic-rendering/foreach"),
    ("/docs/library/layout/match", "/docs/library/dynamic-rendering/match"),
    ("/docs/library/layout/cond", "/docs/library/dynamic-rendering/cond"),
    # redirect previous chakra links to the new chakra docs
    ("/docs/library/chakra/[...component]", "https://chakra.reflex.run/introduction/"),
]

for source, target in redirects:
    app.add_page(lambda: rx.fragment(), route=source, on_load=rx.redirect(target))

app.add_custom_404_page(page404.component)

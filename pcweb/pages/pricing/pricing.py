import reflex as rx
from pcweb.components.webpage.badge import badge
from pcweb.pages.index.index_colors import index_colors
from pcweb.pages.index.views.footer_index import footer_index
from pcweb.pages.pricing.header import header
from pcweb.pages.pricing.plan_cards import plan_cards
from pcweb.pages.pricing.table import comparison_table_hosting, comparison_table_oss
from pcweb.views.bottom_section.get_started import get_started
from pcweb.pages.pricing.faq import faq
from pcweb.pages.pricing.calculator import calculator_section
from pcweb.meta.meta import hosting_meta_tags

pricing_path = "/pricing"
@rx.page(route=pricing_path, title="Reflex · Pricing", meta=hosting_meta_tags)
def pricing() -> rx.Component:
    """Get the Pricing landing page."""
    from pcweb.components.docpage.navbar import navbar

    return rx.box(
        index_colors(),
        navbar(),
        rx.el.main(
            rx.box(
                header(),
                plan_cards(),
                comparison_table_hosting(),
                comparison_table_oss(),
                calculator_section(),
                faq(),
                class_name="flex flex-col relative justify-center items-center w-full",
            ),
            class_name="flex flex-col w-full relative h-full justify-center items-center",
        ),
        footer_index(),
        badge(),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
    )

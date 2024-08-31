"""Test the counter example on the main page."""

import re

import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
from reflex.testing import AppHarness


@pytest.fixture
def intro_page_url() -> str:
    from pcweb.pages import docs

    return docs.getting_started.introduction.path


def test_counter(reflex_web_app: AppHarness, page: Page, intro_page_url) -> None:
    assert reflex_web_app.frontend_url is not None

    page.goto(reflex_web_app.frontend_url)
    page.set_default_timeout(10000)

    # Go to the docs intro page.
    page.get_by_role("link", name="Docs", exact=True).click()
    expect(page).to_have_url(re.compile(intro_page_url))

    counter_block = page.locator('[id="counter"]')
    expect(counter_block).to_be_visible()

    # Find increment button and click it twice. (Playwright will autoscroll the button into view)
    increment_button = counter_block.get_by_role("button", name="Increment")
    expect(increment_button).to_be_visible()
    increment_button.click()
    increment_button.click()

    counter_heading = counter_block.get_by_role("heading")

    # Check that the counter is now 2.
    expect(counter_heading).to_have_text(expected="2")

    # Find decrement button and click it.
    decrement_button = counter_block.get_by_role("button", name="Decrement")
    decrement_button.click()

    # Check that the counter is now 1.
    expect(counter_heading).to_have_text("1")

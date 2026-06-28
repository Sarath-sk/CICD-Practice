from playwright.sync_api import Page


def test_navigate_page(page: Page):
    page.goto("https://cnarios.com")
    page.pause()  # Pause for 5 seconds to observe the page
    assert "Cnarios" in page.title()

from playwright.sync_api import Page


def test_navigate_page(page: Page):
    page.goto("https://cnarios.com")
    assert "Cnarios" in page.title()

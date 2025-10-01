import os

import pytest
from playwright.sync_api import sync_playwright

from utils import config


@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        # If running in CI (like GitHub Actions), force headless=True
        if os.getenv("CI"):
            headless = True
        else:
            headless = config.HEADLESS

        browser = getattr(p, config.BROWSER).launch(
            headless=headless,
            args=["--start-maximized"],
        )

        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        yield page
        browser.close()

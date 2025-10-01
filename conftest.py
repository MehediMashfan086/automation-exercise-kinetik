import pytest
from playwright.sync_api import sync_playwright

from utils import config


@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = getattr(p, config.BROWSER).launch(headless=config.HEADLESS)
        page = browser.new_page()
        yield page
        browser.close()

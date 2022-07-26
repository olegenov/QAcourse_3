import pytest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class TestItemsCase:
    def test_items(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
        
        assert button.is_enabled(), 'Purchase button is not active or doesnt exist.'

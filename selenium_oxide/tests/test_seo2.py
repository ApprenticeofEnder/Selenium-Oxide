import unittest
import requests
from urllib.parse import urlparse

from selenium_oxide.exploit_builder import ExploitBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSeo2(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.base_url = "http://test_server:1337/"
        self.parsed_url = urlparse(self.base_url)
        self.xss_marker = "XSS"
        self.exploit = ExploitBuilder(
            self.parsed_url.scheme, self.parsed_url.netloc, headless=True
        )
        self.xss_marker = "XSS"

    @property
    def driver(self):
        return self.exploit.driver

    def setUp(self) -> None:
        self.driver.delete_all_cookies()
        return super().setUp()

    def test_navigation(self):
        self.exploit.get("/")
        self.assertEqual(self.driver.current_url, self.base_url)

    def test_content_extraction(self):
        username_label_xpath = '//*[@id="username-label"]'
        target = "Username"
        self.exploit.get("/login")
        get_results = self.exploit.get_contents(username_label_xpath)
        self.assertEqual(get_results, target)

    def test_entry(self):
        username_xpath = "/html/body/form/div[1]/input[1]"
        password_xpath = "/html/body/form/div[1]/input[2]"
        (
            self.exploit.get("/login")
            .type_entry(username_xpath, self.xss_marker)
            .type_entry(password_xpath, self.xss_marker)
        )
        entered_username = self.driver.find_element(
            value="username-input"
        ).get_attribute("value")
        entered_password = self.driver.find_element(
            value="password-input"
        ).get_attribute("value")
        self.assertEqual(entered_username, self.xss_marker)
        self.assertEqual(entered_password, self.xss_marker)

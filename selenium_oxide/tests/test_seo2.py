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

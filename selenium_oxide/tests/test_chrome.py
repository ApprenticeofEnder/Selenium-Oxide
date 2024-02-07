import unittest
from urllib.parse import urlparse

from selenium_oxide.exploit_builder import ExploitBuilder
from selenium_oxide.tests.test_seo2 import TestSeo2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @unittest.skip("need to solidify Chrome testing")
# class TestChrome(TestSeo2):
#     def __init__(self, methodName: str = ...) -> None:
#         super().__init__(methodName)
#         self.exploit = ExploitBuilder(
#             self.parsed_url.scheme, self.parsed_url.netloc, browser="chrome"
#         )

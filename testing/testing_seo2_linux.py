import unittest

from selenium_oxide.exploit_builder import ExploitBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

testfire_exploit = ExploitBuilder(
    "http",
    "demo.testfire.net"
)

testfire_driver = testfire_exploit.driver
xss_marker = "ECHO-ALPHA-TANGO"

# (
#     first_exploit
#         .get("/")
#         .get("/login.jsp")
#         .type_by_id("uid", "' OR 1=1 --")
#         .type_by_id("passw", "e")
#         .send_enter_by_id("passw")
#         .type_by_id("query", f"<script>alert(`{xss_marker}`)</script>")
#         .send_enter_by_id("query")
# )


class TestFire(unittest.TestCase):
    def test_navigation(self):
        testfire_exploit.get("/")
        self.assertEqual(testfire_driver.current_url,
                         "http://demo.testfire.net/")

    def test_content_extraction(self):
        testfire_exploit.get("/")
        login_txt = testfire_exploit.get_contents_by_id("LoginLink")
        self.assertEqual(login_txt, "Sign In")

    def test_text_entry_by_id(self):
        (
            testfire_exploit
            .get("/")
            .type_by_id("query", xss_marker)
        )
        self.assertEqual(testfire_driver.find_element_by_id(
            "query").get_attribute("value"), xss_marker)

    def test_enter_by_id(self):
        (
            testfire_exploit
            .get("/")
            .type_by_id("query", xss_marker)
            .send_enter_by_id("query")
        )
        WebDriverWait(testfire_driver, 2).until(
            EC.text_to_be_present_in_element(
                (By.TAG_NAME, 'p'),
                xss_marker
            )
        )


if __name__ == '__main__':
    unittest.main()

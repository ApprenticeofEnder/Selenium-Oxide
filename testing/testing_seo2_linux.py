# import unittest

# from selenium_oxide.exploit_builder import ExploitBuilder
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# xss_marker = "XSS"
# testfire_firefox_exploit = ExploitBuilder(
#     "http",
#     "demo.testfire.net"
# )
# testfire_chrome_exploit = ExploitBuilder(
#     "http",
#     "demo.testfire.net",
#     browser="chrome"
# )
# juice_shop_firefox_exploit = ExploitBuilder(
#     "https",
#     "juice-shop.herokuapp.com"
# )
# juice_shop_chrome_exploit = ExploitBuilder(
#     "https",
#     "juice-shop.herokuapp.com",
#     browser="chrome"
# )

# # (
# #     first_exploit
# #         .get("/")
# #         .get("/login.jsp")
# #         .type_by_id("uid", "' OR 1=1 --")
# #         .type_by_id("passw", "e")
# #         .send_enter_by_id("passw")
# #         .type_by_id("query", f"<script>alert(`{xss_marker}`)</script>")
# #         .send_enter_by_id("query")
# # )


# class TestFireFirefox(unittest.TestCase):
#     def __init__(self, methodName: str = ...) -> None:
#         super().__init__(methodName)
#         self.exploit = testfire_firefox_exploit
#         self.driver = self.exploit.driver

#     def test_navigation(self):
#         self.exploit.get("/")
#         self.assertEqual(self.driver.current_url,
#                          "http://demo.testfire.net/")

#     def test_content_extraction(self):
#         self.exploit.get("/")
#         login_txt = self.exploit.get_contents_by_id("LoginLink")
#         self.assertEqual(login_txt, "Sign In")

#     def test_text_entry_by_id(self):
#         (
#             self.exploit
#                 .get("/")
#                 .type_by_id("query", xss_marker)
#         )
#         self.assertEqual(self.driver.find_element_by_id(
#             "query").get_attribute("value"), xss_marker)

#     def test_enter_by_id(self):
#         (
#             self.exploit
#                 .get("/")
#                 .type_by_id("query", xss_marker)
#                 .send_enter_by_id("query")
#         )
#         WebDriverWait(self.driver, 2).until(
#             EC.text_to_be_present_in_element(
#                 (By.TAG_NAME, 'p'),
#                 xss_marker
#             )
#         )

# class TestFireChrome(unittest.TestCase):
#     def __init__(self, methodName: str = ...) -> None:
#         super().__init__(methodName)
#         self.exploit = testfire_chrome_exploit
#         self.driver = self.exploit.driver

#     def test_navigation(self):
#         self.exploit.get("/")
#         self.assertEqual(self.driver.current_url,
#                          "http://demo.testfire.net/")

#     def test_content_extraction(self):
#         self.exploit.get("/")
#         login_txt = self.exploit.get_contents_by_id("LoginLink")
#         self.assertEqual(login_txt, "Sign In")

#     def test_text_entry_by_id(self):
#         (
#             self.exploit
#                 .get("/")
#                 .type_by_id("query", xss_marker)
#         )
#         self.assertEqual(self.driver.find_element_by_id(
#             "query").get_attribute("value"), xss_marker)

#     def test_enter_by_id(self):
#         (
#             self.exploit
#                 .get("/")
#                 .type_by_id("query", xss_marker)
#                 .send_enter_by_id("query")
#         )
#         WebDriverWait(self.driver, 2).until(
#             EC.text_to_be_present_in_element(
#                 (By.TAG_NAME, 'p'),
#                 xss_marker
#             )
#         )

# class JuiceShopFirefox(unittest.TestCase):
#     def __init__(self, methodName: str = ...) -> None:
#         super().__init__(methodName)
#         self.exploit = juice_shop_firefox_exploit
#         self.driver = self.exploit.driver

#     def setUp(self) -> None:

#         return super().setUp()

#     def test_navigation(self):
#         self.exploit.get("/")
#         self.assertEqual(self.driver.current_url,
#                          "https://juice-shop.herokuapp.com/#/")

#     def test_click_by_class(self):
#         (
#             self.exploit
#                 .get("/#/")
#         )
#         WebDriverWait(self.driver, 2).until(
#             EC.presence_of_element_located(
#                 (By.CLASS_NAME, 'close-dialog')
#             )
#         )
#         self.exploit.click_by_class("close-dialog")
#         with self.assertRaises(Exception):
#             self.exploit.get_contents_by_class("mat-dialog-container")


#     def test_alert_waiting(self):
#         pass

# class JuiceShopChrome(unittest.TestCase):
#     def __init__(self, methodName: str = ...) -> None:
#         super().__init__(methodName)
#         self.exploit = juice_shop_chrome_exploit
#         self.driver = self.exploit.driver

#     def setUp(self) -> None:

#         return super().setUp()

#     def test_navigation(self):
#         self.exploit.get("/")
#         self.assertEqual(self.driver.current_url,
#                          "https://juice-shop.herokuapp.com/#/")

#     def test_click_by_class(self):
#         (
#             self.exploit
#                 .get("/#/")
#         )
#         WebDriverWait(self.driver, 2).until(
#             EC.presence_of_element_located(
#                 (By.CLASS_NAME, 'close-dialog')
#             )
#         )
#         self.exploit.click_by_class("close-dialog")
#         with self.assertRaises(Exception):
#             self.exploit.get_contents_by_class("mat-dialog-container")


#     def test_alert_waiting(self):
#         pass

# if __name__ == '__main__':
#     unittest.main()

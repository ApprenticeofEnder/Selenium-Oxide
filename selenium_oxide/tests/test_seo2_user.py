import unittest

from selenium_oxide import SeO2User
from faker import Faker


class TestSeO2User(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.fake = Faker()
        self.default_password = "Password1!"

    def setUp(self) -> None:
        Faker.seed(0)
        self.base_profile = self.fake.simple_profile()
        Faker.seed(0)
        self.user = SeO2User(password=self.default_password)
        Faker.seed(0)
        return super().setUp()

    def test_sex(self):
        self.assertEqual(self.user.sex, self.base_profile["sex"])

    def test_name(self):
        tmp_base_profile = self.fake.simple_profile()
        sex = tmp_base_profile["sex"]
        if sex == "M":
            name = self.fake.name_male()
        elif sex == "F":
            name = self.fake.name_female()
        else:
            name = self.fake.name_nonbinary()
        self.assertEqual(self.user.name, name)
        (first_name, last_name) = name.split()
        self.assertEqual(self.user.first_name, first_name)
        self.assertEqual(self.user.last_name, last_name)

    def test_username(self):
        self.assertEqual(self.user.username, self.base_profile["username"])

    def test_password(self):
        self.assertEqual(self.user.password, self.default_password)

    def test_email(self):
        self.assertEqual(self.user.email, self.base_profile["mail"])

    def test_address(self):
        self.assertEqual(self.user.address, self.base_profile["address"])

    def test_birthdate(self):
        self.assertEqual(self.user.birthdate, self.base_profile["birthdate"])

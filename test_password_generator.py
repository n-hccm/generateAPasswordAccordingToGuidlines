import unittest

from convert_to_sha1 import convert_to_sha1
from check_deny_list import check_deny_list
from password_generator import generate_password, check_password


class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self):
        password = generate_password()
        self.assertTrue(check_password(password))

    def test_convert_to_sha1(self):
        text = "password"
        self.assertEqual(convert_to_sha1(text), "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")

    def test_check_deny_list(self):
        password = "password"
        self.assertTrue(check_deny_list(password))

    def test_check_password(self):
        password = "Password1!"
        self.assertTrue(check_password(password))

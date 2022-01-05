import unittest
from Password import *

class TestPassword(unittest.TestCase):
    def test_validation_password(self):
        password = Password()
        self.assertFalse(password.validate_password("azertyuiop"), "Easy password are not allowed !")
        self.assertFalse(password.validate_password("qwertyuiop"), "Easy password are not allowed !")
        self.assertFalse(password.validate_password("1234567890"), "Easy password are not allowed !")
        self.assertFalse(password.validate_password("motdepasse"), "Easy password are not allowed !")
        self.assertFalse(password.validate_password("ejkvbejbveJB"), "Password must contain at least 1 digit and 1 special character")
        self.assertFalse(password.validate_password("ejkvbejbveJB1"), "Password must contain at least 1 digit")
        self.assertTrue(password.validate_password("ejkvbejbveJB1/"))
        self.assertFalse(password.validate_password("toto"), "Password must contain at 10 characters and max 25 characters")
        self.assertEqual(password.validate_password("ejkvbejbveJB1"), False)

if __name__ == '__main__':
    unittest.main()

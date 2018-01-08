from unittest import TestCase
from model import singIn,sqllite

class TestSign_in(TestCase):
    def test_sign_in(self):
        sqllite.connectDatabase()
        self.assertEqual(singIn.sign_in("",""),None)
        self.assertEqual(singIn.sign_in("david", ""), None)
        self.assertEqual(singIn.sign_in("", "456"), None)
        self.assertEqual(singIn.sign_in("david", "465165"), None)
        self.assertEqual(singIn.sign_in("david", "456"), "ca")
        self.assertEqual(singIn.sign_in("david", "456"), "ca")
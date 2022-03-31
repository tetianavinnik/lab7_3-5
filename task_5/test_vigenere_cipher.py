"""Test chipher"""
import unittest
from unittest import TestCase
from vigenere_cipher import VigenereCipher
from vigenere_cipher import combine_character, separate_character


class TestVigenereCipher(TestCase):
    def setUp(self) -> None:
        self.cipher1 = VigenereCipher("TRAIN")
        self.cipher2 = VigenereCipher("TRain")
        self.cipher3 = VigenereCipher(None)


    def test_encode_character(self):
        """
        Test character encoding.
        """
        self.assertTrue(self.cipher1.encode("E") == "X")
        self.assertRaises(Exception, lambda: self.cipher3.encode("E"))


    def test_encode_spaces(self):
        """
        Test space encoding.
        """
        self.assertTrue(self.cipher1.encode("ENCODED IN PYTHON") == "XECWQXUIVCRKHWA")
        


    def test_encode_lowercase(self):
        """
        Test lovercase encoding.
        """
        self.assertTrue(self.cipher2.encode("encoded in Python") == "XECWQXUIVCRKHWA")


    def test_encode(self):
        """
        Test encoding.
        """
        self.assertTrue(self.cipher1.encode("ENCODEDINPYTHON") == "XECWQXUIVCRKHWA")


    def test_extend_keyword(self):
        """
        Test extend keywords.
        """
        self.assertTrue(self.cipher1.extend_keyword(16) == "TRAINTRAINTRAINT")


    def test_decode(self):
        """
        Decoding test.
        """
        self.assertTrue(self.cipher1.decode("XECWQXUIVCRKHWA") == "ENCODEDINPYTHON")


    def test_combine_character(self):
        """
        Test combine character.
        """
        self.assertTrue(combine_character("E", "T") == "X")
        self.assertTrue(combine_character("N", "R") == "E")


    def test_separate_character(self):
        """
        Test separate character.
        """
        self.assertTrue(separate_character("X", "T") == "E")
        self.assertTrue(separate_character("E", "R") == "N")
        self.assertRaises(Exception, separate_character(" ", "R"))


if __name__ == '__main__':
    unittest.main()

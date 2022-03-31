"""Vigenere chipher"""


def combine_character(plain, keyword):
    """
    Combine characters.
    """
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)


def separate_character(cypher, keyword):
    """
    Separate characters.
    """
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_num - keyword_num) % 26)


class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword


    def extend_keyword(self, number):
        """
        Return string in which the word is repeated
        until its length reaches number.
        """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]


    def _code(self, text, combine_func):
        """
        Function for encode and decode.
        """
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p,k in zip(text, keyword):
            combined.append(combine_func(p,k))
        return "".join(combined)


    def encode(self, plaintext):
        """
        Encode text.
        """
        return self._code(plaintext, combine_character)


    def decode(self, ciphertext):
        """
        Decode text.
        """
        return self._code(ciphertext, separate_character)

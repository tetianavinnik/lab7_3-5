"""Document, Cursor and Character class"""
from genericpath import isfile
import os

class Cursor:
    """Class for cursor representation"""
    def __init__(self, document):
        self.document = document
        self.position = 0


    def forward(self):
        """
        Move cursor forward.
        """
        self.position += 1


    def back(self):
        """
        Move cursor back.
        """
        self.position -= 1


    def home(self):
        """
        Move cursor to the beginning of the line.
        """
        while self.document.characters[
                self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break


    def end(self):
        """
        Move cursor to the end of the line.
        """
        while self.position < len(
                self.document.characters) and \
                self.document.characters[
                self.position].character != '\n':
            self.position += 1


class Document:
    """Class for document representation"""
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''


    def insert(self, character):
        """
        Insert character at current cursor possition.
        """
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position,
        character)
        self.cursor.forward()


    def delete(self):
        """
        Delete character.
        """
        del self.characters[self.cursor.position]


    def save(self):
        """
        Save document.
        """
        if not os.path.isfile(self.filename) or not os.path.exists(self.filename):
            raise TereIsNoSuchFile
        with open(self.filename, 'w') as file:
            file.write(''.join(self.characters))


    @property
    def string(self):
        """
        String representation of document.
        """
        return "".join((str(c) for c in self.characters))


class Character:
    """Class for character representation"""
    def __init__(self, character,
                 bold=False, italic=False, underline=False):
        self.character = character
        if len(character) != 1:
            raise WrongLength
        self.bold = bold
        self.italic = italic
        self.underline = underline

    
    @property
    def character(self):
        return self.character


    @character.setter
    def character(self, character):
        if not isinstance(character, str):
            raise WrongType


    def __str__(self):
        """
        Return string representation of character.
        """
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character


class WrongType(Exception):
    pass


class WrongLength(Exception):
    pass


class TereIsNoSuchFile(Exception):
    pass

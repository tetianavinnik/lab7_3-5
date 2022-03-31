import datetime


last_id = 0
class Note:
    """Represent a note in the notebook. Match against a
    string in searches and store tags for each note."""
    def __init__(self, memo, tags=''):
        """
        Initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.
        >>> note = Note('buy some sugar', 'goods')
        >>> isinstance(note, Note)
        True
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id


    def match(self, filter):
        """
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitive and matches both text and
        tags.
        >>> note = Note('buy some sugar', 'goods')
        >>> note.match('goods')
        True
        """
        return filter in self.memo or filter in self.tags


class Notebook:
    """Represent a collection of notes that can be tagged,
    modified, and searched."""
    def __init__(self):
        """
        Initialize a notebook with an empty list.
        """
        self.notes = []


    def new_note(self, memo, tags=''):
        """
        Create a new note and add it to the list.
        >>> notebook = Notebook()
        >>> notebook.new_note('buy salt', 'goods')
        """
        self.notes.append(Note(memo, tags))


    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its
        tags to the given value.
        >>> notebook = Notebook()
        >>> notebook.new_note('buy salt', 'goods')
        >>> notebook.modify_tags(1, 'bought')
        False
        """
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False


    def search(self, filter):
        """
        Find all notes that match the given filter
        string.
        >>> notebook = Notebook()
        >>> notebook.new_note('buy salt', 'goods')
        >>> notebook.new_note('buy sugar', 'goods')
        >>> len(notebook.search('goods'))
        2
        """
        return [note for note in self.notes if
                note.match(filter)]


    def _find_note(self, note_id):
        """
        Locate the note with the given id.
        >>> notebook = Notebook()
        >>> notebook.new_note('buy salt', 'goods')
        >>> notebook._find_note(3).tags
        'goods'
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None


    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and change its
        memo to the given value.
        >>> notebook = Notebook()
        >>> notebook.new_note('buy salt', 'goods')
        >>> notebook.modify_memo(4, 'bought')
        True
        >>> note = notebook._find_note(4)
        >>> note.memo
        'bought'
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

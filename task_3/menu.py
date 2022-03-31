from ast import Break
import sys
# from auth_account import Editor
from notebook import Notebook, Note
# from auth_account import Editor


class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_note,
        "4": self.modify_note,
        "5": self.back,
        "6": self.quit
        }
        self.permitions = {
            "1": ['basic', 'mid', 'pro'],
            "2": ['basic', 'mid', 'pro'], 
            "3": ['mid', 'pro'],
            "4": ['pro'],
            "5": ['basic', 'mid', 'pro'],
            "6": ['basic', 'mid', 'pro']
        }


    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes (basic)
        2. Search Notes (basic)
        3. Add Note (mid)
        4. Modify Note (pro)
        5. Back
        6. Quit
        """)
    

    def permission_check(self, user, choice):
        """Check permission"""
        return user.is_permitted(choice)


    def get_permission(self, user):
        return user.get_perm()
    

    def ask_permission(self, user, permission):
        while True:
            print('Do you want to ask for permission? (yes/no)')
            choice = input('>')
            if choice == 'no':
                from auth_account import Editor
                Editor().menu()
                # Menu().run(user)
            elif choice == 'yes':
                user.ask_perm(permission)
                break
            else:
                print('Enter yes or no')


    def run(self, user):
        '''Display the menu and respond to choices.'''
        while True:
            self.user = user
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                if self.get_permission(user) in self.permitions[choice]:
                    action()
                else:
                    self.ask_permission(user, self.permitions[choice][0])
            else:
                print("{0} is not a valid choice".format(choice))


    def show_notes(self, notes=None):
        """Show all notes"""
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                  note.id, note.tags, note.memo))


    def search_notes(self):
        """
        Return note.
        """
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)


    def add_note(self):
        """
        Add note to the notebook.
        """
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")


    def modify_note(self):
        """
        Modify note.
        """
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)


    def quit(self):
        """
        Exit the notebook.
        """
        print("Thank you for using your notebook today.")
        raise SystemExit()


    def back(self):
        """
        Back to the main menu.
        """
        from auth_account import Editor
        Editor().menu()

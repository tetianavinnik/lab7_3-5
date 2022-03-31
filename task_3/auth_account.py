import auth
from menu import Menu


def create_pro():
    try:
        auth.authenticator.add_user("pro_user", "propassword")
        auth.authorizor.add_permission("basic")
        auth.authorizor.add_permission("mid")
        auth.authorizor.add_permission("pro")
        auth.authorizor.permit_user("pro", "pro_user")
    except auth.UsernameAlreadyExists:
        print('', end='')


MESSAGE = []
class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
        "login": self.login,
        "notebook": self.notebook,
        "signup": self.signup,
        "quit": self.quit
        }
    

    def give_permission(self, permission, user):
        """
        Pro user can give permission.
        """
        auth.authorizor.permit_user(permission, user.username)
    

    def signup(self):
        """
        Create new user.
        """
        register = False
        while not register:
            username = input("username: ")
            password = input("password: ")
            try:
                auth.authenticator.add_user(username, password)
                auth.authorizor.permit_user('basic', username)
                register = True
            except auth.UsernameAlreadyExists:
                print('This username is already exists')
            except auth.PasswordTooShort:
                print('Password should be more than 5 charscters')


    def login(self):
        """
        Login.
        """
        length = 0
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(
                        username, password)
                global MESSAGE
                if username == 'pro_user' and MESSAGE != []:
                    for i in MESSAGE[::-1]:
                        print('{} asks you for {} permission'.format(i[0].username, i[1]))
                        while True:
                            print('Give permission? (yes/no)')
                            choice = input('>')
                            if choice == 'yes':
                                length += 1
                                self.give_permission(i[1], i[0])
                                break
                            elif choice == 'no':
                                break
                    MESSAGE = MESSAGE[:len(MESSAGE)-length]
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
                # Menu().run(self)


    def is_permitted(self, permission):
        """
        Check if action is permited for the user.
        """
        try:
            auth.authorizor.check_permission(
                permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} do not have {} permission".format(
                e.username, permission))
            return False
        else:
            return True
    

    def ask_perm(self, permission):
        """
        ASk pro user for permission.
        """
        print('Log in as a pro user')
        MESSAGE.append((self, permission))
        Editor().menu()
    

    def get_perm(self):
        """
        Ask pro user for permission.
        """
        result = ''
        for i in auth.authorizor.permissions:
            for j in auth.authorizor.permissions[i]:
                if j == self.username:
                    result = i
        return result


    def notebook(self):
        """
        Go to notebook.
        """
        for i in auth.authenticator.users:
            if auth.authenticator.is_logged_in(i):
                return Menu().run(self)
        print('You should login')
        return Editor().menu()


    def quit(self):
        """
        Exit the programm.
        """
        raise SystemExit()


    def menu(self):
        try:
            answer = ""
            while True:
                print("""
Please enter a command:
\tlogin\t\tLogin
\tsignup\t\tSign up
\tnotebook\tNotebook
\tquit\t\tQuit
""")
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(
                        answer))
                else:
                    # if func == self.login:
                    #     func(MESSAGE)
                    # else:
                    func()
        finally:
            print("")
create_pro()
Editor().menu()

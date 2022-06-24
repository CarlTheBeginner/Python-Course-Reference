class User:
    def __init__(self, first_name, last_name, age, birthday):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.birthday = birthday

    def describe_user(self):
        print(f"User information: \n"
              f"FULL NAME : {self.first} {self.last}\n"
              f"AGE       : {self.age}\n"
              f"BIRTHDAY  : {self.birthday}")

    def greet_user(self):
        print(f"Hello and Welcome, User : {self.first}")

class Privileges:
    """Storing the list of privileges to the attribute..."""
    def __init__(self, privileges=("Can add post", "Can delete post", "Can ban user")):
        self.privileges = privileges

    def show_privileges(self):
        """show all the privileges by using forloop"""
        print("The user can do the following: ")
        for privs in self.privileges:
            print(privs)

class Admin(User):
    def __init__(self, first_name, last_name, age, birthday):
        super().__init__(first_name, last_name, age, birthday)
        self.privilege = Privileges()


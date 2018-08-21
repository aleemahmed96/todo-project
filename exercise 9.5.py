class User():
    """docstring for User."""
    def __init__(self, f_name, l_name, gender, age, joined):
        self.firstname = f_name
        self.lastname = l_name
        self.age = age
        self.gender = gender
        self.joined = joined
        self.login_attempts = 0

    def describe_user(self):
        print("\nContact Details")
        print('Name: ' + self.firstname + " " + self.lastname)
        print("Age: " + self.age)
        print("Gender: " + self.gender)
        print("Joined: " + self.joined)

    def greet_user(self):
        print("\nHello " + self.firstname + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("You have attempted " + str(self.login_attempts) + " login attempts.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("The Login attempt has been reset to " + str(self.login_attempts) + ".")

obj = User("dani","david","Male","21","25 feb 2018")
obj.increment_login_attempts()
obj.increment_login_attempts()
obj.increment_login_attempts()
obj.reset_login_attempts()
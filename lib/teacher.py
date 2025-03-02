# lib/teacher.py
import random
from user import User  # Ensure user.py is correctly imported

class Teacher(User):  # Teacher inherits from User
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Corrected call to User's constructor
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        return random.choice(self.knowledge)

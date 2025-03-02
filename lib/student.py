# lib/student.py
from user import User  # Ensure correct import

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Call User's constructor
        self.knowledge = []  # Ensure this attribute is initialized as an empty list

    def learn(self, lesson):
        """Adds a lesson to the student's knowledge."""
        self.knowledge.append(lesson)

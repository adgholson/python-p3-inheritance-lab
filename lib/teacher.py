#!/usr/bin/env python

from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
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

    def teach(self, knowledge_list=None):
        if knowledge_list is not None:
            self.knowledge.extend(knowledge_list)
            return knowledge_list
        else:
            random_knowledge = random.choice(self.knowledge)
            self.knowledge.append(random_knowledge)
            return random_knowledge
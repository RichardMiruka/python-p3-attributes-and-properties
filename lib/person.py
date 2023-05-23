#!/usr/bin/env python3

APPROVED_JOBS = [
    "Engineer",
    "Teacher",
    "Doctor",
    "Lawyer",
    "Designer",
    "Salesperson",
    "Programmer",
    "Writer",
    "Chef",
    "Manager"
]

class Person:
    def __init__(self):
        self._name = None
        self._job = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")

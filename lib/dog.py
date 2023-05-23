#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Pug",
    "Labrador",
    "Bulldog",
    "Beagle",
    "Poodle",
    "Rottweiler",
    "German Shepherd",
    "Golden Retriever",
    "Siberian Husky",
    "Chihuahua"
]

class Dog:
    def __init__(self):
        self._name = None
        self._breed = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")

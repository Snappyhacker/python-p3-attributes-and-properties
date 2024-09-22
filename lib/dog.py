#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Mutt"):
        # Validate name first before proceeding with breed validation
        self._breed = None  # Temporarily set breed to None to avoid triggering setter
        self.name = name  # This will trigger name validation first
        if self._name:  # If name is valid, proceed to set breed
            self.breed = breed

    # Name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            self._name = None  # Set to None to prevent breed validation if name is invalid
            print("Name must be string between 1 and 25 characters.")

    # Breed property
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            if value:  # Ensure error is printed only if breed is set to something non-empty
                print("Breed must be in list of approved breeds.")

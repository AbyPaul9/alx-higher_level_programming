#!/usr/bin/python3
""" say_my_name module """


def say_my_name(prmFirstName, prmLastName=""):
    """ say_my_name function
    this function concatenated first name and last name and print the result
    Attributes:
        prmFirstName: first name
        prmLastName: last name
    """
    if not isinstance(prmFirstName, str):
        raise TypeError("first_name must be a string")
    if not isinstance(prmLastName, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(prmFirstName, prmLastName))

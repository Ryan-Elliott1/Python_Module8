"""
Program: assign_average.py
Author: Ryan Elliott
Last date modified: 06/28/2020
This program uses a dictionary to replicate a switch-case in python
Input a choice from 1-6 to get a return or anything else for a default
Outputs choice or default
"""


def a():
    return "You chose a"


def A():
    return "You chose A"


def b():
    return "You chose b"


def B():
    return "You chose B"


def c():
    return "You chose c"


def C():
    return "You chose C"


def default():
    return "Invalid choice"


switch = {
    1: a(),
    2: A(),
    3: b(),
    4: B(),
    5: c(),
    6: C()
}


def switch_average(choice):
    """Returns a statement using the dictionary and functions depending on the input
    :param choice the users selection
    :returns the users choice
    """
    return switch.get(choice, default())


if __name__ == '__main__':
    print(switch_average(0))

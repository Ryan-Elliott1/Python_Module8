"""
Program: assign_average.py
Author: Ryan Elliott
Last date modified: 06/28/2020
"""


def a():
    return "You chose a"
def A():
    return "You chose A"
def b():
    return "You chose b"
def B():
    return "You chose B"


switch = {
    1: a(),
    2: A(),
    3: b(),
    4: B()
}


def switch_average(choice):
    return switch.get(choice)


if __name__ == '__main__':
    print(switch_average(1))

"""
Program: set_membership
Author: Ryan Elliott
Last date modified: 06/26/2020
This program returns true or false if the given value is in the users set
Input set and value to look for
Outputs true or false
"""


def in_set(my_set, look):
    """Returns true is the element is in the set or false if not
    :param my_set the users set
    :param look the element to search for
    :returns true or false
    """
    return look in my_set


if __name__ == '__main__':
    my_sets = {1, 4, 2, 3, 4}
    print(in_set(my_sets, 3))

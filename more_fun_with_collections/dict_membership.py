"""
Program: dict_membership
Author: Ryan Elliott
Last date modified: 06/26/2020
This program returns true or false if the given key is in the users dictionary
Input dictionary and key to look for
Outputs true or false
"""


def in_dict(my_dict, look):
    """Returns true is the key is in the dictionary or false if not
    :param my_dict the users dictionary
    :param look the key to search for
    :returns true or false
    """
    return look in my_dict


if __name__ == '__main__':
    diction = {'Billy': 1, 'Bob': 2, 'Jerry': 3}
    print(in_dict(diction, 'Bob'))

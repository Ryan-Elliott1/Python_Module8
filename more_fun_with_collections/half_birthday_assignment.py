"""
Program: half_birthday_assignment.py
Author: Ryan Elliott
Last date modified: 06/28/2020
This program calculates the half birthday of a given date
Input birthday
Outputs the half birthday
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import *


def half_birthday(birthday_in):
    """Calculates the half birthday of a given date
    :param birthday_in, the users birthday
    :return The users half birthday
    """
    birthday = datetime.strptime(birthday_in, '%d/%m/%Y')
    birthday = birthday + relativedelta(months=-6)
    return str(birthday)


if __name__ == '__main__':
    print((half_birthday('8/8/2020')))

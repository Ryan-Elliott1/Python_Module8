"""
Program: dictionary_update.py
Author: Ryan Elliott
Last date modified: 06/26/2020
This program uses a dictionary to get a number of test scores and returns the average of those scores
Input is the users number of test scores and the value of the scores
Outputs the average of the users test scores
"""


def get_test_scores():
    """Asks for number of test scores and the values for the scores
    """
    scores_dict = dict()
    num_scores = int(input("Enter the number of test scores: "))
    test_num = 1
    try:
        while test_num <= num_scores:
            score = int(input("Enter a test score: "))
            scores_dict.update({test_num: score})
            test_num += 1
    except ValueError as err:
        print("ValueError encountered")
    print(average_scores(scores_dict))


def average_scores(my_dict):
    """Returns true is the element is in the set or false if not
    :param my_dict the users dictionary of test scores
    :returns the average of the test scores
    """
    num_sco = len(my_dict)
    total_points = 0
    count = 1
    for x in my_dict:
        total_points += my_dict.get(count)
        count += 1
    return total_points / num_sco


if __name__ == '__main__':
    get_test_scores()

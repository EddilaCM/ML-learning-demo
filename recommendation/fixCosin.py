# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fixCosin
   Description :
   Author :       cm
   date：          2019/4/29
-------------------------------------------------
   Change Activity:
                   2019/4/29:
-------------------------------------------------
"""
from math import sqrt


users3 = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
          "Lorde": 4, "Fall Out Boy": 1},
          "Matt": {"Imagine Dragons": 3, "Daft Punk": 4,
          "Lorde": 4, "Fall Out Boy": 1},
          "Ben": {"Kacey Musgraves": 4, "Imagine Dragons": 3,
          "Lorde": 3, "Fall Out Boy": 1},
          "Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
          "Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
          "Tori": {"Kacey Musgraves": 5, "Imagine Dragons": 4,
          "Daft Punk": 5, "Fall Out Boy": 3}}


def fixedCosin(band1, band2, userRating):
    """
    fixed cosin function:
    :param band1:
    :param band2:
    :param userRating:
    :return:
    """
    averages = {}
    for key, ratings in userRating.items():
        tmp_val = ratings.values()
        averages[key] = (float(sum(tmp_val)))/len(tmp_val)

    num = 0
    denominator1 = 0
    denominator2 = 0
    for user, ratings in userRating.items():
        if band1 in ratings and band2 in ratings:
            avg = averages[user]
            num += (ratings[band1] - avg) * (ratings[band2] - avg)
            denominator1 += (ratings[band1] - avg)**2
            denominator2 += (ratings[band2] - avg)**2
    return num / (sqrt(denominator1)*sqrt(denominator2))


if __name__ == '__main__':
    print(fixedCosin('Kacey Musgraves', 'Lorde', users3))
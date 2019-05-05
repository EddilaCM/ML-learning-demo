# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     similarityCompute
   Description :
   Author :       cm
   date：          2019/4/29
-------------------------------------------------
   Change Activity:
                   2019/4/29:
-------------------------------------------------
"""
from math import sqrt


users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }


"""
manhattan
"""


def manhatten(rating1, rating2):
    """
    compute manhatten distance : sum all abs between two same item
    :param rating1:
    :param rating2:
    :return:
    """
    distance = 0
    for key in rating1.keys():
        if key in rating2.keys():
            distance += abs(rating1[key] - rating2[key])
    return distance


def minkowski(rating1, rating2, r):
    """
    compute minkowski distance
    :param rating1:
    :param rating2:
    :param r:
    :return:
    """
    distance = 0
    for key in rating1.keys():
        if key in rating2.keys():
            distance += pow(abs(rating1[key] - rating2[key]), r)
    return distance


def pearson(rating1, rating2):
    """
    pearson
    :param rating1:
    :param rating2:
    :return:
    """
    sum_xy, sum_x, sum_y, sum_x2, sum_y2 = 0, 0, 0, 0, 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator


def computeNearestNeighbor(username, users, r):
    """
    compute someone's neightbor with other
    :param username:
    :param users:
    :return:
    """
    distances = []
    for user in users.keys():
        if user != username:
            distance = minkowski(users[user], users[username], r)
            distances.append((distance, user))
    distances.sort()
    return distances


def recommend(username, users, r):
    """
    give username some recommendations
    :param username:
    :param users:
    :return: recommend list
    """
    # find the nearest user for username
    nearest = computeNearestNeighbor(username, users, r)[0][1]
    recommends = []

    # filter the nearest user have score but the username hasn't comment on
    rating_nearest = users[nearest]
    rating_username = users[username]
    for key in rating_nearest.keys():
        if key not in rating_username.keys():
            recommends.append((key, rating_nearest[key]))
    sort_recommend = sorted(recommends, key=lambda temp:temp[1], reverse=True)
    return sort_recommend


def my_main():
    print(manhatten(users["Hailey"], users["Veronica"]))
    print("----")
    print(computeNearestNeighbor("Hailey", users, 2))
    print("----")
    print(recommend('Hailey', users, 1))
    print(recommend('Hailey', users, 2))
    print('-----')
    print(pearson(users["Angelica"], users["Jordyn"]))


if __name__ == '__main__':
    my_main()
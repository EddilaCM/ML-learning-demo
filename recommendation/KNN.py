# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     KNN
   Description :
   Author :       cm
   date：          2019/4/29
-------------------------------------------------
   Change Activity:
                   2019/4/29:
-------------------------------------------------
"""


class KNN:
    def __init__(self, data, K=1, metric="pearson", n=5):
        """
        init data
        :param data: train data
        :param K: the number of nearest
        :param metric: smailarity formula
        :param n: the numnber of recommend
        """
        self.K = K
        self.n = n

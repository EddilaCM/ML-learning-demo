#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Eddila
@file: np_continuaion.py
@time: 2019/05/29
"""

import math
import numpy as np


def compute_gaussian_pro(mean, var, x):
    """
    compute Gaussian density function
    :param mean:
    :param var:
    :param x:
    :return:
    """
    coeff = (1.0 /(math.sqrt((2 * math.pi) * var)))
    exponent = math.exp(-(math.pow(x-mean, 2) / (2 * var)))
    return coeff * exponent


class NPContinuation:

    def __init__(self):
        self.classes = None
        self.X = None
        self.y = None
        self.Guass_prams = None

    def fit(self, train_df, y_label_name):
        group_data = train_df.groupby(y_label_name)
        self.classes = train_df[y_label_name].unique()
        for name, tmp_df in group_data:
            temp_cols = [i for i in tmp_df.columns if i != y_label_name]
            attr_dict = {}
            for tmp_col in temp_cols:
                vals = {}
                attr_dict[tmp_col] = vals







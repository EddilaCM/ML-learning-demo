#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Eddila
@file: np_continuaion.py
@time: 2019/05/29
"""

import math

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
#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:chengmin
@file: np_discrete.py
@time: 2019/05/{DAY}
"""

import numpy as np


"""step 1: load data """



"""step 2: reset sample according to classify label """

def reset_dataset(dataset):
    rec_dict = {}
    if dataset is not None:
        for idx, row in dataset.iterrows():
            class_label = row[-1]
            if class_label not in rec_dict.keys():
                rec_dict[class_label] = [row[:-1]]
            else:
                rec_dict[class_label].append(row[:-1])
    else:
        print('INPUT ERROR: input dataset can not be None!')
    return rec_dict

"""step three: compute probability """
"""step four: train model """
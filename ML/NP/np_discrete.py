#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:chengmin
@file: np_discrete.py
@time: 2019/05/{DAY}
"""

import pandas as pd
from collections import Counter
"""step 1: load data """



"""step 2: reset sample according to classify label """

def reset_dataset(dataset):
    rec_dict = {}
    if dataset is not None:
        for idx, row in dataset.iterrows():
            class_label = row[0]
            if class_label not in rec_dict.keys():

                rec_dict[class_label] = [row[1:]]
            else:
                rec_dict[class_label].append(row[1:])
    else:
        print('INPUT ERROR: input dataset can not be None!')
    return rec_dict


"""step three: compute probability """
def pro_label_y(data_dict):
    rec_dict = {}
    rec_label_dict = None
    if data_dict is not None and len(data_dict) > 0:
        pro_label = {}
        for tmp_k, tmp_v in data_dict.items():
            tmp_len = len(tmp_v)

            # data frame transform
            temp_count = {}
            for tmp_i in tmp_v:
                dict_i = tmp_i.to_dict()
                for temp_k, temp_v in dict_i.items():
                    if temp_k in temp_count.keys():
                        temp_count[temp_k].append(temp_v)
                    else:
                        temp_count[temp_k] = [temp_v]

            # compute probability
            temp_pro = {}
            for count_k, count_v in temp_count.items():
                number_count = Counter(count_v)
                temp_c = {tmp_k:tmp_v/len(count_v) for tmp_k, tmp_v in number_count.items()}
                temp_pro[count_k] = temp_c

            rec_dict[tmp_k] = temp_pro
            pro_label[tmp_k] = tmp_len

        rec_label_dict = {t_k: t_v/sum(pro_label.values()) for t_k, t_v in pro_label.items()}
    print(rec_dict)
    print(rec_label_dict)

    return rec_label_dict, rec_dict


"""step four: predict """
def predict_label(series_predict, dataset):
    label_pro, label_attribute_pro = pro_label_y(reset_dataset(dataset))
    if label_pro is not None:
        total_pro = {}
        temp_dict = series_predict.to_dict()
        for label, pro in label_pro.items():
            tmp_pro = pro
            for tmp_k, tmp_v in temp_dict.items():
                tmp_pro *= label_attribute_pro[label][tmp_k][tmp_v]

            total_pro[label] = tmp_pro

        print(total_pro)


if __name__ == '__main__':
    test_data = pd.read_csv('../../data-zip/np_discrete.csv')
    tmp_s = test_data.iloc[1][1:]
    print(test_data.iloc[0])
    predict_label(tmp_s, test_data)
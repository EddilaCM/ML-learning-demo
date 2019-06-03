#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Eddila
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
            print('\n--{}----\n'.format(temp_count))
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
    rec_key = None
    label_pro, label_attribute_pro = pro_label_y(reset_dataset(dataset))
    if label_pro is not None:
        total_pro = {}
        temp_dict = series_predict.to_dict()
        for label, pro in label_pro.items():
            tmp_pro = pro
            for tmp_k, tmp_v in temp_dict.items():
                try:
                    tmp_pro *= label_attribute_pro[label][tmp_k][tmp_v]
                except KeyError:
                    print()
                    tmp_pro *= (1 - sum(label_attribute_pro[label][tmp_k].values()))

            total_pro[label] = tmp_pro

        print(total_pro)
        rec_key = max(total_pro, key=total_pro.get)
    return rec_key



"""
拉普拉斯修正
：测试集中可能出现测试集中没有的属性取值

"""
class NPLaplace:
    def __init__(self, dataframe, train_test_scale=0.7):
        self.train_data = None
        self.test_data = None
        self.pro_label = None
        self.pro_detail = None

        self.attr_values = self.all_attribute_value(dataframe)
        self.divide_train_test(dataframe, train_test_scale)
        self.train_model()


    def all_attribute_value(self, dataframe):
        """
        statistics the all values of every attribute
        :param dataframe: before
        :return:
        """
        attr_vals = {}
        if dataframe is not None and len(dataframe) > 0:
            cols = dataframe.columns
            for tmp_attr in cols:
                if tmp_attr != 'y_label':
                    attr_vals[tmp_attr] = dataframe[tmp_attr].unique()
        else:
            print('Input dataFrame can not be None or null!')
        return attr_vals

    def divide_train_test(self, dataframe, train_test_scale):
        reset_data = reset_dataset(dataframe)
        len_label = {tmp_k: len(tmp_v) for tmp_k, tmp_v in reset_data.items()}
        min_number = min(len_label.values())
        train_number = int(min_number * train_test_scale)
        self.train_data = {tmp_k:tmp_v[:train_number] for tmp_k, tmp_v in reset_data.items()}
        self.test_data = {tmp_k:tmp_v[train_number:] for tmp_k, tmp_v in reset_data.items()}

    def train_model(self):
        rec_dict = {}
        rec_label_dict = None
        if self.train_data is not None and len(self.train_data) > 0:
            pro_label = {}
            for tmp_k, tmp_v in self.train_data.items():
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
                for c_k, c_v in self.attr_values.items():
                    t_c = {}
                    number_count = Counter(temp_count[c_k])
                    len_c_v = len(c_v)
                    denominator = tmp_len + len_c_v
                    for i in c_v:
                        if i in number_count.keys():
                            t_c[i] = (number_count[i] + 1) / denominator
                        else:
                            t_c[i] = 1 / denominator

                    temp_pro[c_k] = t_c

                rec_dict[tmp_k] = temp_pro

                pro_label[tmp_k] = tmp_len

            rec_label_dict = {t_k: t_v / sum(pro_label.values()) for t_k, t_v in pro_label.items()}

        self.pro_label = rec_label_dict
        self.pro_detail = rec_dict

    def predict_label(self,):
        """
        test
        :param test_serieses:
        :return:
        """
        real_lable = []
        predict_lable = []

        if self.test_data is not None and len(self.test_data) > 0:
            test_lst = []
            for key_t, val_t in self.test_data.items():
                test_lst += val_t
                real_lable += [key_t for i in range(len(val_t))]

            for tmp_row in test_lst:
                total_pro = {}
                temp_dict = tmp_row.to_dict()
                for label, pro in self.pro_label.items():
                    tmp_pro = pro
                    for tmp_k, tmp_v in temp_dict.items():
                        try:
                            tmp_pro *= self.pro_detail[label][tmp_k][tmp_v]
                        except KeyError:
                            print()
                            tmp_pro *= (1 - sum(self.pro_detail[label][tmp_k].values()))

                    total_pro[label] = tmp_pro

                rec_key = max(total_pro, key=total_pro.get)
                predict_lable.append(rec_key)

        else:
            print('DATA ERROR: test data can not be None or null!')
        return real_lable, predict_lable

    def evaluate_accurate(self, real_y, predict_y):
        """
        compute the accuracy of prediction
        :return:
        """
        accuracy = None
        if real_y and predict_y and len(real_y) == len(predict_y):
            count_accurate = 0
            for i, j in zip(real_y, predict_y):
                if i == j:
                    count_accurate += 1

            accuracy = count_accurate / len(real_y)
        else:
            print('INPUT DATA ERROR: real_y or predict_y is error, or, the length of real is not equal!')
        return accuracy

    def get_predict_info(self,):
        real_labels, predict_labels = self.predict_label()
        accuracy = self.evaluate_accurate(real_labels, predict_labels)
        return accuracy, predict_labels, real_labels


if __name__ == '__main__':
    test_data = pd.read_csv('../../data-zip/np_discrete.csv')
    # tmp_s = ['青', '非规则', '大']
    # tmp_s = pd.Series(tmp_s, index=['颜色','形状','大小'])
    # print(predict_label(tmp_s, test_data))
    test_ddf = test_data
    obj_np = NPLaplace(test_data)
    acc, predict_labels, real_labels = obj_np.get_predict_info()
    print('{}\n{}\n{}'.format(acc, predict_labels, real_labels))


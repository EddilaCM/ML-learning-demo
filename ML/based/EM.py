#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:
@file: EM.py
@time: 2019/06/12 
"""


import math
import numpy as np
from scipy import stats




class MyEM:
    """
    icon problem
    e.g.  two icons throwing problem
    """
    def __init__(self, data_X, max_J, prior_thetas, thres=1e-6):
        """

        :param data_X: np.array; data matrix ; e.g. observations
                                                np.array([[1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                                                        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                                                        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                                                        [1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                                                        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]])
        :param max_J: int; the number of iterations; e.g. 1000
        :param prior_thetas: dict; init probability; e.g. {A:p(x=1), B:p(x=1)}
        """

        self.X = data_X
        self.max_J = max_J
        self.prior_thetas = prior_thetas
        self.val = np.unique(data_X)
        self.thres = thres

    def iteration(self):
        iter_num = 0
        for i in range(self.max_J):
            if i == 0:
                priors = self.prior_thetas
            tmp_counts = self.e_step(priors)
            new_prior = self.m_step(tmp_counts)

            change = np.abs(priors[0] - new_prior[0])
            if change < self.thres:
                break
            else:
                priors = new_prior
                iter_num += 1
        return new_prior, iter_num

    def e_step(self, thetas):
        theta_A = thetas[0]
        theta_B = thetas[1]
        counts = {'A':{'True':0, 'false':0}, 'B':{'True':0, 'false':0}}
        if self.X is not None and len(self.X) > 0:
            for temp_instance in self.X:
                total_len = len(temp_instance)
                true_number = sum(temp_instance)
                false_number = total_len - true_number
                c_A = stats.binom.pmf(true_number, total_len, theta_A)
                c_B = stats.binom.pmf(true_number, total_len, theta_B)
                weight_A = c_A /( c_A + c_B)
                weight_B = c_B /( c_A + c_B)

                # update
                counts['A']['True'] += weight_A * true_number
                counts['A']['false'] += weight_A * false_number
                counts['B']['True'] += weight_B * true_number
                counts['B']['false'] += weight_B * false_number

        return counts


    def m_step(self, counts):
        new_theta_A = counts['A']['True'] / (counts['A']['True'] + counts['A']['false'])
        new_theta_B = counts['B']['True'] / (counts['B']['True'] + counts['B']['false'])
        return [new_theta_A, new_theta_B]




class MyGMMM:
    def __init__(self):
        pass

    """
    step 1: initialize
    
    """
    def initialize(self):
        pass
    """
    step 2: E-step
    
    """
    def e_step(self):
        pass

    """
    step 3: M-step
    
    """
    def m_step(self):
        pass
    """
    step 4: evaluate
    
    """
    def evaluate(self):
        pass



if __name__ == '__main__':
    observations = np.array([[1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                             [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                             [1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                             [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]])
    simple_obj = MyEM(observations, 10000, [0.6, 0.4])
    print(simple_obj.iteration())
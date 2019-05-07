# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     simpleDemo
   Description :  BP + pyTorch
   Author :       cm
   date：          2019/5/6
-------------------------------------------------
   Change Activity:
                   2019/5/6:
-------------------------------------------------
"""

import torch
import numpy as np

#  test
# np_data = np.arange(6).reshape((2, 3))
# torch_data = torch.from_numpy(np_data)
# tensor2arr = torch_data.numpy()
# print(
#   '\nnumpy array:\n', np_data,
#   '\ntorch tensor:', torch_data,
#   '\ntensor to array:\n', tensor2arr,
# )
#
#
# data = [-1, -2, 2, 2]
# tensor = torch.FloatTensor(data)
# print(
#     '\nabs:',
#     '\ntorch tensor:', np.abs(data),
#     '\ntensor to array:\n', torch.abs(tensor)
# )

"""
logistic
"""
from torch.autograd import Variable
import torch.nn.functional as F


x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = x.pow(2) + 0.2 * torch.rand(x.size())

x, y = Variable(x), Variable(y)
# construct neural net


class neuralNet(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(neuralNet, self).__init__()




















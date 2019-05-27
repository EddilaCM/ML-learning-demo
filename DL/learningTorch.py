# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     simpleDemo
   Description :  learningTorch
   Author :       cm
   date：          2019/5/6
-------------------------------------------------
   Change Activity:
                   2019/5/6:
-------------------------------------------------
"""
import torch
import torch.nn as nn
import torch.nn.functional as F


"""define a network"""
class myNet(nn.Module):
    """
    Module 的作用就是结构化定义网络的层，提供对该层的封装（层结构， 参数，操作）
    """

    def __init__(self):
        super(myNet, self).__init__()
        # kernel
        # 创建子网络，同时初始化网络参数
        self.conv1 = nn.Conv2d(1, 6, 5)    # 输入的channel是1， 输出的channel是8，卷积核的尺寸是5X5
        self.conv2 = nn.Conv2d(6, 16, 5)   # 输入的channel是6， 输出的channel是16，卷积核的尺寸是5X5


class Net(torch.nn.Module):
    """一个卷积层，一个池化层，一个全连接层"""
    def __init__(self):
        super(Net, self).__init__()
        self.conv = nn.Conv2d(3, 8, 5)
        self.pool = nn.MaxPool2d(3)
        self.fc = nn.Linear(256, 10)

    def forward(self, x):
        x = self.conv(x)
        x = F.relu(x)
        x = self.pool(x)
        x = x.view(-1, 256)
        x = self.fc(x)
        return x

import torch.optim as optim
from torch.autograd import Variable


if __name__ == '__main__':
    # train model
    dataloader = ''
    net = Net()
    # net = Net().cuda() # use GPU
    net = Net().cuda() # use GPU
    from torch.nn import DataParallel

    net = DataParallel(Net().cuda()) # use multiple GPUS in one machine

    criterion = nn.CrossEntropyLoss()
    # criterion = nn.CrossEntropyLoss().cuda() # use GPU

    optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)
    for epoch in range(10):
        for i, data in enumerate(dataloader):
            x, label = data
            x, label = Variable(x), Variable(label)
            # x, label = Variable(x).cuda(), Variable(label).cuda() # use GPU
            output = net.forward(x)
            loss = criterion(output, label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()



#!/usr/bin/python
# -*-coding: UTF-8 -*-
from dataread import dataread

MAX_ELEMENT = 101
origin = "temp_origin.dat"
iteration = "temp.dat"


def evaluation(bias: list):
    index_origin = []
    index_iteration = []
    temp_origin = []
    temp_iteration = []

    low = 0
    nearby = 0
    high = 0

    dataread(origin, index_origin, temp_origin)
    dataread(iteration, index_iteration, temp_iteration)

    for i in range(0, MAX_ELEMENT):
        bias.append(temp_iteration[i] - temp_origin[i])
        if bias[i] < 0:
            low = low + 1
        elif bias[i] > 0:
            high = high + 1
        else:
            nearby = nearby + 1

    return low, nearby, high


if __name__ == '__main__':
    bias = []
    low, nearby, high = evaluation(bias)
    print(low, nearby, high)

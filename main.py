#!/usr/bin/python
# -*-coding: UTF-8 -*-
from APDLmodify import APDLmodify
from ansys import ansys
from evaluation import evaluation


def stepCalc(low: int, nearby: int, high: int, bias: list):
    if ((nearby != 0) and (low == 0) and (high == 0)):
        return 0
    elif ((low != 0) and (high == 0)):
        return 0.1
    elif ((low == 0) and (high != 0)):
        return -0.1


def calc():
    depth = 0.3
    bias = []

    while True:
        print("cur: " + str(depth))
        APDLmodify(depth)
        ansys()
        low, nearby, high = evaluation(bias)
        step = stepCalc(low, nearby, high, bias)
        print(low, nearby, high)
        if step == 0:
            break
        depth = depth + step
        bias.clear()
        if depth > 0.6:
            break

    print("fin: " + str(depth))


if __name__ == '__main__':
    calc()

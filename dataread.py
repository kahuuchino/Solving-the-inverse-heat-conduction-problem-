#!/usr/bin/python
# -*-coding: UTF-8 -*-
import re

pos_start = 482
pos_offset = 1643
length_line = 28
column = 42


def dataread(filename: str, index: list, temperature: list):
    data = open("../" + filename, "r")

    data.seek(pos_start, 0)
    for i in range(0, column):
        dataStr = data.read(length_line)
        ss = re.findall(r"[-+]?\d*\.\d+|\d+", dataStr);
        index.append(float(ss[0]))
        if i == 1:
            temperature.append(float(ss[2]))
        else:
            temperature.append(float(ss[1]))

    data.seek(pos_start + pos_offset * 1, 0)
    for i in range(0, column):
        dataStr = data.read(length_line)
        ss = re.findall(r"[-+]?\d*\.\d+|\d+", dataStr);
        index.append(float(ss[0]))
        temperature.append(float(ss[1]))

    data.seek(pos_start + pos_offset * 2, 0)
    for i in range(0, 17):
        dataStr = data.read(length_line)
        ss = re.findall(r"[-+]?\d*\.\d+|\d+", dataStr);
        index.append(float(ss[0]))
        temperature.append(float(ss[1]))

    data.close()


if __name__ == '__main__':
    index = []
    temperature = []
    dataread("temp.dat", index, temperature)
    for i in range(0, 101):
        print(index[i], temperature[i])

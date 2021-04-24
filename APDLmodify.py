#!/usr/bin/python
# -*-coding: UTF-8 -*-

inst = "!DEPTH-IDENTIFIER-AHEAD \nWPOFFS,0.3,0\n"


def APDLmodify(depth: float):
    inst = "!DEPTH-IDENTIFIER-AHEAD \nWPOFFS," + str(depth) + ",0\n"

    APDL = open("../modify.txt", "a+", encoding="UTF-8")
    APDL.seek(0, 0)
    content = APDL.read()
    APDL.close()

    pos1 = content.find("!DEPTH-IDENTIFIER-AHEAD")
    pos2 = content.find("!DEPTH-IDENTIFIER-TAIL")

    content = content[:pos1] + inst + content[pos2:]
    APDL = open("../modify.txt", "w", encoding="UTF-8")
    APDL.write(content)
    APDL.close()


if __name__ == '__main__':
    APDLmodify(0.3)

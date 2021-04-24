import os

ansys_inst = "D:\\Graduation Project\\Arithmetic\\Python\\ansys_batch.bat"
commandText = '"' + ansys_inst + '"'


def ansys():
    os.system(commandText)
    # print("Complete")


if __name__ == '__main__':
    os.system(commandText)
    print("Complete")

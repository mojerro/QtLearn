"""
    author: JoeyGaojingxing
    time:
"""
from ctypes import CDLL, cdll, windll, oledll

oledll.LoadLibrary('test.dll')
lib = CDLL('test.dll')

if __name__ == '__main__':
    res = lib.Sum(2, 3)
    print(res)

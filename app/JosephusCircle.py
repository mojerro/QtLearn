from ctypes import CDLL, c_char_p
from utils.utils import convert_byte
import os

"""
types:
9 5 1
[1 2 3 4 5 6 7 8 9]
end1 [5 1 7 4 3 6 9 2 8]
end2 [5 1 7 4 3 6 9 2 8]
result: 
b'\x05\x01\x07\x04\x03\x06\t\x02\x08\x01\x10\xac\xef\x01'
b'\x05\x01\x07\x04\x03\x06\t\x02\x08\x01\x10\xac\xef\x01'
"""

path = os.path.join(os.getcwd(), r'build\JosephusCircle.so')
josephus = CDLL(path)


def josephus_circle_arr(length: int, times: int, starter: int) -> list:
    res = josephus.JosephusCircleArr
    res.restype = c_char_p
    return convert_byte(res(length, times, starter))[:length]


def josephus_circle_linked_list(length: int, times: int, starter: int) -> list:
    res = josephus.JosephusCircleLinkedList
    res.restype = c_char_p
    return convert_byte(res(length, times, starter))[:length]

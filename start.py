"""
    author: JoeyGaojingxing
    time:
"""

from ctypes import *
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

josephus = CDLL(r'D:\Programming\dataStructureByGo\test.so')

if __name__ == '__main__':
    res = josephus.JosephusCircleArr
    link = josephus.JosephusCircleLinkedList
    res.restype = c_char_p
    link.restype = c_char_p
    res = res(9, 5, 1)
    # chr(code)
    # ord(c)
    link = link(9, 5, 1)
    print('result: ', res, link, sep='\n')

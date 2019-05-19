"""
    author: JoeyGaojingxing
    time:
"""
from app.JosephusCircle import josephus_circle_arr, josephus_circle_linked_list

if __name__ == '__main__':
    print('linked list: ', josephus_circle_linked_list(9, 5, 1))
    print('arr: ', josephus_circle_arr(9, 5, 1))

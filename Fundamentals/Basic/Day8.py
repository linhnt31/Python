"""
12 / 3 / 2019
- Material : https://dttvn0010.github.io
"""
import time


# set_ = set()
# set_.add(10)
# print(set_)


# dicts = {
#     'one' : 1, 
#     'two' : 2
# }
# print(dicts.get('one'))

# for k in dicts:
#     print(k, ' -----> ', dicts[k])

# for k, v in dicts.items():
#     print(k, ' ---> ', v)

# print(dicts.'one')

import string

text = """
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
"""
# text = text.split()
# tokens = []

# for x in text:
#     if x not in string.punctuation:
#         tokens.append(x)

# word_counts = {}

# for ch in tokens:
#     word_counts[ch] = word_counts.get(ch, 0) + 1

# items = [(v, k) for k, v in word_counts.items()]
# items = sorted(items, reverse= True)

# for count, word in items:
#     print(f'{word} : {count}') #string template


def sum_of_items(n):
    if n == 1:
        return 1
    return n + sum_of_items(n - 1)

if __name__ == "__main__":
    print(sum_of_items(5))
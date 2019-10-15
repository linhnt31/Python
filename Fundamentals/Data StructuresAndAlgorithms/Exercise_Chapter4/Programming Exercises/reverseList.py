"""
Write a recursive function to reverse a list.
"""

def reverse_list(lst):
    if len(lst) == 1:
        return lst
    return lst[-1:] + reverse_list(lst[:-1])

if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 1, -5]))
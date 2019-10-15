"""ex1: """

# def count_money(m, p):
#     diff = m - p
#     n_5k, n_20k, n_50k = 0, 0, 0
#     while diff > 0:
#         if diff >= 50000:
#             n_50k += 1
#             diff -= 50000
#         elif diff >= 20000:
#             n_20k += 1
#             diff -= 20000
#         else:
#             n_5k += 1
#             diff -= 5000
#     return [n_5k, n_20k, n_50k]
        

# if __name__ == "__main__":
#     p = int(input("Price of products: "))
#     m = int(input("A number of money entered: "))
#     print(count_money(m, p))


""" ex2 """
# import string

# def check_pass(pass_word)->bool:
#     if len(pass_word) < 6:
#         return False

#     for ch in pass_word:
#         if ch in string.punctuation or ch == ' ':
#             return False
#     return True

# if __name__ == "__main__":
#     pass_word = input("Enter a password: ")
#     valid = check_pass(pass_word)
#     if valid:
#         print('password is valid')
#     else:
#         print('pass is not valid')

""" ex3"""
import string

def encode(data, k):
    data = data.upper()
    res = []
    for ch in data:
        if 'A' <= ch <= 'Z':
            if chr(ord(ch) + k) <= 'Z':
                res.append(chr(ord(ch) + k))
            else:
                res.append(chr(155 - ord(ch) + k  - 1))
        else:
            res.append(ch)
    return "".join(res)

if __name__ == "__main__":
    print(encode('abc dz',2))
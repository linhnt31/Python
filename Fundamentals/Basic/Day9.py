# def calcRect(width, height=10):
#     p = 2 * ( width + height)
#     s = width * height

#     return p, s

# p, s = calcRect(2, 3)
# print(f'Chu= {p} vs dien tich= {s}')


# def f(x):
#     return x ** 3 + x - 1

# a, b = 0, 1
# eps = 10**6 -6

# while b - a > eps:
#     m = (b + a) / 2
#     fm = f(m)
#     if fm < 0:
#         a = m
#     else:
#         b = m 

""" Lambda function """

# def intergate(f, a, b):
#     N = 1000
#     step = (b - a) / N

#     return sum([f(a+ i * step) for i in range(N + 1)]) * (b - a) /(N + 1)

# def f(x):
#     return x * x

# if __name__ == "__main__":
#     print(round(intergate(f, 0, 1), 2))
#     print(intergate(lambda x : x ** 3, 0, 1)
# import sys

# text = """ Beautiful is better than ugly.Explicit is better than implicit Simple is better than complex Complex is better than complicated"""
# words = text.split()
# word_count = {}

# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# items = word_count.items()
# # print(items)

# items = sorted(items, key= lambda x : x[1], reverse= True)
# print(items)

# print(sys.path)


""" File I/O """
""" File CSV: """
# def readInput(fileName):
#     # f = open(fileName, encoding='utf-8')
#     # lines = f.read()
#     # print(lines)
#     # f.close()

#     #Don't need close file --> more useful than above method
#     with open(fileName, encoding='utf-8') as f:
#         lines = f.read()
#         print(lines)

# def writeInput(fileName):
#     with open(fileName, 'w', encoding='utf-8') as f:
#         f.write('Python is impressive')


# if __name__ == "__main__":
#     writeInput('test.txt')
#     readInput('test.txt')



if __name__ == "__main__":
    fi =  open('bill.csv', encoding='utf-8')
    fo = open('billOutPut.csv', 'w', encoding='utf-8')

    lines = fi.readlines()

    for line in lines:
        tmp = line.strip().split(',')
        Materials, Amount, Price = tmp
        if '0' <= Amount <= '9':
            luong, gia = int(Amount), int(Price)

            sum_of_price = luong * gia
            fo.write(f'{Materials}, {luong}, {gia}, {sum_of_price}\n')
        else:
            fo.write(f'{Materials}, {Amount}, {Price}, {"Sum of money"}\n')
        
    fi.close()
    fo.close()


#Exercise: 

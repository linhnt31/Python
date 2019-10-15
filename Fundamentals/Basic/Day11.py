# def sumOfList(alist):
#     for i in range(len(alist)):
#         for j in range(i + 1, len(alist)):
#             if (alist[i] + alist[j]) in alist:
#                 res = alist[i] + alist[j]
#                 print(f'{alist[i]} + {alist[j]} = {res} ')

# if __name__ == "__main__":
#     alist = [10, 20, 30, 50, 15, 75, 65]
#     sumOfList(alist)

# def ex2():
#     s = '123456789'
#     sign = ['', '+', '-']
#     # res = ''
#     for num in range(0, 6561):
#         digits = convert3base(num)
#         exp = ''
#         for i in range(len(s) - 1):
#             exp += s[i]
#             exp += sign[digits[i]]
        
#         exp += s[-1]
#         value = eval(exp)
#         if value == 100:
#             print(exp)

# def convert3base(x):
#     tmp = int(x)
#     digits = []
#     while tmp > 0 :
#         digits.insert(0, tmp % 3)
#         tmp //= 3


#     return [0] * (8 - len(digits)) + digits

# if __name__ == "__main__":
#     ex2()


# if __name__ == "__main__":
#     i = int(input("Enter row: "))
#     j = int(input("Enter column: "))

#     a, b = i, j
#     matrix = [[0] * 4 for _ in range(4)]
#     matrix[a][b] = 2
    
#     for i in range(len(matrix)):
#             if i == a or i == b:
#                 matrix[i][i] = 1

#     a, b = i, j
#     while 0 <= a < 4 and 0 <= b < 4 :
#         matrix[a][b] = 1
#         a -= 1
#         b -= 1
#     a, b = i, j
#     while 0 <= a < 4 and 0 <= b < 4 :
#         matrix[a][b ] = 1
#         a += 1
#         b += 1
#     a, b = i, j
#     while 0 <= a < 4 and 0 <= b < 4 :
#         matrix[a][b] = 1
#         a += 1
#         b -= 1
#     a, b = i, j
#     while 0 <= a < 4 and 0 <= b < 4 :
#         matrix[a ][b ] = 1
#         a -= 1
#         b += 1
                
#     print(matrix)


# points  =  ['A', 'B', 'C', 'D']

# distances = {
#     ('A', 'B') : 10,
#     ('B', 'C') : 5,
#     ('A', 'C') : 15,
#     ('B', 'D') : 7,
#     ('C', 'D') : 5
# }

# def find_path(p1, p2):
#     paths = []
#     if p1 == p2:
#         return 0, p1
#     for p in points:
#         if (p1, p) in distances:
#             d_p1_p = distances[(p1,p)]
#             del distances[(p1,p)]
#             route_length, route = find_path(p, p2)
#             distances[(p1,p)] = d_p1_p
#             if route_length >= 0:
#                 route_length += d_p1_p
#                 route = p1 + '->' + route
#                 paths.append((route_length, route))

#     if len(paths) > 0:
#         paths = sorted(paths)
#         return paths[0]
#     else:
#         return -1, ''
# print(find_path('A', 'A'))


points = ['A', 'B', 'C', 'D']
edges = {('A','B'), ('B', 'C'), ('B', 'D'), ('C', 'D')}

def find_path(src, dst):
    routes = {src : [src]}
    leaves = [src]
    while len(leaves) > 0:
        next_leaves = set()
        for leaf in leaves:
            neigbours = [p for p in points if (leaf, p) in edges
                         and p not in routes]

            for p in neigbours:
                routes[p] = routes[leaf] + [p]
                next_leaves.add(p)
        leaves = next_leaves
    return routes[dst]
print(find_path('A', 'D'))
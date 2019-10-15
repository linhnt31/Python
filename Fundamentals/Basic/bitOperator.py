"""
-Refferences: https://www.tutorialspoint.com/python3/bitwise_operators_example.htm
- Link: https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/introduction_to_bitwise_operators/bitwise_operators.html
"""


a = 60 # 0011 1100
b = 13 # 0000 1101

print(a & b , bin(a & b))
print(b | a, bin( a | b))
print(a ^ b , bin(a ^ b))
print(a >> 2, bin(a >> 2))
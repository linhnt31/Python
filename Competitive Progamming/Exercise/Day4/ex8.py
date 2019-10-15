'''
BT8:
Cho 1 list như sau:
samples = ["python", None, "cpython", True, 1, 1 + 1j, False, [100, 200, 300], 99.99, (31, "January")]
Lọc lấy ra các phần từ là số của list samples
'''


samples = ["python", None, "cpython", True, 1, 1 + 1j, False, [100, 200, 300], 99.99, (31, "January")]
res = []

for sample in samples:
    if isinstance(sample, (int, float, complex)) \
                and sample is not True \
                and sample is not False:
        res.append(sample)

print(res)
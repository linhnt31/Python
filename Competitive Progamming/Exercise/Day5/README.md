    
### BT1

- Tạo 1 file .txt chứa 30 triệu dòng, dòng mà số dòng chia hết cho 3 thì ghi "Buzz", chia hết cho 5 thì ghi "Fizz", chia hết cho 15 thì ghi "FizzBuzz", còn ko thì ghi số thứ tự chính là dòng hiện tại

```python
1
2
Buzz
4
Fizz
...
```

- Ko up file data (.txt) lên github

### BT2

- Với file đã tạo ra từ bài 1, làm thế nào để có 1 list chứa 10 dòng cuối (list 10 phần tử)

### BT3

- Tính tiền điện dùng trong 1 tháng: với ít hơn 50 số điện, tính giá 15000vnd/1 số, từ số điện thứ 51 đến 200, tính giá 16500vnd/1 số, dùng lớn hơn 200 số điện thì tính giá 20000vnd/ 1 số

- Lần lượt tính tiền điện ứng với các số điện đã dùng sau: 48, 100, 150, 199, 250, 1000

### BT4

- Cho đoạn văn bản sau

```text
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python Web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.

The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.

This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.

For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.

This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library.
```

Làm theo 2 cách:

- Trả vể list chứa 10 tuple ứng với 10 từ xuất hiện nhiều nhất theo format:

```python
result = [('if', 10), ...]
```

- Trả về dict chứa 10 phần tử xuất hiện nhiều nhất cùng số lần xuất hiện theo format:

```python
result = {"if": 10, ...}
```

- Lưu ý: không quan trọng uppercase và lowercase 

### BT5

- Với 2 list:

```python
L1 = [1, 2, 3, 4, 5, 6]
L2 = [3, 4, 5, 6, 7, 8, 9, 10]
```

- Lấy các phần tử:
  - Có trong cả A, B
  - Chỉ có trong A
  - Chỉ có trong B
  - Không có trong cả A và B
  
 - Dùng kiến thức đã học trong buổi hôm nay, ko dùng vòng lặp sử dụng list

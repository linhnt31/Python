# Note

- import dbn; dbn
- list
    - list chứa sample cùng kiểu dữ liệu
- tuple 
    - chứa các sample thuộc cùng 1 đối tượng
- tuple is iterable
- 'is' keyword : None , True, False


***Useful Function***
- sorted(iterable, key, reverse)
    - [Referrences]( https://www.geeksforgeeks.org/sorted-function-python/ )
    -  returns a new sorted list, leaving the original list.
    - iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset)

- What is the difference between `sorted(list)` vs `list.sort()`?
    - [Referrences]( https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort )

- all(iterable)
    - [Referrences] ( https://www.programiz.com/python-programming/methods/built-in/all )
    - returns True when all elements in the given iterable are true. If not, it returns False.

- any(iterable)
    - [Referrences] ( https://www.programiz.com/python-programming/methods/built-in/any )
    -  returns True if any element of an iterable is True. If not, any() returns False.

- yeild
    - [yield_Keyword] ( https://www.geeksforgeeks.org/python-yield-keyword/ )

    - return a generator from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement.

    - Advantages:
        1. Overhead of memory allocation is controlled.
        2. Since the old state is retained, flow doesn’t start from the beginnning and hence saves time.
    
    - Disadvantages: 
        1. Logic is difficult to understand.

    - Important: 
        1. when you call the function, the code you have written in the function body does not run. It only trturns the generator obk=ject

        
***Map, Reduce, Filter***
- [Referrences]( http://book.pythontips.com/en/latest/map_filter.html )

- map(func, inp_list):
    - applies a func to all the items in an inp_list
    - Mosts of the times we use lambdas with 'map'

- reduce(func , inp_list):
    - func(arg1, arg2)
    - arg1: previous results
    - arg2: computing now 

- filter(func, list):
    - creates a list of elements for which a func returns true.


***String***
- __strip()__ :
    -Elimunating space at the begin and last of string

- __ord(char)__: 
    - return an integer representing the Unicode code point of that character.
    - example: ord('a') --> return 97 

- __chr(number)__:
    -Return the string representing a character whose Unicode code point is the integer number.
    - example: chr(97) --> 'a
    - This is the inverse of ord() method


- __zip()__ :
    - is to map the similar index of multiple containers


***File I / O*** 
[Referrences]( http://openbookproject.net/thinkcs/python/english3e/files.html )
- __Mode__:
    - Mode "w" means that we are opening the file for writing.
    - write() method: put data in the file.
    - readline() method: returns everything up to and including the newline character.
    - readlines() method: reads all the lines and returns a lists of strings
    - if we don’t supply the mode, Python opens the file for reading.


***Python Frequently Asked Questions***

- [UnboundLocalError](https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value)
- How to fix: 'global' keyword


***Addition***

- __Underscore__ :
    - _nameVariable : private in Java but we can acess != Java

- *args, **kwargs
    - Allow you to pass a variable number of arguments to a function.

    -When we dont know how many arguments need to be passed to a python function --> __use Packing  to pack all arguments in a tuple__.


    
- __Packing__ and __Unpacking__ :
    - Use 2 operators :
        1. * for tuple()
        2. ** for dictionary
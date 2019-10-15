***Class***
- If the first line after the class header is a string, it becomes the docstring of the class, and will be recognized by various tools. (This is also the way docstrings work in functions.)

- Every class should have a method with the special name "__init__"
    - This initializer method is automatically called whenever a new instance of Class is created.

- Keyword 'self' <==> Keyword 'this' in Java, C#


***Object***
- Objects are mutable

- We can change attributes of an object

- By default, '==' operator on an obj does a shallow equallity test
    - In contrast to using '==' operator in list.
    - By default , '==' operator does a deep equality test on lists.

***Attributes***
- One object has both attributes and methods


***Sameness***
- Module : import copy

- deepcopy: 
    - To copy the contents of an object as well as any embedded objects, and any objects embedded in them, and so on; implemented by the deepcopy function in the copy module.

- shallow copy:
    - To copy the contents of an object, including any references to embedded objects; implemented by the copy function in the copy module.

- deep equality:
    - Equality of values, or two references that point to objects that have the same value.

- shallow equality:
    - Equality of references, or two references that point to the same object.
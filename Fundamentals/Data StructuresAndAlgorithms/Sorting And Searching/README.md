# Hashing

- __Hash table__: 
    - is a collection of items which are stored in such a way as to make it easy to find them later.

    - Each position of the hash table, often called a __slot__, can hold an item and is named by an integer value starting at 0.

    ![Image](http://interactivepython.org/runestone/static/pythonds/_images/hashtable.png)

    - The mapping between an item and the slot where that item belongs in the hash table is called the __hash function__. 

    - __load factor__  = numberOfItems / tableSize
    ![Image](http://interactivepython.org/runestone/static/pythonds/_images/hashtable2.png)

    - Ways to extent remainder method: 
        1. The __folding method__ for constructing hash functions begins by dividing the item into equal-size pieces (the last piece may not be of equal size).

        2. The mid-square method: square the item and then extract some portion of the resulting digits.

  


# Sorting

__Bubble Sort__ 

- The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.

![Image](http://interactivepython.org/runestone/static/pythonds/_images/bubblepass.png)




__Selection Sort__

- The selection sort improves on the bubble sort by making _only one exchange_ for every pass through the list.

- So selection sort excutes faster than bubble sort

![Image](http://interactivepython.org/runestone/static/pythonds/_images/selectionsortnew.png)




__Insertion Sort__

- Each pass produces a longer sorted list.

- It always maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.

- One note about shifting versus exchanging is also important. In general, ***a shift operation*** requires approximately ***a third of the processing work*** of ***an exchange*** since only one assignment is performed.

![Image](http://interactivepython.org/runestone/static/pythonds/_images/insertionsort.png)



__Shell Sort__ 

- is ultimate version of __insertion sort__

- Keyword: __gap__

- In shellSort, we make the array gap-sorted for a large value of gap. We keep reducing the value of gap until it becomes 1.

![Image](http://interactivepython.org/runestone/static/pythonds/_images/shellsortC.png)
![Image](http://interactivepython.org/runestone/static/pythonds/_images/shellsortA.png)




__Merge Sort__

- Using divide and conquer strategy.

- A merge sort is O(n log n), but requires additional space for the merging process.

![Image](http://interactivepython.org/runestone/static/pythonds/_images/mergesortA.png)




__Quick Sort__

- uses divide and conquer as the merge sort.
- Not using additional storage
- __The key process__ in quickSort is __partition()__, __in place algorithm != merge sort__
- Key word: ***pivot value***, ***split point***
- All arrangement is happening in original list
![Image](http://interactivepython.org/runestone/static/pythonds/_images/partitionA.png)
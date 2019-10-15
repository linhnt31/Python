# NOTE

[Source](https://www.geeksforgeeks.org/dynamic-programming/)

- Concept: Dynamic Programming is mainly an optimization over plain recursion.
    - Dynamic progamming = Recursion + memoization

- Application:
    - This simple optimization reduces time complexities from __exponential__ to __polynomial__.
    - Wherever __we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming__.

![Image](https://www.geeksforgeeks.org/wp-content/uploads/Dynamic-Programming-1-768x384.png)

- Tabulation vs Memoizatation:
    - There are following two different ways to store the values so that the values of a problem can be reused.
    1. Tabulation: Bottom up
    2. Memoizatation: Top down

- Running time: 
    - Time = sum of subproblems * (time per subproblem)
        - ex:  n * O(1)
        - Tips: Dont count recursions
# Nth Fibonacci

## Problem

The Fibonacci sequence is defined as follows: the first number of the sequence is `0`, the second number is `1`, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a function that takes in an integer `n` and returns the nth Fibonacci number.
Important note: the Fibonacci sequence is often defined with its first two numbers as `F0 = 0`
and
`F1 = 1`. For the purpose of this question, the first Fibonacci number is `F0`; therefore, `getNthFib (1)`
is equal to
`F0`,
`getNthFib(2)` is equal to
`F1``
. etc..

**Sample Input #1**

```
n = 2
```

**Sample Output #1**

```
1 // 0, 1
```

**Sample Input #2**

```
n = 6
```

**Sample Output #2**

```
5 // 0, 1, 1, 2, 3, 5
```

#

## Approach 1: BruteForce

```PYTHON
def getNthFib(n):
    n1=0
    n2=1
    n3=n1+n2
    counter=3

    if n == 1:
        return 0
    else:
        while counter < n:
               n1=n2
               n2=n3
               n3=n1+n2
               counter+=1

        return n3


```

### Complexity Analysis

- Time Complexity: O(n), where N is the length of the input array.
- Space Complexity: O(1).

## Approach 2: Recursive

```PYTHON
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)

```

### Complexity Analysis

- Time Complexity: O(2^n), where N is the length of the input array.
- Space Complexity: O(n).

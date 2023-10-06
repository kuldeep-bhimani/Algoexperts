# Sorted Squared Array

## Problem

Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

Sample Input

```
array = [1, 2, 3, 5, 6, 8, 9]
```

Sample Output

```
[1, 4, 9, 25, 36, 64, 81]
```

#

## Approach 1: Brute Force + Sort

```PYTHON

def sortedSquaredArray(array):
    result=[0 for _ in array]
    for item in array:
        mul=item*item
        result.append(mul)

    result.sort()
    return result

```

### Complexity Analysis

- Time Complexity: O(N \* log(N)), where N is the length of the input array.
- Space Complexity: O(N), where N is the length of the input array.

#

## Approach 2: Two Pointers

```PYTHON
def sortedSquaredArray(array):
    result=[0 for _ in array]
    start=0
    end=len(array)-1
    last_index=len(array)-1

    for i in array:
        counter=0
        if abs(array[start]) < abs(array[end]):
            mul=array[end]*array[end]
            result[last_index-counter]=mul
            last_index-=1
            end-=1
        else:
            mul=array[start]*array[start]
            result[last_index-counter]=mul
            last_index-=1
            start+=1
            counter+=1
    return result

```

### Complexity Analysis

- Time Complexity: O(N), where N is the length of the input array.
- Space Complexity: O(N), where N is the length of the input array.

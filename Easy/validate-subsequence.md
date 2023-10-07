# Validate Subsequence

## Problem

Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers `[1, 3, 4]` form a subsequence of the array `[1, 2, 3, 4]`, and so do the numbers `[2, 4]`. Note that a single number in an array and the array itself are both valid subsequences of the array.

Sample Input

```
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
```

Sample Output

```
true
```

#

## Approach 1: Array Single Scan

```PYTHON
def isValidSubsequence(array, sequence):
    # Write your code here.
    index=0
    for idx, element in enumerate(array):
        if index == len(sequence):
            return True
        if sequence[index] == element:
            index+=1
    return True if index == len(sequence) else False

```

### Complexity Analysis

- Time Complexity: O(N), where N is the length of the input array.
- Space Complexity: O(1).

## Approach 2: Liner Traversing of array

```PYTHON

def isValidSubsequence(array, sequence):
    result = [0 for _ in sequence]
    counter=0
    arr_len = len(array)
    seq_len = len(sequence)
    seq_item = 0
    arr_item = 0
    # comapring array item with sequence array
    # if match found continues from the next sequ item and array item
    # do not need to traverse whole array
    while counter != arr_len:
        if seq_item == seq_len:
            break
        elif array[arr_item] == sequence[seq_item]:
            result[seq_item]=sequence[seq_item]
            print(result)
            seq_item+=1
        arr_item+=1
        counter+=1

    if result == sequence:
        return True
    else:
        return False


```

### Complexity Analysis

- Time Complexity: O(N), where N is the length of the input array.
- Space Complexity: O(1).

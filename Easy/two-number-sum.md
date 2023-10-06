# Two Number Sum

## Problem

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

You can assume that there will be at most one pair of numbers summing up to the target sum.

Sample Input

```
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
```

Sample Output

```
[-1, 11] // the numbers could be in reverse order
```

#

## Approach 1: Brute Force (one for loop)

```PYTHON

def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in array:
        sum=targetSum-i

        if sum in array and sum != i:
            print(sum,i)
            return [sum, i]
    return []

```

### Complexity Analysis

- Time Complexity: O(N), where N is the length of the input array.
- Space Complexity: O(1).

#

## Approach 2: One Pass with Two Pointers

```PYTHON

def twoNumberSum(array, targetSum):
    # sorting array
    sorted_array=array.sort()
    # pointers at the start & end of array
    left=0
    right=len(array)-1

    # looping array and summing it's last and first value
    # if sum is greater than target then must decrement pointer from the end
    for item in array:
        sum=array[left]+array[right]
        if sum == targetSum:
            return [array[left], array[right]]
        elif sum > targetSum:
            right=right-1
        else:
            left=left+1
    return []

```

### Complexity Analysis

- Time Complexity: O(N), where N is the length of the input array.
- Space Complexity: O(N), where N is the length of the input array.

# Minimum Waiting Time

## Problem

You are given a non-empty array of positve integers representing the amounts of time that specific queries take to execute. Only one can be executed at a time, but the queries can be executed in any order.

A query's **waitng time** is defined as the amount of time it must wait before its execution starts. In other words, if a query is executed second, then its waiting time is the duration of the first query; if a query is executed third, then its waiting time is the sum of the durations of the first two queries.

Write a function that returns the minimu amount of total waiting time for all the queries. For example, if you're given the queries of durations `[1, 4, 5]`, then the total waiting time if the queries were executed in the order of `[5, 1, 4]` would be `(0) + (5) + (5 + 1) = 11` . The first query of duration `5` would be executed immediately, so its waiting time would be `0`, the second query of duration `1` would have to wait `5` seconds (the duration of the first query) to be executed, and the last query would have to wait the duration of the first two queries before being executed.

**Note**: you're allowed to mutate the input array.

**Sample Input**

```
queries = [3, 2, 1, 2, 6]
```

**Sample Output**

```
17
```

#

## Approach 1: Two loops

```PYTHON
def minimumWaitingTime(queries):
    sorted_array=queries.sort()
    sum=0
    mainSum=0
    length=len(queries)
    for i in range(length):
        index=0
        while index < i:
            sum+=queries[index]
            print(queries[index])
            index+=1
    mainSum+=sum
    return mainSum

```

### Complexity Analysis

- Time Complexity: O(nlogn), where N is the length of the input array.
- Space Complexity: O(1).

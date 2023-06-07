def isValidSubsequence(array, sequence):
    # Write your code here.
    index=0
    for idx, element in enumerate(array):
        if index == len(sequence):
            return True
        if sequence[index] == element:
            index+=1
    return True if index == len(sequence) else False
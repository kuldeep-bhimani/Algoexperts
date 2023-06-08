def sortedSquaredArray(array):
    # Write your code here.
    result=[]
    for item in array:
        mul=item*item
        result.append(mul)


    result.sort()
    print(result)
                
        # return [item*item]
    return result

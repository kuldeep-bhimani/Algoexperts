def sortedSquaredArray(array):
    # temp array
    result=array.copy()
    start=0
    index=0
    end=len(array) - 1    
    deadend=len(array) - 1   

    # iterating array from both the end and compare the squared value to sort it
    while index < len(array):
        left=array[start]
        right=array[end]
        leftmost=abs(left)
        rightmost=abs(right)
        print(leftmost,"fghjk", rightmost)
        if leftmost < rightmost:
            mul=right*right
            result[deadend-index]=mul
            end-=1
            index+=1
        elif leftmost > rightmost:
            mul=left*left
            result[deadend-index]=mul
            index+=1
            start+=1
        elif leftmost == rightmost:
            mulLeft=left*left
            mulRight=right*right
            result[deadend-index]=mulLeft
            result[deadend-index]=mulRight
            index+=1
            start+=1
        else:
            mul=left*left
            result[deadend-index]=mul
            index+=1
    return result

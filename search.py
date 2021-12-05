#binary search using recursion
lst=[12,13,24,25,35,46,56,57,67,68,78,79,89,90,123,234,456,789]
def func(n,left,right):
    if left<=right:
        middle=(left+right)//2
        if n>lst[middle]:
            left=middle+1
            return func(n,left,right)  #Recursive Entrance
        if n<lst[middle]:
            right=middle-1
            return func(n, left, right)  # Recursive
        if n==lst[middle]:
            print("Find it!")
            return middle #Recursive return returns terminate recursion
    else:
        print("There isn't the number")
        return -1
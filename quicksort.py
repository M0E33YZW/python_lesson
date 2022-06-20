def quickSort(A, left, right):
    Left = left
    Right = right
    pivot = A[int((left + right) / 2)]
    
    print('A :', A)
    print('pivot:', pivot)

    while Left < Right:

        while A[Left] < pivot:
            Left += 1

        while pivot < A[Right]:
            Right -= 1

        if Left >= Right:
            break

        temp = A[Left]
        A[Left] = A[Right]
        A[Right] = temp

        Left += 1
        Right -= 1
    
    if left < Left - 1:
        quickSort(A, left, Left-1)
    
    if Right + 1 < right:
        quickSort(A, Right+1, right)

array = [8,2,7,6,5,1,4,3,9]
left = 0
right = (len(array) - 1)
quickSort(array, left, right)



def quickSort(x, top, last):
    i = top
    j = last
    pivot = x[int((top + last) / 2)]


  





    while True:
        print('x: ', x, 'pivot: ', pivot, 'i: ', i, 'j: ', j)
        while x[i] < pivot:
            i += 1

        while pivot < x[j]:
            j -= 1

        if i >= j:
            break

        work = x[i]
        x[i] = x[j]
        x[j] = work
        i += 1
        j -= 1
    
    if top < i - 1:
        quickSort(x, top, i-1)
    
    if j + 1 < last:
        quickSort(x, j+1, last)

array = [8,2,7,6,5,1,4,3,9]
top = 0
last = (len(array) - 1)
quickSort(array, top, last)
import sys

def insertionSort1(n, arr):
    # Complete this function
    temp = arr[n-1]
    flag = 0
    for i in range(n-2,-1,-1):
        if(temp < arr[i]):
            arr[i+1] = arr[i]
            for j in arr:
                print(j, end=' ')
            print('')
        else:
            arr[i+1] = temp
            for k in arr:
                print(k, end = ' ')
                flag = 1
            break
    if flag!=1:
        arr[0]=temp
        for k in arr:
            print(k, end =' ')
n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
insertionSort1(n, arr)

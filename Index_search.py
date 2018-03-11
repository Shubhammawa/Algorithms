import sys

def introTutorial(V, arr,n):
    # Complete this function
    l = 0
    u = n
    flag = 0
    while(flag != 1):
        m = int((u+l)/2)
        if(V == arr[m]):
            flag = 1
            return m
        elif(V >= arr[m]):
            l = m
        else:
            u = m

if __name__ == "__main__":
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = introTutorial(V, arr,n)
    print(result)

from bisect import bisect_left 
def binarySearch(arr,n,li,ri):
    leftindex = li
    rightIndex = ri
    while(leftindex<=rightIndex):
        mid = (leftindex+rightIndex)//2
        if(arr[mid]==n):
            return mid
        elif(arr[mid]<n):
            leftindex = mid+1
        else:
            rightIndex = mid-1
def binarySearchUsingBisect(a,x):
    i = bisect_left(a,x)
    if(i!=len(a) and a[i]==x):
        return i
    else:
        return -1
print(binarySearchUsingBisect([123,234,564,3445,6554,10000],6554))
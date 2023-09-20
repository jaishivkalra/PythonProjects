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
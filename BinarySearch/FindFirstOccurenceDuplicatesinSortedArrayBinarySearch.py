def FindFirstOccurenceDuplicatesinSortedArrayBinarySearch(arr):
    leftindex = 0
    rightIndex = len(arr)
    if(rightIndex==0):
       return 0
    elif(rightIndex<0):
        return -1
    while(leftindex<=rightIndex):
        mid = (leftindex+rightIndex)//2
        if(arr[mid] == arr[mid-1] or arr[mid] == arr[mid+1]):
            while(arr[mid-1] == arr[mid]):
                k = mid-1
                mid -= 1
            return k    
        elif(mid+1>arr[mid]):
            rightIndex = mid-1
        else:
            leftindex = mid+1
if __name__ == "__main__":
    l = [1,2,3,4,6,6,7]
    k = FindFirstOccurenceDuplicatesinSortedArrayBinarySearch(l)
    print(l[k])
    print(k)
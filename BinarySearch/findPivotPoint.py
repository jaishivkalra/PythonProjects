def findPivotPoint(arr):
    leftindex = 0
    rightIndex = len(arr)-1
    if(arr[leftindex]<arr[rightIndex]):
        return rightIndex
    if(rightIndex==0):
       return 0
    elif(rightIndex<0):
        return -1
    while(leftindex<=rightIndex):
        mid = (leftindex+rightIndex)//2
        if(arr[mid]>arr[mid+1] and arr[mid]> arr[mid-1]):
            return mid
        elif(arr[mid]>arr[leftindex]):
            leftindex = mid+1
        else:
            rightIndex = mid-1
if __name__ == "__main__":
    arr = [20,50,700,9000,100000,2000000,300000000,2,3]
    k = findPivotPoint(arr)
    print("Index is : "+str(k)+" and Element is : "+str(arr[k])+" and Key is : "+str(len(arr)-1-k)) 
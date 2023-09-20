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
def FindTargetInRotatedSortedArray(arr,t):
    pp = findPivotPoint(arr)
    if(arr[pp]==t):
        return pp
    if(t>arr[0] and t<arr[pp]):
        return binarySearch(arr,t,0,pp)
    else:
        return binarySearch(arr,t,pp+1,len(arr))
if __name__=="__main__":
    a = [3,4,5,6,7,8,9,1,2]
    b = [3,4,5,6,7,8,9,10,14,29]
    print(findPivotPoint(a))
    print(FindTargetInRotatedSortedArray(a,8))
    print (binarySearch(b,29,0,len(b)))

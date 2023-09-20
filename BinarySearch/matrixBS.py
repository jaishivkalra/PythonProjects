import numpy as np

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
def matrixBS(arr, n,i):
    arr1 = np.array(arr)
    oneDArrayF = arr1.flatten()
    a = binarySearch(oneDArrayF,n,0,len(oneDArrayF)-1)
    colIndex = ((a)%i)
    rowIndex = (a)//i
    return [rowIndex,colIndex]
if(__name__=="__main__"):
    a=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        [17,18,19,20]
        ]
    b = matrixBS(a,9,4)
    print("Row = "+str(b[0])+" Col = "+str(b[1]))
    
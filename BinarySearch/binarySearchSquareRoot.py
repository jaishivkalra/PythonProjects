def binarySearchSquareRoot(n):
    leftindex = 0
    rightIndex = n-1
    if(n==0):
       return 0
    elif(n<0):
        return -1
    while(leftindex<=rightIndex):
        mid = (leftindex+rightIndex)//2
        if(mid*mid==n or ((mid*mid<n) and ((mid+1)*(mid+1))>n)):
            return mid
        elif(mid*mid >n):
            rightIndex = mid-1
        else:
            leftindex = mid+1
if __name__ == "__main__":
    print(binarySearchSquareRoot(-34))            

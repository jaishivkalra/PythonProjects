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
def binarySearchSquareRootTillNDecimalPlaces(n,d):
    storedN = n
    l = binarySearchSquareRoot(n)
    if(l*l==n):
        return l
    n = l
    leftindex = 0
    rightIndex = 9
    count =0
    k = n
    res=n
    while(count<d):
        mid = (leftindex+rightIndex)//2
        if(count==0 and str(k).find('.')):
            k = round(float(str(res)+"."+str(mid)),count+1)
        else:
            k = round(float(str(res)+str(mid)),count+1)
        squareAtIndex = k*k
        squareAtNextIndex = (k+(10**-(count+1)))*(k+10**-(count+1))
        if(squareAtIndex==storedN or ((squareAtIndex<storedN) and (squareAtNextIndex>storedN))):
            count += 1
            res = round(k,count+1)
            leftindex=0
            rightIndex=9
        elif(squareAtIndex >storedN):
            rightIndex = mid-1
        else:
            leftindex = mid+1
    return res
if __name__ == "__main__":
    a = binarySearchSquareRootTillNDecimalPlaces(16876837618,6)
    print(a)
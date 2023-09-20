def printMatrixWave(arr):
    m = len(arr)
    n = len(arr[0])
    count = 0
    j = 0
    for j in range(0,n):
        if(j&1==0):
            for i in range(0,m):
                print(arr[i][j])
                count +=1
        else:
            for i in range(m-1,-1,-1):
                print(arr[i][j])
                count += 1
if(__name__=="__main__"):
    a=[
        [1,2,3,4,1],
        [5,6,7,8,2],
        [9,10,11,12,3],
        [13,14,15,16,4],
        [17,18,19,20,5]
        ]
    printMatrixWave(a) 
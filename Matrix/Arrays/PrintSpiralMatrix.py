def printSpiralofMatrix(arr):
    m = len(arr)-1
    n = len(arr[0])-1
    a=9
    firstRowIndex = 0 
    lastRowIndex = m
    firstColIndex = 0
    lastColIndex = n 
    while(firstRowIndex<=lastRowIndex and firstColIndex<=lastColIndex):
        #print upmost row right
        for i in range(firstColIndex,lastColIndex+1):
            print(arr[firstRowIndex][i])
        firstRowIndex += 1
        #print rightmost col down
        for i in range(firstRowIndex,lastRowIndex+1):
            print(arr[i][lastColIndex])
        lastColIndex -= 1
        #print downmost row left
        for i in range(lastColIndex,firstColIndex-1,-1):
            print(arr[lastRowIndex][i])
        lastRowIndex -= 1 
        #print leftmost col up
        for i in range(lastRowIndex,firstRowIndex-1,-1):
            print(arr[i][firstColIndex])
        firstColIndex += 1

if(__name__=="__main__"):
    a=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        [17,18,19,20]
        ]
    printSpiralofMatrix(a)
from collections import defaultdict
def findFirstRepeatingElement(arr):
    dict = defaultdict(int)
    for i in arr:
        dict[i] += 1    
    for i in arr:
        if dict[i]>1:
            return i
if __name__ == "__main__":
    l = [2,3,4,1,3,5,3,1,4]
    print(findFirstRepeatingElement(l))
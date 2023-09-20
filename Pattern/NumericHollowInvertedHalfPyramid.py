n = 5
for i in range(n):
    a=i+1
    for j in range(n-i,0,-1):
        if i == n-1 or i == 0 or j== n-i or j==1:
            print(a,end='')
            a+=1
        else:
            a+=1
            print (' ',end='')
    print('\n')
n = 5
for i in range(n):
    a=1
    for j in range((n-i-1)*2,0,-1):
        print(' ',end='')
    for j in range(2*i+1):
        print(str(a)+' ',end='')
        if(j < (2*i+1)//2):
            a+=1
        else:
            a-=1
    print('\n')
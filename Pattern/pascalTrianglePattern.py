n= 10
for i in range(1,n+1):
    a=1
    for j in range(1,i+1):
        print(str(a),end = '')
        a *= ((i-j)//j)
    print()
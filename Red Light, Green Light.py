n=int(input())
for i in range(n):
    a,b=map(int,input().split(' '))
    c=list(map(int,input().split(' ')))
    s=len(c)
    count=0
    for i in range(s):
        if c[i]>b:
            count+=1
    print(count)

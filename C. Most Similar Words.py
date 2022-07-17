t= int(input())
def diff(a,b):
	dif=0
	le= len(a)
	for i in range(le):
		dif+= abs(ord(a[i])-ord(b[i]))
	return dif
while t>0:
    t=t-1
    n,m= map(int, input().split())
    
    li=[]
    ans= 999999
    for i in range(0,n):
        j=i
        s= input()
        li.append(s)
        while(j>0):
            j-=1
            ans= min(ans, diff(s, li[j]))
    
    print(ans)

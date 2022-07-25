# https://www.hackerrank.com/challenges/triple-sum/problem?isFullScreen=true

a,b,c= map(int, input().split())

ans= 0
i,k= 0,0
la= map(int, input().split())
lb= map(int, input().split())
lc= map(int, input().split())

la= list(sorted(set(la)))
lb= list(sorted(set(lb)))
lc= list(sorted(set(lc)))

for j in lb:
	while i<a and la[i]<=j:
		i+=1
	while k<c and lc[k]<=j:
		k+=1
	ans+=(i*k)
print(ans)

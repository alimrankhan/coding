#backtracking #permutation
n= 3
visit= [False]*10
ans= []
ans2= [None]*n
def permutation(at, n):
	if at== n:
		print(ans, ans2)
		return
	
	for i in range(0,n):
		if not visit[i]:
			visit[i]= True
			ans.append(i)
			ans2[at] =i
			permutation(at+1, n)
			visit[i]= False
			ans.pop()	#extra for ans	
permutation(0,n)

#backtracking #n_queens problem

col= [False]* 20
diagonal1= [False]*20
diagonal2= [False]*20
ans= []
queens= [None] * 5

def nqueens(at, n):
	if at== n:
		print('\n')
		print(ans, queens)
		return
	
	for i in range(0,n):
		if col[i] or diagonal1[n-at+i-1] or diagonal2[i+at]:
			continue
		col[i]= diagonal1[n+i-at-1]= diagonal2[i+at]= True
		ans.append(i)
		queens[at]= i
		nqueens(at+1, n)
		col[i]= diagonal1[n-at+i-1]= diagonal2[i+at]= False
		ans.pop()
			
			
nqueens(0,3)
print(ans, queens )

#two knights #cses.fi #introductory problem

def comb(n,r):
    ncr= 1
    for i in range(r):
        ncr*= (n-i)/(i+1)
    return int(ncr)
n= int(input())
for i in range(1,n+1):
    print(comb(i*i, 2)- 4*(i-1)*(i-2))
# n,r= map(int, input().split())
# ncr= 1
# for i in range(1, r):
#     ncr*= (n-i)/(i+1)
# print(n,r)
# print(ncr)

#bitmask #bit reprsentation

x= -23
for i in range(7,-1,-1):
    if(x&(1<<i)):
        print(1,end='')
    else:
        print(0,end='')
print()
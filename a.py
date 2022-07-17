# cook your dish here
t= int(input())

while(t>0):
    t-= 1 
    n= int(input())
    s= input()
    ans=0
    for i in range(1,n):
        if s[i]=='0' and s[i-1]=='1':
            ans+=1
    print(ans)
    

# cook your dish here
t= int(input())
while(t>0):
    t-= 1 
    n= int(input())
    li= list(map(int, input().split()))
    if (len(li)) == len(set(li)):
        print('YES')
    else:
        print('NO') 
    

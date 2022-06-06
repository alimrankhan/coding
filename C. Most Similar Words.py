t= int(input())
while t>0:
    t=t-1
    n,m= map(int, input().split())
    su= 0
    se= set()
    for i in range(0,n):
        s= input()
        su= 0
        for i in s:
            su= su+ ord(i)
#ord('a') and chr(97)
        se.add(su)
    print(se)
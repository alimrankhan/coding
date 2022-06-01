t= int(input())
while t>0:
    t=t-1
    n=input()
    sum1,sum2=0,0
    for i in range(0,3):
        sum1= sum1+ int(n[i])
        sum2= sum2+ int(n[5-i])
    if sum1==sum2:
        print("Yes")
    else:
        print("No")
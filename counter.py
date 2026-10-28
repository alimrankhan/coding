print('Write a program to count anything, like Tasbih. It will simply starts with digit= 0 and always increament by 1 everytime after tapping a particular key on keyboard or mouse')

cnt=0
print(0)
while(1):
    
    n= input()
    if n==' ': #modify to buffer the input to count only when space is pressed
        cnt= cnt+1
        print(cnt)

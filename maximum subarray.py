#maximum subarray

li= [-2, 1, -3, 4, -1, 2, 1, -5,44]
def display_subarray(li:list):
    for i in range(0,len(li)):
        for j in range(i,len(li)):
            for k in range(i,j+1):
                print(li[k],end=' ')
            print()
def max_subarray(li:list):
    sum= 0
    max_sum= 0
    for i in range(0,len(li)):
        sum= max(li[i], sum+li[i])
        max_sum= max(sum, max_sum)
    return max_sum
#display_subarray(li)
print(max_subarray(li))

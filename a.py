#codewars #maximum subarray
#max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
arr= [1,-2,3]
ans= 0
best= 0
for i in range(len(arr)):
    best= max(arr[i], best+arr[i])
    ans= max(best, ans)
    print(best,ans)
print(ans)

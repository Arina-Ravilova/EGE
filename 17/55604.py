nums = list(map(int, open('17.txt').readlines()))
min1=10**10
cnt=0
maxSum = 0
for i in range(len(nums)):
    if (abs(nums[i])//10%10)==(abs(nums[i])%10):
        if nums[i]<min1:
            min1=nums[i]

for i in range(len(nums)-1):
    if (((abs(nums[i])%10) == (abs(nums[i+1])//10%10)) or ((abs(nums[i+1])%10) == (abs(nums[i])//10%10))) and ((nums[i]%7==0) != (nums[i+1]%7==0)) and (nums[i]**2+nums[i+1]**2 <= min1**2):
          cnt+=1
          maxSum = max(maxSum, nums[i]**2+nums[i+1]**2)
print(cnt)
print(maxSum)


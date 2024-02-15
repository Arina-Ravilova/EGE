# map(функция, список) - применяет функцию к каждому элементу последовательности
nums = list(map(int, open('48465.txt').readlines()))

min_num = 10001
max_sum = 0
for num in nums:
    if abs(num) % 10 == 6:
        min_num = min(min_num, num)

# Альтернативный вариант
# min_num = min(nums, key=lambda x: x if abs(x) % 10 == 6 else 10000)

'''
a b xor
0 0 0
0 1 1
1 0 1
1 1 0
'''

count = 0
for i in range(len(nums) - 1):
    if (abs(nums[i]) % 10 == 6) != (abs(nums[i + 1]) % 10 == 6) and (nums[i] ** 2 + nums[i + 1] ** 2 < min_num ** 2):
        count += 1
        max_sum = max(max_sum, nums[i] ** 2 + nums[i + 1] ** 2)
print(count, max_sum)


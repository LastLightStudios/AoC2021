with open('input1.txt') as f:
    lines = f.readlines()

nums = [int(line.strip()) for line in lines]

count = 0
prev = -1

# part 1
for num in nums[:-1]:
    if num > prev:
        count += 1
    prev = num

print(count)

#part 2
count = 0
for i in range(3, len(nums)):
    if (sum(nums[i-3:i])) > (sum(nums[i-4:i-1])):
        count += 1

print(count)
nums = []
for i in range(1,10000):
        if i == sum(j for j in range(1,i) if i % j == 0):
                nums.append(i)
print(nums)

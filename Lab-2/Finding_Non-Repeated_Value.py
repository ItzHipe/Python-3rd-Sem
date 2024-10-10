nums = list(map(int, input("Enter the elements of the list: ").split()))

nums.sort()

for x in nums:
    if nums.count(x) == 1:
        print(x)
        break
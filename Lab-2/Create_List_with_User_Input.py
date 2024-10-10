# Method 1

l1 = list(map(int, input("Enter the elements of the list: ").split()))
print(l1)

# Method 2

l2 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    l2.append(int(input("Enter the element: ")))
print(l2)
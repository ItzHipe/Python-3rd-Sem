l1 = list(map(int, input("Enter values seperated by a space ").split(" ")))

for x in range(len(l1)):
    if l1[x+1] != l1[x]+1:
        print("The missing element is: ",l1[x]+1)
# Solution 1

def sort_tuple(tuples):
    n = len(tuples)
    for i in range(n):
        for j in range(0, n-i-1):
            if (tuples[j][1] > tuples[j + 1][1]):
                temp = tuples[j]
                tuples[j] = tuples[j + 1]
                tuples[j + 1] = temp
    return tuples

l1 = [("Jay", 19), ("Adi", 20), ("Aman", 34)]

print(sort_tuple(l1))

# Solution 2

l1.sort(key=lambda x: x[1])
print(l1)
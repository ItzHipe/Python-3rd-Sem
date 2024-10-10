def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def calculate_total_cost(**kwargs):
    total = 0
    for key, value in kwargs.items():
        total += value
    return total

print_details(name="Jay", age=19, occupation="Doctor")
total_cost = calculate_total_cost(kiwi=2.2, pistachio=28, oranges=4.1)
print(f"Total Cost: ${total_cost}")
def splitTheBill(group):
    total_cost = sum(group.values())
    avg_cost = total_cost / len(group)
    result = {name: round(cost - avg_cost, 2) for name, cost in group.items()}
    return result
#Example
group = {“A”: 20, “B”: 15, “C”: 10}
result = spiltTheBill(group)
print(result)

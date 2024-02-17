def splitTheBill(group):
    total_cost = sum(group.values())    #รวมค่าใช้จ่ายทั้งหมด
    avg_cost = total_cost / len(group)    #หาค่าใช้จ่ายเฉลี่ย
    #นำค่าใช้จ่ายของแต่ละคนมาหักกับค่าใช้จ่ายเฉลี่ยแล้วแจกแจงขของแต่ละคนพร้อมแสดงค่าด้วยทศนิยม 2 ตำแหน่ง
    result = {name: round(cost - avg_cost, 2) for name, cost in group.items()}    
    return result
#ตรวจสอบโดยการใส่คำสั่ง 
group = {“A”: 20, “B”: 15, “C”: 10} 
result = spiltTheBill(group)
print(result)

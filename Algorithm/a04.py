def fibonacci(n):
    if n == 0:    #ถ้า F ที่ n =0 จะได้ค่า 0
        return 0
    elif n == 1:   #ถ้า F ที่ n =1 จะได้ค่า 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)   #ถ้า F ที่ n =1 จะได้ค่า 1
n = int(input("Input: "))    #รับค่าเป็นจำนวนเต็ม
if n > 0:    #ถ้าเป็นจำนวนเต็มบวก ให้ใช้ฟังก์ชันคำนวณค่า Fibonacci และแสดงค่า
    output = fibonacci(n)
    print("Output:", output) 
else:    #ถ้าไม่ใช่จำนวนเต็มบวกให้บอกว่าไม่ใช่ แล้วไม่คำนวณ
    print(“Input is not correct number”)


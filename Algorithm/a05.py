def palindrome(text):
    if len(text) <= 1:    #ถ้าความยาวของ text มีแค่ 1 ตัวอักษรหรือไม่มี จะส่งค่า True ออก
        return True
    elif len(text) > 1:    #ถ้าความยาวของ text มีมากกว่า 1 ตัวอักษร จะทำคำสั่งข้างล่างต่อ
#ตรวจสอบตัวอักษรตัวแรกและตัวสุดท้ายว่าตรงกันหรือไม่ ถ้าตรงกันก็ตรวจสอบตัวที่สองและตัวรองสุดท้ายต่อ ทำไปจนจบที่ตัวกลางของ text 
#ระหว่างนี้ถ้าเจอตัวที่ไม่ตรงกันจะส่งค่า False ออก แต่ถ้าตรวจสอบจนครบแล้วจะส่งค่า True ออก
        for i in range(len(text) // 2 + 1):    
            if text[i] != text[-i + 1]
                return False
    return True
#คำสั่งด้านล่างเป็นการทดสอบว่า text ที่ใส่ไปเป็น Palindrome หรือไม่
text = input("Enter text: ")
if palindrome(text):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")


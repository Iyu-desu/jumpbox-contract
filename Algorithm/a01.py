def matching(s, p):
    if s.islower() and (p.islower() or p == ".*" or p[0] == "." or p[1] == "*"):    #ตรวจสอบ input ว่ารับตัวอักษรพิมพ์เล็กเข้ามาหรือไม่แล้วสร้าง array dp ที่มีค่า false ทุกตำแหน่งยกเว้นตำแหน่งที่ row = 0 และ column = 0
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True    
        #ถ้ามีการรับ input ‘*’ เข้ามาที่ตำแหน่งที่ 2 ของ p จะให้ค่าที่ตำแหน่ง row ที่ 0 และ column ที่ 2 = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        #เช็ค input รับเข้ามาว่าที่ตำแหน่งตัวแรกและตัวที่สองของทั้ง input s และ p เหมือนกันหริอไม่ หรือ input p ได้รับมาเป็น “.*”
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 1]) or p[j - 1] == '*')
        print("Output: ", dp[len(s)][len(p)])
    else:
        print("inputs are incorrect")
#ทดสอบฟังก์ชันโดยคำสั่งด้านล่าง
s = str(input("Input: S = ", ))
p = str(input("Input: P = ", ))
matching(s, p)

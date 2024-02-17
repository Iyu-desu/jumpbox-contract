def distribute(total_servers, total_jobs):
    jobs_per_server = total_jobs // total_servers    #หาจำนวน job ที่ต้องใส่ต่อ 1 server
    extra_jobs = total_jobs % total_servers    #หาจำนวน job ที่เกินมาเมื่อแบ่งให้ server ไม่ลงตัว
    actual_jobs_per_server = []    #กำหนด array เปล่า
  
    #ตรวจสอบว่าแต่ละ server จะมี job เท่าไร
    temp = extra_jobs
    for i in range(total_servers):
        if temp > 0:    #ถ้ามี job เกินมาให้แบ่ง Job ที่เกินใส่ไปที่ server ไล่จากตัวแรกสุด
            job_qty = jobs_per_server + 1
            temp -= 1
        else:    #ถ้าไม่มี job เกินมาให่แบ่งลงทุก server เท่าๆกัน
            job_qty = jobs_per_server
        actual_jobs_per_server.append(job_qty)
    print("Actual jobs per server are ", actual_jobs_per_server)

   #กำหนด array เปล่า
    distribution = []

    # เอา job ลง server ตามลำดับ
    step = 0
    for i in range(total_servers):
        server = []
        for j in range(step,(actual_jobs_per_server[i]+step)):
            server.append(j)
        distribution.append(server)
        step += actual_jobs_per_server[i]
    print("Distribution for jobs to each server is ",distribution)

#ทดสอบฟังก์ชันโดยการใส่คำสั่งด้านล่าง
distribute(2,3)
distribute(3,3)     
distribute(4,10)

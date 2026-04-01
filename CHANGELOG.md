# CHANGELOG

 - **วันที่ 1 เมษา 2569:** 
    เพิ่ม Feature contact ในการส่ง payload เของผู็ใช้ที่จะส่งข้อความให้ Dev เข้า google sheet โดยเก็บข้อมูล name , email , message 
    
 - [x] แก้ปัญหา Silence Error ส่ง payload เข้า Google App Script คืนค่า 200 success แต่บันทีกไฟล์ลง google sheet **ล้มเหลว**  
  **(ANS)** **วันที่ 2 เมษา 2569:** ปัญหาเกิดจากใส่ค่า parameter ชื่อไฟล์บน method .GetSheetByName ผิด ทำให้ข้อมูลส่งไปไม่ได้ แล้ว return null กลับมา

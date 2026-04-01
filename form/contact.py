import streamlit as st

import re 
import requests

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzRYkRm00BREE6EelZu9RjlSXYaWWD56H29aq7y0QhOrhOGovJh0F_nSkevXGJGDHXY/exec"


def is_valid_email(email) : #ฟังก์ชันตรวจสอบความถูกต้องของอีเมล
    #basic regex pattern for email validation 
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None #เช็คจุดเริ่มต้นของข้อความ ว่า ตรงตาม pattern ไหม หากไม่จะคืนค่า none  

def contact_form() : #เอาไว้ให้ views/about_me.py เรียกใช้
    with st.form("contact_form") : 
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_buton = st.form_submit_button("Submit")
        
        if submit_buton :
            #st.success("Message sucessfully sent!")
            if not WEBHOOK_URL : #เช็คว่า webhook url มีค่าหรือไม่ หากมีข้อมูล = Ture , ไม่มี = False
                st.error("Email service is not set up. Please try again later.",icon = "😓") #แสดง Error message  
                st.stop()
            
            if not name :
                st.error("please probide your name.",icon = "🧍‍♂️")
                st.stop()            
           
            if not email:
               st.error("Please provide your email address.", icon = "🤸‍♂️")
               st.stop()
            
            if not is_valid_email(email) : # pattern email ถูกต้องไหม
                st.error("Please provide a valid email address.", icon = "📧")
                st.stop()
                
            if not message :
                st.error("Please provide a message" , icon = "💬")
                st.stop()
                
            # Prepare the payload and send it to the specified webhook URL
            data = {"email": email, "name" : name, "message" : message} #สร้าง payload ที่รับค่าเข้ามา
            response = requests.post(WEBHOOK_URL, json=data) #ให้ data ร่างเป็น json แล้วส่งไปที่ WEBHOOK_URL 
            # response รับค่าที่ตอบกลับ ว่า 200 OK  หรือ 404 Not Found
            
            if response.status_code == 200 : #เช็คว่า response status code ส่งกลับมาเป็น 200 OK หรือไม่
                st.success("Your message has been sent successfully! 🎉", icon = "✌") #success message
            else :
                st.error("There was an error sending your message. 😭",icon = "🤬")
import streamlit as st
#st.title("About Me")

from form.contact import contact_form #function จาก form/contact.py 

@st.dialog("Contact Me") #การใาต่างโต้ตอบใช้ Decorator(@) เพื่อสร้าง Dialog เพื่อสร้างหน้าตา (Modal Dialog / Pop-up) ขึ้นมาบนแอป
def show_contact_form() : 
    #st.text_input("First Name") #ถูกคุมให้ขึ้นหน้าต่างโดย Decorator(@st.dialog) ที่สร้างขึ้นมา
    contact_form() #เรียกใช้ function contact_form() ที่สร้างไว้ใน form/contact.py

# --- HERO SETION ---

col1 , col2 = st.columns(2,gap = "small" , vertical_alignment="top")

with col1 :
    st.image("assets/_DSC5154.JPG", width = 300)
with col2 :
    st.title("KaNOM_Pak", anchor=False) # achor = create link to this title
    st.write("Welcome to my portfolio!")
    if st.button("😎 Contact Me") :
        show_contact_form()
        
    
# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications" , anchor = False)
st.write(
    """
    - กินปลาดุกย่าง 20 ตัวใน 10  วินาที
    - กินข้าวเหนียวมะม่วง 10 จานใน 5 วินาที
    - กินส้มตำ 5 จานใน 3 วินาที
    """
)

#--- SKILLS ---
st.write("\n")
st.subheader("Hard Skills" , anchor = False)
st.write(
    """
    - Python
    - Machine Learning
    - Lua
    """
)
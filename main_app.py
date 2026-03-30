import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    page = "views/about_me.py",   #page location
    title = "About Me",          #name navigation menu
    icon = ":material/account_circle:",  #can be emoji can find on google fonts or press key "windows + ." to open emoji menu
    default = True , #set this page as first page when open the app
)

project_1_page = st.Page(
    page = "views/sales_dashboard.py",
    title = "Sales Dashboard",
    icon = ":material/bar_chart:",
)

project_2_page = st.Page(
    page = "views/chatbot.py",
    title = "Chat Bot",
    icon = ":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS} ---
#pg = st.navigation(pages = [about_page, project_1_page, project_2_page]) # แบ่งแต่ละหน้า

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info" : [about_page],
        "Projects" : [project_1_page, project_2_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/_DSC5154.JPG")
st.sidebar.text("KaNOM_Pak")

# --- RUN NAVIGATION ---
pg.run()
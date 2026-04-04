import streamlit as st
import numpy as np
import cv2 as cv
import zipfile
import io

st.set_page_config(
    page_title="Pengolahan Citra Digital",  
    page_icon="logo.webp",
)
st.logo("assets/LOGO_UNESA.png")

def home():
    st.title("👤 Home Page")
    st.write("Selamat datang di dashboard pembelajaran Pengolahan Citra Digital!")
    st.write("Pilih materi yang ingin Anda pelajari dari sidebar.")
    
def Kriptografi():
    st.title("🫸 Kriptografi: Vigenere")
    st.write("Materi tentang Kriptografi dengan metode Vigenere akan ditampilkan di sini.")
    st.write("Anda dapat menambahkan konten pembelajaran, contoh kode, dan penjelasan tentang metode Vigenere.")

courses_page = {
    "👤 Home Page": home,
    "🪄 Kriptografi: Vigenere": Kriptografi,
}

with st.sidebar:
    st.title("🎓 Learning Dashboard")
    st.markdown("""
    <div style="display: grid; grid-template-columns: 60px auto; gap: 5px; margin-bottom: 1rem;">
        <div>Nama</div><div>: <b>Maliq Rafaldo</b></div>
        <div>NIM</div><div>: <b>24051204132</b></div>
        <div>Kelas</div><div>: <b>TI 2024 D</b></div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    selectedCourse = st.selectbox("Pilih Materi", list(courses_page.keys()))
    
courses_page[selectedCourse]()
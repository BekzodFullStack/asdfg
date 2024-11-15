import streamlit as st
import requests

# API kalitni kiriting
API_KEY = "aL6Cpssn5jwMC2UHFlf7yQ==LCM8BPQORDjKhi6G"

# API manzili (bu yerda mos API URLini kiriting)
API_URL = "https://api.example.com/data"  # APIingiz URLini almashtiring

# Streamlit interfeysi
st.title("Streamlit API Ulanish Demo")
st.sidebar.header("So'rov parametrlarini kiriting")

# Foydalanuvchi parametrlarini qabul qilish
param1 = st.sidebar.text_input("Parametr 1", "default1")
param2 = st.sidebar.text_input("Parametr 2", "default2")

if st.sidebar.button("So'rov yuborish"):
    # APIga so'rov yuborish
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"param1": param1, "param2": param2}
    response = requests.get(API_URL, headers=headers, params=params)

    # Javobni ko'rsatish
    if response.status_code == 200:
        data = response.json()
        st.success("Ma'lumot muvaffaqiyatli olindi!")
        st.json(data)  # Ma'lumotlarni ko'rsatish
    else:
        st.error(f"Xato: {response.status_code} - {response.text}")

import streamlit as st
import requests
#uzgarish
# API sozlamalari
API_URL = 'https://api.api-ninjas.com/v1/objectdetection'
API_KEY = 'aL6Cpssn5jwMC2UHFlf7yQ==LCM8BPQORDjKhi6G'

def detect_objects(image_file):
    """Rasmni API orqali aniqlash"""
    files = {'image': image_file}
    headers = {'X-Api-Key': API_KEY}
    response = requests.post(API_URL, files=files, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f"API qaytargan xato: {response.status_code}, {response.text}"}

# Streamlit interfeysi
st.title("Rasmni Aniqlash Ilovasi")
st.write("Yuklangan rasmni API orqali aniqlaydi va natijani JSON formatida qaytaradi.")

# Rasm yuklash uchun komponent
uploaded_file = st.file_uploader("Rasm yuklang (JPEG yoki PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Rasmni ko'rsatish
    st.image(uploaded_file, caption="Yuklangan rasm", use_column_width=True)

    # API orqali aniqlash
    with st.spinner("Rasmni aniqlash jarayoni..."):
        result = detect_objects(uploaded_file)

    # Natijani ko'rsatish
    st.subheader("Aniqlash natijasi:")
    st.json(result)
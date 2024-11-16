import streamlit as st
import requests

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
st.write("Yuklangan rasmni API orqali aniqlaydi va aniqlash ehtimolligini ko'rsatadi.")

# Rasm yuklash uchun komponent
uploaded_file = st.file_uploader("Rasm yuklang (JPEG yoki PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Rasmni ko'rsatish
    st.image(uploaded_file, caption="Yuklangan rasm", use_column_width=True)

    # API orqali aniqlash
    with st.spinner("Rasmni aniqlash jarayoni..."):
        result = detect_objects(uploaded_file)

    # Natijani qayta ishlash va ko'rsatish
    st.subheader("Aniqlash natijasi:")
    if "error" in result:
        st.error(result["error"])
    else:
        if "objects" in result and result["objects"]:
            for obj in result["objects"]:
                object_name = obj.get("label", "Aniqlanmagan obyekt")
                confidence = obj.get("confidence", 0) * 100  # Ehtimollikni foizga o'zgartirish
                st.write(f"**{object_name}**: {confidence:.2f}%")
        else:
            st.write("Hech qanday obyekt aniqlanmadi.")

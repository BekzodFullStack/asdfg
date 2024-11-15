import streamlit as st
import requests
#dfghjkmgfdgh
# API sozlamalari
API_URL = 'https://api.api-ninjas.com/v1/objectdetection'
API_KEY = 'aL6Cpssn5jwMC2UHFlf7yQ==LCM8BPQORDjKhi6G'

def detect_objects(image_file):
    """Rasmni API orqali aniqlash"""
    files = {'image': image_file}
    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.post(API_URL, files=files, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f"API xatosi: {response.status_code}, {response.text}"}
    except Exception as e:
        return {'error': f"APIga ulanishda xato: {str(e)}"}

# Streamlit interfeysi
st.title("Rasmni Aniqlash Ilovasi")
st.write("Yuklangan rasmni API orqali aniqlaydi va aniqlik darajasini foizda ko‘rsatadi.")

# Rasm yuklash uchun komponent
uploaded_file = st.file_uploader("Rasm yuklang (JPEG yoki PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Yuklangan rasmni ko‘rsatish
    st.image(uploaded_file, caption="Yuklangan rasm", use_column_width=True)

    # API orqali aniqlash
    with st.spinner("Rasmni aniqlash jarayoni..."):
        result = detect_objects(uploaded_file)

    # Natijani ko‘rsatish
    st.subheader("Aniqlash natijasi:")
    if 'error' in result:
        st.error(result['error'])
    else:
        # Aniqlangan obyektlar va aniqlik darajasi
        if len(result) == 0:
            st.write("Hech qanday obyekt aniqlanmadi.")
        else:
            for obj in result:
                object_name = obj.get('object', 'Noma’lum obyekt')
                confidence = obj.get('confidence', 0) * 100  # Aniqlik darajasini foizga aylantirish
                st.write(f"Bu {object_name}, aniqlik: {confidence:.2f}%")

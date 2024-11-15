import streamlit as st
import requests
#uzgardi
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

def process_detection_results(results):
    """Natijani qayta ishlash va kerakli matn shaklida qaytarish"""
    objects_detected = []
    for obj in results:
        name = obj.get('object', 'Noma’lum obyekt')
        confidence = obj.get('confidence', 0) * 100  # Foizga o‘tkazish
        if name.lower() == "car":  # Agar mashina bo‘lsa
            objects_detected.append(f"Bu mashina, aniqlik: {confidence:.2f}%")
        else:
            objects_detected.append(f"Bu {name}, aniqlik: {confidence:.2f}%")
    return objects_detected

# Streamlit interfeysi
st.title("Rasmni Aniqlash Ilovasi")
st.write("Yuklangan rasmni API orqali aniqlaydi va natijani foiz aniqlik bilan ko'rsatadi.")

# Rasm yuklash uchun komponent
uploaded_file = st.file_uploader("Rasm yuklang (JPEG yoki PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Rasmni ko'rsatish
    st.image(uploaded_file, caption="Yuklangan rasm", use_column_width=True)

    # API orqali aniqlash
    with st.spinner("Rasmni aniqlash jarayoni..."):
        result = detect_objects(uploaded_file)

    # Natijani qayta ishlash
    if 'error' in result:
        st.error(result['error'])
    else:
        processed_results = process_detection_results(result)
        st.subheader("Aniqlash natijasi:")
        for obj_text in processed_results:
            st.write(obj_text)

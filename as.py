import streamlit as st
import requests

# API sozlamalari
API_URL = 'https://api.api-ninjas.com/v1/facedetect'
API_KEY = 'aL6Cpssn5jwMC2UHFlf7yQ==LCM8BPQORDjKhi6G'  # O'zingizning API kalitingizni bu yerga kiriting

# Streamlit interfeysi
st.title("Yuzni aniqlash dasturi")
st.write("Quyidagi oynaga suratni yuklang va aniqlangan yuzlar haqida ma'lumot oling.")

# Foydalanuvchidan rasm yuklash
uploaded_file = st.file_uploader("Rasm yuklang", type=["jpeg", "jpg", "png"])

if uploaded_file is not None:
    # API orqali rasmni yuborish
    files = {'image': uploaded_file}
    headers = {'X-Api-Key': API_KEY}

    with st.spinner("Yuzni aniqlash amalga oshirilmoqda..."):
        response = requests.post(API_URL, files=files, headers=headers)

    # Natijalarni qayta ishlash
    if response.status_code == 200:
        data = response.json()
        st.success("Yuzni aniqlash muvaffaqiyatli bajarildi!")
        st.write(f"Rasmdagi yuzlar soni: {len(data['faces'])}")
        st.json(data)
    else:
        st.error(f"API xatosi: {response.status_code}")
        st.write(response.text)















# import streamlit as st
# import requests
# #uzgarishlar
# # API sozlamalari
# API_URL = 'https://api.api-ninjas.com/v1/objectdetection'
# API_KEY = 'aL6Cpssn5jwMC2UHFlf7yQ==LCM8BPQORDjKhi6G'

# def detect_objects(image_file):
#     """Rasmni API orqali aniqlash"""
#     files = {'image': image_file}
#     headers = {'X-Api-Key': API_KEY}
#     response = requests.post(API_URL, files=files, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {'error': f"API qaytargan xato: {response.status_code}, {response.text}"}

# st.title("Rasmni Aniqlash")
# st.write("Yuklangan rasmni API orqali aniqlaydi va natijani JSON formatida qaytaradi.")

# # Rasm yuklash uchun komponent
# uploaded_file = st.file_uploader("Rasm yuklang (JPEG yoki PNG)", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Rasmni ko'rsatish
#     st.image(uploaded_file, caption="Yuklangan rasm", use_column_width=True)

#     # API orqali aniqlash
#     with st.spinner("Rasmni aniqlash jarayoni..."):
#         result = detect_objects(uploaded_file)

#     # Natijani ko'rsatish
#     st.subheader("Aniqlash natijasi:")
#     st.json(result)
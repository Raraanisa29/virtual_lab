
import streamlit as st

st.set_page_config(page_title="Kalkulator Suhu Ajaib 🧙‍♂️", page_icon="🌈")

# Tampilan header
st.markdown(
    """
    <div style='text-align: center; color: #FF69B4;'>
        <h1 style='font-family:Comic Sans MS;'>🌈 Kalkulator Suhu Ajaib 🔥❄️</h1>
        <h3>Masukkan salah satu suhu, dan yang lainnya akan otomatis dikonversi!</h3>
    </div>
    """, unsafe_allow_html=True
)

# Input suhu
col1, col2, col3 = st.columns(3)

with col1:
    celsius = st.number_input("🌡️ Celcius (°C)", key="celsius", format="%.2f", step=0.1)

with col2:
    fahrenheit = st.number_input("🔥 Fahrenheit (°F)", key="fahrenheit", format="%.2f", step=0.1)

with col3:
    kelvin = st.number_input("❄️ Kelvin (K)", key="kelvin", format="%.2f", step=0.1)

# Deteksi input yang aktif dan konversi otomatis
input_option = st.radio("Pilih suhu yang kamu masukkan:", ["Celcius", "Fahrenheit", "Kelvin"])

if input_option == "Celcius":
    f = celsius * 9 / 5 + 32
    k = celsius + 273.15
    st.success(f"🔥 Fahrenheit = {f:.2f} °F")
    st.success(f"❄️ Kelvin = {k:.2f} K")
elif input_option == "Fahrenheit":
    c = (fahrenheit - 32) * 5 / 9
    k = c + 273.15
    st.success(f"🌡️ Celcius = {c:.2f} °C")
    st.success(f"❄️ Kelvin = {k:.2f} K")
elif input_option == "Kelvin":
    c = kelvin - 273.15
    f = c * 9 / 5 + 32
    st.success(f"🌡️ Celcius = {c:.2f} °C")
    st.success(f"🔥 Fahrenheit = {f:.2f} °F")

# Footer
st.markdown(
    """
    <hr>
    <div style='text-align: center; font-family:Comic Sans MS; color: gray;'>
        Dibuat oleh Kakak Python 🐍 untuk anak-anak cerdas 🌟
    </div>
    """, unsafe_allow_html=True
)

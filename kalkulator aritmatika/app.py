import streamlit as st

st.set_page_config(page_title="Kalkulator Aritmatika", page_icon="🧮", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Kalkulator Barisan Aritmatika</h1>", unsafe_allow_html=True)

with st.form("aritmatika_form"):
    a = st.number_input("Suku pertama (a)", value=1.0)
    d = st.number_input("Beda (d)", value=1.0)
    n = st.number_input("Jumlah suku (n)", min_value=1, value=5)

    submitted = st.form_submit_button("Hitung")

if submitted:
    suku_ke_n = a + (n - 1) * d
    jumlah_n_suku = (n / 2) * (2 * a + (n - 1) * d)

    st.success(f"Suku ke-{int(n)}: {suku_ke_n}")
    st.info(f"Jumlah {int(n)} suku pertama: {jumlah_n_suku}")

    st.line_chart([a + i * d for i in range(int(n))])

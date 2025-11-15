import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Verificación de Identidad – Tulkit Pay", layout="centered")

st.title("Verificación de Identidad – Tulkit Pay")
st.write("Completa estos pasos para verificar tu identidad en menos de 2 minutos.")


# ---------------- PASO 1: DNI ----------------
st.header("1️⃣ Ingresa tu DNI")

dni = st.text_input("Número de DNI", max_chars=8)

dni_ok = False
if dni:
    if dni.isdigit() and len(dni) == 8:
        st.success("DNI válido ✔️")
        dni_ok = True
    else:
        st.error("El DNI debe tener 8 dígitos.")


# ---------------- PASO 2: SELFIE ----------------
st.header("2️⃣ Tómate una selfie para prueba de vida")

selfie = st.camera_input("Tómate una foto")

selfie_ok = False
if selfie is not None:
    st.success("Selfie capturada correctamente ✔️")
    selfie_ok = True


# ---------------- PASO 3: VERIFICACIÓN ----------------
st.header("3️⃣ Confirmar Verificación")

if st.button("Verificar identidad"):
    if not dni_ok:
        st.error("❌ Falta un DNI válido.")
    elif not selfie_ok:
        st.error("❌ Falta tomar la selfie.")
    else:
        with st.spinner("Verificando identidad, por favor espera..."):
            time.sleep(2.5)

        st.success("🎉 ¡Tu identidad ha sido verificada exitosamente!")
        st.balloons()

        st.info("""
Tu verificación ha sido completada.  
Ya puedes usar **Tulkit Pay** y acceder a todas sus funciones.
""")


st.write("---")
st.caption("Prototipo funcional – KYC básico en Streamlit.")

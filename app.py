import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Verificación – Tulkit Pay", layout="wide")

st.title("Verificación de Identidad – Tulkit Pay")
st.write("Completa estos pasos para verificar tu identidad en menos de 2 minutos.")
st.write("---")

# COLUMNAS: IZQUIERDA (VERIFICACIÓN) / DERECHA (APP EN SEGUNDO PLANO)
col_verif, col_preview = st.columns([1.2, 0.8])

# ---------------------- COLUMNA IZQUIERDA ----------------------
with col_verif:

    st.header("1️⃣ Ingresa tu DNI")
    dni = st.text_input("Número de DNI", max_chars=8)

    dni_ok = False
    if dni:
        if dni.isdigit() and len(dni) == 8:
            st.success("DNI válido ✔️")
            dni_ok = True
        else:
            st.error("El DNI debe tener 8 dígitos.")

    st.header("2️⃣ Tómate una selfie para prueba de vida")
    selfie = st.camera_input("Tómate una foto")

    selfie_ok = False
    if selfie is not None:
        st.success("Selfie capturada correctamente ✔️")
        selfie_ok = True

    st.header("3️⃣ Confirmar Verificación")

    if st.button("Verificar identidad"):
        if not dni_ok:
            st.error("❌ Falta un DNI válido.")
        elif not selfie_ok:
            st.error("❌ Falta tomar la selfie.")
        else:
            with st.spinner("Verificando identidad… Esto tomará unos segundos."):
                time.sleep(3)

            st.success("🎉 ¡Tu identidad ha sido verificada exitosamente!")
            st.balloons()

            st.info("""
Tu verificación ha sido completada.  
Ahora puedes usar **Tulkit Pay** sin restricciones.
""")


# ---------------------- COLUMNA DERECHA (APP EN SEGUNDO PLANO) ----------------------
with col_preview:

    st.header("👀 Vista previa de la app")
    st.write("Puedes explorar mientras verificamos tu identidad:")

    st.subheader("💳 Tu futura tarjeta Tulkit Pay")
    st.image("card.png", caption="Tarjeta (puedes reemplazar esta imagen)", use_container_width=True)

    st.subheader("🔄 Opciones de Recarga")
    st.write("""
    - Recarga bancaria  
    - Cripto a tarjeta  
    - Transferencias instantáneas  
    """)

    st.subheader("🎁 Beneficios y Cashback")
    st.write("""
    - Cashback del 2% en compras  
    - Bonos por recargas  
    - Recompensas semanales  
    """)

    st.subheader("📱 Vista general de la app")
    st.image("app_preview.png", caption="Pantalla previa (reemplazar)", use_container_width=True)

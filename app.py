import streamlit as st
import time

st.set_page_config(page_title="Verificación – Tulkit Pay", layout="wide")

st.title("Verificación de Identidad – Tulkit Pay")
st.write("Completa estos pasos para verificar tu identidad en menos de 2 minutos.")
st.write("---")

# ---------------- COLUMNAS ----------------
col_verif, col_preview = st.columns([1.25, 1])

# --------------------- COLUMNA IZQUIERDA (VERIFICACIÓN) ---------------------
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

    st.header("2️⃣ Tómate una selfie")
    selfie = st.camera_input("Captura tu selfie para la prueba de vida")

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
            with st.spinner("Verificando identidad…"):
                time.sleep(2.5)

            st.success("🎉 ¡Tu identidad ha sido verificada exitosamente!")
            st.balloons()

            st.info("""
Tu verificación ha sido completada.  
Ahora puedes usar **Tulkit Pay** sin restricciones.
""")

# --------------------- COLUMNA DERECHA (PREVIEW APPSIMULADA) ---------------------
with col_preview:

    st.header("👀 Vista previa de la app (modo lectura)")
    st.write("Puedes explorar mientras verificamos tu identidad.")

    # Tarjeta simulada
    st.subheader("💳 Tu tarjeta Tulkit Pay")
    st.markdown("""
    <div style='padding:20px; border-radius:15px; background:#4f46e5; color:white; box-shadow:0 0 10px rgba(0,0,0,0.2);'>
        <h3 style='margin:0;'>TULKIT PAY</h3>
        <p>**** 9832</p>
        <p>Juan Pérez</p>
        <p style='font-size:12px;'>Válida hasta 12/29</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Opciones de recarga
    st.subheader("🔄 Opciones de Recarga")
    st.markdown("""
    <div style='padding:15px; border-radius:10px; background:#f3f4f6;'>
        • Recarga bancaria<br>
        • Cripto a tarjeta<br>
        • Transferencias instantáneas
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Beneficios
    st.subheader("🎁 Beneficios y Cashback")
    st.markdown("""
    <div style='padding:15px; border-radius:10px; background:#f3f4f6;'>
        • Cashback del 2% en compras<br>
        • Bonos por recargas<br>
        • Promociones semanales<br>
        • Misiones y recompensas
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Vista previa de la app simulada
    st.subheader("📱 Pantalla principal (Simulada)")
    st.markdown("""
    <div style='padding:20px; border-radius:15px; background:#e5e7eb; box-shadow:0 0 10px rgba(0,0,0,0.15);'>
        <strong>Saldo:</strong> S/ 0.00<br><br>
        Menú rápido:<br>
        - Enviar dinero<br>
        - Recargar<br>
        - Historial<br>
        - Configuración<br><br>
        (Simulación visual)
    </div>
    """, unsafe_allow_html=True)

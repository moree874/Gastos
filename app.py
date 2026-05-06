import streamlit as st
import pandas as pd

st.title("💸 Control de Gastos")

if "gastos" not in st.session_state:
    st.session_state.gastos = []

st.subheader("➕ Añadir gasto")

monto = st.number_input("Monto", min_value=0.0)
categoria = st.text_input("Categoría")

if st.button("Guardar"):
    st.session_state.gastos.append({
        "monto": monto,
        "categoria": categoria
    })
    st.success("Gasto guardado")

if st.session_state.gastos:
    df = pd.DataFrame(st.session_state.gastos)

    st.subheader("📋 Lista de gastos")
    st.dataframe(df)

    st.subheader("💰 Total")
    st.write(df["monto"].sum())

import streamlit as st

st.title("Mi segunda app con Streamlit")
st.header("Hola mundo")
st.write("Este es mi primr Streamlit")
st.write("Hola mund")

fig = px.bar(x=["A", "B", "C"], y=[1, 2, 3])
st.plotly_chart(fig)
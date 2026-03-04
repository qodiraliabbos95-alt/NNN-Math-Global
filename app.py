import streamlit as st
from main import mega_math_engine

st.set_page_config(page_title="MEGA MATH AI")

st.title("🧮 MEGA MATH AI")
st.write("Sun'iy intellekt matematik yechuvchi")

command = st.text_input("Masalani kiriting:")

if st.button("Yechish"):
    if command:
        result = mega_math_engine(command)

        st.write("### Natija:")

        if isinstance(result, list):
            for step in result:
                st.write(step)
        else:
            st.write(result)
    else:
        st.warning("Masala kiriting!")

st.write("Misol: solve 2*x+5=15")

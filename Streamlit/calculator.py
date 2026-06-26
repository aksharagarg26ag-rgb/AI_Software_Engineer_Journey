import streamlit as st
st.title("Calculator")

# a = st.number_input("Number A")
# b = st.number_input("Number B")
#or
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("A")

with col2:
    b = st.number_input("B")

operation = st.selectbox("Choose Operation ", ["Add", "Sub", "Mul", "Div"])

if st.button("Add"):
    st.write(a+b)
    st.success("Addition done!")

if st.button("Subtract"):
    st.write(a-b)

if st.button("Multiply"):
    st.write(a*b)

if st.button("Divide"):
    if b==0:
        st.error("Cannot divide ")
    else:
        st.write(a/b)
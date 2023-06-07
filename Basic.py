import streamlit as st

st.title("Hello Streamlit")

st.header("This is a header")

st.subheader("This is a subheader")

st.text("Hellow Welcome to Streamlit!")

st.success("Success")

st.info("Information")

st.warning("Warning")

st.error("Error")

exp= ZeroDivisionError("Trying to divide by zero")
st.exception(exp)

st.write("Text with write") 
#write function enables us to display code in coding format which is not possible using st.text("")

st.write(range(10))
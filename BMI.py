import streamlit as st
st.title('Welcome to BMI Calculator')

weight=st.number_input("Enter your weight (in kgs)")
height=st.number_input("Enter your height (in cms)")
try:
    bmi = weight / ((height/100)**2)
except:
    st.text("Enter some value of height")

if(st.button('Calculate BMI')):
    st.text("Your BMI Index is {}.".format(bmi))

    if(bmi<16):
        st.error("You are Extremely Underweight")
    elif(bmi>=16 and bmi<18.5):
        st.warning("You are Underweight")
    elif(bmi>=18.5 and bmi<25):
        st.success("Healthy")
    elif(bmi>=25 and bmi<30):
        st.warning("You are Overweight")
    elif(bmi>=30):
        st.error("You are Extremely Overweight")
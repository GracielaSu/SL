import streamlit as st

elective =st.selectbox("Elective:", 
                   ["Music","Computer","Business","English","Religion"])

st.write("Your elective subject is:",elective)

hobbies = st.selectbox("Hobbies: ",
                       ["Swimming","Painting","Sightseeing","Gaming","Singing"])

st.write("You selected ",len(hobbies),"hobbies")

if (st.button("Click me.. Click me")):
    st.text("Hello!Welcome to Streamlit")

name = st.text_input("Enter Your name", "Type Here ...")

if(st.button("Submit")):
    result=name.title()
    st.write("Hello",result)

level=st.slider("Select the level",1,10)

st.text("Selected: {}".format(level))


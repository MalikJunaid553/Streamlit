import streamlit as st

st.title("Malik Chatbot")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")

st.divider()

st.subheader("Welcome user!!")

st.text("Enter your query here.")
st.write("Write with text, numbers, dicts, dataframes and more")
st.divider()


#form
st.text_input("Name:", placeholder="Enter Your Name")
st.text_input("Email:", placeholder="Enter Your Email")
st.text_area("Message:", placeholder="Enter Your Message")
st.number_input("Age:", placeholder="Enter Your Age")
st.selectbox("Country:", ["Pakistan", "India" , "England"])
st.multiselect("Hobbies:" , ["Reading" , "Writing", "Swimming"] )
st.button("Submit")


# Percentage Calculator
obt_marks=st.number_input("Obtained Marks" , min_value=0, value=0, placeholder="Enter Obtained Marks here")
total_marks=st.number_input("Total Marks" , min_value=0, value=0, placeholder="Enter Obtained Marks here")
if st.button("Calculate Percentage"):
    percentage=(obt_marks/total_marks)*100
    st.write(f"You percentage is {percentage:.2f}%")
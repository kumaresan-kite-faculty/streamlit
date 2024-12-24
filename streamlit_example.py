import streamlit as st
st.write("Hello World")
st.title("KGiSL Institute of Technology")
def add():
    num1=st.number_input("enter number 1")
    num2=st.number_input("enternumber 2")
    if st.button("ADD"):
        num3=num1+num2
        st.success(f"The addition of {num1} and {num2} is {num3}")
        st.html(
            "<marquee>This is my new code slider</marquee>"
        )
if __name__=="__main__":
    add()
import streamlit as st
st.title("Find Factorial Values")
st.title("Kumaresan First Deployment Program")
def fact(n):
        if n==0 or n==1:
            return 1
        else:
            return n*fact(n-1)
if __name__=="__main__":
    x=st.number_input("Enter Number")
    if st.button("Factorial1 Value"):
        st.success(f"{fact(x)}")
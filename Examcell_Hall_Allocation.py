import streamlit as st 
import random
from PIL import Image
image = Image.open('Header.JPG')
st.image(image, caption='KGiSL EDU')
st.subheader("EMS - FACULTY HALL ALLOCATION SYSTEM")
def generate_random_number_without_repetition(number_list):

    if not number_list:
        return None

    random_index = random.randint(0, len(number_list) - 1)
    random_number = number_list.pop(random_index)
    return random_number
if __name__=="__main__":
    my_numbers = [214,301,302,303,311,312,202,203,211,212,401,402,403,412,414,415,416,501,502,504,511,103,106,114,201,313,315,316,603,604,613,516,601,513,514,515,618,'KGX HALL 1B 2', 'KGX HALL 1B 3', 'KGX HALL 2A 1']
    st.text("\n")
    if st.button("Generate Hall Number"):
        st.success(f"EXAM EXAM HALL NO. {generate_random_number_without_repetition(my_numbers)}")

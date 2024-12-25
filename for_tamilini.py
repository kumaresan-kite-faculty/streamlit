import streamlit as st
import time
from PIL import Image,ImageOps
st.title("Hello K.Tamilini")
st.html("<h1>Find the differences between YOU and THANVI </h1>")
st.markdown("""
<style>
.stApp {
    background-color: yellow;
}
</style>
""", unsafe_allow_html=True)
def countdown(duration):
        with st.empty():
                while duration >= 0:
                        st.html(f"<center><font size=50 color=red><b>{duration}</b></font></center>")
                        time.sleep(1)
                        duration -= 1
                        st.text("\n\n")
                        st.html("<font size=20>OK. Let's Go...</font>")
                image1=Image.open("Tamilini.jpg")
                image2=Image.open("Thanvi.JPG")
                image1 = ImageOps.exif_transpose(image1)
                image2 = ImageOps.exif_transpose(image2)
                st.image([image1,image2],caption=['Tamilini','Thanvi'],width=350)
        st.audio("Thanvi_voice.mp4",autoplay=True,start_time=9)
        x=st.radio("Who gives voice for this Audio",["K.Tamilini","K.Thanvi"])
        if x=="K.Tamilini":
                st.write("Sorry, You are wrong")
        else:
                st.write("Yes. You are correct")
if __name__=="__main__":
        if st.button("Touch Me"):
                countdown(5)
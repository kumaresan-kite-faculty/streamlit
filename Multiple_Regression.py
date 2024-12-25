import streamlit as st
import pandas as pd
st.title("Multiple Linear Regression")
df=pd.read_excel('Multipe Linear Regresion.xlsx')
def read_data_set():
    with st.empty():
        st.dataframe(df)
def view_title():
    with st.empty():
        st.dataframe(df.head(3))
def EDA():
    st.header("Data Overview")
    st.write(df.head())
    st.write(f"Shape: {df.shape}")
    st.write(df.info())
    st.write(df.describe())
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['School Studied encode']=le.fit_transform((df['School Studied']))
print(df['School Studied encode'],df['School Studied'])
X=df[['Study Time','Travel Time','School Studied encode']]
y=df[['Mark']]
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)
def predict_mark():
    st.text("Predict Mark")
    st.text("\n\n")
    st.text("Enter Your Input's")
    x=st.number_input("Study Time")
    y=st.number_input("Enter Travel Time")
    z=st.number_input("School Type")
    if st.button("Predict Mark"):
        st.success(f"Predicted mark is {model.predict([[x,y,z]])}")
if __name__=="__main__":
    if st.button("View Full Data Set"):
        read_data_set()
    if st.button("View First 3 Data's"):
        view_title()
    if st.button("Perform EDA"):
        EDA()
    predict_mark()
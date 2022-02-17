#in gcc
# cd C:\Users\cosn\OneDrive\Python\aktuelle_Arbeit\Streamlit\mytest
# Streamlit run Testapp.py
#Buch Beispiele https://machine-learning.tokyo/ https://github.com/caron14/streamlit_LinearRegression
#https://share.streamlit.io/cotrader/mytest/Testapp.py


import streamlit as st
import streamlit.components.v1 as stc 
from datetime import date
import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go
import pandas as pd
from PIL import Image
import cufflinks as cf
username = 'cotrader'
token = '48cb91a0c4a78777dcb09be71e7c92d0ddabbec6'
api_token = '48cb91a0c4a78777dcb09be71e7c92d0ddabbec6'
mykey='Test'
st.write(mykey)

#st.image("https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg",
#width=800) # Manually Adjust the width of the image as per requirement)
st.image("https://www.pythonanywhere.com/user/cotrader/files/home/cotrader/mysite1/static/3463.T.png",width=800) 
# Manually Adjust the width of the image as per requirement)

#Laden einer CSV Datei
name='http://cotrader.pythonanywhere.com/static/rand.csv'
df=pd.read_csv(name,delimiter=';')


st.dataframe(df)

st.write('Das ist mein Uploadversuch')
user_input = st.text_input("eigener Wert", 'GOOG')
stocks = (user_input, '^GDAXI', 'MSFT', 'GME')
stockname= st.selectbox('Select', stocks)
st.write(stockname)
st.write(mykey)
#Download File Files aus Python Anywhere in CSV
import requests
from urllib.parse import urljoin
import pandas as pd

#def Daten_laden(pfad_)
pythonanywhere_host = "www.pythonanywhere.com"

api_base = "https://{pythonanywhere_host}/api/v0/user/{username}/".format(
    pythonanywhere_host=pythonanywhere_host,
    username=username,
)

resp1 = requests.get(
    urljoin(api_base, "files/path/home/{username}/Testweb/Liste_csv.csv".format(username=username)),
    headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
)
#print(resp1.content)
from io import StringIO
text=StringIO(resp1.content.decode('utf-8'))
#df=pd.read_csv(text)
#st.dataframe(df)

#st.image("https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg",
#width=400, # Manually Adjust the width of the image as per requirement)
user_input = st.text_input("Passwort eingeben",type='password')
if user_input==mykey:
    st.write('Korrektes Passwort')
else:
    st.write('Falsches Passwort')

#Funktion für Download
path_any='/Testweb/Liste_csv.csv'
def Daten_laden(username,api_token,path_any):
    pythonanywhere_host = "www.pythonanywhere.com"
    path_any='files/path/home/'+username+path_any
    api_base = "https://{pythonanywhere_host}/api/v0/user/{username}/".format(
        pythonanywhere_host=pythonanywhere_host,
        username=username,
    )

    resp1 = requests.get(
        urljoin(api_base,path_any ),
        headers={"Authorization": "Token {api_token}".format(api_token=api_token)}
    )
    #print(resp1.content)
    from io import StringIO
    text=StringIO(resp1.content.decode('utf-8'))
    df=pd.read_csv(text)
    return df
df=Daten_laden(username,api_token,path_any)
st.dataframe(df)
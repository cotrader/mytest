# cd C:\Users\cosn\OneDrive\Python\aktuelle_Arbeit\Streamlit
# Streamlit run Testapp.py
#Buch Beispiele https://machine-learning.tokyo/ https://github.com/caron14/streamlit_LinearRegression

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
import datetime

st.write('Das ist mein Uploadversuch')
user_input = st.text_input("eigener Wert", 'GOOG')
stocks = (user_input, '^GDAXI', 'MSFT', 'GME')
stockname= st.selectbox('Select', stocks)
st.write(stockname)
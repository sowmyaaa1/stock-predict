import streamlit as st, pandas as pd , numpy as np
import plotly.express as px
from jugaad_data.nse import stock_df
from datetime import date



st.title("App for Stock Data")
ticker = st.sidebar.text_input("Stock Name")
start_date = st.sidebar.date_input("Start Date ")
end_date = st.sidebar.date_input("End Date ")

data = stock_df(symbol=ticker, from_date=start_date,
            to_date=end_date, series="EQ")
fig = px.line(data, x=data['DATE'], y=data['PREV. CLOSE'], title = ticker)
st.plotly_chart(fig)
st.header("Pricing Movements")
data2 = data
data2['% Change']=data['PREV. CLOSE'] / data['PREV. CLOSE'].shift(1) - 1
st.write(data2)
annual_return = data2['% Change'].mean()*252*100
st.write('Annual Return is ', annual_return,'%')
stdev = np.std(data2['% Change'])*np.sqrt(252)
st.write('Standard Deviation is ', stdev*100, "%")
st.write('Risk Adj. Return is ', annual_return/(stdev*100))


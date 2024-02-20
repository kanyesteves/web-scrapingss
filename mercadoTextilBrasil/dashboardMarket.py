import streamlit as st
import pandas as pd
from web_scraping_mercado_textil import TextilMarket


textilMarket = TextilMarket()

st.sidebar.header("Mercado textil no Brasil")


df = textilMarket.loadMarket()

for address in list(df["Endereço"]):
    if 'Jaragua do Sul' in address:
        df_filtered = df[df["Endereço"] == address]
        df_filtered
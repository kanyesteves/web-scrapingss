import streamlit as st
import pandas as pd
import re
from web_scraping_mercado_textil import TextilMarket


textilMarket = TextilMarket()
df = textilMarket.loadMarket()

def converter_string_para_float(valor_string):
    numeros = float(''.join(value for value in valor_string if value.isdigit()))
    if 'milhões' in valor_string:
        numeros *= 100_000
    
    return numeros


df_filtrado = df[df['Endereço'].str.contains('Jaragua do sul', case=False)]

regex_nome = re.compile(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}(.+)$')


df_filtrado["Empresa"] = df_filtrado['Empresa'].apply(lambda x: regex_nome.search(x).group(1) if regex_nome.search(x) else None)
df_filtrado["Receita"] = df_filtrado['Receita'].apply(converter_string_para_float)
receita_total = df_filtrado["Receita"].sum()
df_filtrado

st.metric("Receita Total", receita_total)
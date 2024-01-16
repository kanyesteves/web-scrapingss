import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import streamlit as st


def remove_html(html):
    pattern = re.compile('<.*?>')
    cleantext = re.sub(pattern, '', html)
    return cleantext.replace('*', '').strip()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.econodata.com.br/maiores-empresas/todo-brasil/textil'
}

url = "https://www.econodata.com.br/maiores-empresas/todo-brasil/textil"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    cnpjs      = []
    empresas   = []
    enderecos  = []
    atividades = []
    receitas   = []

    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr', {'class': 'w-fit'})

    for row in rows:
        cnpj = remove_html(str(row.select_one('td:nth-child(1)')))
        empresa = remove_html(str(row.select_one('td:nth-child(2)')))
        endereco = remove_html(str(row.select_one('td:nth-child(3)')))
        atividade = remove_html(str(row.select_one('td:nth-child(4)')))
        receita = remove_html(str(row.select_one('td:nth-child(5)')))

        cnpjs.append(cnpj)
        empresas.append(empresa)
        enderecos.append(endereco)
        atividades.append(atividade)
        receitas.append(receita)

    df = pd.DataFrame({
        'CNPJ':     (cnpjs),
        'Empresa':  (empresas),
        'Endereço': (enderecos),
        'Atividade':(atividades),
        'Receita':  (receitas)
    })
    df

else:
    print("Erro ao acessar a página:", response.status_code)
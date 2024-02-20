import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


class TextilMarket:

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Referer': 'https://www.econodata.com.br/maiores-empresas/todo-brasil/textil'
        }
        self.url = "https://www.econodata.com.br/maiores-empresas/todo-brasil/textil"

        self.response = requests.get(self.url, headers=self.headers)


    def remove_html(self, html):
        pattern = re.compile('<.*?>')
        cleantext = re.sub(pattern, '', html)
        return cleantext.replace('*', '').strip()

    def loadMarket(self):
        try: 
            if self.response.status_code == 200:
                cnpjs      = []
                empresas   = []
                enderecos  = []
                atividades = []
                receitas   = []

                soup = BeautifulSoup(self.response.text, 'html.parser')
                rows = soup.find_all('tr', {'class': 'w-fit'})

                for row in rows:
                    cnpj      = self.remove_html(str(row.select_one('td:nth-child(1)')))
                    empresa   = self.remove_html(str(row.select_one('td:nth-child(2)')))
                    endereco  = self.remove_html(str(row.select_one('td:nth-child(3)')))
                    atividade = self.remove_html(str(row.select_one('td:nth-child(4)')))
                    receita   = self.remove_html(str(row.select_one('td:nth-child(5)')))

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
            return df
        except requests.HTTPError as er:
            print("Erro ao acessar a página:", er)
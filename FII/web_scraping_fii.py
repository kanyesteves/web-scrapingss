import requests
from bs4 import BeautifulSoup
import re


def remove_html(html):
    pattern = re.compile('<.*?>')
    cleantext = re.sub(pattern, '', html)
    return cleantext.replace('*', '').strip()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.fundamentus.com.br/ultimos-resultados.php'
}

url = "https://www.fundamentus.com.br/ultimos-resultados.php"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    tbody = soup.find_all('tbody')
    # print(soup)

    for element in tbody:
        print(remove_html(element.text))
else:
    print("Erro ao acessar a página:", response.status_code)
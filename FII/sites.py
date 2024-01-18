import requests
from bs4 import BeautifulSoup

class Site: 
    def __init__(self, site):
        self.site = site
        self.news = []

    def update_news(self):
        if self.site.lower() == "fii":
            new_dict_fii = {}
            browsers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            url = "https://fiis.com.br/noticias/"
            page = requests.get(url, headers=browsers)
            html = page.text
            soup = BeautifulSoup(html, 'html.parser')

            tg_class1 = 'link-noticia-highlith'
            tg_class2 = 'link-noticia-mais-lidas'
            tg_class3 = 'loopNoticias__content__title'
            noticias = soup.find_all('a')

            for noticia in noticias:
                if (noticia.get('class') != None) and (tg_class1 in noticia.get('class')):
                    new_dict_fii[noticia.h3.text] = noticia.get('href')
                if (noticia.get('class') != None) and (tg_class2 in noticia.get('class')):
                    new_dict_fii[noticia.h3.text] = noticia.get('href')
                if (noticia.get('class') != None) and (tg_class3 in noticia.get('class')):
                    new_dict_fii[noticia.h3.text] = noticia.get('href')
                    
            self.news = new_dict_fii
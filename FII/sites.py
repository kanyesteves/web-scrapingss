import requests
from bs4 import BeautifulSoup

class Site: 
    def __init__(self, site):
        self.site = site
        self.news = []

    def update_news(self):
        if self.site.lower() == "fii":
            browsers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            url = "https://fiis.com.br/artigos/"
            page = requests.get(url, headers=browsers)
            html = page.text
            soup = BeautifulSoup(html, 'html.parser')

            tg_class1 = 'higlithArticle__grid__box__title'
            tg_class2 = 'loopNoticias__content__title'

            new_dict_fii = {}
            noticias = soup.find_all('a')

            for noticia in noticias:
                if (noticia.h3 != None) and (tg_class1 in noticia.h3.get('class')):
                    new_dict_fii[noticia.h3.text] = noticia.get('href')
                if (noticia.get('class') != None) and (tg_class2 in noticia.get('class')):
                    new_dict_fii[noticia.h2.text] = noticia.get('href')
                    
            self.news = new_dict_fii

            

self = Site('Fii')
self.update_news()
print(self.news)
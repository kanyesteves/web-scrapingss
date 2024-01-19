# Web Scraping de FIIs utilizando Threads

Neste repositório vamos buscar as notícias do site [FIIs](https://www.fiis.com.br/) em tempo real.


## Classes

- **fii_news:** Classe responsável para controlar as execuções das Threads. 
- **sites:** Classe responsável por fazer o web-scraping do site.

## Objetivo
Tem como objetivo praticar e estudar os conceitos de Threads e web-scrapings.

## O que é uma Thread?

Uma thread é uma unidade de execução dentro de um processo. Um processo pode ter múltiplas threads que compartilham o mesmo espaço de endereçamento, recursos do sistema e arquivos abertos.Threads em um mesmo processo podem se comunicar mais facilmente entre si, uma vez que compartilham a mesma memória.

#### Qual motivo fez implementar o Thread no projeto?
O motivo principal é que para cada `Thread` um web-scraping está sendo executado por background sem precisar que o script esteja em execução e sem precisar ter que ocupar um novo espaço de endereçamento, recursos do sistema e arquivos abertos.

#### Estrutura do projeto

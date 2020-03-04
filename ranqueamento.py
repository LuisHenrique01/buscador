import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('db_cache', backend='sqlite', expire_after=300)

base_url = 'https://www.suamusica.com.br/noticia/leo-santana-tranquiliza-os-fas-apos-cirurgia-foi-um-sucesso'
response = requests.get(base_url)

pagina_inicial = BeautifulSoup(response.text, 'html5lib')
lista_tags_a = pagina_inicial.find_all('a')
links = []


def limpar_links(lista_tags):
    for a in lista_tags:
        try:
            link_atual = a['href']
            if link_atual[0] == '/':
                links.append(base_url + link_atual[1:])
            elif link_atual[0] != '#' and link_atual[0] != 'j':
                links.append(link_atual)
        except KeyError:
            pass


limpar_links(lista_tags_a)

print(links)

# 1 - Página inicial
# 2 - Página inicial -> Link
# 3 - Página inicial -> Link -> Link

'''
def gera_texto_pagina(pagina):
    texto_pagina = ''

    lista_a = pagina.find_all('a')


    while i < len(pagina):
        


def buscar(palavra_chave, profundidade, url):
    palavra_chave = palavra_chave.lower()
    ranking = []
    dados_busca = {}

    if profundidade == 1:
        texto_pagina = pagina_inicial.get_text().lower()
        dados_busca = {base_url: texto_pagina.count(palavra_chave)}
        ranking.append(dados_busca)

    elif profundidade == 2:
        links_passados = []

        for i in range(len(links)):
            if links[i] not in links_passados:
                response = requests.get(links[i], allow_redirects=False)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html5lib')
                    texto_pagina = soup.text.lower()
                    dados_busca = {links[i]: texto_pagina.count(palavra_chave)}
                    ranking.append(dados_busca)
                else:
                    print('Deu merda')
            links_passados.append(links[i])

    return ranking


ranking = buscar('futebol', 2, base_url)

print(ranking)'''
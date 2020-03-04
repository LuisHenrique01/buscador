import requests
from bs4 import BeautifulSoup

url = 'https://pt.wikisource.org/wiki/Wikisource:P%C3%A1gina_principal'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html5lib')
lista_a = soup.find_all('a')
links = []

# Limpeza de links

for a in lista_a:
    try:
        if a['href'][0] == '/':
            links.append(url + a['href'][1:])
        elif a['href'][0] != '#':
            links.append(a['href'])
    except:
        pass

#texto_pagina = soup.get_text().lower()
texto_pagina = soup.prettify()
texto_limpo = ''
i = 0

while True:
    try:
        if i == len(texto_pagina):
            break
        if texto_pagina[i] == '<':
            while texto_pagina[i] != '>':
                i += 1
            i += 1
        texto_limpo += texto_pagina[i]
        i += 1
    except:
        break

print(texto_limpo)

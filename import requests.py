import requests
from bs4 import BeautifulSoup

url = 'https://www.olx.com.br/brasil?q=fuzz%20face'

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
fuzz = soup.find_all('div', class_='sc-12rk7z2-2 gSNULD')
ultima_pagina = soup.find('span', class_='sc-ifAKCX fiwAfL').get_text().strip()

for i in range (1,int(ultima_pagina)):
    url_pag = f'https://www.olx.com.br/brasil?o={i}&q=fuzz%20face'
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
fuzz = soup.find_all('div', class_='sc-12rk7z2-2 gSNULD')

with open ('precos_fuzz.csv', 'a', newline='',encoding='UTF-8') as f:
    for fuzz1 in fuzz:
        marca = fuzz1.find('h2', class_="kgl1mq-0 eFXRHn sc-ifAKCX iUMNkO").get_text().strip()
        preco = fuzz1.find('span', class_="m7nrfa-0 eJCbzj sc-ifAKCX jViSDP").get_text().strip()
   
        linha = marca + ';' + preco + '\n'
        print(linha)
        f.write(linha)
  

# -----------------------------
# CAPÍTULO 20 - WEB SCRAPING
# -----------------------------
import requests
from bs4 import BeautifulSoup
print("Capítulo 20 - Scraping")
url = "https://news.google.com"
resposta = requests.get(url)
sopa = BeautifulSoup(resposta.content, 'html.parser')
print("Conteúdo da página inicial do Google News coletado.")

## Capítulo 9 - Arquivos

### Gravação em arquivos

with open('arquivo.txt', 'w') as f:
    f.write("Olá, mundo!\n")


### Leitura de arquivos CSV

import csv
with open('dados.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)


### Desafio

# Criar um arquivo com nome e idade de 3 pessoas
pessoas = [('João', 30), ('Ana', 25), ('Carlos', 40)]
with open('pessoas.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['Nome', 'Idade'])
    escritor.writerows(pessoas)
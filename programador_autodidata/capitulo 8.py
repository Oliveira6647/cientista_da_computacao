## Capítulo 8 - Módulos

### Módulos internos importantes

import math
print(math.sqrt(25))

import random
print(random.randint(1, 10))


### Importação de outros módulos

import datetime as dt
print(dt.datetime.now())


### Desafio

import statistics
valores = [5, 10, 15, 20]
print("Média:", statistics.mean(valores))

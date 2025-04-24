
# -----------------------------
# CAPÍTULO 21 - ESTRUTURAS DE DADOS
# -----------------------------
print("Capítulo 21 - Estrutura de Dados")
pilha = []
pilha.append('a')
pilha.append('b')
print("Topo da pilha:", pilha.pop())

from collections import deque
fila = deque()
fila.append('cliente1')
fila.append('cliente2')
print("Atendido:", fila.popleft())
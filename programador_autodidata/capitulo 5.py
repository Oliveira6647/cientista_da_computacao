
# ---------------------- Capítulo 5: Contêineres ----------------------

# Listas
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")
print(frutas)

# Tuplas
coordenadas = (10, 20)
print(coordenadas[0])

# Dicionários
dados = {"nome": "Márcio", "idade": 45}
print(dados["nome"])

# Contêineres em contêineres
alunos = [{"nome": "Ana", "nota": 8}, {"nome": "João", "nota": 7}]
for aluno in alunos:
    print(f"{aluno['nome']} tirou nota {aluno['nota']}")

# Desafio
notas = [7, 8, 6, 9, 5]
media = sum(notas) / len(notas)
print(f"Média da turma: {media:.2f}")
# -----------------------------
# CAPÍTULO 17 - EXPRESSÕES REGULARES
# -----------------------------
import re
print("Capítulo 17 - Expressões Regulares")
texto = "Meu número é 123-456-7890"
resultado = re.search(r"\d{3}-\d{3}-\d{4}", texto)
print("Telefone encontrado:", resultado.group())
print(re.findall(r"\b\w{4}\b", "Esta frase tem várias palavras com quatro letras."))
import string

def cipher(a_string, key):
    uppercase= string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ''
    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt

print(cipher('Michelly', 1))

#código traduzindo para o português
import string  # Importa o módulo que contém letras do alfabeto

def cifra(uma_string, chave):
    maiusculas = string.ascii_uppercase  # Letras maiúsculas: 'A' até 'Z'
    minusculas = string.ascii_lowercase  # Letras minúsculas: 'a' até 'z'
    criptografado = ''  # String vazia onde vamos guardar o resultado

    for caractere in uma_string:  # Para cada caractere da string original
        if caractere in maiusculas:  # Se for letra maiúscula
            nova_posicao = (maiusculas.index(caractere) + chave) % 26
            criptografado += maiusculas[nova_posicao]
        elif caractere in minusculas:  # Se for letra minúscula
            nova_posicao = (minusculas.index(caractere) + chave) % 26
            criptografado += minusculas[nova_posicao]
        else:
            criptografado += caractere  # Se não for letra, mantém igual (espaço, número, etc.)

    return criptografado

print(cifra('Michelly', 1))  # Teste da função com a palavra "Michelly" e chave 1

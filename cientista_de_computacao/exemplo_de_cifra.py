import string

def cipher(a_string, key):
    uppercase = string.ascii_uppercase
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

# Frase cifrada:
mensagem_cifrada = "R whvrxur hvwá hqwhuudgr shqwr gd dúuyuh"

# Decifrando com chave -3:
mensagem_decifrada = cipher(mensagem_cifrada, -3)

print(mensagem_decifrada)

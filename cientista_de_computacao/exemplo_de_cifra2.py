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

# MENU INTERATIVO
print("=== MENU CÓDIGO SECRETO ===")
print("1 - Cifrar uma mensagem")
print("2 - Decifrar uma mensagem")
opcao = input("Escolha uma opção (1 ou 2): ")

mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave (um número inteiro): "))

if opcao == "1":
    resultado = cipher(mensagem, chave)
    print("\n🔒 Mensagem Cifrada:")
    print(resultado)
elif opcao == "2":
    resultado = cipher(mensagem, -chave)
    print("\n🔓 Mensagem Decifrada:")
    print(resultado)
else:
    print("❌ Opção inválida. Por favor, escolha 1 ou 2.")

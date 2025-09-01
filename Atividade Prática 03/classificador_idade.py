""""
Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).

"""

# Classificador de Idade
# Programa que classifica uma pessoa em categorias baseadas na idade

print("=== Classificador de Idade ===")
print()

# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Classifica a idade em categorias
if idade >= 0 and idade <= 12:
    categoria = "Criança"
elif idade >= 13 and idade <= 17:
    categoria = "Adolescente"
elif idade >= 18 and idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"

# Exibe o resultado
if categoria != "Idade inválida":
    print(f"Classificação: {categoria} ({idade} anos)")
else:
    print("Por favor, digite uma idade válida (número positivo).")

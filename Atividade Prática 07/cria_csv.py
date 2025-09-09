import csv

# Nome do arquivo CSV
arquivo = "dados_pessoais.csv"

# Dados de exemplo
dados = [
    ["Nome", "Idade", "Cidade"],   # Cabeçalho
    ["Ana", 25, "São Paulo"],
    ["Pedro", 30, "Rio de Janeiro"],
    ["Carla", 28, "Belo Horizonte"],
    ["João", 35, "Curitiba"]
]

# Escrevendo no arquivo CSV
with open(arquivo, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(dados)

print(f"Arquivo '{arquivo}' criado com sucesso!")

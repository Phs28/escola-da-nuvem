import csv

# Nome do arquivo CSV
arquivo = "dados_pessoais.csv"

# Abrindo e lendo o CSV
with open(arquivo, "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    
    # Lendo linha por linha
    for linha in leitor:
        print(linha)


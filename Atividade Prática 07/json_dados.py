import json

# Nome do arquivo JSON
arquivo = "pessoa.json"

# Dados de exemplo
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

# --- Escrevendo no arquivo JSON ---
with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)

print(f"Arquivo '{arquivo}' criado com sucesso!")

# --- Lendo o arquivo JSON ---
with open(arquivo, "r", encoding="utf-8") as f:
    dados = json.load(f)

print("\nConteúdo do arquivo JSON:")
print(dados)
print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")

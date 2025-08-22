""""
Calculadora de Preço Total

Desenvolva um programa que calcule o preço total de uma compra.
 Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

"""


def main():
    # Informações do produto
    nome_produto = "Cadeira Infantil"
    preco_unitario = 12.40
    quantidade = 3
    
    print("=" * 50)
    print("         CALCULADORA DE PREÇO TOTAL")
    print("=" * 50)
    print()
    
    # Exibindo informações do produto
    print("INFORMAÇÕES DA COMPRA:")
    print(f"Produto: {nome_produto}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Quantidade: {quantidade} unidades")
    print()
    
    # Calculando o preço total
    preco_total = preco_unitario * quantidade
    
    print("CÁLCULO:")
    print(f"Preço Total = R$ {preco_unitario:.2f} × {quantidade}")
    print(f"Preço Total = R$ {preco_total:.2f}")
    print()
    
    print("=" * 50)
    print(f"RESULTADO FINAL: R$ {preco_total:.2f}")
    print("=" * 50)

if __name__ == "__main__":
    main()

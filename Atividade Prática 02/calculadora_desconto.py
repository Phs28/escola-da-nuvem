"""""
calculadora de Desconto 

Desenvolva um programa que calcula o desconto em uma loja.
 Use as seguintes informações:



Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, 
exibindo todos os detalhes.

"""

def calcular_desconto(preco_original, porcentagem_desconto):
    """
    Calcula o valor do desconto e o preço final
    
    Args:
        preco_original (float): Preço original do produto
        porcentagem_desconto (float): Porcentagem de desconto
    
    Returns:
        tuple: (valor_desconto, preco_final)
    """
    valor_desconto = preco_original * (porcentagem_desconto / 100)
    preco_final = preco_original - valor_desconto
    return valor_desconto, preco_final

def main():
    """Função principal do programa"""
    
    # Dados do produto
    nome_produto = "Camiseta"
    preco_original = 50.00
    porcentagem_desconto = 20
    
    print("=" * 50)
    print("🏷️  CALCULADORA DE DESCONTO")
    print("=" * 50)
    
    # Exibir informações do produto
    print("\n📦 INFORMAÇÕES DO PRODUTO:")
    print("-" * 30)
    print(f"Produto: {nome_produto}")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto: {porcentagem_desconto}%")
    
    # Calcular desconto
    valor_desconto, preco_final = calcular_desconto(preco_original, porcentagem_desconto)
    
    # Exibir cálculos
    print("\n🧮 CÁLCULOS:")
    print("-" * 30)
    print(f"Valor do Desconto: R$ {preco_original:.2f} × {porcentagem_desconto}% = R$ {valor_desconto:.2f}")
    print(f"Preço Final: R$ {preco_original:.2f} - R$ {valor_desconto:.2f} = R$ {preco_final:.2f}")
    
    # Exibir resultado final
    print("\n💰 RESULTADO FINAL:")
    print("-" * 30)
    print(f"Produto: {nome_produto}")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto ({porcentagem_desconto}%): -R$ {valor_desconto:.2f}")
    print(f"Preço Final: R$ {preco_final:.2f}")
    
    # Calcular economia
    economia_percentual = (valor_desconto / preco_original) * 100
    print(f"\n🎉 Você economizou R$ {valor_desconto:.2f} ({economia_percentual:.0f}%)!")
    
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("Verifique os dados e tente novamente.")

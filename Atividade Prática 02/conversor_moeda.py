""""
Conversor de Moeda 

Crie um programa que converte um valor em reais para dólares e euros.
 Use os seguintes dados:



Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.60

Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos,
arredondando para duas casas decimais.
"""

def converter_moeda():
    """Função principal para conversão de moeda"""
    
    # Dados fornecidos
    valor_reais = 100.00
    taxa_dolar = 5.60
    taxa_euro = 6.60
    
    # Cálculos de conversão
    valor_dolares = valor_reais / taxa_dolar
    valor_euros = valor_reais / taxa_euro
    
    # Exibição dos resultados
    print("=" * 50)
    print("🏦 CONVERSOR DE MOEDA 💱")
    print("=" * 50)
    print()
    
    print("📊 DADOS DE ENTRADA:")
    print(f"   💰 Valor em Reais: R$ {valor_reais:.2f}")
    print(f"   💵 Taxa do Dólar: R$ {taxa_dolar:.2f}")
    print(f"   💶 Taxa do Euro: R$ {taxa_euro:.2f}")
    print()
    
    print("🔄 CÁLCULOS:")
    print(f"   Dólares = R$ {valor_reais:.2f} ÷ R$ {taxa_dolar:.2f}")
    print(f"   Euros = R$ {valor_reais:.2f} ÷ R$ {taxa_euro:.2f}")
    print()
    
    print("✅ RESULTADOS DA CONVERSÃO:")
    print(f"   💵 Valor em Dólares: $ {valor_dolares:.2f}")
    print(f"   💶 Valor em Euros: € {valor_euros:.2f}")
    print()
    
    print("=" * 50)
    print("Conversão realizada com sucesso! ✨")
    print("=" * 50)

def main():
    """Função principal do programa"""
    try:
        converter_moeda()
    except Exception as e:
        print(f"❌ Erro durante a conversão: {e}")

if __name__ == "__main__":
    main()

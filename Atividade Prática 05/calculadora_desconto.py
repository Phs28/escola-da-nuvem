def calcular_desconto(preco_original, percentual_desconto):
    """
    Calcula o preço final após aplicar desconto.
    
    Parâmetros:
    preco_original (float): O preço original do produto
    percentual_desconto (float): O percentual de desconto (ex: 10 para 10%)
    
    Retorna:
    tuple: (valor_desconto, preco_final)
    """
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return valor_desconto, preco_final

def validar_entrada_numerica(prompt, tipo="float"):
    """Valida entrada numérica do usuário."""
    while True:
        try:
            valor = input(prompt)
            if tipo == "float":
                return float(valor)
            elif tipo == "int":
                return int(valor)
        except ValueError:
            print("❌ Por favor, digite um número válido!")

def main():
    print("=" * 50)
    print("🛍️  CALCULADORA DE DESCONTO")
    print("=" * 50)
    
    # Exemplo de uso da função
    print("\n📋 Exemplo de uso:")
    exemplo_preco = 250.75
    exemplo_desconto = 10
    exemplo_valor_desc, exemplo_preco_final = calcular_desconto(exemplo_preco, exemplo_desconto)
    
    print(f"Preço original: R$ {exemplo_preco:.2f}")
    print(f"Desconto de {exemplo_desconto}%: R$ {exemplo_valor_desc:.2f}")
    print(f"Preço final: R$ {exemplo_preco_final:.2f}")
    
    print("\n" + "=" * 50)
    
    while True:
        print("\n💰 Calcule seu desconto:")
        
        # Entrada do usuário
        preco = validar_entrada_numerica("Digite o preço original do produto (R$): ")
        
        if preco < 0:
            print("❌ O preço não pode ser negativo!")
            continue
            
        desconto = validar_entrada_numerica("Digite o percentual de desconto (%): ")
        
        if desconto < 0 or desconto > 100:
            print("❌ O desconto deve estar entre 0% e 100%!")
            continue
        
        # Cálculo
        valor_desconto, preco_final = calcular_desconto(preco, desconto)
        
        # Resultado
        print("\n" + "-" * 40)
        print("📊 RESULTADO DO CÁLCULO:")
        print("-" * 40)
        print(f"Preço original:     R$ {preco:.2f}")
        print(f"Desconto ({desconto}%):      R$ {valor_desconto:.2f}")
        print(f"Preço final:        R$ {preco_final:.2f}")
        print(f"Economia:           R$ {valor_desconto:.2f}")
        
        # Informações adicionais
        if desconto >= 50:
            print("🎉 Excelente desconto! Mais de 50% de economia!")
        elif desconto >= 30:
            print("👍 Bom desconto! Economia significativa!")
        elif desconto >= 10:
            print("💡 Desconto razoável!")
        
        print("-" * 40)
        
        # Continuar ou sair
        continuar = input("\nDeseja calcular outro desconto? (s/n): ").lower().strip()
        if continuar not in ['s', 'sim', 'y', 'yes']:
            break
    
    print("\n🙏 Obrigado por usar a Calculadora de Desconto!")
    print("💡 Dica: Sempre compare preços antes de comprar!")

if __name__ == "__main__":
    main()

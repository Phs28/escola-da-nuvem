def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula a gorjeta a ser deixada em um restaurante.
    
    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
    
    Retorna:
    float: O valor da gorjeta calculada
    """
    if valor_conta < 0:
        raise ValueError("O valor da conta não pode ser negativo")
    
    if porcentagem_gorjeta < 0:
        raise ValueError("A porcentagem de gorjeta não pode ser negativa")
    
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

def calcular_total_com_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor total a ser pago (conta + gorjeta).
    
    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta
    
    Retorna:
    float: O valor total a ser pago
    """
    gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
    total = valor_conta + gorjeta
    return round(total, 2)

def main():
    """Função principal com interface interativa."""
    print("=" * 50)
    print("🍽️  CALCULADORA DE GORJETA DE RESTAURANTE  🍽️")
    print("=" * 50)
    
    try:
        # Solicita dados do usuário
        valor_conta = float(input("\n💰 Digite o valor total da conta: R$ "))
        porcentagem_gorjeta = float(input("📊 Digite a porcentagem de gorjeta desejada (%): "))
        
        # Calcula os valores
        gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
        total = calcular_total_com_gorjeta(valor_conta, porcentagem_gorjeta)
        
        # Exibe os resultados
        print("\n" + "=" * 40)
        print("📋 RESUMO DO CÁLCULO:")
        print("=" * 40)
        print(f"Valor da conta:     R$ {valor_conta:.2f}")
        print(f"Porcentagem:        {porcentagem_gorjeta}%")
        print(f"Valor da gorjeta:   R$ {gorjeta:.2f}")
        print(f"Total a pagar:      R$ {total:.2f}")
        print("=" * 40)
        
        # Sugestões de gorjeta
        print("\n💡 SUGESTÕES DE GORJETA:")
        sugestoes = [10, 15, 20]
        for sugestao in sugestoes:
            gorjeta_sugestao = calcular_gorjeta(valor_conta, sugestao)
            total_sugestao = valor_conta + gorjeta_sugestao
            print(f"   {sugestao}%: R$ {gorjeta_sugestao:.2f} (Total: R$ {total_sugestao:.2f})")
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("❌ Erro: Por favor, digite apenas números válidos.")
        else:
            print(f"❌ Erro: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

# Exemplos de uso da função
def exemplos():
    """Demonstra exemplos de uso da função."""
    print("\n🔍 EXEMPLOS DE USO:")
    print("-" * 30)
    
    exemplos_teste = [
        (100.0, 15.0),
        (50.75, 10.0),
        (200.0, 20.0),
        (35.50, 18.0)
    ]
    
    for conta, porcentagem in exemplos_teste:
        gorjeta = calcular_gorjeta(conta, porcentagem)
        total = calcular_total_com_gorjeta(conta, porcentagem)
        print(f"Conta: R$ {conta:.2f} | Gorjeta {porcentagem}%: R$ {gorjeta:.2f} | Total: R$ {total:.2f}")

if __name__ == "__main__":
    # Executa exemplos primeiro
    exemplos()
    
    # Executa o programa principal
    main()
    
    # Pergunta se o usuário quer calcular novamente
    while True:
        continuar = input("\n🔄 Deseja calcular outra gorjeta? (s/n): ").lower().strip()
        if continuar in ['s', 'sim', 'y', 'yes']:
            main()
        elif continuar in ['n', 'não', 'nao', 'no']:
            print("\n👋 Obrigado por usar a Calculadora de Gorjeta!")
            break
        else:
            print("❌ Resposta inválida. Digite 's' para sim ou 'n' para não.")

from datetime import datetime, date

def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade de uma pessoa em dias baseada no ano de nascimento.
    
    Parâmetros:
    ano_nascimento (int): O ano de nascimento da pessoa
    
    Retorna:
    int: A idade em dias
    """
    try:
        # Data atual
        data_atual = date.today()
        
        # Data de nascimento (assumindo 1º de janeiro do ano informado)
        data_nascimento = date(ano_nascimento, 1, 1)
        
        # Calcula a diferença em dias
        diferenca = data_atual - data_nascimento
        
        return diferenca.days
    
    except ValueError as e:
        print(f"Erro: Ano inválido - {e}")
        return None

def calcular_idade_precisa(ano_nascimento, mes_nascimento=1, dia_nascimento=1):
    """
    Calcula a idade em dias com data completa de nascimento.
    
    Parâmetros:
    ano_nascimento (int): Ano de nascimento
    mes_nascimento (int): Mês de nascimento (padrão: 1)
    dia_nascimento (int): Dia de nascimento (padrão: 1)
    
    Retorna:
    int: A idade em dias
    """
    try:
        # Data atual
        data_atual = date.today()
        
        # Data de nascimento completa
        data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
        
        # Verifica se a data de nascimento não é no futuro
        if data_nascimento > data_atual:
            print("Erro: Data de nascimento não pode ser no futuro!")
            return None
        
        # Calcula a diferença em dias
        diferenca = data_atual - data_nascimento
        
        return diferenca.days
    
    except ValueError as e:
        print(f"Erro: Data inválida - {e}")
        return None

def validar_ano(ano):
    """Valida se o ano está dentro de um range razoável."""
    ano_atual = datetime.now().year
    if ano < 1900 or ano > ano_atual:
        return False
    return True

def main():
    print("=" * 50)
    print("    CALCULADORA DE IDADE EM DIAS")
    print("=" * 50)
    
    # Exemplos de teste
    print("\n📊 EXEMPLOS DE CÁLCULO:")
    exemplos = [
        (1990, "Nascido em 1990"),
        (2000, "Nascido em 2000"),
        (1985, "Nascido em 1985")
    ]
    
    for ano, descricao in exemplos:
        dias = calcular_idade_em_dias(ano)
        if dias:
            anos_aproximados = dias // 365
            print(f"• {descricao}: {dias:,} dias (~{anos_aproximados} anos)")
    
    print("\n" + "=" * 50)
    
    while True:
        try:
            print("\nEscolha uma opção:")
            print("1 - Calcular idade apenas com ano de nascimento")
            print("2 - Calcular idade com data completa")
            print("3 - Sair")
            
            opcao = input("\nDigite sua opção (1-3): ").strip()
            
            if opcao == "3":
                print("\n👋 Obrigado por usar a calculadora!")
                break
            
            elif opcao == "1":
                print("\n📅 CÁLCULO POR ANO DE NASCIMENTO")
                ano_str = input("Digite o ano de nascimento: ").strip()
                
                if not ano_str.isdigit():
                    print("❌ Por favor, digite apenas números!")
                    continue
                
                ano = int(ano_str)
                
                if not validar_ano(ano):
                    print(f"❌ Ano deve estar entre 1900 e {datetime.now().year}!")
                    continue
                
                dias = calcular_idade_em_dias(ano)
                
                if dias is not None:
                    anos_aproximados = dias // 365
                    meses_aproximados = (dias % 365) // 30
                    
                    print(f"\n✅ RESULTADO:")
                    print(f"   Idade: {dias:,} dias")
                    print(f"   Aproximadamente: {anos_aproximados} anos e {meses_aproximados} meses")
                    print(f"   (Considerando 1º de janeiro de {ano} como data de nascimento)")
            
            elif opcao == "2":
                print("\n📅 CÁLCULO COM DATA COMPLETA")
                
                # Ano
                ano_str = input("Digite o ano de nascimento: ").strip()
                if not ano_str.isdigit():
                    print("❌ Por favor, digite apenas números para o ano!")
                    continue
                ano = int(ano_str)
                
                if not validar_ano(ano):
                    print(f"❌ Ano deve estar entre 1900 e {datetime.now().year}!")
                    continue
                
                # Mês
                mes_str = input("Digite o mês de nascimento (1-12): ").strip()
                if not mes_str.isdigit() or not (1 <= int(mes_str) <= 12):
                    print("❌ Mês deve ser um número entre 1 e 12!")
                    continue
                mes = int(mes_str)
                
                # Dia
                dia_str = input("Digite o dia de nascimento (1-31): ").strip()
                if not dia_str.isdigit() or not (1 <= int(dia_str) <= 31):
                    print("❌ Dia deve ser um número entre 1 e 31!")
                    continue
                dia = int(dia_str)
                
                dias = calcular_idade_precisa(ano, mes, dia)
                
                if dias is not None:
                    anos = dias // 365
                    meses = (dias % 365) // 30
                    dias_restantes = (dias % 365) % 30
                    
                    print(f"\n✅ RESULTADO:")
                    print(f"   Data de nascimento: {dia:02d}/{mes:02d}/{ano}")
                    print(f"   Idade: {dias:,} dias")
                    print(f"   Aproximadamente: {anos} anos, {meses} meses e {dias_restantes} dias")
            
            else:
                print("❌ Opção inválida! Digite 1, 2 ou 3.")
            
            # Pergunta se quer continuar
            if opcao in ["1", "2"]:
                continuar = input("\nDeseja fazer outro cálculo? (s/n): ").strip().lower()
                if continuar not in ['s', 'sim', 'y', 'yes']:
                    print("\n👋 Obrigado por usar a calculadora!")
                    break
        
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tente novamente.")

if __name__ == "__main__":
    main()

def verificar_par_impar(numero):
    """
    Verifica se um número é par ou ímpar
    
    Args:
        numero (int): Número a ser verificado
        
    Returns:
        str: 'par' se o número for par, 'ímpar' se for ímpar
    """
    return 'par' if numero % 2 == 0 else 'ímpar'

def obter_numero_usuario():
    """
    Solicita um número do usuário com tratamento de erros
    
    Returns:
        int or str: Número inteiro válido ou 'fim' para encerrar
    """
    while True:
        try:
            entrada = input("📝 Digite um número inteiro (ou 'fim' para encerrar): ").strip()
            
            # Verifica se o usuário quer sair
            if entrada.lower() == 'fim':
                return 'fim'
            
            # Tenta converter para inteiro
            numero = int(entrada)
            return numero
            
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números inteiros válidos!")
            continue
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            return 'fim'

def exibir_relatorio(contador_pares, contador_impares, numeros_processados):
    """
    Exibe o relatório final com estatísticas
    
    Args:
        contador_pares (int): Quantidade de números pares
        contador_impares (int): Quantidade de números ímpares
        numeros_processados (list): Lista dos números processados
    """
    print("\n" + "="*50)
    print("📊 RELATÓRIO FINAL")
    print("="*50)
    
    total = contador_pares + contador_impares
    
    if total == 0:
        print("❌ Nenhum número válido foi inserido.")
        return
    
    print(f"📈 Total de números processados: {total}")
    print(f"🔢 Números pares: {contador_pares}")
    print(f"🔢 Números ímpares: {contador_impares}")
    
    # Calcula percentuais
    if total > 0:
        perc_pares = (contador_pares / total) * 100
        perc_impares = (contador_impares / total) * 100
        
        print(f"📊 Percentual de pares: {perc_pares:.1f}%")
        print(f"📊 Percentual de ímpares: {perc_impares:.1f}%")
    
    # Mostra os números processados se não forem muitos
    if len(numeros_processados) <= 10:
        print(f"📋 Números inseridos: {numeros_processados}")
    
    print("="*50)

def main():
    """
    Função principal do programa
    """
    print("🔢 VERIFICADOR DE NÚMEROS PARES E ÍMPARES")
    print("="*50)
    print("Digite números inteiros para verificar se são pares ou ímpares.")
    print("Digite 'fim' quando quiser encerrar o programa.")
    print("-"*50)
    
    contador_pares = 0
    contador_impares = 0
    numeros_processados = []
    
    try:
        while True:
            numero = obter_numero_usuario()
            
            # Verifica se o usuário quer sair
            if numero == 'fim':
                break
            
            # Verifica se é par ou ímpar
            resultado = verificar_par_impar(numero)
            
            # Atualiza contadores
            if resultado == 'par':
                contador_pares += 1
            else:
                contador_impares += 1
            
            # Adiciona à lista de números processados
            numeros_processados.append(numero)
            
            # Exibe o resultado
            print(f"✅ O número {numero} é {resultado}.")
            
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    
    finally:
        # Exibe o relatório final
        exibir_relatorio(contador_pares, contador_impares, numeros_processados)
        print("\n👋 Obrigado por usar o verificador de números!")

if __name__ == "__main__":
    main()

"""
Calculadora de Comissão


Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais,
representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

"""

# Calculadora de Comissão
# Calcula o total a receber por um vendedor baseado no salário fixo e comissão de 15% sobre vendas

def main():
    print("=== CALCULADORA DE COMISSÃO ===")
    print("Calcula o total a receber com salário fixo + 15% de comissão sobre vendas")
    print()
    
    try:
        # Entrada de dados
        nome_vendedor = input("Digite o nome do vendedor: ").strip()
        
        # Validação do nome
        if not nome_vendedor:
            print("Erro: Nome do vendedor não pode estar vazio!")
            return
        
        salario_fixo = float(input("Digite o salário fixo (R$): "))
        total_vendas = float(input("Digite o total de vendas no mês (R$): "))
        
        # Validação dos valores
        if salario_fixo < 0:
            print("Erro: Salário fixo não pode ser negativo!")
            return
        
        if total_vendas < 0:
            print("Erro: Total de vendas não pode ser negativo!")
            return
        
        # Cálculos
        percentual_comissao = 0.15  # 15%
        comissao = total_vendas * percentual_comissao
        total_a_receber = salario_fixo + comissao
        
        # Saída formatada
        print("\n" + "="*50)
        print("RESULTADO DO CÁLCULO")
        print("="*50)
        print(f"Vendedor: {nome_vendedor}")
        print(f"Salário fixo: R$ {salario_fixo:.2f}")
        print(f"Total de vendas: R$ {total_vendas:.2f}")
        print(f"Comissão (15%): R$ {comissao:.2f}")
        print("-" * 30)
        print(f"TOTAL A RECEBER: R$ {total_a_receber:.2f}")
        print("="*50)
        
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos para salário e vendas!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()

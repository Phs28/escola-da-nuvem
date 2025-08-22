"""
Calculadora de Soma

Desenvolva um programa que soma dois números.
Use as variáveis numero1 = 12 e numero2 = 14. 
O programa deve calcular a soma e exibir o resultado.

"""


def main():
    # Definindo as variáveis conforme solicitado
    numero1 = 12
    numero2 = 14
    
    # Calculando a soma
    soma = numero1 + numero2
    
    # Exibindo o resultado de forma organizada
    print("=" * 40)
    print("        CALCULADORA DE SOMA")
    print("=" * 40)
    print()
    print(f"Primeiro número: {numero1}")
    print(f"Segundo número:  {numero2}")
    print("-" * 25)
    print(f"Soma:            {soma}")
    print()
    print("=" * 40)
    print("Cálculo realizado com sucesso!")
    print("=" * 40)

if __name__ == "__main__":
    main()

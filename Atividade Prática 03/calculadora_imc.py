"""
Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"

"""

# Calculadora de IMC (Índice de Massa Corporal)
# Solicita peso e altura do usuário, calcula o IMC e fornece classificação

print("=== Calculadora de IMC ===")
print()

# Entrada de dados
try:
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))
    
    # Validação básica
    if peso <= 0 or altura <= 0:
        print("Erro: Peso e altura devem ser valores positivos!")
    else:
        # Cálculo do IMC
        imc = peso / (altura ** 2)
        
        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        
        # Exibição dos resultados
        print()
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print()
        print("Tabela de referência:")
        print("< 18.5: Abaixo do peso")
        print("18.5 - 24.9: Peso normal")
        print("25.0 - 29.9: Sobrepeso")
        print(">= 30.0: Obeso")

except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos!")


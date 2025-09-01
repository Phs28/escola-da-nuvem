"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas 
(adição, subtração, multiplicação e divisão)
 entre dois números.
 A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação.
 Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida

Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro,
 o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.

"""

def obter_numero(mensagem):
    """Solicita um número do usuário com tratamento de erro."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Erro: Por favor, insira um número válido.")

def obter_operacao():
    """Solicita uma operação válida do usuário."""
    operacoes_validas = ['+', '-', '*', '/']
    while True:
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        if operacao in operacoes_validas:
            return operacao
        else:
            print("❌ Erro: Operação inválida. Use apenas +, -, * ou /")

def realizar_calculo(num1, num2, operacao):
    """Realiza o cálculo baseado na operação escolhida."""
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida")
        return num1 / num2

def main():
    """Função principal da calculadora."""
    print("🧮 CALCULADORA PYTHON")
    print("=" * 30)
    
    while True:
        try:
            # Solicitar os números
            print("\n📝 Insira os dados para o cálculo:")
            num1 = obter_numero("Primeiro número: ")
            num2 = obter_numero("Segundo número: ")
            
            # Solicitar a operação
            operacao = obter_operacao()
            
            # Realizar o cálculo
            resultado = realizar_calculo(num1, num2, operacao)
            
            # Exibir o resultado
            print(f"\n✅ Resultado: {num1} {operacao} {num2} = {resultado}")
            print("Calculadora encerrada com sucesso!")
            break
            
        except ZeroDivisionError as e:
            print(f"❌ Erro: {e}")
            print("Tente novamente com um divisor diferente de zero.\n")
            
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            print("Tente novamente.\n")

if __name__ == "__main__":
    main()

"""
Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D.
A seguir, calcule e
mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.


"""

def calcular_diferenca():
    """
    Função principal que lê 4 valores inteiros e calcula a diferença
    """
    print("=" * 50)
    print("🔢 CALCULADORA DE DIFERENÇA DE PRODUTOS")
    print("=" * 50)
    print("Fórmula: DIFERENCA = (A * B - C * D)")
    print("-" * 50)
    
    try:
        # Lendo os quatro valores inteiros
        print("Digite os quatro valores inteiros:")
        A = int(input("Valor A: "))
        B = int(input("Valor B: "))
        C = int(input("Valor C: "))
        D = int(input("Valor D: "))
        
        print("-" * 50)
        
        # Calculando os produtos
        produto_AB = A * B
        produto_CD = C * D
        
        # Calculando a diferença
        diferenca = produto_AB - produto_CD
        
        # Exibindo os cálculos
        print("📊 CÁLCULOS:")
        print(f"A * B = {A} * {B} = {produto_AB}")
        print(f"C * D = {C} * {D} = {produto_CD}")
        print(f"DIFERENCA = {produto_AB} - {produto_CD} = {diferenca}")
        
        print("-" * 50)
        
        # Resultado final conforme especificação
        print(f"DIFERENCA = {diferenca}")
        
        print("=" * 50)
        
    except ValueError:
        print("❌ Erro: Por favor, digite apenas números inteiros!")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

def main():
    """
    Função principal do programa
    """
    calcular_diferenca()

if __name__ == "__main__":
    main()

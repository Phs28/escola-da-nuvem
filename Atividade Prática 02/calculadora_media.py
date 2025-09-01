"""

Calculadora de Média Escolar 

Crie um programa que calcula a média escolar de um aluno.
 Use as seguintes notas:

Nota 1: 7.5

Nota 2: 8.0

Nota 3: 6.5 
O programa deve calcular a média e exibir todas as notas e 
o resultado final, arredondando para duas casas decimais.

"""

def calcular_media(nota1, nota2, nota3):
    """
    Calcula a média de três notas
    
    Args:
        nota1, nota2, nota3: Notas do aluno
    
    Returns:
        float: Média das notas arredondada para 2 casas decimais
    """
    media = (nota1 + nota2 + nota3) / 3
    return round(media, 2)

def main():
    """Função principal do programa"""
    
    # Dados das notas
    nota1 = 7.5
    nota2 = 8.0
    nota3 = 6.5
    
    print("=" * 50)
    print("🎓 CALCULADORA DE MÉDIA ESCOLAR 🎓")
    print("=" * 50)
    
    # Exibir as notas
    print("\n📋 NOTAS DO ALUNO:")
    print("-" * 30)
    print(f"   Nota 1: {nota1:.1f}")
    print(f"   Nota 2: {nota2:.1f}")
    print(f"   Nota 3: {nota3:.1f}")
    
    # Calcular a média
    media = calcular_media(nota1, nota2, nota3)
    
    # Exibir cálculo detalhado
    print("\n🧮 CÁLCULO DA MÉDIA:")
    print("-" * 30)
    print(f"   Soma das notas: {nota1} + {nota2} + {nota3} = {nota1 + nota2 + nota3}")
    print(f"   Divisão por 3: {nota1 + nota2 + nota3} ÷ 3 = {media}")
    
    # Resultado final
    print("\n📊 RESULTADO FINAL:")
    print("-" * 30)
    print(f"   Média Final: {media:.2f}")
    
    # Classificação da média
    if media >= 9.0:
        classificacao = "Excelente! 🌟"
    elif media >= 7.0:
        classificacao = "Bom! 👍"
    elif media >= 6.0:
        classificacao = "Regular 📚"
    else:
        classificacao = "Precisa melhorar 📖"
    
    print(f"   Classificação: {classificacao}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()

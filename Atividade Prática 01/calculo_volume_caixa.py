"""
Calculadora de Volume
Crie um programa que calcule o volume de uma caixa retangular.
Use as seguintes dimensões:
Comprimento: 12 cm
Largura: 14 cm
Altura: 20 cm 
O programa deve calcular o volume e exibir o resultado em cm³.
"""

def calcular_volume(comprimento, largura, altura):
    
    return comprimento * largura * altura

def main():
    """Função principal do programa"""
    
    # Cabeçalho do programa
    print("=" * 50)
    print("    CALCULADORA DE VOLUME - CAIXA RETANGULAR")
    print("=" * 50)
    print()
    
    # Definindo as dimensões da caixa
    comprimento = 12  # cm
    largura = 14      # cm
    altura = 20       # cm
    
    # Exibindo as dimensões
    print("📦 DIMENSÕES DA CAIXA:")
    print(f"   Comprimento: {comprimento} cm")
    print(f"   Largura:     {largura} cm")
    print(f"   Altura:      {altura} cm")
    print()
    
    # Calculando o volume
    volume = calcular_volume(comprimento, largura, altura)
    
    # Exibindo o cálculo
    print("🔢 CÁLCULO DO VOLUME:")
    print(f"   Volume = Comprimento × Largura × Altura")
    print(f"   Volume = {comprimento} × {largura} × {altura}")
    print(f"   Volume = {volume} cm³")
    print()
    
    # Resultado final
    print("✅ RESULTADO FINAL:")
    print(f"   O volume da caixa retangular é: {volume:,.0f} cm³")
    print()
    print("=" * 50)

if __name__ == "__main__":
    main()

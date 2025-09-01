"""
Calculadora de Consumo de Combustível

 Desenvolva um programa que calcula o consumo médio de combustível de um veículo. 
 Use os seguintes dados:



Distância percorrida: 300 km

Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem,
 incluindo o resultado final arredondado para duas casas decimais.

"""

def calcular_consumo(distancia, combustivel):
    """
    Calcula o consumo médio de combustível
    
    Args:
        distancia (float): Distância percorrida em km
        combustivel (float): Combustível gasto em litros
    
    Returns:
        float: Consumo médio em km/l
    """
    return distancia / combustivel

def classificar_consumo(consumo):
    """
    Classifica o consumo de combustível
    
    Args:
        consumo (float): Consumo em km/l
    
    Returns:
        str: Classificação do consumo
    """
    if consumo >= 15:
        return "Excelente"
    elif consumo >= 12:
        return "Bom"
    elif consumo >= 10:
        return "Regular"
    else:
        return "Ruim"

def main():
    """Função principal do programa"""
    
    # Dados da viagem
    distancia = 300  # km
    combustivel = 25  # litros
    
    print("=" * 50)
    print("🚗 CALCULADORA DE CONSUMO DE COMBUSTÍVEL 🚗")
    print("=" * 50)
    
    # Exibir dados da viagem
    print("\n📊 DADOS DA VIAGEM:")
    print("-" * 30)
    print(f"🛣️  Distância percorrida: {distancia} km")
    print(f"⛽ Combustível gasto: {combustivel} litros")
    
    # Calcular consumo médio
    consumo_medio = calcular_consumo(distancia, combustivel)
    
    # Exibir cálculo detalhado
    print("\n🔢 CÁLCULO DETALHADO:")
    print("-" * 30)
    print(f"Consumo médio = Distância ÷ Combustível")
    print(f"Consumo médio = {distancia} km ÷ {combustivel} litros")
    print(f"Consumo médio = {consumo_medio:.2f} km/l")
    
    # Classificar consumo
    classificacao = classificar_consumo(consumo_medio)
    
    # Exibir resultado final
    print("\n🎯 RESULTADO FINAL:")
    print("-" * 30)
    print(f"📈 Consumo médio: {consumo_medio:.2f} km/l")
    print(f"🏆 Classificação: {classificacao}")
    
    # Informações adicionais
    print("\n💡 INFORMAÇÕES ADICIONAIS:")
    print("-" * 30)
    print(f"💰 Com 1 litro você percorre: {consumo_medio:.2f} km")
    print(f"⛽ Para percorrer 100 km você precisa de: {100/consumo_medio:.2f} litros")
    
    print("\n" + "=" * 50)
    print("✅ Cálculo concluído com sucesso!")
    print("=" * 50)

if __name__ == "__main__":
    main()

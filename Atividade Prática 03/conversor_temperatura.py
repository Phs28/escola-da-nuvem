"""

Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem 
e a unidade para qual deseja converter.

"""

# Conversor de Temperatura
# Converte temperaturas entre Celsius, Fahrenheit e Kelvin

def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    """Converte Celsius para Kelvin"""
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    """Converte Fahrenheit para Kelvin"""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    """Converte Kelvin para Celsius"""
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    """Converte Kelvin para Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32

def exibir_menu():
    """Exibe o menu de opções de unidades"""
    print("\n=== CONVERSOR DE TEMPERATURA ===")
    print("Unidades disponíveis:")
    print("1 - Celsius (°C)")
    print("2 - Fahrenheit (°F)")
    print("3 - Kelvin (K)")

def obter_unidade(tipo):
    """Obtém a escolha da unidade do usuário"""
    while True:
        try:
            escolha = int(input(f"Escolha a unidade {tipo} (1-3): "))
            if escolha in [1, 2, 3]:
                return escolha
            else:
                print("Opção inválida! Escolha entre 1, 2 ou 3.")
        except ValueError:
            print("Por favor, digite um número válido!")

def converter_temperatura(temperatura, origem, destino):
    """Realiza a conversão de temperatura"""
    # Se origem e destino são iguais, não há conversão
    if origem == destino:
        return temperatura
    
    # Converter para Celsius primeiro (como base)
    if origem == 1:  # Celsius
        temp_celsius = temperatura
    elif origem == 2:  # Fahrenheit
        temp_celsius = fahrenheit_para_celsius(temperatura)
    else:  # Kelvin
        temp_celsius = kelvin_para_celsius(temperatura)
    
    # Converter de Celsius para a unidade de destino
    if destino == 1:  # Celsius
        return temp_celsius
    elif destino == 2:  # Fahrenheit
        return celsius_para_fahrenheit(temp_celsius)
    else:  # Kelvin
        return celsius_para_kelvin(temp_celsius)

def obter_nome_unidade(codigo):
    """Retorna o nome da unidade baseado no código"""
    unidades = {1: "Celsius (°C)", 2: "Fahrenheit (°F)", 3: "Kelvin (K)"}
    return unidades[codigo]

def main():
    """Função principal do programa"""
    print("=== CONVERSOR DE TEMPERATURA ===")
    print("Converte temperaturas entre Celsius, Fahrenheit e Kelvin")
    
    try:
        # Solicitar temperatura
        temperatura = float(input("\nDigite a temperatura: "))
        
        # Exibir menu e obter unidades
        exibir_menu()
        origem = obter_unidade("de origem")
        destino = obter_unidade("de destino")
        
        # Validação para Kelvin (não pode ser negativo)
        if origem == 3 and temperatura < 0:
            print("Erro: Temperatura em Kelvin não pode ser negativa!")
            return
        
        # Realizar conversão
        resultado = converter_temperatura(temperatura, origem, destino)
        
        # Exibir resultado
        nome_origem = obter_nome_unidade(origem)
        nome_destino = obter_nome_unidade(destino)
        
        print(f"\n=== RESULTADO ===")
        print(f"{temperatura:.2f} {nome_origem} = {resultado:.2f} {nome_destino}")
        
    except ValueError:
        print("Erro: Por favor, digite um número válido para a temperatura!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()

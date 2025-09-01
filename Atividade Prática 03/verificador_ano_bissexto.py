""""
Verificador de Ano Bissexto


Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.

Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) 
que não são divisíveis por 400.

"""
# Verificador de Ano Bissexto
# Um ano é bissexto se:
# - É divisível por 4 E
# - Se for divisível por 100, também deve ser divisível por 400

def verificar_ano_bissexto(ano):
    """
    Verifica se um ano é bissexto
    
    Regras:
    - Divisível por 400: bissexto
    - Divisível por 100 mas não por 400: não bissexto
    - Divisível por 4 mas não por 100: bissexto
    - Não divisível por 4: não bissexto
    """
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

def main():
    print("=== VERIFICADOR DE ANO BISSEXTO ===")
    print()
    
    try:
        # Solicita o ano do usuário
        ano = int(input("Digite um ano: "))
        
        # Verifica se é bissexto
        if verificar_ano_bissexto(ano):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
            
        print()
        print("Regras para ano bissexto:")
        print("• Divisível por 4")
        print("• Exceto anos centenários (divisíveis por 100)")
        print("• A menos que sejam divisíveis por 400")
        
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()

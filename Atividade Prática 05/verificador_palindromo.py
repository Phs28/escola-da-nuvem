import re
import string

def eh_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    
    Parâmetros:
    texto (str): A palavra ou frase a ser verificada
    
    Retorna:
    str: "Sim" se for palíndromo, "Não" se não for
    """
    # Remove espaços, pontuação e converte para minúsculas
    texto_limpo = re.sub(r'[^a-zA-ZÀ-ÿ0-9]', '', texto.lower())
    
    # Verifica se o texto é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

def testar_palindromos():
    """Testa a função com alguns exemplos conhecidos"""
    exemplos = [
        "arara",
        "A base do teto desaba",
        "Anotaram a data da maratona",
        "python",
        "12321",
        "A man a plan a canal Panama",
        "race a car",
        "Socorram-me, subi no ônibus em Marrocos"
    ]
    
    print("=== TESTANDO EXEMPLOS ===")
    for exemplo in exemplos:
        resultado = eh_palindromo(exemplo)
        print(f"'{exemplo}' → {resultado}")
    print()

def main():
    """Função principal do programa"""
    print("=" * 50)
    print("    VERIFICADOR DE PALÍNDROMOS")
    print("=" * 50)
    print("Este programa verifica se uma palavra ou frase")
    print("é um palíndromo (lê igual de trás para frente).")
    print("Espaços e pontuação são ignorados.")
    print()
    
    # Testa com exemplos
    testar_palindromos()
    
    # Interface interativa
    while True:
        print("-" * 30)
        texto = input("Digite uma palavra ou frase (ou 'sair' para terminar): ").strip()
        
        if texto.lower() == 'sair':
            print("Obrigado por usar o verificador de palíndromos!")
            break
        
        if not texto:
            print("Por favor, digite algo válido.")
            continue
        
        resultado = eh_palindromo(texto)
        print(f"\n'{texto}' é um palíndromo? {resultado}")
        
        # Mostra o texto limpo para debug
        texto_limpo = re.sub(r'[^a-zA-ZÀ-ÿ0-9]', '', texto.lower())
        print(f"Texto processado: '{texto_limpo}'")
        print(f"Reverso: '{texto_limpo[::-1]}'")
        print()

if __name__ == "__main__":
    main()

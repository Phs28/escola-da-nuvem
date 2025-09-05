import requests
import json

def gerar_usuario_aleatorio():
    """
    Gera um perfil de usuário aleatório usando a API Random User Generator
    e exibe nome, email e país do usuário
    """
    try:
        # Fazendo requisição para a API Random User Generator
        print("Gerando usuário aleatório...")
        response = requests.get('https://randomuser.me/api/')
        
        # Verificando se a requisição foi bem-sucedida
        if response.status_code == 200:
            data = response.json()
            usuario = data['results'][0]
            
            # Extraindo informações do usuário
            nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']
            
            # Exibindo as informações
            print("\n" + "="*50)
            print("           PERFIL DE USUÁRIO GERADO")
            print("="*50)
            print(f"Nome: {nome_completo}")
            print(f"Email: {email}")
            print(f"País: {pais}")
            print("="*50)
            
        else:
            print(f"Erro na requisição: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except KeyError as e:
        print(f"Erro ao processar dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def main():
    """Função principal do programa"""
    print("=== GERADOR DE USUÁRIO ALEATÓRIO ===")
    print("Usando a API Random User Generator\n")
    
    while True:
        gerar_usuario_aleatorio()
        
        # Pergunta se o usuário quer gerar outro perfil
        continuar = input("\nDeseja gerar outro usuário? (s/n): ").lower().strip()
        
        if continuar not in ['s', 'sim', 'y', 'yes']:
            print("\nObrigado por usar o gerador de usuários!")
            break
        
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()

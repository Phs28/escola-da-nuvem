"""
Crie um programa que gera uma senha aleatória com o módulo random, 
utilizando caracteres especiais, 
possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.

"""

import requests
import json
from datetime import datetime

def gerar_usuarios(quantidade=1):
    """
    Gera perfis de usuários aleatórios usando a API Random User Generator
    """
    try:
        # URL da API Random User Generator
        url = f"https://randomuser.me/api/?results={quantidade}"
        
        print(f"🔄 Gerando {quantidade} usuário(s) aleatório(s)...")
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            usuarios = []
            
            print("\n" + "="*70)
            print(f"📋 {quantidade} PERFIL(S) DE USUÁRIO GERADO(S)")
            print("="*70)
            
            for i, usuario in enumerate(data['results'], 1):
                nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
                email = usuario['email']
                pais = usuario['location']['country']
                cidade = usuario['location']['city']
                telefone = usuario['phone']
                
                if quantidade == 1:
                    print(f"👤 Nome: {nome_completo}")
                    print(f"📧 Email: {email}")
                    print(f"🌍 País: {pais}")
                else:
                    print(f"\n👤 USUÁRIO {i}:")
                    print(f"   Nome: {nome_completo}")
                    print(f"   📧 Email: {email}")
                    print(f"   🌍 País: {pais}")
                    print(f"   🏙️ Cidade: {cidade}")
                    print(f"   📞 Telefone: {telefone}")
                    print("-" * 50)
                
                usuarios.append({
                    'nome': nome_completo,
                    'email': email,
                    'pais': pais,
                    'cidade': cidade,
                    'telefone': telefone
                })
            
            print("="*70)
            return usuarios
            
        else:
            print(f"❌ Erro na requisição: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return None
    except KeyError as e:
        print(f"❌ Erro ao processar dados: {e}")
        return None
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return None

def salvar_usuarios_arquivo(usuarios, nome_arquivo="usuarios_gerados.json"):
    """
    Salva os usuários gerados em um arquivo JSON
    """
    try:
        dados = {
            'data_geracao': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'total_usuarios': len(usuarios),
            'usuarios': usuarios
        }
        
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=2, ensure_ascii=False)
        
        print(f"💾 Usuários salvos em: {nome_arquivo}")
        
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {e}")

def main():
    """
    Função principal do programa
    """
    print("🎲 Gerador de Perfil de Usuário Aleatório")
    print("Usando a API Random User Generator\n")
    
    while True:
        try:
            print("Opções:")
            print("1 - Gerar 1 usuário")
            print("2 - Gerar múltiplos usuários")
            print("3 - Sair")
            
            opcao = input("\nEscolha uma opção (1-3): ").strip()
            
            if opcao == "1":
                usuarios = gerar_usuarios(1)
                
            elif opcao == "2":
                try:
                    quantidade = int(input("Quantos usuários deseja gerar? (1-100): "))
                    if 1 <= quantidade <= 100:
                        usuarios = gerar_usuarios(quantidade)
                        
                        if usuarios:
                            salvar = input("\n💾 Deseja salvar em arquivo? (s/n): ").lower().strip()
                            if salvar in ['s', 'sim', 'y', 'yes']:
                                salvar_usuarios_arquivo(usuarios)
                    else:
                        print("❌ Quantidade deve ser entre 1 e 100")
                        continue
                except ValueError:
                    print("❌ Por favor, digite um número válido!")
                    continue
                    
            elif opcao == "3":
                print("\n👋 Obrigado por usar o gerador de usuários!")
                break
                
            else:
                print("❌ Opção inválida! Escolha 1, 2 ou 3.")
                continue
                
            if opcao in ["1", "2"] and usuarios:
                continuar = input("\n🔄 Deseja continuar? (s/n): ").lower().strip()
                if continuar not in ['s', 'sim', 'y', 'yes']:
                    print("\n👋 Obrigado por usar o gerador de usuários!")
                    break
                    
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()

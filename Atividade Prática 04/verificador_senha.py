def verificar_senha_forte(senha):
    """
    Verifica se uma senha atende aos critérios de força.
    
    Args:
        senha (str): A senha a ser verificada
        
    Returns:
        tuple: (bool, list) - (é_forte, lista_de_problemas)
    """
    problemas = []
    
    # Verificar comprimento mínimo
    if len(senha) < 8:
        problemas.append("deve ter pelo menos 8 caracteres")
    
    # Verificar se contém pelo menos um número
    tem_numero = any(char.isdigit() for char in senha)
    if not tem_numero:
        problemas.append("deve conter pelo menos um número")
    
    return len(problemas) == 0, problemas

def obter_senha():
    """
    Solicita uma senha do usuário com tratamento de entrada vazia.
    
    Returns:
        str: A senha digitada pelo usuário
    """
    while True:
        try:
            senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()
            if senha == "":
                print("⚠️  Por favor, digite uma senha válida.")
                continue
            return senha
        except KeyboardInterrupt:
            print("\n\n👋 Programa encerrado pelo usuário.")
            return 'sair'
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            continue

def exibir_resultado(senha, eh_forte, problemas):
    """
    Exibe o resultado da verificação da senha.
    
    Args:
        senha (str): A senha verificada
        eh_forte (bool): Se a senha é forte
        problemas (list): Lista de problemas encontrados
    """
    print(f"\n{'='*50}")
    print(f"Senha analisada: {'*' * len(senha)}")
    
    if eh_forte:
        print("✅ SENHA FORTE! Atende a todos os critérios de segurança.")
        print("🔒 Sua senha está protegida.")
    else:
        print("❌ SENHA FRACA! Problemas encontrados:")
        for i, problema in enumerate(problemas, 1):
            print(f"   {i}. A senha {problema}")
        print("\n💡 Dica: Use uma combinação de letras, números e símbolos.")
    
    print(f"{'='*50}\n")

def main():
    """
    Função principal do programa.
    """
    print("🔐 VERIFICADOR DE SENHA FORTE")
    print("="*50)
    print("Critérios para senha forte:")
    print("• Pelo menos 8 caracteres")
    print("• Pelo menos um número")
    print("• Digite 'sair' para encerrar")
    print("="*50)
    
    tentativas = 0
    
    while True:
        try:
            tentativas += 1
            print(f"\n--- Tentativa {tentativas} ---")
            
            senha = obter_senha()
            
            # Verificar se o usuário quer sair
            if senha.lower() == 'sair':
                print("👋 Obrigado por usar o verificador de senhas!")
                break
            
            # Verificar a força da senha
            eh_forte, problemas = verificar_senha_forte(senha)
            
            # Exibir resultado
            exibir_resultado(senha, eh_forte, problemas)
            
            # Se a senha é forte, encerrar o programa
            if eh_forte:
                print("🎉 Parabéns! Senha aceita com sucesso.")
                break
            else:
                print("🔄 Tente novamente com uma senha mais forte.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            print("🔄 Tentando novamente...")
            continue
    
    print(f"\n📊 Total de tentativas: {tentativas}")
    print("🔐 Lembre-se: senhas fortes protegem seus dados!")

if __name__ == "__main__":
    main()

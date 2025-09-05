import requests
import re

def validar_cep(cep):
    """Valida se o CEP está no formato correto (8 dígitos)"""
    # Remove espaços, hífens e outros caracteres
    cep_limpo = re.sub(r'[^0-9]', '', cep)
    
    # Verifica se tem exatamente 8 dígitos
    if len(cep_limpo) == 8 and cep_limpo.isdigit():
        return cep_limpo
    return None

def consultar_cep(cep):
    """Consulta informações do CEP na API ViaCEP"""
    try:
        # URL da API ViaCEP
        url = f"https://viacep.com.br/ws/{cep}/json/"
        
        # Faz a requisição
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Converte para JSON
        dados = response.json()
        
        # Verifica se o CEP foi encontrado
        if 'erro' in dados:
            return None
        
        return dados
        
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def exibir_endereco(dados):
    """Exibe as informações do endereço de forma organizada"""
    print("\n" + "="*50)
    print("           INFORMAÇÕES DO ENDEREÇO")
    print("="*50)
    print(f"CEP:        {dados.get('cep', 'N/A')}")
    print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
    print(f"Bairro:     {dados.get('bairro', 'N/A')}")
    print(f"Cidade:     {dados.get('localidade', 'N/A')}")
    print(f"Estado:     {dados.get('uf', 'N/A')} - {dados.get('estado', 'N/A')}")
    print(f"Região:     {dados.get('regiao', 'N/A')}")
    print("="*50)

def main():
    """Função principal do programa"""
    print("CONSULTA DE CEP - API ViaCEP")
    print("="*40)
    
    while True:
        try:
            # Solicita o CEP do usuário
            cep_input = input("\nDigite o CEP (ou 'sair' para encerrar): ").strip()
            
            # Verifica se o usuário quer sair
            if cep_input.lower() in ['sair', 'exit', 'quit']:
                print("Programa encerrado. Até logo!")
                break
            
            # Valida o CEP
            cep_valido = validar_cep(cep_input)
            if not cep_valido:
                print("CEP inválido! Digite um CEP com 8 dígitos (ex: 01310-100 ou 01310100)")
                continue
            
            print(f"Consultando CEP: {cep_valido}...")
            
            # Consulta o CEP
            dados_endereco = consultar_cep(cep_valido)
            
            if dados_endereco:
                exibir_endereco(dados_endereco)
            else:
                print("CEP não encontrado! Verifique se o CEP está correto.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()

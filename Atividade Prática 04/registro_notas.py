def obter_nota():
    """
     Crie um programa que permita a um professor registrar as notas de uma turma.
     O programa deve continuar solicitando notas até que o professor digite 'fim'.
     Notas válidas são de 0 a 10. 
     O programa deve ignorar notas inválidas e continuar solicitando. 
     No final, deve exibir a média da turma.
    """
    while True:
        entrada = input("Digite uma nota (0-10) ou 'fim' para encerrar: ").strip().lower()
        
        # Verifica se o usuário quer encerrar
        if entrada == 'fim':
            return None
        
        try:
            # Tenta converter para float
            nota = float(entrada)
            
            # Valida se a nota está no intervalo correto
            if 0 <= nota <= 10:
                return nota
            else:
                print("❌ Nota inválida! Digite uma nota entre 0 e 10.")
        
        except ValueError:
            print("❌ Entrada inválida! Digite um número entre 0 e 10 ou 'fim'.")

def calcular_media(notas):
    """
    Calcula a média das notas fornecidas
    """
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def main():
    """
    Função principal do programa de registro de notas
    """
    print("=" * 50)
    print("📚 SISTEMA DE REGISTRO DE NOTAS DA TURMA")
    print("=" * 50)
    print("Digite as notas dos alunos (0-10)")
    print("Digite 'fim' quando terminar de inserir todas as notas")
    print("-" * 50)
    
    notas = []
    
    while True:
        nota = obter_nota()
        
        # Se retornou None, o usuário digitou 'fim'
        if nota is None:
            break
        
        # Adiciona a nota válida à lista
        notas.append(nota)
        print(f"✅ Nota {nota} registrada! Total de notas: {len(notas)}")
    
    # Exibe os resultados finais
    print("\n" + "=" * 50)
    print("📊 RELATÓRIO FINAL DA TURMA")
    print("=" * 50)
    
    if len(notas) == 0:
        print("❌ Nenhuma nota foi registrada.")
    else:
        print(f"📝 Total de notas registradas: {len(notas)}")
        print(f"📋 Notas: {', '.join(map(str, notas))}")
        
        media = calcular_media(notas)
        print(f"📈 Média da turma: {media:.2f}")
        
        # Classificação da média
        if media >= 9:
            print("🏆 Excelente desempenho da turma!")
        elif media >= 7:
            print("👍 Bom desempenho da turma!")
        elif media >= 5:
            print("⚠️ Desempenho regular da turma.")
        else:
            print("📉 A turma precisa de mais atenção.")
    
    print("=" * 50)
    print("Programa encerrado. Obrigado por usar o sistema!")

if __name__ == "__main__":
    main()

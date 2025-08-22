"""

Calculadora da Média


Faça um programa que leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". 

Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".
 No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). 

Para estes dois casos
(aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media
final: " seguido da média final para esse aluno.


Entrada: A entrada contém quatro números de ponto flutuante correspondentes às notas dos alunos.


Saída: Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema.

"""

# Calculadora da Média - Sistema de Avaliação de Alunos

def main():
    # Leitura das quatro notas
    print("Digite as quatro notas do aluno:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))
    
    # Cálculo da média ponderada (pesos: 2, 3, 4, 1)
    media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)
    
    # Exibir a média com uma casa decimal
    print(f"Media: {media:.1f}")
    
    # Verificar situação do aluno
    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else:  # média entre 5.0 e 6.9 (inclusive)
        print("Aluno em exame.")
        
        # Ler nota do exame
        nota_exame = float(input("Digite a nota do exame: "))
        print(f"Nota do exame: {nota_exame:.1f}")
        
        # Recalcular média final
        media_final = (media + nota_exame) / 2
        
        # Verificar aprovação após exame
        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        
        # Exibir média final
        print(f"Media final: {media_final:.1f}")

if __name__ == "__main__":
    main()

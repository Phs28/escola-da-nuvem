"""
Área da circunferência


A fórmula para calcular a área de uma circunferência é: área = π ×raio2.
 Considerando para
este problema que π = 3.14159265: 

• Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), 
no caso, a variável
raio.
Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo
abaixo, com 4 casas após o ponto decimal.

"""

# Programa para calcular a área de uma circunferência
# Fórmula: área = π × raio²
# π = 3.14159265

# Lê o valor do raio
raio = float(input())

# Define o valor de π
pi = 3.14159265

# Calcula a área da circunferência
area = pi * (raio ** 2)

# Exibe o resultado com 4 casas decimais
print(f"A={area:.4f}")

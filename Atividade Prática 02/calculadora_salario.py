# Calculadora de Salário por Horas Trabalhadas
# Lê dados do funcionário e calcula o salário baseado nas horas trabalhadas

# Leitura dos dados de entrada
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Saída formatada conforme especificação
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salario:.2f}")

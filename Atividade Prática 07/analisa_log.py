import re
import statistics

# Nome do arquivo de log
arquivo = "treinamento.log"

tempos = []

with open(arquivo, "r") as f:
    for linha in f:
        # procura um número seguido de 's' (segundos)
        match = re.search(r"tempo:\s*([\d.]+)s", linha)
        if match:
            tempos.append(float(match.group(1)))

if tempos:
    media = statistics.mean(tempos)
    desvio = statistics.pstdev(tempos)  # desvio padrão populacional
    print(f"Média do tempo de execução: {media:.2f}s")
    print(f"Desvio padrão: {desvio:.2f}s")
else:
    print("Nenhum tempo de execução encontrado no log.")

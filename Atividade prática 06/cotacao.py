import requests
from datetime import datetime

def consultar_cotacao():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # dispara erro se a requisição falhar
        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("⚠️ Moeda não encontrada. Verifique o código e tente novamente.")
            return

        cotacao = dados[chave]

        valor_atual = float(cotacao["bid"])
        valor_maximo = float(cotacao["high"])
        valor_minimo = float(cotacao["low"])
        atualizacao = datetime.fromtimestamp(int(cotacao["timestamp"]))

        print(f"\n💰 Cotação {moeda}/BRL")
        print(f"➡️ Valor atual: R$ {valor_atual:.2f}")
        print(f"📈 Máximo: R$ {valor_maximo:.2f}")
        print(f"📉 Mínimo: R$ {valor_minimo:.2f}")
        print(f"⏰ Última atualização: {atualizacao.strftime('%d/%m/%Y %H:%M:%S')}")

    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a API:", e)

if __name__ == "__main__":
    consultar_cotacao()

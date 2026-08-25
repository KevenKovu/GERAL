def escarquivo(dados, narquivo):
    with open(narquivo, 'w') as arquivo:
        for produto in dados:
            arquivo.write(f"{produto['cod']} {produto['nome']} {produto['quantidade']}\n")

def ler_dados_arquivo(narquivo):
    try:
        with open(narquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            dados = [{'cod': linha.split(' ')[0], 'nome': linha.split(' ')[1], 'quantidade': float(linha.split(' ')[2])} for linha in linhas]
        return dados
    
    except FileNotFoundError:
        print(f"Arquivo '{narquivo}' não encontrado.")
        return None

def main():
    narquivo = 'text.txt'

    infsupermercado = [
        {'cod': 1 ,'nome': 'Arroz', 'quantidade': 3},
        {'cod': 2 ,'nome': 'Feijao', 'quantidade': 4},
        {'cod': 3 ,'nome': 'Sal', 'quantidade': 2},
        {'cod': 4 ,'nome': 'Acucar', 'quantidade': 7},
        {'cod': 5 ,'nome': 'Leite', 'quantidade': 5},
        {'cod': 6 ,'nome': 'Macarrao', 'quantidade': 10},
    ]

    escarquivo(infsupermercado, narquivo)
    dados_lidos = ler_dados_arquivo(narquivo)

    if dados_lidos is not None:
        print("Dados lidos do arquivo:")
        for produto in dados_lidos:
            print(f"Codigo: {produto['cod']}, Nome: {produto['nome']},  Quantidade : {produto['quantidade']}")

if __name__ == "__main__":
    main()
    
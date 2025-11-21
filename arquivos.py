import csv
import json
import pandas as pd

# ================================
# 11. Contar linhas e palavras de dados.txt
# ================================
def contar_linhas_palavras(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        total_linhas = len(linhas)
        total_palavras = sum(len(linha.split()) for linha in linhas)

        print(f"\nArquivo: {arquivo}")
        print(f"Total de linhas: {total_linhas}")
        print(f"Total de palavras: {total_palavras}")

    except FileNotFoundError:
        print(f"Erro: arquivo '{arquivo}' não encontrado.")


# ================================
# 12. Soma e média de numeros.txt → resumo.txt
# ================================
def soma_media_numeros():
    try:
        with open("numeros.txt", "r", encoding="utf-8") as f:
            numeros = [float(linha.strip()) for linha in f]

        soma = sum(numeros)
        media = soma / len(numeros)

        with open("resumo.txt", "w", encoding="utf-8") as f:
            f.write(f"Soma: {soma}\n")
            f.write(f"Média: {media}")

        print("\nArquivo 'resumo.txt' criado com sucesso!")
        print(f"Soma = {soma}, Média = {media}")

    except FileNotFoundError:
        print("Erro: 'numeros.txt' não encontrado.")


# ================================
# 13. Filtrar aprovados.csv (nota >= 7)
# ================================
def gerar_aprovados():
    try:
        with open("tabela.csv", "r", encoding="utf-8") as f_in:
            leitor = csv.DictReader(f_in)

            with open("aprovados.csv", "w", newline="", encoding="utf-8") as f_out:
                campos = ["id", "nome", "nota"]
                escritor = csv.DictWriter(f_out, fieldnames=campos)
                escritor.writeheader()

                for linha in leitor:
                    if float(linha["nota"]) >= 7:
                        escritor.writerow(linha)

        print("\nArquivo 'aprovados.csv' gerado com sucesso!")

    except FileNotFoundError:
        print("Erro: 'tabela.csv' não encontrado.")


# ================================
# 14. Ler JSON config.json e validar campos
# ================================
def ler_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            dados = json.load(f)

        print("\n=== CONFIGURAÇÃO ===")
        print("Nome:", dados.get("nome", "Não encontrado"))
        print("Parâmetros:", dados.get("parametros", "Não encontrado"))

        if "versao" in dados:
            print("Versão:", dados["versao"])
        else:
            print("Erro: campo 'versao' não existe no JSON.")

    except FileNotFoundError:
        print("Erro: 'config.json' não encontrado.")


# ================================
# 15. Pandas: média da coluna e normalização
# ================================
def normalizar_csv():
    try:
        df = pd.read_csv("dados.csv")

        if "valor" not in df.columns:
            print("Erro: coluna 'valor' não existe no arquivo dados.csv")
            return

        media = df["valor"].mean()
        df["valor_normalizado"] = df["valor"] / media

        df.to_csv("dados_com_media.csv", index=False)
        print("\nArquivo 'dados_com_media.csv' criado com sucesso!")
        print(f"Média da coluna valor = {media}")

    except FileNotFoundError:
        print("Erro: 'dados.csv' não encontrado.")


# ================================
# Execução dos exercícios
# ================================
if __name__ == "__main__":
    print("\n===== PARTE 2 – MANIPULAÇÃO DE ARQUIVOS =====\n")

    # 11
    contar_linhas_palavras("dados.txt")

    # 12
    soma_media_numeros()

    # 13
    gerar_aprovados()

    # 14
    ler_config()

    # 15
    normalizar_csv()

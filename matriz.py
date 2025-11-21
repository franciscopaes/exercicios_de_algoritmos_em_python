import numpy as np
import csv

# ================================
# 1. Criar matriz 3x3 sem NumPy
# ================================
def criar_matriz_3x3():
    matriz = []
    print("\n=== MATRIZ 3x3 ===")
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o valor para [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    print("\nMatriz formatada:")
    for linha in matriz:
        print(" ".join(map(str, linha)))
    return matriz


# ================================
# 2. Soma dos elementos da matriz
# ================================
def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        for valor in linha:
            soma += valor
    return soma


# ================================
# 3. Diagonal principal + soma
# ================================
def diagonal_principal(matriz):
    diagonal = []
    for i in range(3):
        diagonal.append(matriz[i][i])
    return diagonal, sum(diagonal)


# ================================
# 4. Matriz identidade 4x4 sem NumPy
# ================================
def identidade_4x4():
    ident = []
    for i in range(4):
        linha = []
        for j in range(4):
            linha.append(1 if i == j else 0)
        ident.append(linha)
    return ident


# ================================
# 5. Transposta de matriz 2x3 → 3x2
# ================================
def transposta_2x3():
    matriz = []
    print("\nDigite os valores da matriz 2x3:")
    for i in range(2):
        linha = []
        for j in range(3):
            valor = int(input(f"M[{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    transposta = [[matriz[j][i] for j in range(2)] for i in range(3)]
    return matriz, transposta


# ================================
# 6. Operações com NumPy
# ================================
def operacoes_numpy():
    A = np.random.randint(1, 11, (2, 2))
    B = np.random.randint(1, 11, (2, 2))

    print("\nMatriz A:\n", A)
    print("Matriz B:\n", B)

    print("\nSoma:\n", A + B)
    print("Multiplicação matricial:\n", A @ B)
    print("Transposta A:\n", A.T)
    print("Transposta B:\n", B.T)


# ================================
# 7. Determinante de matriz 3x3
# ================================
def determinante_3x3():
    print("\nDigite os valores da matriz 3x3:")
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = float(input(f"M[{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    matriz_np = np.array(matriz)
    print("\nDeterminante =", np.linalg.det(matriz_np))


# ================================
# 8. Resolver sistema linear
# ================================
def resolver_sistema():
    A = np.array([[2, 1],
                  [1, -1]])
    B = np.array([5, 1])

    solucao = np.linalg.solve(A, B)
    print("\nSistema:")
    print("2x + y = 5")
    print("x - y = 1")
    print("Solução (x, y) =", solucao)


# ================================
# 9. Vetores: produto escalar e norma
# ================================
def vetores_numpy():
    v1 = list(map(float, input("\nDigite o vetor 1 separado por espaços: ").split()))
    v2 = list(map(float, input("Digite o vetor 2 separado por espaços: ").split()))

    v1 = np.array(v1)
    v2 = np.array(v2)

    print("\nProduto escalar =", np.dot(v1, v2))
    print("Norma do vetor 1 =", np.linalg.norm(v1))
    print("Norma do vetor 2 =", np.linalg.norm(v2))


# ================================
# 10. Regressão linear (a*x + b)
# ================================
def regressao_linear_csv(caminho):
    xs = []
    ys = []

    with open(caminho, "r", newline="") as file:
        leitor = csv.reader(file)
        next(leitor)  # pular cabeçalho
        for linha in leitor:
            xs.append(float(linha[0]))
            ys.append(float(linha[1]))

    x = np.array(xs)
    y = np.array(ys)

    n = len(x)
    a = (n * (x*y).sum() - x.sum() * y.sum()) / (n * (x**2).sum() - (x.sum() ** 2))
    b = (y.sum() - a * x.sum()) / n

    print("\nRegressão linear:")
    print(f"y = {a:.4f} * x + {b:.4f}")


# ================================
# Execução dos exercícios
# ================================
if __name__ == "__main__":
    print("\n============= PARTE 1 =============\n")

    matriz = criar_matriz_3x3()
    print("\nSoma da matriz =", soma_matriz(matriz))

    diag, soma_diag = diagonal_principal(matriz)
    print("\nDiagonal principal:", diag)
    print("Soma da diagonal =", soma_diag)

    print("\nMatriz identidade 4x4:")
    for l in identidade_4x4():
        print(l)

    mat23, trans = transposta_2x3()
    print("\nMatriz 2x3:", mat23)
    print("Transposta 3x2:", trans)

    operacoes_numpy()
    determinante_3x3()
    resolver_sistema()
    vetores_numpy()
    regressao_linear_csv("dados.csv")



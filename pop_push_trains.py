import sys
input = sys.stdin.read

def pode_reorganizar_vagoes(N, permutacao):
    pilha = []
    indice = 0  # índice para percorrer a permutação desejada
    
    # Processa cada vagão que chega na ordem crescente
    for vagao in range(1, N + 1):
        pilha.append(vagao)  # Empilha o vagão
        # Tenta retirar da pilha se coincidir com a permutação desejada
        while pilha and pilha[-1] == permutacao[indice]:
            pilha.pop()  # Desempilha o vagão
            indice += 1  # Avança para o próximo vagão na permutação
    
    # Se conseguimos esvaziar a pilha, a permutação é possível
    return indice == N

def main():
    dados = input().strip().splitlines()
    i = 0
    
    resultado = []
    while True:
        N = int(dados[i])
        i += 1
        if N == 0:
            break
        
        bloco_resultado = []
        while True:
            linha = dados[i]
            i += 1
            permutacao = list(map(int, linha.split()))
            if permutacao[0] == 0:
                break
            
            if pode_reorganizar_vagoes(N, permutacao):
                bloco_resultado.append("Yes")
            else:
                bloco_resultado.append("No")
        
        resultado.extend(bloco_resultado)
        resultado.append("")  # Linha em branco entre blocos
    
    # Exibe o resultado com blocos separados por linhas em branco
    print("\n".join(resultado))

if __name__ == "__main__":
    main()

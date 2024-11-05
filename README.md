# Reorganização de Vagões na Estação PopPush

## Descrição

Este programa resolve o problema de reorganização de vagões em uma estação de trem fictícia chamada PopPush. A estação possui uma pista única para receber e reorganizar os vagões, que chegam em ordem crescente. O objetivo é verificar se é possível reorganizar esses vagões para que eles saiam na ordem desejada.

Cada vagão que entra na estação pode sair apenas na direção da saída (direção B) e não pode voltar à direção de entrada (direção A). O programa utiliza uma estrutura de pilha para simular a entrada e saída dos vagões e determinar se a ordem de saída desejada é possível.

## Entrada

O programa lê múltiplos blocos de entrada. Cada bloco é estruturado da seguinte forma:

1. A primeira linha de cada bloco contém um número inteiro `N` (1 ≤ N ≤ 1000), indicando a quantidade de vagões.
2. As próximas `N` linhas contêm uma permutação dos valores `1` até `N`, que representam as ordens desejadas de saída dos vagões.
3. A última linha de cada bloco contém um `0`, que sinaliza o término das permutações para aquele conjunto de vagões.

A entrada termina com uma linha contendo apenas `0`, o que indica o fim dos dados de entrada.

### Exemplo de Entrada
```plaintext
5
5 4 3 2 1
1 2 3 4 5
2 1 5 4 3
0
3
3 1 2
0
0
```

## Saída

Para cada permutação de vagões, o programa imprime `Yes` se for possível obter a ordem desejada usando a estrutura da estação, ou `No` caso contrário. Após cada bloco de permutações, o programa imprime uma linha em branco.

### Exemplo de Saída
```plaintext
Yes
Yes
No

No

```

## Estratégia de Solução

1. **Pilha para Gerenciar Ordem de Saída**: Uma pilha é usada para simular a entrada e saída dos vagões na estação.
2. **Simulação da Entrada e Saída**:
   - O programa empilha os vagões em ordem crescente até que o próximo vagão a ser empilhado corresponda ao vagão desejado na ordem de saída.
   - Quando há uma correspondência, o vagão é removido da pilha, e o programa avança para o próximo vagão da sequência de saída.
3. **Verificação de Possibilidade**: Se for possível esvaziar a pilha em uma sequência que atenda à ordem de saída desejada, a resposta é `Yes`; caso contrário, é `No`.

## Exemplo de Execução

Dado o seguinte bloco de entrada:
```plaintext
5
5 4 3 2 1
1 2 3 4 5
2 1 5 4 3
0
```

O programa processará cada permutação:

1. Para a permutação `5 4 3 2 1`, os vagões podem ser reorganizados na ordem inversa de entrada, portanto, a saída é `Yes`.
2. Para a permutação `1 2 3 4 5`, os vagões já estão na ordem correta, então a saída é `Yes`.
3. Para a permutação `2 1 5 4 3`, não é possível reorganizar os vagões para atender à ordem desejada, resultando em `No`.

## Como Executar

1. Certifique-se de que o arquivo de código (`pop_push_trains.py`) está salvo em seu diretório de trabalho.
2. Execute o programa com Python 3.11:
   ```bash
   python3.11 pop_push_trains.py
   ```
3. Insira as entradas conforme o formato descrito e observe as saídas.

## Dependências

- Python 3.11 ou superior

# Red-Black Tree & AVL Tree

Este projeto implementa tanto uma **Árvore Red-Black** (Árvore Rubro-Negra) quanto uma **Árvore AVL**, ambas são estruturas de dados auto-balanceadas usadas para armazenar dados de maneira eficiente, garantindo operações de busca, inserção e remoção com tempo de execução O(log n). As implementações foram feitas em Python e utilizam a biblioteca `matplotlib` para desenhar as árvores visualmente.

## Estrutura de Dados

### Árvore Red-Black

A árvore Red-Black é um tipo especial de árvore binária de busca com as seguintes propriedades:

1. **Cada nó é vermelho ou preto**.
2. **A raiz é preta**.
3. **Nódos vermelhos não podem ter filhos vermelhos**.
4. **Todos os caminhos de qualquer nó para suas folhas têm o mesmo número de nós pretos**.

### Árvore AVL

A árvore AVL (Adelson-Velsky and Landis) é uma árvore binária de busca balanceada, onde a diferença de altura entre as subárvores esquerda e direita de qualquer nó é no máximo 1. Isso garante que todas as operações (inserção, remoção, busca) tenham tempo de execução O(log n).

## Funcionalidades

- **Inserção de nós**: Adiciona novos nós na árvore, balanceando automaticamente a estrutura quando necessário.
- **Remoção de nós**: Remove nós da árvore, mantendo as propriedades da Red-Black Tree ou AVL Tree.
- **Busca**: Permite buscar um nó na árvore com um valor específico.
- **Visualização**: Utiliza o `matplotlib` para desenhar as árvores visualmente, com nós vermelhos e pretos (para a Red-Black Tree) ou com o equilíbrio de altura (para a AVL Tree).

## Como Usar

### Pré-requisitos

Para rodar o projeto, é necessário ter o Python instalado. Além disso, a biblioteca `matplotlib` deve estar instalada. Para instalar as dependências, execute:

```bash
pip install matplotlib

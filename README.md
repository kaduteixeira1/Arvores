# Red-Black Tree

Este projeto implementa uma árvore Red-Black (Árvore Rubro-Negra), uma estrutura de dados auto-balanceada usada para armazenar dados de maneira eficiente, garantindo operações de busca, inserção e remoção com tempo de execução O(log n). A implementação foi feita em Python e utiliza a biblioteca `matplotlib` para desenhar a árvore visualmente.

## Funcionalidades

- **Inserção de nós**: Adiciona novos nós na árvore, balanceando automaticamente a estrutura quando necessário.
- **Remoção de nós**: Remove nós da árvore, mantendo as propriedades da Red-Black Tree.
- **Busca**: Permite buscar um nó na árvore com um valor específico.
- **Visualização**: Utiliza o `matplotlib` para desenhar a árvore visualmente, com nós vermelhos e pretos, e as conexões entre eles.

## Estrutura de Dados

A árvore Red-Black é um tipo especial de árvore binária de busca com as seguintes propriedades:

1. **Cada nó é vermelho ou preto**.
2. **A raiz é preta**.
3. **Nódos vermelhos não podem ter filhos vermelhos**.
4. **Todos os caminhos de qualquer nó para suas folhas têm o mesmo número de nós pretos**.

## Como Usar

### Pré-requisitos

Para rodar o projeto, é necessário ter o Python instalado. Além disso, a biblioteca `matplotlib` deve estar instalada. Para instalar as dependências, execute:

```bash
pip install matplotlib

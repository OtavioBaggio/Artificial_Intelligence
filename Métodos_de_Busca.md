# Métodos de Busca

## 1. Busca Cega (Força Bruta)

Busca sem informação adicional sobre o problema.

### 1.1 Busca em Profundidade (Depth-First Search - DFS)

- Tipo: **Dedutivo**
- Estrutura utilizada: **Pilha**
  - Normalmente implementada com **recursão (pilha do S.O.)**
- Controle de estados:
  - **Lista de visitados**

### 1.2 Busca em Largura / Amplitude (Breadth-First Search - BFS)

Utilizada principalmente em **árvores completas**.

- Estrutura utilizada: **Fila**
- Controle de estados:
  - **Lista de visitados**

---

# Busca Heurística

Heurísticas utilizam **informação adicional ("dicas")** para guiar a busca.

> Heurística ≈ Informação ≈ "Dica"

## Métodos Heurísticos

Todos os métodos abaixo utilizam **lista de visitados**.

### 1. Subida de Encosta / Montanha (Hill Climbing)

- Estratégia: **Busca em profundidade**
- Estrutura: **Pilha recursiva**
- Função de custo:
  - **Custo real → g(n)**

---

### 2. Busca Gulosa (Greedy Search)

- Estratégia: **Busca em largura / amplitude**
- Estrutura: **Fila**
- Função de custo:
  - **Custo estimado / heurístico → h(n)**

---

### 3. A* (A Estrela)

- Estratégia: **Busca em largura / amplitude**
- Estrutura: **Fila**

Combina dois tipos de custo:

- **Custo real acumulado → g(n)**
- **Custo estimado heurístico → h(n)**

Função de avaliação:

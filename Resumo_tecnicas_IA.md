# 🧠 Resumo Teórico — Técnicas de Inteligência Artificial

## 📌 Problemas que a IA resolve

- **Problemas de diagnóstico**
  - Objetivo: reconhecer padrões
  - Exemplo: detecção de doenças, reconhecimento de imagens

- **Problemas sem caminho explícito até a solução**
  - Não se sabe exatamente como chegar no estado final
  - Exemplo: problemas de "empacotamento", jogos, planejamento

---

## 🤖 Sistemas de Comportamento Inteligente

As técnicas de IA são usadas para gerar sistemas capazes de simular inteligência:

- **Base de Conhecimento**
  - Conjunto de fatos e regras sobre o domínio

- **Motores de Raciocínio**
  - Responsáveis por inferir novos conhecimentos

### 🔍 Tipos de raciocínio

- **Dedução**
  - Parte de regras gerais para chegar a conclusões específicas

- **Indução**
  - Aprende padrões a partir de exemplos

---

## 🔎 Algoritmos de Busca

Utilizados para encontrar soluções em espaços de estados.

### 🔹 Busca Não Informada (Cega / Força Bruta)

Não utiliza conhecimento adicional sobre o problema.

- **Busca em Profundidade (DFS - Depth-First Search)**
  - Estrutura: **Pilha (Stack)**
  - Vai fundo antes de explorar outros caminhos

- **Busca em Largura (BFS - Breadth-First Search)**
  - Estrutura: **Fila (Queue)**
  - Explora todos os nós de um nível antes de avançar

---

### 🔹 Busca Informada (Heurística)

Utiliza conhecimento do problema para melhorar a eficiência.

#### 📊 Custos

- **Custo Real → g(n)**
  - Custo acumulado até o nó atual

- **Custo Heurístico → h(n)**
  - Estimativa do custo até o objetivo
  - Pode ser:
    - **Admissível**: nunca superestima o custo real
    - **Inadmissível**: pode superestimar

---

## ⚙️ Métodos Heurísticos

- **Subida de Encosta (Hill Climbing)**
  - Baseado em profundidade
  - Foca no custo real
  - Pode ficar preso em máximos locais

- **Busca Gulosa (Greedy)**
  - Baseada em largura
  - Foca apenas no custo heurístico `h(n)`
  - Rápida, mas nem sempre encontra a melhor solução

- **A\***
  - Combina custo real e heurístico:
  
    ```
    f(n) = g(n) + h(n)
    ```
  
  - Completo e ótimo (se a heurística for admissível)
  - Corrige limitações da busca gulosa

---

## 🎯 Métodos de Busca — Objetivo

Resolver problemas através de:

- Gerar ou atingir **estado(s) desejado(s)**
- Construir um **passo a passo** até a solução
- Explorar o espaço de estados de forma eficiente

---

## 📚 Observações Extras

- Espaço de estados: conjunto de todas as possíveis configurações do problema
- Estado inicial: ponto de partida
- Estado objetivo: solução desejada
- Função de transição: define como ir de um estado para outro

---

## 🚀 Dica para Estudos 

- Entenda **quando usar cada tipo de busca**
- Praticar com problemas clássicos:
  - 8-puzzle
  - Labirintos
  - Problema das Torres de Hanoi

---

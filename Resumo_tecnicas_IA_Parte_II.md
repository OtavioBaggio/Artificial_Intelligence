# Resumo Teórico — Técnicas de Inteligência Artificial - Parte II
## Parte II: Busca Heurística, Modelagem e Paradigmas de Programação

---

## 1. Métodos de Busca Heurística

A busca heurística utiliza informações sobre o domínio do problema para guiar a exploração de estados, tornando-a mais eficiente do que a busca cega.

### Tipos de Custo

| Tipo de Custo | Algoritmos |
|---|---|
| **Real** (custo já percorrido) | Subida de Encosta, A* |
| **Estimado** (heurística h(n)) | Busca Gulosa, A* |

> O **A\*** combina os dois: `f(n) = g(n) + h(n)`, onde `g(n)` é o custo real acumulado e `h(n)` é a estimativa até a meta. Isso o torna **ótimo** (se a heurística for admissível) e **completo**.

- **Subida de Encosta (Hill Climbing):** move-se sempre para o vizinho com melhor avaliação. Pode ficar preso em ótimos locais.
- **Busca Gulosa:** expande sempre o nó mais próximo da meta segundo a heurística. Rápida, mas não garante solução ótima.

---

## 2. Métodos de Busca em Geral

### 2.1 Gerar e Testar

O ciclo fundamental de qualquer busca:

1. **Gerar** um novo estado clonado a partir do estado atual
2. **Testar** o estado gerado:
   - `ehValido()` — respeita as restrições do problema?
   - `visitado()` — já foi explorado antes?
   - `ehMeta()` — é o estado objetivo?

### 2.2 Modelagem de Problemas

| Conceito | Implementação |
|---|---|
| **Estados** | Estruturas de dados (atributos/variáveis) |
| **Regras de Transição** | Métodos que geram novos estados |
| **Estrutura de Visitados** | Listas ou `HashMaps` |
| **Função Meta/Objetivo** | Método que verifica se o estado é solução |

### 2.3 Clonagem de Objetos

Em linguagens orientadas a objetos, variáveis guardam **referências** (endereços de memória), não cópias. Por isso, ao gerar novos estados, é essencial **clonar** os objetos:

```java
Aluno aTmp = a.clone();
Aluno bTmp = b.clone();
metodo(aTmp, bTmp);
```

Sem o `clone()`, modificar `aTmp` modificaria o objeto original `a`, corrompendo a busca.

---

## 3. Sistemas de Comportamento Inteligente

Um sistema inteligente é composto por três pilares:

```
┌─────────────────────────────────────────┐
│     SISTEMA DE COMPORTAMENTO            │
│           INTELIGENTE                   │
├───────────────┬─────────────┬───────────┤
│  Base de      │  Motor de   │Aprendizado│
│Conhecimento   │ Raciocínio  │de Máquina │
│               │             │           │
│ Representar   │ Métodos de  │  ML / IA  │
│ e raciocinar  │   busca     │ simbólica │
└───────────────┴─────────────┴───────────┘
```

O principal desafio da **base de conhecimento** é *representar* o conhecimento de forma que o motor possa raciocinar sobre ele.

---

## 4. Paradigmas de Programação

Paradigmas definem **como** o programador expressa soluções. A diferença central está em *o que* o programador especifica e *o que* fica implícito para o sistema.

### 4.1 Imperativo

> "Diga ao computador **o quê**, **como** e **quando** fazer."

O programador descreve o passo a passo exato da execução. O fluxo de controle é explícito (loops, condicionais, sequência).

- **Exemplos:** C, Java, Python (uso comum), Pascal
- **Característica:** Controle total sobre o estado da memória e a ordem de execução.

```java
// Exemplo imperativo: soma de uma lista
int soma = 0;
for (int x : lista) {
    soma += x;
}
```

### 4.2 Lógico

> "Diga ao computador **o quê** e **quando** — ele descobre o **como**."

O programador define **fatos** e **regras** (o conhecimento do domínio). O motor de inferência (mecanismo de busca interno) decide como derivar conclusões — geralmente via *backtracking* (retrocesso).

- **Exemplo principal:** Prolog
- **Característica:** Declarativo em relação ao processo. Ideal para problemas de IA simbólica, planejamento e parsing.
- **Base:** Lógica de primeira ordem (predicados, variáveis, quantificadores).

```prolog
% O programador declara o que é verdade:
pai(joao, maria).
pai(joao, pedro).

% E o que pode ser inferido:
irmao(X, Y) :- pai(P, X), pai(P, Y), X \= Y.

% O motor responde: irmao(maria, pedro)? -> true
```

### 4.3 Funcional

> "Diga ao computador **o quê** e **quando** — via composição de funções."

O programa é uma composição de funções matemáticas puras (sem efeitos colaterais, sem estado mutável). A execução é guiada pela **avaliação de expressões**, não pela sequência de instruções.

- **Exemplos:** Haskell, Erlang, Clojure, Scala; elementos funcionais em Python, Java e Kotlin.
- **Característica:** Alta previsibilidade (mesma entrada → mesma saída sempre), facilidade de paralelização, sem efeitos colaterais.

```haskell
-- Exemplo funcional: soma de uma lista
soma [] = 0
soma (x:xs) = x + soma xs
```

### 4.4 Comparativo

| Paradigma | O Quê | Como | Quando | Exemplo |
|---|---|---|---|---|
| **Imperativo** | ✅ | ✅ (explícito) | ✅ (explícito) | Java, C, Python |
| **Lógico** | ✅ | ❌ (inferido) | ✅ (consulta) | Prolog |
| **Funcional** | ✅ | ❌ (composto) | ✅ (avaliação) | Haskell |

---

## 5. Prolog — Paradigma Lógico em Detalhe

Prolog (Programming in Logic) opera sobre **lógica de primeira ordem**. Toda a "programação" consiste em popular uma base de conhecimento com fatos e regras, e depois fazer consultas.

### 5.1 Elementos de uma Sentença

| Elemento | Característica | Exemplos |
|---|---|---|
| **Átomo/Objeto** | Começa com minúsculo | `zeno`, `mamifero`, `poa` |
| **Literal (String)** | Entre aspas | `"Zeno"`, `"Golfinho"` |
| **Variável** | Começa com Maiúsculo | `X`, `Pai`, `NomeCompleto` |

> ⚠️ Variáveis em Prolog **não têm tipo** e **não são instanciadas** antes da unificação. Elas são preenchidas pelo mecanismo de busca.

### 5.2 Fatos

Verdades incontestáveis na base de conhecimento. Terminam com `.`

```prolog
progenitor(zeno, jurandir).
% zeno tem relação de progenitor com jurandir

disciplina(alex, ia, cc, 2026).
% alex leciona IA no curso de CC em 2026

eh(vaca, mamifero, terrestre).

jogos(counterStrike, fps, 18).
```

### 5.3 Regras

Hipóteses: verdades condicionais usando `:-` ("se"). Usam variáveis e podem chamar outros predicados.

```prolog
% Família
progenitor(george, germano).
progenitor(george, regina).
progenitor(zeno, ivete).
progenitor(zeno, alex).
progenitor(zeno, jurandir).
progenitor(zeno, abilio).

% A e B são irmãos se têm o mesmo pai e são distintos
irmaos(A, B) :-
    progenitor(Pai, A),
    progenitor(Pai, B),
    A \= B.

% A e B são primos se seus pais são irmãos
primos(A, B) :-
    irmaos(PA, PB),
    progenitor(PA, A),
    progenitor(PB, B).

% T é tio de S se é irmão do progenitor de S
tio(T, S) :-
    progenitor(P, S),
    irmaos(P, T).
```

### 5.4 Busca em Grafos com Prolog

Prolog é naturalmente adequado para busca em grafos, pois seu mecanismo de backtracking explora caminhos automaticamente.

```prolog
% Grafo de cidades (arestas)
conecta(sm, itaara).
conecta(itaara, jc).
conecta(jc, ca).
conecta(ca, sol).
conecta(sol, poa).

% Caso base: origem e destino são diretamente conectados
caminho(O, D) :-
    conecta(O, D).

% Caso recursivo: vai de O até D passando por um intermediário I
caminho(O, D) :-
    conecta(O, I),
    caminho(I, D).
```

> **Exemplo de consulta:** `caminho(sm, poa).` → Prolog faz backtracking e encontra `sm → itaara → jc → ca → sol → poa`.

> ⚠️ Sem controle de visitados, grafos com ciclos podem causar **loop infinito**. Para grafos com ciclos, é necessário manter uma lista de nós visitados como argumento adicional.

---

## Referências Rápidas

- **A\*:** `f(n) = g(n) + h(n)` — combina custo real e heurística
- **Prolog:** base de conhecimento = fatos + regras; execução = backtracking
- **Clone:** sempre clonar objetos ao gerar novos estados em buscas OO
- **Paradigmas:** imperativo (como fazer), lógico (o que é verdade), funcional (o que computar)

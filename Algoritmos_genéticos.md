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

---

### 2.2 Modelagem de Problemas

| Conceito | Implementação |
|---|---|
| **Estados** | Estruturas de dados (atributos/variáveis) |
| **Regras de Transição** | Métodos que geram novos estados |
| **Estrutura de Visitados** | Listas ou `HashMaps` |
| **Função Meta/Objetivo** | Método que verifica se o estado é solução |

---

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
 
| Base de Conhecimento | Motor de Raciocínio | Aprendizado de Máquina |
|---|---|---|
| Representar e raciocinar | Métodos de busca | ML / IA simbólica |
 
O principal desafio da base de conhecimento é representar o conhecimento de forma que o motor possa raciocinar sobre ele.
 
---
 
## 4. Paradigmas de Programação
 
Paradigmas definem como o programador expressa soluções.
 
### 4.1 Imperativo
 
> "Diga ao computador o quê, como e quando fazer."
 
```java
int soma = 0;
for (int x : lista) {
    soma += x;
}
```
 
### 4.2 Lógico
 
> "Diga ao computador o quê e quando — ele descobre o como."
 
```prolog
pai(joao, maria).
irmao(X, Y) :- pai(P, X), pai(P, Y), X \= Y.
```
 
### 4.3 Funcional
 
> "Diga ao computador o quê via composição de funções."
 
```haskell
soma [] = 0
soma (x:xs) = x + soma xs
```
 
### 4.4 Comparativo
 
| Paradigma | O Quê | Como | Quando |
|---|---|---|---|
| Imperativo | ✅ | ✅ | ✅ |
| Lógico | ✅ | ❌ | ✅ |
| Funcional | ✅ | ❌ | ✅ |
 
---
 
## 5. Prolog — Paradigma Lógico
 
### 5.1 Elementos
 
| Elemento | Exemplo |
|---|---|
| Átomo | `zeno` |
| Variável | `X` |
| String | `"Zeno"` |
 
### 5.2 Fatos
 
```prolog
progenitor(zeno, jurandir).
```
 
### 5.3 Regras
 
```prolog
irmaos(A, B) :-
    progenitor(P, A),
    progenitor(P, B),
    A \= B.
```
 
### 5.4 Grafos
 
```prolog
caminho(O, D) :-
    conecta(O, I),
    caminho(I, D).
```
 
---
 
## 6. Algoritmos Genéticos (Busca Heurística Populacional)
 
Os Algoritmos Genéticos (AGs) são métodos de busca heurística inspirados na evolução natural.
 
Testam várias soluções ao mesmo tempo e evoluem ao longo das gerações.
 
### 6.1 Ideia Central
 
- Indivíduo = solução
- População = conjunto de soluções
- Evolução ao longo de gerações
### 6.2 Componentes
 
| Componente | Função |
|---|---|
| População | Soluções |
| Fitness | Qualidade |
| Seleção | Escolha |
| Cruzamento | Combinação |
| Mutação | Variação |
| Elitismo | Melhores sobrevivem |
 
### 6.3 Fitness
 
- Boa solução → fitness alto
- Solução ruim → fitness baixo
- Aproxima da solução → recompensa
- Viola restrição → penaliza
### 6.4 Processo
 
1. Gerar população
2. Avaliar fitness
3. Selecionar melhores
4. Cruzar e mutar
5. Repetir
### 6.5 Características
 
- Paralelismo
- Heurística dinâmica
- Não garante ótimo
- Boa para alta complexidade
### 6.6 Comparação
 
| Método | Estratégia |
|---|---|
| Hill Climbing | Local |
| A* | Caminho ótimo |
| Genético | Evolução |
 
### 6.7 Quando usar
 
- Problemas complexos
- Muitas restrições
- Espaço grande
 
A*	Caminho ótimo
Genético	Evolução
6.7 Quando usar
Problemas complexos
Muitas restrições
Espaço grande

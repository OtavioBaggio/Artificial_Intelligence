# Resumo Teórico — Sistemas Multiagentes (SMA) e JASON

## Parte I: Conceitos Fundamentais de Sistemas Multiagentes

---

## 1. Sistemas Multiagentes (SMA)

Os **Sistemas Multiagentes (SMA)** consistem em uma abordagem da Inteligência Artificial baseada na cooperação entre múltiplos agentes autônomos.

A ideia central é resolver problemas de forma coletiva, semelhante ao funcionamento de:

- Sociedades
- Comunidades
- Times
- Equipes

> Em vez de uma única entidade resolver tudo sozinha, vários agentes trabalham em conjunto para atingir objetivos.

---

## 2. Conceito de Agente

Um **agente** é uma entidade capaz de:

- Perceber o ambiente
- Raciocinar
- Planejar ações
- Executar ações

### Componentes de um Agente

| Componente | Função |
|---|---|
| Sensores | Perceber o ambiente |
| Crenças/Fatos | Conhecimento do agente |
| Regras/Planos | Definem comportamento |
| Planejamento | Escolha de ações |
| Atuadores | Executar ações |

---

## 3. Tipos de Agentes

### 3.1 Agente Reativo

O agente reativo atua diretamente com base nos estímulos recebidos do ambiente.

Fluxo básico:

```text
Perceber → Agir
```

Características:

- Não realiza raciocínio complexo
- Resposta rápida
- Comportamento simples
- Muito usado em simulações naturais

### Exemplo

- Colônias de formigas
- Enxames
- Robôs simples

> O comportamento coletivo emergente pode produzir soluções inteligentes mesmo com agentes simples.

---

### 3.2 Agente Cognitivo

O agente cognitivo possui capacidade de raciocínio e planejamento antes de agir.

Fluxo básico:

```text
Perceber → Raciocinar → Planejar → Agir
```

Características:

- Analisa diferentes possibilidades
- Possui objetivos internos
- Trabalha com tomada de decisão
- Mais sofisticado que agentes reativos

### Exemplo

- Assistentes inteligentes
- Sistemas especialistas
- IA de automação avançada

---

## 4. Aplicações dos Sistemas Multiagentes

Os SMA são utilizados em diversas áreas:

| Área | Aplicação |
|---|---|
| Aviação | Controle e coordenação |
| Automação | Sistemas industriais |
| Robótica | Cooperação entre robôs |
| Jogos | NPCs inteligentes |
| Redes | Sistemas distribuídos |
| Logística | Coordenação de entregas |

---

## 5. Paradigma Mental BDI

O modelo **BDI (Belief-Desire-Intention)** é um paradigma utilizado para representar o comportamento mental de agentes cognitivos.

| Elemento | Significado |
|---|---|
| **Belief** | Crenças/Fatos conhecidos |
| **Desire** | Desejos ou objetivos possíveis |
| **Intention** | Plano atualmente em execução |

---

### 5.1 Belief (Crenças)

Representa tudo que o agente acredita ser verdade.

Exemplos:

```text
porta_aberta
energia_baixa
usuario_logado
```

---

### 5.2 Desire (Desejos)

Representa objetivos que o agente gostaria de atingir.

Exemplos:

```text
fechar_porta
recarregar_bateria
enviar_mensagem
```

> Um desejo ainda não está necessariamente sendo executado.

---

### 5.3 Intention (Intenção)

É o plano que foi selecionado e está sendo executado.

Características:

- Ativado por eventos
- Possui contexto
- Define ações práticas

Exemplo:

```text
Se energia estiver baixa:
    → iniciar recarga
```

---

# Resumo Teórico — Framework JASON

## Parte II: Linguagem AgentSpeak e Framework JASON

---

## 6. JASON

O **JASON** é um framework utilizado para desenvolvimento de Sistemas Multiagentes.

Ele é baseado na linguagem **AgentSpeak**, inspirada no paradigma lógico do Prolog.

---

## 7. AgentSpeak

A linguagem AgentSpeak trabalha principalmente com:

| Elemento | Função |
|---|---|
| Fatos | Informações conhecidas |
| Regras | Relações lógicas |
| Planos | Comportamentos do agente |

---

### 7.1 Influência do Prolog

Assim como no Prolog, o conhecimento é baseado em lógica.

### Exemplo de fatos

```prolog
energia(baixa).
porta(fechada).
```

### Exemplo de regra

```prolog
precisa_recarregar :-
    energia(baixa).
```

---

## 8. Estrutura do Framework JASON

O framework oferece vários componentes para construção de SMA.

### Principais Recursos

| Recurso | Função |
|---|---|
| Interpretador AgentSpeak | Executa agentes |
| Simulador | Simula ambiente |
| Integração com Java | Comunicação externa |
| Gerenciamento de agentes | Coordenação do sistema |

---

## 9. Integração com Java

O JASON permite integração direta com Java.

Isso possibilita utilizar:

- Socket
- TCP/IP
- APIs externas
- Banco de dados
- Interfaces gráficas
- Sistemas distribuídos

> O Java geralmente é utilizado para implementar o ambiente e recursos externos.

---

## 10. Estrutura de um Projeto MAS (SMA)

Um projeto de Sistemas Multiagentes normalmente possui três partes principais.

---

### 10.1 Arquivo do Projeto (`.mas2j`)

Define a configuração geral do sistema.

### Responsabilidades

- Definir agentes
- Quantidade de agentes
- Protocolos de comunicação
- Arquitetura do sistema
- Ambiente utilizado

### Exemplo

```text
Projeto.mas2j
```

---

### 10.2 Arquivos `.asl`

Os arquivos `.asl` armazenam a lógica dos agentes.

### Contêm:

- Crenças
- Planos
- Objetivos
- Regras

### Exemplo

```asl
+!iniciar : true <- .print("Iniciando agente").
```

---

### 10.3 Ambiente (`Environment`)

O ambiente normalmente é implementado em Java.

Responsável por:

- Interação com o mundo externo
- Inserção de percepções
- Execução de ações

---

## 11. Métodos Principais do Ambiente

### 11.1 `init()`

Executado na inicialização do ambiente.

Pode:

- Adicionar percepções
- Configurar estados iniciais

### Exemplo

```java
addPercept();
removePercept();
```

---

### 11.2 `executeAction()`

Executado quando um agente solicita uma ação.

Responsável por:

- Processar ações
- Atualizar percepções
- Modificar ambiente

### Exemplo

```java
executeAction() {
    addPercept();
    removePercept();
}
```

---

## 12. Fluxo Geral de Funcionamento

O funcionamento básico de um SMA com JASON ocorre da seguinte forma:

```text
Ambiente → Sensores → Agente
Agente → Raciocínio → Plano
Plano → Ação → Ambiente
```

---

## 13. Resumo Geral

| Conceito | Ideia Principal |
|---|---|
| SMA | Cooperação entre agentes |
| Agente Reativo | Percebe e age |
| Agente Cognitivo | Percebe, raciocina e age |
| BDI | Modelo mental do agente |
| JASON | Framework para SMA |
| AgentSpeak | Linguagem lógica dos agentes |
| `.mas2j` | Configuração do projeto |
| `.asl` | Lógica dos agentes |
| Environment | Integração com ambiente |

---

## 14. Ideia Central

> Sistemas Multiagentes utilizam vários agentes autônomos cooperando entre si para resolver problemas complexos de forma distribuída e inteligente.

O agente reativo atua diretamente com base nos estímulos recebidos do ambiente.

Fluxo básico:

```text
Perceber → Agir

  # INTELIGENCIA ARTIFICIAL 

UNIDADE 1: método de busca
construir programas que apliquem os diferentes métodos de busca existentes em contextos reais da programação

UNIDADE 2: representação de conhecimento
aplicar as diferentes formas de representação de conhecimento e seus motores de raciocínio em problemas reais

UNIDADE 3: sistemas multiagentes
construir sistemas multi-agentes, aplicando os conceitos e práticas para que o sistema tenha comportamento inteligente e emergente

UNIDADE 4: redes neurais
contruir programas utilizando técnicas de Redes Neurais para reconhecimento de padrões em situações mais reais possíveis


IA:
  - Área de Ciência da Computação -> metodologia e técnicas/métodos
    - Projetar e Construir SISTEMA DE COMPORTAMENTO INTELIGENTE
      - BASE DE CONHECIMENTO (PROLOG; SMA; RNA):
          - Estruturada
              - Banco de Dados
          - Não Estruturada
              - fatos
              - regras
              - experiências
      - MOTORES DE RACIOCINIO (MÉTODOS DE BUSCA; SMA):
         - Dedução ou Indução
             - profundidade e largura (força bruta)
             - subida de encosta, guloso, A*, Algortimos Genéticos (heurísticas)
      - APRENDIZADO DE MÁQUINA OU RECONHECIMENTO DE PADRÕES POR AMOSTRAS (REDES NEURAIS ARTIFICIAIS - RNA)
          - Repetição e volume de amostras
          
  - Tipos de problemas adequados para IA:
      - Diagnostico - reconhecimento de padrões (substituir o especialista)
      - 'Empacotamento' - descobrir o estado final e/ou os passos até o estado final
   
MOTORES DE RACIOCÍNIO
    - algoritmos que buscam solução de problema
        - busca de força bruta (mais processamento e mais consumo de memória)
            - SEMPRE SE CHEGA NA SOLUÇÃO MELHOR
        - busca de heurística (menos processamento e menos consmo de memória)
            - NEM SEMPRE SE CHEGA NA SOLUÇÃO MELHOR (depende da heurística)
    - solucionar um problema com métodos de busca exige:
        - estados
        - regras de transição
        - restrições
        - visitados (lista ou hash)
        - função objetivo (saber se o sistema atingiu a solução)

jogou(avenida, 2, 0, interzinho).
jogou(santos, 0, 3, palmeiras).

- validação de um dado deve começar a ser feito procurando o erro/restrição e não o acerto
- IA resolve problema de diagnostico (especialista) ➜ reconhecimento de padrões, a partir das amostra que IA teve acesso
  quando maior a amostra que uma IA teve acesso mais especialista em algo ela se torna, ou seja, maior sua base de conhecimento

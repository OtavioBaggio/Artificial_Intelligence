#             Trabalho Avaliativo - Inteligência Artificial
#                 Aluno: José Otávio R. Baggio

# Tendo como base os código disponíveis na pasta 3 - AG, que trata da aplicação de AG em palavras, modelar e implementar (na sua 
# linguagem de preferência) o problema de roteamento. Imagine que existam 9 cidades (1, 2, 3, 4, 5, 6, 7, 8 e 9), 
# representadas em um grafo/mapa imaginário. A rota perfeita, para este problema, é 123456789. O cálculo de aptidão é baseado em restrições:

# uma cidade de número maior vier primeiro que uma cidade de número menor, deve ter restrição com nota 10;
# se na rota aparecer mais de uma vez a mesma cidade (número); para cada par de ocorrência dar nota 20.
# Dessa forma, refatore o código de AG das palavras para resolver o problema de roteamento com aplicação das técnicas de AG.

# Por exemplo uma rota [2, 8, 4, 0, 1, 5, 3, 6, 7] Qual seria a nota de aptidao?


import copy
import os
import time

from ag import AG

os.system('cls')

tamanho_populacao = int(input("Tamanho da população: "))
taxa_selecao = int(input("Taxa de seleção (entre 20 a 40%): "))
taxa_reproducao = 100 - taxa_selecao
taxa_mutacao = int(input("Taxa de mutação (entre 5 a 10%): "))
qtd_geracoes = int(input("Quantidade de gerações: "))

estado_final = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Objetivo final

populacao = []          # População atual
nova_populacao = []     # População da próxima geração, gerada a cada iteração

AG.gerar_populacao(populacao, tamanho_populacao, estado_final)      # Gera uma pop random inicial
populacao.sort()    # Ordena do melhor para o pior
print("Geracao 1")
AG.exibir(populacao)

# Laço das gerações:
for i in range(1, qtd_geracoes):
    AG.selecionar_por_torneio(populacao, nova_populacao, taxa_selecao)
    
    AG.reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final)
    
    # A frequência da mutação é controlada por: i % (tamanho_populacao / taxa_mutacao) == 0
    # Ex: população 30, mutação 10% → muta a cada 3 gerações
    if (i % (len(populacao) / taxa_mutacao) == 0):
        AG.mutar(nova_populacao, estado_final)
    
    # Do prof:
    #populacao.clear()
    #populacao = copy.deepcopy(nova_populacao)

    populacao = nova_populacao.copy()   # armazena na nova população
    nova_populacao.clear()              # Limpa para a próxima geração
    populacao.sort()                    # ordena

    print(f"\n\nGeração   {(i + 1)}")
    AG.exibir(populacao)
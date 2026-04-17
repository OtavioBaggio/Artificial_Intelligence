% Exercicio 3
estrada("CidadeA", "CidadeB").
estrada("CidadeB", "CidadeC").

pode_viajar(De, Para) :-
    estrada(De, Para).

% Por que estrada(a, b) não implica em estrada(b, a)
% Porque no Prolog as relações não são automáticas nem simétricas.Para isso fazemos assim:

pode_viajar(De, Para) :-
    estrada(Para, De).
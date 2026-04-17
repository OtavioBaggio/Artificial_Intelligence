% Problema 10: Torneio de Jogos. Com fatos venceu(JogadorA, JogadorB), crie uma regra
% invicto(Jogador) que verifica se ninguém venceu aquele jogador.

time(gramado).
time(canela).
time(santa_maria).

venceu(gramado, canela).
venceu(gramado, santa_maria).
venceu(canela, santa_maria).
venceu(santa_maria, canela).

invicto(X) :-
    time(X),
    venceu(X, _),
    not(venceu(_, X)).

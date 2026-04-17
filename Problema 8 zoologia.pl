% Dominio: Mundo de blocos (Clássico de IA):
% 7. Empilhamento: Use fatos sobre(BlocoA, BlocoB) (A está acima de B) e no_chao(BlocoB).
% Crie a regra abaixo(X, Y) e a regra bloco_livre(X) (se não há nada sobre ele).

% 4
% 3
% 2
% 1
% 0

sobre(4, 3).
sobre(3, 2).
sobre(2, 1).
sobre(1, 0).


abaixo(BAb, BAc) :-
    sobre(BAc, BAb).

abaixo(BAb, BAc) :-
    sobre(BAc, I),
    abaixo(BAb, I).
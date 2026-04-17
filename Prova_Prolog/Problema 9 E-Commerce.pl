% Problema 8. Crie fatos sobre caracteristicas (ex: tem_penas(pinguim), poe_ovos(pinguim))
% e regras para classificar: ave(X) :- tem_penas(X), poe_ovos(X).

tem_penas(pinguim).
tem_penas(galinha).
tem_penas(coruja).

poe_ovos(pinguim).
poe_ovos(coruja).
poe_ovos(galinha).

ave(A) :-
    tem_penas(A),
    poe_ovos(A).
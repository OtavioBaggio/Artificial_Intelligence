% Problema 4
esta_em("livro", "Sala").
comodo_em("Sala", "Casa de vó").

localizacao_geral(Objeto, Casa) :-
    esta_em(Objeto, Comodo),
    comodo_em(Comodo, Casa).
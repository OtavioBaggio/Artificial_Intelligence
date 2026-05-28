viagens(r2,2).
guarda(med).

!start.

+!start : true
    <- 
    ?viagens(r2,Qtd);
    ?guarda(Peca);
    .print("estou ativo e posso guardar peças ", Peca, " e tenho ", Qtd, " viagens possíveis").


+!guardar(Peca)[source(Agt)] : true
    <-
        .print("vou ajudar ", Agt, " a guardar peça ", Peca).
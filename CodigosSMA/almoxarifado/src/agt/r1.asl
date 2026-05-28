viagens(r1,5).
guarda(peq).

!start.

+!start : true
    <- 
        ?guarda(Peca);
        ?viagens(r1,Qtd);
        .print("estou ativo e posso guardar peças ", Peca, " e tenho ", Qtd, " viagens possíveis").

+peca(Peca) : guarda(Peca) & viagens(r1,Qtd) & Qtd > 0
    <-
        -viagens(r1,Qtd);
        NovoQtd = Qtd - 1;
        +viagens(r1,NovoQtd);
        .print("percebi uma peça ", Peca, " na entrada e vou guarda-la....tenho mais ", NovoQtd, " de viagens");
        guardar(Peca).
        

+peca(Peca) : guarda(Peca)
    <-
        .print("percebi uma peça ", Peca, " mas nao tenho como guarda-la");
        empilhar(Peca).

+peca(Peca) : Peca == grd & viagens(r1,Qtd) & Qtd > 0
    <-
        .print("percebi uma peça ", Peca, " mas vou convidar r2 para me ajudar");
        
        // 1. Envia a pergunta
        .send(r2, askOne, viagens(r2, Qtd_r2));
        
        // 2. Trava a execução aqui até a resposta de viagens(r2, _) chegar de r2
        .wait(viagens(r2, _)[source(r2)]); 
        
        // 3. Busca o valor que r2 acabou de adicionar na sua base de crenças
        ?viagens(r2, Valor_R2)[source(r2)];
        
        // 4. Faz o teste com o valor numérico recebido
        Valor_R2 > 0;
        .print("r2 aceitou me ajudar");

        // continue o código de ajuda aqui...
        //guardar(Peca);
        .print("eu e r2 estamos indo guardar a peça grande");
        .send(r2,achieve,guardar(Peca)).
        
+peca(Peca) : Peca == grd & viagens(r1,Qtd) & Qtd > 0
    <-
       .print("r2 nao pode me ajudar.... ");
       empilhar(Peca). 

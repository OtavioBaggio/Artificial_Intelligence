laboratorio(ia,101).
laboratorio(ed,108).
laboratorio(redes,316).

!start.

/* Plans */

+!start : true 
    <- 
        .print("hello world.");
        .send(bob, tell, lanche(sanduiche)).

//alice.asl executando raciocionio antes de responder
+!kqml_received(Agente,askOne, laboratorio(Disciplina,Laboratorio),MsgId)
    <- 
    ?laboratorio(Disciplina,Laboratorio);
    .print(Agente, " está me perguntando qual o laboratoriode ",Disciplina," que é no ", Laboratorio);
    // calcular ou verifica internamente
    .send(Agente,reply,laboratorio(Disciplina, Laboratorio)).
        

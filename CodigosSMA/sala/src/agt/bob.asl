time(gremio).
idade(19).
disciplina(ia,sexta).
disciplina(ed,quarta).

!start.

/* Plans */

+!start : true 
    <- 
        .print("hello world.").

+dia(Dia) : disciplina(Disciplina, Dia)
    <-
        .print("Oba...Tenho aula de IA... Alice...qual é o laboratorio?");
        .send(alice,askOne,laboratorio(Disciplina, Laboratorio),MsgId).


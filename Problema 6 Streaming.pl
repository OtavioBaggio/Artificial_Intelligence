% Problema 5: Cardápio. Crie fatos ingredientes(Prato, Item) e vegano(Item). 
% Escreva a regra prato_vegano(Prato) que é verdadeira apenas se todos os pratos
% os ingredientes forem veganos (útil para introduzir o conceito de negação e falha).

ingrediente(salada, alface).
ingrediente(salada, tomate).
ingrediente(salada, cenoura).
ingrediente(churrasco,arroz).
ingrediente(churrasco,carne).

vegano(alface).
vegano(tomate).
vegano(cenoura).
vegano(pao).
vegano(arroz).
 

prato_vegano(Prato) :-
    ingrediente(Prato, _),
    forall(ingrediente(Prato, Item), vegano(Item)).
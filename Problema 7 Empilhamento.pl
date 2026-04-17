% Questão 6: Streaming
% Com fatos filme(Nome, Genero) e usuario_gosta(Usuario, Genero),
%  crie a regra recomendar(Filme, Usuario).

filme(star_wars, ficcao).
filme(harry_potter, fantasia).
filme(senhor_dos_aneis, fantasia).
filme(blade_runner, ficcao).
filme(hobbit, fantasia).
filme(it, terror).
filme(exorcista, terror).

usuario_gosta(alex, ficcao).
usuario_gosta(alex, fantasia).
usuario_gosta(bernardo, terror).
usuario_gosta(andrisa, terror).

recomendar(F, U) :-
    filme(F, Genero),
    usuario_gosta(U, Genero).
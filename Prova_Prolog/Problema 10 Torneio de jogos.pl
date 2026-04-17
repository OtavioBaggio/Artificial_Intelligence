disciplina("Inteligência Artificial").
disciplina("Estrutura de Dados").
disciplina("Algoritmos B").

pre_requisito("Algoritmos B", "Estrutura de Dados").
pre_requisito("Estrutura de Dados", "Inteligência Artificial").

ja_cursou("Freitas", "Algoritmos B").
ja_cursou("Henriques", "Estrutura de Dados").

pode_cursar(Aluno, Disciplina) :-
	ja_cursou(Aluno, Pre),
	pre_requisito(Pre, Disciplina).

aprovado(Aluno, Disciplina) :-
    nota(Aluno, Disciplina, Valor),
    Valor >= 7.0.

reprovado(Aluno, Disciplina) :-
    nota(Aluno, Disciplina, Valor),
    Valor < 7.0.

nota("Freitas", "Algoritmos B", 8.5).
nota("Henriques", "Estrutura de Dados", 6.0).
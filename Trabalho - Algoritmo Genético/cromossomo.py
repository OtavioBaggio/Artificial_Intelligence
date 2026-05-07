class Cromossomo:


    def __init__(self, valor, estado_final):
        self.valor = valor
        self.aptidao = self.calcular_aptidao(estado_final)

    def calcular_aptidao(self, estado_final):
        """
        Calcula a aptidão do cromossomo — quanto MENOR, melhor
        """
        nota = 0

        # Vai penalizar se vier uma cidade com número maior antes:
        for i in range(len(estado_final) - 1):
            if(self.valor[i] > self.valor[i + 1]):
                nota += 10

        # Penaliza cidades repetidas, cada par repetido vale 20:
        for i in range(len(self.valor)):
            for j in range(i + 1, len(self.valor)):
                if self.valor[i] == self.valor[j]:
                    nota += 20

        return nota
    

    # Equals:
    def __eq__(self, other):
        """
        Dois cromossomos são iguais se tiverem o mesmo valor (mesma rota).
        Usado pelo operador == e pelo 'in' em listas.
        """
        if isinstance(other, Cromossomo):
            return self.valor == other.valor
        return False
    

    # Maior que:
    def __gt__(self, other):
        """
        Define 'maior que' com base na aptidão.
        Como aptidão menor é melhor, um cromossomo com aptidão MAIOR é o pior.
        Usado pelo sort() para ordenar a população do melhor para o pior.
        """
        return self.aptidao > other.aptidao
    

    # toString:
    def __str__(self):
        return f"valor= {self.valor}, aptidao= {self.aptidao}"
        # return "valor=" + str(self.valor) + ", aptidao=" + str(self.aptidao )
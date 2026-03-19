/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package trabalhocanibais;

/*
Tarefa IA:
Modelar e implementar (utilizando o pacote buscaJava.jar, do professor Jomi Hubner) o problema dos missionarios e canibais.

    ------- Aluno: José Otávio R. Baggio ---------

Descrição do problema:
Três missionarios e três canibais estão à beira de um rio e dispõem de um barco com capacidade para apenas duas pessoas. 
O problema consiste em determinar as tripulações de uma série de travessias de forma que todo o grupo atravesse 
para o outro lado do rio, respeitando a condição de que, em nenhum momento, 
os canibais sejam mais numerosos do que os missionarios em qualquer uma das margens.
*/

import busca.*;
import exemplos.MissionarioCanibal;
import java.util.*;

/**
 ** Problema dos Missionários e Canibais - FOI UTILIZADO O MÉTODO DE BUSCA EM PROFUNDIDADE
 *
 * Estado representado por (m, c, b):
 *   m = nº de missionarios na margem ESQUERDA (inicial)
 *   c = nº de canibais   na margem ESQUERDA
 *   b = posição do barco  (1 = esquerda, 0 = direita)
 *
 * Estado inicial: (3, 3, 1)
 * Estado meta:    (0, 0, 0)
 * 
 * @author Otávio Baggio
 */
public class TrabalhoCanibais implements Estado, Antecessor {
    
    
    final int m;    // missionarios, começam na margem esquerda
    final int c;    // canibais também na margem esquerda
    final int b;    // barco: na esquerda
    final String op;    // operação do estado

    public TrabalhoCanibais(int m, int c, int b, String op) {
        this.m = m;
        this.c = c;
        this.b = b;
        this.op = op;
    }
    
    @Override
    public String getDescricao() {
        return op; 
    }

    // Esse método é chamado em cada estado visitado. 
    // Quando os três valores chegam a zero, o problema está resolvido.
    @Override
    public boolean ehMeta() {
        return m == 0 && c == 0 && b == 0;
    }

    @Override
    public int custo() { 
        return 1; 
    }

    @Override
    public List<Estado> sucessores() {
        List<Estado> suc = new LinkedList<>();
        if (b == 1) {
            // barco na esquerda -> travessias para a direita
            tentar(suc, m - 2, c,     0, "Levar 2 missionarios para direita\n");
            tentar(suc, m,     c - 2, 0, "Levar 2 canibais para direita\n");
            tentar(suc, m - 1, c - 1, 0, "Levar 1 missionario e 1 canibal para direita\n");
            tentar(suc, m - 1, c,     0, "Levar 1 missionario para direita\n");
            tentar(suc, m,     c - 1, 0, "Levar 1 canibal para direita\n");
        } else {
            // barco na direita -> travessia para esquerda
            tentar(suc, m + 2, c,     1, "Levar 2 missionarios para esquerda\n");
            tentar(suc, m,     c + 2, 1, "Levar 2 canibais para esquerda\n");
            tentar(suc, m + 1, c + 1, 1, "Levar 1 missionario e 1 canibal para esquerda\n");
            tentar(suc, m + 1, c,     1, "Levar 1 missionario para esquerda\n");
            tentar(suc, m,     c + 1, 1, "Levar 1 canibal para esquerda\n");
        }
        return suc;
    }

    /***
     * 
     * @param lista - de sucessores
     * @param nm - novo valor de missionário na esquerda
     * @param nc - novo valor de canibal na esquerda
     * @param nb - onde o barco ficaria
     * @param desc - descrição da operação
     */
    private void tentar(List<Estado> lista, int nm, int nc, int nb, String desc) {
        if (ehValido(nm, nc))
            lista.add(new TrabalhoCanibais(nm, nc, nb, desc));
    }

    /***
     * Um estado só é aceito se, em ambas as margens, os missionários não forem superados pelos canibais. 
     * A verificação da margem direita usa 3 - nm e 3 - nc porque o total é sempre 3 de cada lado.
     * @param nm - novoMissionario
     * @param nc - novoCanibal
     * @return 
     */
    private boolean ehValido(int nm, int nc) {
        if (nm < 0 || nm > 3 || nc < 0 || nc > 3) return false;
        int md = 3 - nm, cd = 3 - nc;
        if (nm > 0 && nm < nc) return false;  // canibais > missionários na esquerda
        if (md > 0 && md < cd) return false;  // canibais > missionários na direita
        return true;
    }

    @Override
    public List<Estado> antecessores() {
        TrabalhoCanibais invertido = new TrabalhoCanibais(m, c, 1 - b, op);
        return invertido.sucessores();
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof TrabalhoCanibais)) return false;
        TrabalhoCanibais e = (TrabalhoCanibais) o;
        return m == e.m && c == e.c && b == e.b;
    }

    @Override
    public int hashCode() { return m * 100 + c * 10 + b; }

    @Override
    public String toString() {
        StringBuilder esq = new StringBuilder();
        for (int i = 0; i < m; i++) esq.append("M");
        for (int i = 0; i < c; i++) esq.append("C");

        int md = 3 - m, cd = 3 - c;
        StringBuilder dir = new StringBuilder();
        for (int i = 0; i < md; i++) dir.append("M");
        for (int i = 0; i < cd; i++) dir.append("C");

        String barcoEsq = (b == 1) ? "[B]" : "   ";
        String barcoDir = (b == 0) ? "[B]" : "   ";

        return String.format("%-6s %s ~~ %s %-6s   op: %s",
            esq, barcoEsq, barcoDir, dir, op);
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Estado inicial = new TrabalhoCanibais(3, 3, 1, "Estado inicial");

        System.out.println("=============================================================");
        System.out.println("  PROBLEMA DOS MISSIONÁRIOS E CANIBAIS");
        System.out.println("  3 missionarios, 3 canibais, barco p/ 2 pessoas");
        System.out.println("  Algoritmo: Busca em Profundidade");
        System.out.println("=============================================================\n");

        try {
            BuscaProfundidade busca = new BuscaProfundidade();
            busca.usarFechados(true);
            Nodo resultado = busca.busca(inicial);

            if (resultado == null) {
                System.out.println("Sem solução!");
            } else {
                System.out.println(resultado.montaCaminho());
                System.out.println("Profundidade da solução: " + resultado.getProfundidade());
            }
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
            e.printStackTrace();
        }
        
    }
    
}

package example;

// Environment code for project almoxarifado

import jason.asSyntax.*;
import jason.environment.*;
import jason.asSyntax.parser.*;

import java.util.logging.*;
import java.util.Random;

public class Env extends Environment {

    private Logger logger = Logger.getLogger("almoxarifado."+Env.class.getName());
    String peca;

    String sorteiaPeca() {
        Random gerador = new Random();
        String resposta = "";
        switch (gerador.nextInt(3)) {
            case 0:
                resposta = "peca(peq)";
                break;
            case 1:
                resposta = "peca(med)";
                break;        
            case 2:
                resposta = "peca(grd)";
                break;                        
            default:
                break;
        }
        return resposta;
    }

    /** Called before the MAS execution with the args informed in .mas2j */
    @Override
    public void init(String[] args) {
        super.init(args);
        peca = "peca(grd)"; //sorteiaPeca();
        try {
            addPercept(ASSyntax.parseLiteral(peca));
            logger.info("entrou no almox uma peça " + peca);
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }

    @Override
    public boolean executeAction(String agName, Structure action) {
        
        if (agName.equals("r1") && action.getFunctor().toString().equals("guardar") && action.getTerm(0).toString().equals("peq")) {
            logger.info(agName+ " esta guardando a peça " + action.getTerm(0).toString());             
        } else logger.info("tentando executar : "+action+", mas ainda não implementada");

        try {
            removePercept(ASSyntax.parseLiteral(peca));

            //faz o ambiente colocar outra peça
            Thread.sleep(4000);
            peca = "peca(peq)"; //sorteiaPeca();
            addPercept(ASSyntax.parseLiteral(peca));
        } catch (Exception e) {
            // TODO: handle exception
        }

        return true; // the action was executed with success
    }

    /** Called before the end of MAS execution */
    @Override
    public void stop() {
        super.stop();
    }
}




public abstract class Evento {

    private String nome;
    private String data;
    private String local;
    private int ingressosInteira;
    private int ingressosMeia;

    // Construtor, getters e setters...

    public boolean isIngressoDisponivel(Ingresso.TipoIngresso tipo, int quantidade) {
        if(tipo == Ingresso.TipoIngresso.INTEIRA && ingressosInteira >= quantidade) {
            return true;
        } else if(tipo == Ingresso.TipoIngresso.MEIA && ingressosMeia >= quantidade) {
            return true;
        }
        return false;
    }

    public abstract double venderIngresso(Ingresso.TipoIngresso tipo, int quantidade);
}


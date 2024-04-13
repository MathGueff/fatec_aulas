
package JantarFilosofos;

import javax.swing.JFrame;

public class JantarDosFilosofos extends JFrame
{

    public JantarDosFilosofos ()
    {
        // CRIA UMA NOVA MESA NA TELA
        add(new Mesa());

        // DEFINE O TITULO
        setTitle("Jantar dos Filósofos");
        // INFORMA O MÉTODO DE SAÍDA
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        // SETA O TAMANHO
        setSize(410, 410);
        // SETA A LOCALIZAÇÃO
        setLocationRelativeTo(null);
        // SETA A VISIBILIDADE
        setVisible(true);
        // SETA SE É REDIMENSIONAVEL
        setResizable(false);
    }

    public static void main(String[] args)
    {
        new JantarDosFilosofos();
    }

}

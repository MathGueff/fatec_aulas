
import java.util.logging.Level;
import java.util.logging.Logger;


public class Principal {

    public static void main(String[] args) throws InterruptedException {
        // TODO code application logic here
        System.out.println("Hello World");
        
        System.out.println("Inicializando a primeira Thread");
        Thread.sleep(1000);
        System.out.println("Finalizando a primeira Thread");
        
        System.out.println("Inicializando a segunda Thread");
        Thread.sleep(1000);
        System.out.println("Finalizando a segunda Thread");
        
        System.out.println("Inicializando a terceira Thread");
        Thread.sleep(1000);
        System.out.println("Finalizando a terceira Thread");
        
        System.out.println("=======Inicializando as Threads=======");
        new Thread(() -> {
            System.out.println("Thread 1, inicializando");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Logger.getLogger(Principal.class.getName()).log(Level.SEVERE, null, ex);
            }
            System.out.println("Finalizando a primeira Thread");
        }).start();
        new Thread(() -> {
            System.out.println("Thread 2, inicializando");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Logger.getLogger(Principal.class.getName()).log(Level.SEVERE, null, ex);
            }
            System.out.println("Finalizando a segunda Thread");
        }).start();
        new Thread(() -> {
            System.out.println("Thread 3, inicializando");
            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Logger.getLogger(Principal.class.getName()).log(Level.SEVERE, null, ex);
            }
            System.out.println("Finalizando a terceira Thread");
        }).start();
    }
}

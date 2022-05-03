/*
    Manejo de estructuras while
*/

public class a3_estructurasWhile {
    public static void main (String[] args){
        int n=0;
        int resultado=0;
        
        while(n<10){
            System.out.println("numero es: " + n);
            n++;
            resultado = resultado + n;
        }
        System.out.println("La suma de los numeros es: " + resultado);

        do{

            resultado = resultado + 3;
            System.out.println(resultado);

        }while (resultado <10);
    }
}

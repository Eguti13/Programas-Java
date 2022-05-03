/*
    Manejo de estructuras for
*/

public class a4_estructurasFor {
    public static void main (String[] args){
        int i;
        int resultado=0;
        
        for (i=0;i<10;i++){
            System.out.println("numero es: " + i);
            resultado = resultado + i;
        }
        System.out.println("La suma de los numeros es: " + resultado);
    }
}

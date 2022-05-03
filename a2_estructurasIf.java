/*
    Manejo de estructura condicional if
*/

public class a2_estructurasIf {
    public static void main (String[] args){
        String nombre;
        System.out.print("Por favor, escriba su nombre: ");
        nombre = System.console().readLine();
        System.out.println("Hola " + nombre + ", por faor igrese dos valores");
        int n=0;
        int resultado=0;
        
        if(n<10){
            System.out.println("numero es: " + n);
            n++;
            resultado = resultado + n;
        }
        System.out.println("La suma de los numeros es: " + resultado);
    }
    
}

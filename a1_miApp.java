public class a1_miApp { 
    
    /*
        Ejemplo básico de entrada y salida en JAVA
        https://javadesdecero.es/io/maneras-lectura-datos-java/
    */
    
    public static void main(String[] aStrings) {

        //Salida
        System.out.println("Hola mundo");
        
        //sentencias
        int n1=2;
        int n2=3;
        int resultado = n1+ n2;
        System.out.println(resultado);

        String nombre;
        System.out.print("Por favor, dime tu nombre: ");
        
        //Entrada
        nombre = System.console().readLine();
        System.out.println("Hola " + nombre + ", ¡bienvenido a Java desde Cero!");
        
    }
        
}

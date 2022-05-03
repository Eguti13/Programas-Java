/*
    Utilización de tipos de datos
*/

public class a1b_tiposDatos {
    public static void main(String[] args) {
        
        // declarando el carácter
         char a = 'G';
          
        // El tipo de datos enteros es generalmente
        // utilizado para valores numéricos
        int i=89;
         
        // use byte y short si la memoria es una prioridad
        byte b = 4;
         
        // esto dará error ya que el número es
        // mayor que el rango de bytes
        // byte b1 = 7888888955;
         
        short s = 56;
         
        // esto dará error ya que el número es 
        // más grande que el rango de short
        // short s1 = 87878787878;
         
         
        // por defecto, el valor de la fracción es double en Java
        double d = 4.355453532;
         
        // para float use 'f' como sufijo
        float f = 4.7333434f;
        
        System.out.println("char: " + a); 
        System.out.println("integer: " + i); 
        System.out.println("byte: " + b); 
        System.out.println("short: " + s); 
        System.out.println("float: " + f); 
        System.out.println("double: " + d); 

        //bytes
        byte a2 = 126;
 
        // byte tiene un valor de 8 bits
        System.out.println(a2);
        
        a2++;
        System.out.println(a2);
         
        // Se desborda aquí porque
        // el byte puede contener valores de -128 a 127
        a2++;
        System.out.println(a2);
         
        // bucle dentro del rango
        a2++;
        System.out.println(a2);

        //buleanos
        boolean dato = true;       
        if (dato == true)
            System.out.println("Hola a todos!");


        
        System.out.println("b es: "+ dato);

        dato=true;
        System.out.println("b es: "+dato);

        //Un valor booleano puede contralar la sentencia if

        if(dato) System.out.println("Esto si ejecutará.");

        dato=false;
        if(dato) System.out.println("Esto no se ejecutará.");

        //El resultado de un operador relacional es un valor booleano
        System.out.printf("10 > 9 es "+ (10 > 9));
    }
    
}

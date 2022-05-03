/*
Programa Java para leer datos de varios tipos usando la clase Scanner
Diferencias entre los tipos de lectura
https://stackoverflow.com/questions/17637032/bufferedreader-vs-console-vs-scanner
*/


import java.util.Scanner;

public class a1c_ejemploScanner{
    public static void main(String[] args)
    {
        // Declarar el objeto e inicializar con
        // el objeto de entrada estándar predefinido

        Scanner sc = new Scanner(System.in);

        // entrada de una cadena
        String name = sc.nextLine();

        // entrada de un carácter
        char gender = sc.next().charAt(0);

        // Entrada de datos numéricos
        // byte, short y float
        int age = sc.nextInt();
        long mobileNo = sc.nextLong();
        double average = sc.nextDouble();

        //Entradas con Parse
        byte b = Byte.parseByte(sc.nextLine());
        short s = Short.parseShort(sc.nextLine());
        int i = Integer.parseInt(sc.nextLine());
        long l = Long.parseLong(sc.nextLine());
        float f = Float.parseFloat(sc.nextLine());
        double d = Double.parseDouble(sc.nextLine());
        boolean b2 = Boolean.parseBoolean(sc.nextLine());
        char ch1 = sc.nextLine().charAt(0);


        // Imprima los valores para verificar si la entrada
        // fue obtenida correctamente.
        System.out.println("Nombre: "+name);
        System.out.println("Género: "+gender);
        System.out.println("Edad: "+age);
        System.out.println("Teléfono: "+mobileNo);
        System.out.println("Promedio: "+average);

        System.out.println("byte: " + b);
        System.out.println("short: " + s);
        System.out.println("int: " + l);
        System.out.println("int: " + i);
        System.out.println("float: " + f);
        System.out.println("double: " + d);
        System.out.println("boolean: " + b2);
        System.out.println("char: " + ch1);
    

        sc.close();
        // se cierra para evitar errores dejando abierta la interface
    }
}
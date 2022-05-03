/*
    Funciones en java
    Funcion sumar y cuadrado
*/
public class a5_funciones1 {
    public static void main(String[] args) {
        int n1 = 5;
        int n2 = 7;
        suma(n1, n2);
        int c1= cuadrado(n1);
        System.out.println(c1);
        System.out.println(cuadrado(n2));
    }

    public static void suma (int a , int b){
        int c = a + b;
        System.out.println(c);
    }

    public static int cuadrado(int a){
        int b = a*a;
        return b;
    }
}

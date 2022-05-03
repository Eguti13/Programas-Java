/*
	Ejercicios con cadenas
*/

public class a1c_manejoCadenas {
	public static void main(String[] args) {
        
		System.out.println("Introduce una cadena de texto");
		String s=new String();
		s=System.console().readLine();
		System.out.println("La longitud de la cadena es: "+s.length());
		System.out.println("El caracter intermedio de la cadena es: "+s.charAt(s.length()/2));
		System.out.println("La parte izquierda de la cadena es: "+s.substring(0, s.length()/2));
		System.out.println("La parte derecha de la cadena es: "+s.substring(s.length()/2, s.length()));

        System.out.println("Introduce la primera cadena de texto");
        String s1;
		s1=System.console().readLine();
		System.out.println("Introduzca ahora la segunda cadena de texto");
		String s2;
		s2=System.console().readLine();
		System.out.println(s1.concat(s2).toUpperCase());

        System.out.println("Introduce la primera cadena de texto");
		s1=System.console().readLine();
		System.out.println("Introduce ahora la segunda cadena de texto");
		s2=System.console().readLine();
		comparar(s1, s2);
		
	}
	public static void comparar (String s, String g){
		if (s.length()==g.length()){
			if (s.equalsIgnoreCase(g)==true){
				System.out.println("Ambas cadenas de texto son iguales");
			}
		}else if (s.length()>g.length()) {
			if (s.indexOf(g)==0)
			System.out.println("La segunda cadena está contenida en la primera");
			else System.out.println("La segunda cadena no está contenida en la primera");
		}else if (g.length()>s.length()){
			if (g.indexOf(s)==0)
				System.out.println("La primera cadena está contenida en la segunda");
				else System.out.println("La primera cadena no está contenida en la segunda");
		}
	}

	
}
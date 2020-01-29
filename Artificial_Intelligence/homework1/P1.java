public class P1 {
    public static void main(String[] args){
    	int k = 8;
        System.out.println(p1(k));
    }

    public static String p1(int k) {
	    StringBuilder sb = new StringBuilder();

		sb.append(factorial(k));

	    for (int i = k - 1; i > 0; i--) {
	    	sb.append(", ");
		    sb.append(factorial(i));
	    }

	    return sb.toString(); 
    }

    public static int factorial(int k) {
        for (int i = k - 1; i > 0; i--) {
        	k *= i;
        }
        return k;
    }

    
}


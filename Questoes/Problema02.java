import java.lang.Math;

class Problema02{
    public static void main(String []args){
        double pi = 0;
        double sum = 0;
        for(int k = 0; k < 100000; k=k+1){
            pi=  ( 1 / Math.pow(16.0,k) ) * ( (4.0/(8*k+1)) - (2.0/(8*k+4)) - (1.0 / (8*k + 5)) - (1.0 / (8*k+6)) ); 
            sum = sum + pi;

        }
        System.out.println("O valor do pi é " + sum);
    }
}
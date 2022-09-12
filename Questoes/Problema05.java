import java.util.Scanner;
import java.lang.Math;

class Problema05 {
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      System.out.println("Valor para a função: ");
      int n = in.nextInt();
      System.out.println(Fi.subfact(n));
   }
}

class Fi{
   static int fact(int n){
      if( n > 1){
         return n * fact(n - 1);
      } else{
         return 1;
      }
   }

   static float subfact(int n){
      int fat = fact(n);
      float som = 0;

      for(int k = n; k > 0; k--){
         som += (Math.pow(-1, k))/fact(k);
      }

      return som;
   }
}
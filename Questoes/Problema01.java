class Problema01 {
    public static void main(String []args){
        int vetX[] = {2,3,4,5,8,12,24,25};
        System.out.println("Valores n que são divisivéis por m: ");
        for(int i = 0; i < vetX.length;i++) {
            for(int j = vetX.length - 1; j >= 0; j--){
                if(vetX[i] % vetX[j] == 0 && vetX[i] != vetX[j]){
                    System.out.print("("+vetX[i] + "," + vetX[j] + ") ");
                }
            }
        }
    }
}

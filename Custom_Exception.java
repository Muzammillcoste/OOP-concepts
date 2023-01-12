import java.util.Scanner;

class Negativenum extends Exception{
    @Override
    public String toString() {
        return "Negative number not allow";
    }
}

public class Custom_Exception {
    public static void main(String[] args) {
        try{
            try (Scanner scanner = new Scanner(System.in)) {
                System.out.print("enter number: ");
                int num =scanner.nextInt();
                if (num<0){
                    throw new Negativenum();
                }
            }
        }
        catch (Negativenum e){
                e.printStackTrace();
        }
        
    }
}

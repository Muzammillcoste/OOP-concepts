import java.util.Scanner;

public class Except {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int[] numbers ={5,3,4,2};
            while(true){
                try{
                    System.out.print("Enter index: ");
                    int ind =scanner.nextInt();
                    System.out.println("Number you get from array is "+numbers[ind]);
                    break;
                }
                catch(ArrayIndexOutOfBoundsException e){
                        System.out.println("IndexOutOfBoundsException, Enter index again");
                }
            }
        }
    } 
}

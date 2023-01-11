abstract class  Animal{
    abstract public void walk();
    public void eat(){
        System.out.println("eat vegeatble");
    }
}
class Horse extends Animal{
    public void walk(){
        System.out.println("walk with 2 legs");
    }
}

public class abstraction {
    public static void main(String[] args) {
        Horse h1 = new Horse();
        h1.eat();
        h1.walk();
        
    }
    
}

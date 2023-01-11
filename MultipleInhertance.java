interface Feature{
    void music();
}
interface ChildFeature extends Feature{
    void wifi();
}
interface video{
    void playMusic();
}
class Phone{
    public void meth1(){
        System.out.println("phone");
    }
}

class SmartPhone extends Phone implements ChildFeature,video{
    public void music(){
        System.out.println("music");
    }
    public void wifi(){
        System.out.println("wifi");
    }
    public void playMusic(){
        System.out.println("playmusic");
    }
}

public class MultipleInhertance {
    public static void main(String[] args) {
        SmartPhone obj = new SmartPhone();
        obj.playMusic();
        obj.meth1();
    
    }
}


public class Puppy {
    int puppyAge;
    public Puppy(String name){
        System.out.println("The puppy's name is " + name);
    }

    public void setAge(int age){
        puppyAge = age;
    }

    public int getAge(){
        System.out.println("The puppy's age is " + puppyAge);
        return puppyAge;
    }

    public static void main(String[] args){
        Puppy mypuppy = new Puppy("tommy");
        mypuppy.setAge(2);
        mypuppy.getAge();
        System.out.println("The age is " + mypuppy.puppyAge);
    }
}

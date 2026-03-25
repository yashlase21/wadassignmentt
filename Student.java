package Teste;

public class Student {
    private String name;
    private int age;
    private int roll;

    public void setAge(int age){
        if (age<0){
            age=0;
        }
        this.age = age;
    }
    public int getAge(){
        return this.age;
    }

    public int getRoll(int roll) {
        return roll;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setRoll(int roll) {
        this.roll = roll;
    }
}

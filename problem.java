import java.util.Scanner;

public class problem {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int sum=0;
        float marksofEachSubject=100;
        System.out.println("The default value of each subject 100 for customized value enter 'custom'");
        System.out.println("Enter the subject One : ");
        int number1= scan.nextInt();
        System.out.println("Enter the subject Two : ");
        int number2= scan.nextInt();
        System.out.println("Enter the subject Three : ");
        int number3= scan.nextInt();
        System.out.println("Enter the subject Four : ");
        int number4= scan.nextInt();
        System.out.println("Enter the subject Five : ");
        int number5= scan.nextInt();
        sum=number1+number2+number3+number4+number5;
        float total= 5 * marksofEachSubject;
        float average = (sum* 100)/total;
        System.out.print("The percentage value is : ");
        System.out.println(average);
        scan.close();

    }
    
}
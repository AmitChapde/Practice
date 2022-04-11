
import java.util.Scanner;public class armstrongnumber {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        System.out.println("Enter a number:");
        int num=scan.nextInt();
        int sum=0;
        int temp=num;
        while(temp>0){
            int digit=num%10;
            sum = sum+digit*digit*digit;
            num =num/10;
        }
        if (sum==num){
            System.out.println("The Number is an armstrong number");
        }else {
            System.out.println("The Number is not an armstrong number");
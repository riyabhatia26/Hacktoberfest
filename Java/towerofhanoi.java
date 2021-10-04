/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
import java.util.Scanner;
public class Main
{
    static void Towerofhanoi(int n,char a, char b, char c)
    {
        if(n==1)
        {
            System.out.println("Move disk 1 from "+a+" to "+c);
            return;
        }
        Towerofhanoi(n-1,a,c,b);
        System.out.println("Move disk "  +n+" from "+a+" to "+c);
        Towerofhanoi(n-1,b,a,c);
    }
	public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
	int n=sc.nextInt();
	
	Towerofhanoi(n,'a','b','c');
	}
}


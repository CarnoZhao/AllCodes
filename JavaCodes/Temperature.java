import java.util.Scanner;

public class Temperature{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int f, c;
		//f = in.nextInt();
		f = 100;
		c = (int)((f - 32) * (5. / 9.));
		System.out.println(c);
	}
}
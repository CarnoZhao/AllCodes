public class Test{
	public static void main(String[] args){
		int ret = 0;
		int start = 1;
		int end = 100;
		OUT:
		for (int i = start; i <= end; i ++){
			int check = i;
			while (check != 0){
				if (check % 10 == 5){
					continue OUT;
				}
				check /= 10;
			}
			ret ++;
			System.out.println(i);
		}
		System.out.println(ret);
	}
}
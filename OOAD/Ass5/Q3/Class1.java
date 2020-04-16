package fact_recursion;
public class Class1{
	public int fact(int k){
		if (k==1 || k==0){
			return 1;
		}
		return k*fact(k-1);
	}
}

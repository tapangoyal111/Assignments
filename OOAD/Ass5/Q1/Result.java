interface sport{
	final int grace=15;
	int tot_marks();
}

public class Result extends Exam implements sport{
	int marks,flag;
	String name;
	public int tot_marks(){
		if (this.flag==1)
		return (this.marks+grace<=100)?this.marks+grace:100;
		else{
			return this.marks;
		}
	}
	public Result(int marks,String name,int flag){
		this.name=name;
		this.marks=marks;
		this.flag=flag;
	}
	
}

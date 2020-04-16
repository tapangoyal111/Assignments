public class Main{
	public static void main(String[] args){
		//System.out.println(args.length);
		if (args[0].equals("1")){
			Student s=new Student(args[1]);
			//System.out.println("dnjhbdk");
			s.intro();
			//Student
		}
		else if (args[0].equals("2")){
			CSEStudent s=new CSEStudent(args[1]);
			s.intro();
		}
		else if (args[0].equals("3")){
			Person s=new Person(args[1]);
			s.intro();
		}
	}
}

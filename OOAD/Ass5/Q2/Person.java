public class Person{
	String name,hobby="Reading";
	public Person (String name1){
		this.name=name1;	
	}
	
	public String getName(){
		return this.name;
	}
	
	public String getHobby(){
		return this.hobby;
	}
	void intro(){
		System.out.println("My Name Is " + this.getName() + " and My Hobby Is " + this.getHobby());
	}
}



class Employee {
	String fname,lname;
	int monthlysal;
	static int objCnt;
	Employee(String fname,String lname,int monthlysal){
		this.fname = fname; 
		this.lname = lname;
		this.monthlysal = monthlysal;
		objCnt++;
	}
	void setFirstName(String fname){
		this.fname = fname;
	}
	void setLastName(String lname){
		this.lname = lname;
	}
	void setMonthlySalary(int monthlysal){
		this.monthlysal = monthlysal;
	}
	String getFirstName(){
		return (fname);
	}
	String getLastName(){
		return (lname);
	}
	int getMonthlySalary(){
		return( monthlysal);
	}
	int getMax(Employee e1,Employee e2){
		int p=e1.getMonthlySalary();
		int q=e2.getMonthlySalary();
		
		return(p>q?p:q);
	}
	int getYearlySalary(){
		return( monthlysal*12);
	}
	void info(){
		System.out.println("\nFirst name: "+this.getFirstName()+"\n Last Name: "+this.getLastName()+"\n Yearly Salary: "+this.getYearlySalary());
	}
}

class Test{
	public static void main(String[] args){
		Employee e1 = new Employee("john", "smith", 15000);
		Employee e2 = new Employee("jason", "clarke", 20000);
		e1.info();
		e2.info();
		
		System.out.println("10% raise");
		e1.setMonthlySalary(e1.monthlysal+(int)(0.1*e1.monthlysal));
		e2.setMonthlySalary(e2.monthlysal+(int)(0.1*e2.monthlysal));
		
		e1.info();
		e2.info();
		
		System.out.println("Maximum Sal: "+e1.getMax(e1, e2));
		System.out.println("Total Objects : "+Employee.objCnt);

	}
}

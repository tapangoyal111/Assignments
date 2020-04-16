
class Invoice{
	String no,name;
	int price,qty; 
	static int objCnt;
	Invoice(final String no, final String name, final int price, final int qty) {
		this.no = no;
		this.name = name;
		this.price = price;
		this.qty = qty;
		objCnt++;
	}


	void setItemNo(final String no) {
		this.no = no;
	}

	void setName(final String name) {
		this.name = name;
	}

	void setPrice(final int price) {
		this.price = price;
	}

	void setQty(final int qty) {
		this.qty = qty;
	}

	String getItemNo() {
		return (this.no);
	}

	String getName() {
		return (this.name);
	}

	int getPrice() {
		return (this.price);
	}

	int getQty() {
		return (this.qty);
	}

	int getInvoieAmount() {
		return (this.qty * this.price);
	}

	int max(final Invoice i1, final Invoice i2) {
		return (i1.qty > i2.qty ? i1.qty : i2.qty);
	}
	static int getObjectCount(){
		return(objCnt);
	}
	void info(){
		System.out.println("SNo."+this.getItemNo()+"\nName: "+this.getName()+"\nPrice: "+this.getPrice()+"\nQty: "+this.getQty()+"\nTotal amount: "+this.getInvoieAmount());

	}
}

class Test {
	public static void main(final String[] args) {
		System.out.println("Initial object count: "+Invoice.objCnt);
		Invoice invoice = new Invoice("1", "bread", 20, 5);
		
		invoice.info();
		
		Invoice invoice2 = new Invoice("2", "milk", 25, 4);
		invoice2.info();
		
		
		System.out.println("Max: "+invoice.max(invoice,invoice2));
		System.out.println("Object count: "+Invoice.objCnt);
	}
}

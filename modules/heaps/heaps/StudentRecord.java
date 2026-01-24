package heaps;

public class StudentRecord implements Comparable<StudentRecord> {
	
	private String Name;
	private int studentNo;
	private double gpa;
	
	private static int nextNum = 1000;
	
	public StudentRecord(String name, double gpa) {
		super();
		Name = name;
		this.studentNo = nextNum;
		nextNum++;
		this.gpa = gpa;
	}
	
	public String getName() {
		return Name;
	}

	public void setName(String name) {
		Name = name;
	}

	public double getGpa() {
		return gpa;
	}

	public void setGpa(double gpa) {
		this.gpa = gpa;
	}

	@Override
	public String toString() {
		return "[Name=" + Name + ", studentNo=" + studentNo + ", gpa=" + gpa + "]";
	}

	@Override
	public int compareTo(StudentRecord that) {
		return this.Name.compareTo(that.Name);
	}

	@Override
	public boolean equals(Object that) {
		return this.Name.equals(((StudentRecord)that).Name);
	}

}

package videoexamples.searching;

import videoexamples.searching.csc205.StudentRecord;

public class HashingExample {

	public static void main(String[] args) {
		
		StudentRecord s[] = new StudentRecord[10];
	    s[0] = new StudentRecord("Alice Fleming", 2.8);
	    s[1] = new StudentRecord("Devin Dennis", 3.1);
	    s[2] = new StudentRecord("Enrique Barrett", 3.2);
	    s[3] = new StudentRecord("Floyd Harrington", 3.5);
	    s[4] = new StudentRecord("Hector Grant", 3.4);
	    s[5] = new StudentRecord("Jennifer Reed", 3.7);
	    s[6] = new StudentRecord("Levi Castillo", 3.0);
	    s[7] = new StudentRecord("Ollie Ramirez", 3.9);
	    s[8] = new StudentRecord("Roy Cobb", 2.0);
	    s[9] = new StudentRecord("Whitney Carroll", 4.0);
	    
		System.out.println("hashString1:");
		System.out.println("Hash of hello: " + hashString("hello"));
		System.out.println("Hash of jello: " + hashString("jello"));
	    System.out.println("Hash of HELLO: " + hashString("HELLO"));
	    System.out.println("Hash of Arizona: " + hashString("Arizona"));
	    System.out.println("Hash of Computers: " + hashString("Computer"));
	    System.out.println("Hash of city: " + hashString("city"));

		System.out.println();
		System.out.println("hashString2:");
		System.out.println("Hash of hello: " + hashString2("hello"));
		System.out.println("Hash of jello: " + hashString2("jello"));
	    System.out.println("Hash of HELLO: " + hashString2("HELLO"));
	    System.out.println("Hash of Arizona: " + hashString2("Arizona"));
	    System.out.println("Hash of Computers: " + hashString2("Computer"));

		System.out.println();
		System.out.println("StudentRecord.hashCode:");
		for(StudentRecord student : s) {
			System.out.println("  " + student + "  hashCode=" + student.hashCode());
		}
	}

	public static int hashString(String s) {
		int hash = 0;
		
		if (s.length() > 0) {
			hash += s.charAt(0);   // char is integer type
		}
		if (s.length() > 1) {
			hash += s.charAt(1); 
		}
		if (s.length() > 4) {
			hash += s.charAt(4); 
		}
		
		hash = (hash * hash) - (s.length() * 2);
		
		return hash;
	}

	public static int hashString2(String s) {
		int hash = 0;
		for (int ii=0;ii<s.length();ii++) {
			hash += s.charAt(ii);
		}
		
		hash *= (s.charAt(s.length()-1) - (s.length() * s.length()));

		return hash;
	}
}

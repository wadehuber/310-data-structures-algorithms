package priorityqueue;
/** 
 * Tests a priority queue.
 * 
 * @author Java Foundations
 */
public class PQTester
{
	public static void main(String[] args)
	{
		PriorityQueue<String> pq = new PriorityQueue<String>();
		
		pq.addElement("first", 1);
		pq.addElement("bbb", 200);
		pq.addElement("third", 50);
		pq.addElement("fifth", 92);
		pq.addElement("second", 10);
		pq.addElement("fourth", 55);
		pq.addElement("aaa", 200);
		pq.addElement("this one should be first", 0);

		while (!pq.isEmpty())
		{
			System.out.println(pq.removeNext());
		}
	}
}

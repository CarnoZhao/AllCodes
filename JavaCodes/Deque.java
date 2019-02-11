import java.util.Iterator;

public class Deque<Item> implements Iterable<Item>{
	public class Node{
		Item item;
		Node prev;
		Node next;
	}
	private Node start;
	private Node end;
	private Node current = start;
	private int lenth;
	public Deque(){
		Node start = new Node();
		start.item = null;
		Node end = start;
		int lenth = 0;
	}                           // construct an empty deque
	public boolean isEmpty(){
		return start.item == null && end.item == null;
	}                 // is the deque empty?
	public int size(){
		return lenth;
	}                        // return the number of items on the deque
	public void addFirst(Item item){
		Node nex = new Node();
		nex.item = item;
		start.next = nex;
		nex.prev = start;
		start = nex;
		lenth += 1;
	}          // add the item to the front
	public void addLast(Item item){
		Node nex = new Node();
		nex.item = item;
		nex.next = end;
		end.prev = nex;
		end = nex;
		lenth += 1;
	}           // add the item to the end
	public Item removeFirst(){
		Item ret;
		ret = start.item;
		start.prev.next = null;
		lenth -= 1;
		return ret;
	}                // remove and return the item from the front
	public Item removeLast(){
		Item ret;
		ret = end.item;
		end.next.prev = null;
		lenth -= 1;
		return ret;
	}                 // remove and return the item from the end
	public Iterator<Item> iterator(){
		public Item next(){
			Item item = current.item;
			current = current.prev;
			return item;
		}
	}         // return an iterator over items in order from front to end
	public static void main(String[] args){
		;
	}   // unit testing (optional)
}
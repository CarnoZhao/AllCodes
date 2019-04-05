import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item>{
	private int size;
	private Node first = new Node(null);
	private Node last = new Node(null);
	private class Node{
		Item item;
		Node next;
		Node prev;
		Node(Item val){
			this.item = val;
		}
	}
	public Deque(){
		first.prev = last;
		last.next = first;
		int size = 0;
	}
	public boolean isEmpty(){
		return size == 0;
	}
	public int size(){
		return size;
	}
	public void addFirst(Item item){
		if(item == null) throw new java.lang.IllegalArgumentException();
		Node newNode = new Node(item);
		Node oldfirst = first.prev;
		newNode.prev = oldfirst;
		oldfirst.next = newNode;
		first.prev = newNode;
		newNode.next = first;
		size ++;
	}
	public void addLast(Item item){
		if(item == null) throw new java.lang.IllegalArgumentException();
		Node newNode = new Node(item);
		Node oldlast = last.next;
		newNode.next = oldlast;
		oldlast.prev = newNode;
		last.next = newNode;
		newNode.prev = last;
		size ++;
	}
	public Item removeFirst(){
		if(size == 0) throw new java.util.NoSuchElementException();
		Item ret = first.prev.item;
		first.prev = first.prev.prev;
		first.prev.next = first;
		size --;
		return ret;
	}
	public Item removeLast(){
		if(size == 0) throw new java.util.NoSuchElementException();
		Item ret = last.next.item;
		last.next = last.next.next;
		last.next.prev = last;
		size --;
		return ret;
	}
	public Iterator<Item> iterator(){
		return new DequeIterator();
	}
	private class DequeIterator implements Iterator<Item>{
		private Node current = first.prev;
		public boolean hasNext(){
			return current.item != null;
		}
		public void remove(){
			throw new java.lang.UnsupportedOperationException();
		}
		public Item next(){
			if(!hasNext()) throw new java.util.NoSuchElementException();
			Item item = current.item;
			current = current.prev;
			return item;
		}
	}
	public static void main(String[] args){
		;
	}
}
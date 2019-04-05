import java.util.Iterator;
import edu.princeton.cs.algs4.StdRandom;
import java.util.NoSuchElementException;


public class RandomizedQueue<Item> implements Iterable<Item>{
	private Item[] list;
	private int size = 1;
	private int current = 0;
	public RandomizedQueue(){
		list = (Item[]) new Object[size];
	}
	public boolean isEmpty(){
		return current == 0;
	}
	public int size(){
		return current;
	}
	public void enqueue(Item item){
		if (item == null) throw new java.lang.IllegalArgumentException();
		if (current == size){
			Item[] oldlist = list;
			list = (Item[]) new Object[size * 2];
			for (int i = 0; i < oldlist.length; i ++){
				list[i] = oldlist[i];
			}
			size = size * 2;
		}
		list[current] = item;
		current ++;
	}
	public Item dequeue(){
		if (isEmpty()) throw new NoSuchElementException();
		if (current == size / 4){
			Item[] oldlist = list;
			list = (Item[]) new Object[size / 2];
			for (int i = 0; i < current; i ++){
				list[i] = oldlist[i];
			}
			size = size / 2;
		}
		int randompos = StdRandom.uniform(current);
		Item ret = list[randompos];
		current --;
		list[randompos] = list[current];
		return ret;
	}
	public Item sample(){
		if (isEmpty()) throw new NoSuchElementException();
		return list[StdRandom.uniform(current)];
	}
	public Iterator<Item> iterator(){
		return new RandomIterator();
	}
	private class RandomIterator implements Iterator<Item>{
		private int i = 0;
		private int[] randomchoose = makeRandom();
		private int[] makeRandom(){
			int[] randomchoose = new int[current];
			for (int pos = 0; pos < current; pos ++){
				randomchoose[pos] = pos;
			}
			StdRandom.shuffle(randomchoose);
			return randomchoose;
		}
		public boolean hasNext(){
			return i != current;
		}
		public void remove(){
			throw new java.lang.UnsupportedOperationException();
		}
		public Item next(){
			if (!hasNext()) throw new NoSuchElementException();
			Item ret = list[randomchoose[i]];
			i ++;
			return ret;
		}
	}
	public static void main(String[] args){
		/*Iterator it;
		Scanner in = new Scanner(System.in);
		RandommizedQueue<Integer> rq = new RandommizedQueue<Integer>();
		while (true){
			int x = in.nextInt();
			if (x != -1){
				rq.enqueue(x);
			} else{
				int out = rq.dequeue();
				System.out.println("Dequeue Out:" + out);
			}
			it = rq.iterator();
			System.out.print("Queue:");
			while (it.hasNext()){
				System.out.print(it.next() + " ");
			}
			System.out.println();
		}*/;
	}
}
import java.util.Iterable;
import edu.princeton.cs.algs4.StdRandom;
import java.util.NoSuchElementExpectation;

public class RandommizedQueue<Item> implements Iterable<Item>{
	private Item[] list;
	private int size = 0;
	private int current = 0;
	public RandommizedQueue(){
		list = new Item[0];
	}
	public boolean isEmpty(){
		reutrn size == 0;
	}
	public int size(){
		return size;
	}
	public void enque(Item item){
		if (current >= size && size != 0){
			oldlist = list;
			Item[] list = new Item[size * 2];
			for (int i = 0; i < size; i ++){
				list[i] = oldlist[i];
			}
		} else if (size == 0){
			size ++;
		}
		list[current] = item;
		current ++;
	}
	public Item dequeque(){
		int randompos = StdRandom.uniform(current);
		Item ret = list[randompos];
		current --;
		size --;
		list[randompos] = list[current];
		return ret;
	}
	public Item sample(){
		return list[StdRandom.uniform(current)];
	}
	public Iterator<Item> iterator(){
		return new RandomIterator();
	}
	private class RandomIterator implements Iterator<Item>{
		private int i = 0;
		private int[] randomchoose = makeRandom();
		private makeRandom(){
			int[] randomchoose = new int[current];
			for (int pos = 0; pos < current - 1; pos ++){
				randomchoose[pos] = StdRandom.uniform(current)
			}
		}
		public hasNext(){
			return i == current - 1;
		}
		public remove(){
			throw new java.util.NoSuchElementExpectation();
		}
		public next(){
			Item ret = list[randomchoose[i]];
			i ++;
			return ret;
		}
	}
}
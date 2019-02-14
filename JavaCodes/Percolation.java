import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation{
	private boolean[] openstate;
	private WeightedQuickUnionUF fullstate;
	private WeightedQuickUnionUF backwash;
	private int width;
	private int numofopen = 0;

	public Percolation(int n){
		if (n <= 0) throw new java.lang.IllegalArgumentException();
		openstate = new boolean[n * n + 2];
		openstate[0] = true;
		fullstate = new WeightedQuickUnionUF(n * n + 2);
		backwash = new WeightedQuickUnionUF(n * n + 1);
		width = n;
	}
	private void unionFunc(int row, int col, WeightedQuickUnionUF wqu){
		if (row == 1) wqu.union(col, 0);
		if (row != 1 && isOpen(row - 1, col)) wqu.union((row - 1) * width + col, (row - 2) * width + col);
		if (row != width && isOpen(row + 1, col)) wqu.union((row - 1) * width + col, row * width + col);
		if (col != 1 && isOpen(row, col - 1)) wqu.union((row - 1) * width + col, (row - 1) * width + col - 1);
		if (col != width && isOpen(row, col + 1)) wqu.union((row - 1) * width + col, (row - 1) * width + col + 1);
	}
	public void open(int row, int col){
		if (row <= 0 || col <= 0 || row > width || col > width) throw new java.lang.IllegalArgumentException();
		if(!isOpen(row, col)){
			numofopen ++;
			openstate[(row - 1) * width + col] = true;
			unionFunc(row, col, backwash);
			unionFunc(row, col, fullstate);
			if (row == width) fullstate.union((row - 1) * width + col, width * width + 1);
		}
	}
	public boolean isOpen(int row, int col){
		if (row <= 0 || col <= 0 || row > width || col > width) throw new java.lang.IllegalArgumentException();
		return openstate[(row - 1) * width + col];
	}
	public boolean isFull(int row, int col){
		if (row <= 0 || col <= 0 || row > width || col > width) throw new java.lang.IllegalArgumentException();
		return fullstate.connected((row - 1) * width + col, 0) && backwash.connected((row - 1) * width + col, 0);
	}
	public int numberOfOpenSites(){
		return numofopen;
	}
	public boolean percolates(){
		return fullstate.connected(width * width + 1, 0);
	}
}
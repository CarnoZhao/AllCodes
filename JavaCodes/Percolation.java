import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation{
	private boolean[] openstate;
	private WeightedQuickUnionUF fullstate;
	private int width;

	public Percolation(int n){
		if (n <= 0) throw new java.lang.IllegalArgumentException();
		openstate = new boolean[n * n + 1];
		openstate[0] = true;
		fullstate = new WeightedQuickUnionUF(n * n + 1);
		width = n;
	}
	public void open(int row, int col){
		if (row <= 0 || col <= 0 || row > width || col > width) throw new java.lang.IllegalArgumentException();
		openstate[(row - 1) * width + col] = true;
		if (row == 1) fullstate.union(col, 0);
		if (row != 1 && isOpen(row - 1, col)) fullstate.union((row - 1) * width + col, (row - 2) * width + col);
		if (row != width && isOpen(row + 1, col)) fullstate.union((row - 1) * width + col, row * width + col);
		if (col != 1 && isOpen(row, col - 1)) fullstate.union((row - 1) * width + col, (row - 1) * width + col - 1);
		if (col != width && isOpen(row, col + 1)) fullstate.union((row - 1) * width + col, (row - 1) * width + col + 1);
	}
	public boolean isOpen(int row, int col){
		if (row <= 0 || col <= 0 || row > width || col > width) throw new java.lang.IllegalArgumentException();
		return openstate[(row - 1) * width + col];
	}
	public boolean isFull(int row, int col){
		if (row <= 0 || col <= 0 || row > width || col > width) throw new java.lang.IllegalArgumentException();
		return fullstate.connected((row - 1) * width + col, 0);
	}
	public int numberOfOpenSites(){
		int cnt = 0;
		for (boolean i : openstate){
			if (i) cnt ++;
		}
		return cnt - 1;
	}
	public boolean percolates(){
		boolean ret = false;
		for (int j = 0; j < width; j ++){
			if (fullstate.connected((width - 1) * width + j + 1, 0)){
				ret = true;
				break;
			}
		}
		return ret;
	}
}
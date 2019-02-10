import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class PercolationStats {
	private double[] nums;
	private int times;
	private int width;
	private final double CONFIDENCE_95 = 1.96;

	public PercolationStats(int n, int trials){
		if (n <= 0 || trials <= 0) throw new java.lang.IllegalArgumentException();
		width = n;
		times = trials;
		nums = new double[trials];
		for (int i = 0; i < trials; i ++){
			Percolation p = new Percolation(n);
			while (!p.percolates()){
				int row = StdRandom.uniform(n) + 1;
				int col = StdRandom.uniform(n) + 1;
				p.open(row, col);
			}
			nums[i] = (double)p.numberOfOpenSites() / (n * n);
		}
	}
	public double mean(){
		return StdStats.mean(nums);
	}
	public double stddev(){
		return StdStats.stddev(nums);
	}
	public double confidenceLo(){
		return mean() - CONFIDENCE_95 * stddev() / Math.sqrt(times);
	}
	public double confidenceHi(){
		return mean() + CONFIDENCE_95 * stddev() / Math.sqrt(times);
	}

	public static void main(String[] args){
		int n = StdIn.readInt();
		int trials = StdIn.readInt();
		PercolationStats ps = new PercolationStats(n, trials);
		StdOut.println("mean = " + ps.mean());  
		StdOut.println("stddev = " + ps.stddev());  
		StdOut.println("95% confidence interval " + ps.confidenceLo() + ", " + ps.confidenceHi());
	}
}
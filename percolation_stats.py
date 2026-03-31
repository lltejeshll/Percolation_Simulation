import random
from percolation import Percolation

class PercolationStats:
    """
    Runs T independent trials on an N x N grid to compute the percolation threshold.
    """
    def __init__(self, n, t):
        # Validate inputs according to the API constraints
        if n <= 0 or t <= 0:
            raise ValueError("Grid size N and number of trials T must be greater than 0")
            
        self.n = n
        self.t = t
        self.thresholds = []  # Array to store the threshold fraction for each trial
        
        self._run_trials()

    def _run_trials(self):
        """Executes the Monte Carlo simulation."""
        total_sites = self.n * self.n
        
        for _ in range(self.t):
            # 1. Initialize a completely blocked N by N grid for each trial
            perc = Percolation(self.n)
            
            # 2. Keep opening random sites until the system percolates
            while not perc.percolates():
                # Generate random coordinates (1-based indexing)
                row = random.randint(1, self.n)
                col = random.randint(1, self.n)
                
                # If the site is already open, the loop continues and picks again
                if not perc.is_open(row, col):
                    perc.open(row, col)
                    
            # 3. Record the fraction of open sites when percolation finally occurs
            fraction = perc.number_of_open_sites() / total_sites
            self.thresholds.append(fraction)

    # -------------------------------------------------------------------------
    # Phase 5 Stubs: Student B will implement the statistical math methods below
    # -------------------------------------------------------------------------
    
    def mean(self):
        """Sample mean of percolation threshold."""
        return sum(self.thresholds) / self.t

    def stddev(self):
        """Sample standard deviation of percolation threshold."""
        # Standard deviation is undefined for a single trial
        if self.t == 1:
            return float('nan')
       
        current_mean = self.mean()
        variance = sum((x - current_mean) ** 2 for x in self.thresholds) / (self.t - 1)
        return math.sqrt(variance)

    def confidenceLo(self):
        """Low endpoint of 95% confidence interval."""
        return self.mean() - ((1.96 * self.stddev()) / math.sqrt(self.t))

    def confidenceHi(self):
        """High endpoint of 95% confidence interval."""
        return self.mean() + ((1.96 * self.stddev()) / math.sqrt(self.t))
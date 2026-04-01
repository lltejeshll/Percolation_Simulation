### Phase 3: Percolation Connection Logic

* **The problem we were stuck on:** We needed an efficient way to connect newly opened grid sites to their adjacent open neighbors without writing repetitive, nested `if` statements for boundary checks. We also needed to dynamically connect the top and bottom rows to the Virtual Top and Virtual Bottom sites to evaluate system percolation in constant time.

* **The exact prompt used:** "Write the Python logic for the open() and percolates() methods in a Percolation Simulation. It needs to check up, down, left, and right neighbors and use a Union-Find object to connect them if they are open. It also needs to connect row 1 to a virtual top site and row N to a virtual bottom site."

* **How we modified the AI's output to fit the Sedgewick API constraints:** The raw AI output attempted to use standard 0-based Python indexing (e.g., checking `row == 0` for the top row). To enforce the strict 1-based indexing required by the Sedgewick API constraints, we modified the code to check `row == 1` and `row == self.n`. We also had to discard the AI's custom coordinate math and route all ID generations through our pre-established `_get_1d_index(row, col)` helper method to maintain encapsulation.

### Phase 1: Grid Scaffold & Union-Find Implementation
* **The problem we were stuck on:** We needed to translate the Sedgewick Java `WeightedQuickUnionUF` API into Python from scratch, including path compression and array size balancing.
* **The exact prompt used:** "Write a Python UnionFind class that implements weighted quick union with path compression. Also provide the boilerplate for a Percolation class that initializes an N by N grid and maps it to a 1D UnionFind array of size N^2 + 2."
* **How we modified the AI's output:** We integrated the AI's UnionFind class directly but had to manually adjust the `Percolation` constructor to ensure the virtual top and bottom sites were assigned the exact indices `N^2` and `N^2 + 1` to match our planned architecture.

### Phase 4: Monte Carlo Simulation Loop
* **The problem we were stuck on:** Creating an efficient `while` loop to randomly open blocked sites without accidentally recounting already open sites or throwing out-of-bounds errors.
* **The exact prompt used:** "Write the `_run_trials()` loop for PercolationStats in Python. It needs to loop T times. Inside each loop, pick random row and col values between 1 and N, open the site if it's blocked, and stop when the system percolates."
* **How we modified the AI's output:** The AI tried to use `random.randrange(0, n)`. We changed this to `random.randint(1, self.n)` to strictly enforce the 1-based indexing required by our API.

### Phase 5: Statistical Calculations
* **The problem we were stuck on:** Translating the mathematical formulas for standard deviation and 95% confidence intervals into Python code.
* **The exact prompt used:** "Write the mean, stddev, confidenceLo, and confidenceHi methods in Python based on an array of threshold fractions. Use the standard 1.96 multiplier for the confidence interval."
* **How we modified the AI's output:** We added an explicit edge-case check in the `stddev()` method to return `float('nan')` if `self.t == 1` to prevent a `ZeroDivisionError`, which the raw AI output failed to account for.
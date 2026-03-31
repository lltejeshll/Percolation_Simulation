### Phase 3: Percolation Connection Logic

* **The problem we were stuck on:** We needed an efficient way to connect newly opened grid sites to their adjacent open neighbors without writing repetitive, nested `if` statements for boundary checks. We also needed to dynamically connect the top and bottom rows to the Virtual Top and Virtual Bottom sites to evaluate system percolation in constant time.

* **The exact prompt used:** "Write the Python logic for the open() and percolates() methods in a Percolation Simulation. It needs to check up, down, left, and right neighbors and use a Union-Find object to connect them if they are open. It also needs to connect row 1 to a virtual top site and row N to a virtual bottom site."

* **How we modified the AI's output to fit the Sedgewick API constraints:** The raw AI output attempted to use standard 0-based Python indexing (e.g., checking `row == 0` for the top row). To enforce the strict 1-based indexing required by the Sedgewick API constraints, we modified the code to check `row == 1` and `row == self.n`. We also had to discard the AI's custom coordinate math and route all ID generations through our pre-established `_get_1d_index(row, col)` helper method to maintain encapsulation.

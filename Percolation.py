class UnionFind:
    """
    Skeleton for Weighted Quick Union with Path Compression.
    (This replaces the algs4.WeightedQuickUnionUF Java library).
    """
    def __init__(self, n):
        # Initialize parent array and size array for balancing
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, p):
        # TODO: Implement path compression
        pass

    def union(self, p, q):
        # TODO: Implement weighted union logic
        pass

    def connected(self, p, q):
        # TODO: Return True if p and q have the same root
        pass


class Percolation:
    """
    Models a percolation system using an N by N grid.
    """
    def __init__(self, n):
        if n <= 0:
            raise ValueError("Grid size N must be greater than 0")
            
        self.n = n
        self.open_sites_count = 0
        
        # 1. Initialize the 2D boolean array to encapsulate grid state.
        # False means the site is blocked, True means it is open.
        self.grid = [[False] * n for _ in range(n)]
        
        # 2. Initialize the 1D Union-Find object.
        # We need N*N standard sites, PLUS 2 extra sites for the optimization trick:
        # a "Virtual Top" site and a "Virtual Bottom" site.
        total_sites = n * n
        self.uf = UnionFind(total_sites + 2)
        
        # Define the specific 1D indices for the virtual sites
        self.virtual_top = total_sites         # Index N^2
        self.virtual_bottom = total_sites + 1  # Index N^2 + 1

    def _get_1d_index(self, row, col):
        """
        Private helper method to map 1-based 2D coordinates 
        to a 0-based 1D array index for the Union-Find object.
        """
        return (row - 1) * self.n + (col - 1)

    def open(self, row, col):
        """
        Opens the site at (row, col) if it is not open already.
        Student B will implement the connection logic here.
        """
        pass

    def is_open(self, row, col):
        """Returns True if the site at (row, col) is open."""
        pass

    def is_full(self, row, col):
        """
        Returns True if the site is connected to the virtual top site.
        """
        pass

    def number_of_open_sites(self):
        """Returns the total number of open sites."""
        return self.open_sites_count

    def percolates(self):
        """
        Returns True if the system percolates (virtual top connects to virtual bottom).
        """
        pass
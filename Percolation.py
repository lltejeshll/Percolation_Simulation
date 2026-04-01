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
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        # TODO: Implement weighted union logic
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
            
        # Weighted tree balancing: link the smaller tree to the larger tree
        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]

    def connected(self, p, q):
        # TODO: Return True if p and q have the same root
        return self.find(p) == self.find(q)


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
            Connects the newly opened site to all adjacent open sites.
            """
            if row < 1 or row > self.n or col < 1 or col > self.n:
                raise ValueError("Index out of bounds")
            
            if self.is_open(row, col):
                return
            
            # 1. Open the site and update the counter
            self.grid[row - 1][col - 1] = True
            self.open_sites_count += 1
        
            current_id = self._get_1d_index(row, col)
        
            # 2. Connect to Virtual Top if it is in the first row
            if row == 1:
                self.uf.union(current_id, self.virtual_top)
            
            # 3. Connect to Virtual Bottom if it is in the last row
            if row == self.n:
                self.uf.union(current_id, self.virtual_bottom)
            
            # 4. Connect to open neighbors (Up, Down, Left, Right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                adj_row, adj_col = row + dr, col + dc
                # Check if the neighbor is within the grid boundaries
                if 1 <= adj_row <= self.n and 1 <= adj_col <= self.n:
                    if self.is_open(adj_row, adj_col):
                        adj_id = self._get_1d_index(adj_row, adj_col)
                        self.uf.union(current_id, adj_id)

    def is_open(self, row, col):
        """Returns True if the site at (row, col) is open."""
        if row < 1 or row > self.n or col < 1 or col > self.n:
            raise ValueError("Index out of bounds")
        return self.grid[row - 1][col - 1]

    def is_full(self, row, col):
        """
        Returns True if the site is connected to the virtual top site.
        """
        if row < 1 or row > self.n or col < 1 or col > self.n:
            raise ValueError("Index out of bounds")
    
        # A site cannot be full if it isn't even open
        if not self.is_open(row, col):
            return False
        
        current_id = self._get_1d_index(row, col)
        return self.uf.connected(current_id, self.virtual_top)

    def number_of_open_sites(self):
        """Returns the total number of open sites."""
        return self.open_sites_count

    def percolates(self):
        """
        Returns True if the system percolates (virtual top connects to virtual bottom).
        """
        # Edge case: A 1x1 grid that is blocked shouldn't percolate
        if self.n == 1 and not self.is_open(1, 1):
            return False
        
        return self.uf.connected(self.virtual_top, self.virtual_bottom)

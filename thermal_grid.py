import numpy as np
from random import randint


class thermal_grid:
    """
    A 2D grid, whose elements are integer values representing units of energy,
        equipped with methods to move units from one grid site to another
    Parent class constructor takes in a 2D grid of integers to initialize
    """
    def __init__(self, initial_state):
        self.x = np.shape(initial_state)[0]
        self.y = np.shape(initial_state)[1]
        self.state = initial_state.copy()


    def exchange(self, site1, site2):
        """Exchanges a unit from `site1` to `site2`"""
        if self.state[site1] != 0:
            self.state[site1] -= 1
            self.state[site2] += 1


    def rand_site(self):
        """Returns coordinates of a randomly chosen site on the grid"""
        return (randint(0, self.x-1), randint(0, self.y-1))


    def exchange_rand(self):
        """Chooses a random pair of sites to exchange between"""
        site1 = self.rand_site()
        # Make sure we aren't starting from a site with zero energy
        while self.state[site1] == 0:
            site1 = self.rand_site()

        site2 = self.rand_site()
        # Make sure we don't pick the same site twice
        while site2 == site1:
            site2 = self.rand_site()

        self.exchange(site1, site2)


    def exchange_rand_nn(self, skip_invalid_exchanges=False):
        """Chooses a random pair of *neighboring* sites to exchange between"""
        site1 = self.rand_site()
        # Make sure we aren't starting from a site with zero energy
        while self.state[site1] == 0:
            site1 = self.rand_site()

        # Decide direction to move
        x_or_y = 'x' if randint(0, 1) else 'y'
        plus_or_minus = 2*randint(0, 1)-1  # +1 or -1

        # Consider edge cases (hah) where we just chose to try to move energy from the edge to off the grid
        valid_exchange = True
        if not skip_invalid_exchanges:
            # Check if the chosen exchange is invalid, and change it into a valid one if so
            if site1[0] == 0:
                if x_or_y == 'x': plus_or_minus = 1
            elif site1[0] == self.x-1:
                if x_or_y == 'x': plus_or_minus = -1
            if site1[1] == 0:
                if x_or_y == 'y': plus_or_minus = 1
            elif site1[1] == self.y-1:
                if x_or_y == 'y': plus_or_minus = -1
        else:
            # Check if the chosen exchange is invalid, and throw it away if so
            if site1[0] == 0 and x_or_y == 'x' and plus_or_minus == -1:
                valid_exchange = False
            elif site1[0] == self.x-1 and x_or_y == 'x' and plus_or_minus == 1:
                valid_exchange = False
            if site1[1] == 0 and x_or_y == 'y' and plus_or_minus == -1:
                valid_exchange = False
            elif site1[1] == self.y-1 and x_or_y == 'y' and plus_or_minus == 1:
                valid_exchange = False

        # Define the chosen neighbor site
        if x_or_y == 'x':
            site2 = (site1[0]+plus_or_minus, site1[1])
        elif x_or_y == 'y':
            site2 = (site1[0], site1[1]+plus_or_minus)
        
        if valid_exchange:
            self.exchange(site1, site2)


class thermal_grid_uniform(thermal_grid):
    """
    Initializes a `thermal_grid` with an equal number of units on each site
    `x, y` are grid dimensions
    `energy_per_site` is the amount of energy units to initialize on each site
    """
    def __init__(self, x, y, energy_per_site):
        initial_state = energy_per_site*np.ones((x, y), dtype=int)
        super().__init__(initial_state)


class thermal_grid_uniform_subgrid(thermal_grid):
    """
    Initializes a `thermal_grid` with an equal number (`energy_per_site`) of units on a `x_sub` x `y_sub` subgrid,
        and zero in the rest
    `x, y` are grid dimensions
    `x_sub, y_sub` are subgrid dimensions
    `energy_per_site` is the amount of energy units to initialize on each site of the subgrid
    """
    def __init__(self, x, y, x_sub, y_sub, energy_per_site):
        initial_state = np.array([[energy_per_site if j<y_sub else 0 for j in range(y)] if i<x_sub else [0]*y for i in range(x)], dtype=int)
        super().__init__(initial_state)


class thermal_grid_allinone(thermal_grid):
    """
    Initializes a `thermal_grid` with some number (`energy`) of energy units on a single site
    `x, y` are grid dimensions
    `site` is a 2-tuple defining the x and y coordinates of the site to place the energy
    `energy` is the number of energy units to place at site `site`
    """
    def __init__(self, x, y, site, energy):
        initial_state = np.zeros((x, y))
        initial_state[site] = energy
        super().__init__(initial_state)
from pygeogrids import BasicGrid
from ease_grid import EASE2_grid
import numpy as np

def EASE01CellGrid():
    ease01 = EASE2_grid(1000)
    lons, lats = np.meshgrid(ease01.londim, ease01.latdim)
    lats = np.flipud(lats) # flip lats, so that origin in bottom left
    grid = BasicGrid(lons.flatten(), lats.flatten(),
                     shape=(ease01.londim.size, ease01.latdim.size)).to_cell_grid(5., 5.)

    return grid
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

def plot_heatmap(grid):
    return sns.heatmap(grid, cmap = "Reds", alpha = 0.5, zorder = 2, annot=True, annot_kws={"size": 7})

def generate_grid(x,y,z, numBins):
    x_min = min(x)
    x_max = max(x)
    x_binSize = math.ceil((x_max - x_min)/numBins)
    
    y_min = min(y)
    y_max = max(y)
    y_binSize = math.ceil((y_max - y_min)/numBins)
    
    zero_data = np.zeros(shape=(numBins,numBins))
    grid = pd.DataFrame(zero_data, columns=list(range(numBins)))
    
    correction = .0001
    
    for i in range(len(x)):
        x[i] = math.ceil((x[i] + correction - x_min)/x_binSize) - 1
        y[i] = math.ceil((y[i] + correction - y_min)/y_binSize) - 1
        grid.loc[x[i],y[i]] = grid.loc[x[i],y[i]] + z[i]
    
    return grid

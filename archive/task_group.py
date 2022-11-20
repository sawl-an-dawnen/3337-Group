import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from folderScanner import list_files
from animate_hotspots import generate_windows, plot_hotspot, generate_windows_filtered

pointCount = 50000 #plot dpi
windowSize = 3 #how many batches to include in each window
frameRate = 6 #frameRate of the animation
plotType = "nearest"
my_files_list = list_files('earthquake_contiguous_usa_12batch', '.csv') #list of all batches names
windows = generate_windows(my_files_list, windowSize) #all window dataframes


w_depth = .3 
w_mag = .7

windows_d1, windows_d2 = generate_windows_filtered(windows,.3,.7)
#print("----------------------------------------------------------------------")
    
# function that draws each frame of the animation
def animate(i):
    ax.clear()
    plot_hotspot(windows[i], pointCount, plotType)

# create the figure and axes objects
fig, ax = plt.subplots()
plot = plot_hotspot(windows[0], pointCount, plotType)
plot.colorbar(label='Magnitude * Depth')
# run the animation
ani = FuncAnimation(fig, animate, frames=len(windows), interval=500, repeat=True)

#save the animation
f = "animation.gif" 
writergif = PillowWriter(fps=frameRate) 
ani.save(f, writer=writergif)

    




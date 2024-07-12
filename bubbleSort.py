import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
# Requires installation of matplotlib through command prompt
# pip install matplotlib numpy

# Determines the number of bars on the plot
amount = 25

# Generate a list of 25 unique integers from 1 to 25
list = np.random.choice(np.arange(1, 26), amount, replace=False)
x = np.arange(0, amount, 1)

# Initialize variables for bubble sort
n = len(list)   # Length of the list
i = 0           # Outer loop index for bubble sort
j = 0           # Inner loop index for bubble sort

# Set up the figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
ax.set_title('Bubble Sort Visualization')

# Function to update the plot with highlighting and labels
def update_plot():
    ax.clear()  # Clear the current plot
    
    # Determine colors for bars: blue for unselected, red for selected
    colors = ['grey' if idx != j and idx != j + 1 else 'red' for idx in range(n)]
    bars = ax.bar(x, list, color=colors)  # Plot bars with determined colors
    
    ax.set_xlim(-0.5, amount - 0.5)  # Set x-axis limits
    ax.set_ylim(0, max(list) + 1)    # Set y-axis limits slightly above max value
    
    # Add text labels above each bar with their respective values
    for bar, value in zip(bars, list):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), str(value),
                ha='center', va='bottom', color='black', fontsize=8)
    
    fig.canvas.draw()  # Update the figure canvas

# Initial plot with labels and colors
update_plot()

# Function to perform one step of bubble sort
def bubble_sort_step(event):
    global i, j, list, n
    
    if i < n:   # Check if outer loop index is within bounds
        if j < n - i - 1:  # Check if inner loop index is within bounds
            if list[j] > list[j + 1]:   # Compare adjacent elements
                list[j], list[j + 1] = list[j + 1], list[j]   # Swap if necessary
            
            j += 1  # Move to the next pair of elements
            update_plot()   # Update plot to reflect current state
        else:
            j = 0   # Reset inner loop index
            i += 1  # Move to the next iteration of the outer loop
            
            if i == n:
                next_button.label.set_text('Done')   # Change button label when sorting is complete

# Function to reset the array and restart the visualization
def reset_array(event):
    global list, i, j, n
    list = np.random.choice(np.arange(1, 26), amount, replace=False)  # Generate new random array
    i = 0   # Reset outer loop index
    j = 0   # Reset inner loop index
    update_plot()   # Update plot with new array

# Add button to trigger the next iteration
axnext = plt.axes([0.7, 0.05, 0.1, 0.075])  # Dimensions and coordinates for the next button
next_button = Button(axnext, 'Step')
next_button.on_clicked(bubble_sort_step)   # Assign function to next button click event

# Add button to reset the array
axreset = plt.axes([0.81, 0.05, 0.1, 0.075])  # Dimensions and coordinates for the reset button
reset_button = Button(axreset, 'Reset')
reset_button.on_clicked(reset_array)   # Assign function to reset button click event

# Show the plot
plt.show()

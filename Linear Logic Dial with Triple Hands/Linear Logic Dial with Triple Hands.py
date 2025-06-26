import numpy as np
import matplotlib.pyplot as plt

def plot_linear_gauge(positive_value, negative_value, third_value):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 4))  # Adjusting for a wide linear layout
    
    # Set up the linear dial, now with negative values
    max_value = 100
    min_value = -100
    ax.set_xlim(min_value, max_value)
    ax.set_ylim(-1, 1)
    
    # Draw the linear dial with tick marks for both negative and positive values
    tick_positions = np.linspace(min_value, max_value, 21)
    for i in range(min_value, max_value + 1, 10):
        ax.text(i, -0.2, str(i), ha='center', va='center')
        ax.plot([i, i], [-0.05, 0.05], color='black')  # Small vertical ticks
    
    # Plot the hands
    ax.plot([positive_value, positive_value], [0, 0.3], color='green', lw=4, label=f'Positive: {positive_value}')
    ax.plot([negative_value, negative_value], [0, -0.3], color='red', lw=4, label=f'Negative: {negative_value}')
    ax.plot([third_value, third_value], [0, 0.3], color='blue', lw=4, label=f'Third: {third_value}', linestyle='--')

    # Plot the base line for the linear dial
    ax.plot([min_value, max_value], [0, 0], color='black', lw=2)
    
    # Add legend on the right side of the dial
    ax.text(max_value + 20, 0.2, str(positive_value), ha='center', fontsize=12, color='green')
    ax.text(max_value + 20, -0.2, str(negative_value), ha='center', fontsize=12, color='red')
    ax.text(max_value + 20, 0, str(third_value), ha='center', fontsize=12, color='blue')
    ax.plot([max_value + 15, max_value + 25], [0, 0], color='black', lw=2)  # Dividing line for legend

    # Set limits and hide axes
    ax.set_xlim(min_value - 20, max_value + 30)  # Leave room for the legend
    ax.set_ylim(-0.5, 0.5)
    ax.axis('off')
    
    # Set the title
    plt.title('Linear Logic Gauge with Three Hands')
    
    # Show the plot
    plt.show()

# Test the linear gauge with three hands and example values
plot_linear_gauge(40, -80, 20)

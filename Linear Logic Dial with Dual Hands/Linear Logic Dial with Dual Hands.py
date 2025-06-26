import numpy as np
import matplotlib.pyplot as plt

def plot_linear_gauge(positive_value, negative_value):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 4))  # Adjusting for a wide linear layout
    
    # Set up the linear dial
    max_value = 100
    ax.set_xlim(0, max_value)
    ax.set_ylim(-1, 1)
    
    # Draw the linear dial with tick marks
    tick_positions = np.linspace(0, max_value, 11)
    for i in range(0, max_value + 1, 10):
        ax.text(i, -0.2, str(i), ha='center', va='center')
        ax.plot([i, i], [-0.05, 0.05], color='black')  # Small vertical ticks
    
    # Plot the hands
    ax.plot([positive_value, positive_value], [0, 0.3], color='green', lw=4, label=f'Positive: {positive_value}')
    ax.plot([negative_value, negative_value], [0, -0.3], color='red', lw=4, label=f'Negative: {negative_value}')
    
    # Plot the base line for the linear dial
    ax.plot([0, max_value], [0, 0], color='black', lw=2)
    
    # Add legend on the right side of the dial
    ax.text(max_value + 10, 0.1, str(positive_value), ha='center', fontsize=12, color='green')
    ax.text(max_value + 10, -0.1, str(negative_value), ha='center', fontsize=12, color='red')
    ax.plot([max_value + 7, max_value + 13], [0, 0], color='black', lw=2)  # Dividing line between positive and negative

    # Set limits and hide axes
    ax.set_xlim(0, max_value + 20)  # Leave room for the legend
    ax.set_ylim(-0.5, 0.5)
    ax.axis('off')
    
    # Set the title
    plt.title('Linear Logic Gauge with Two Hands')
    
    # Show the plot
    plt.show()

# Test the linear gauge with example values
plot_linear_gauge(40, 80)

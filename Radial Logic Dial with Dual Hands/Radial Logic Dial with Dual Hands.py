import numpy as np
import matplotlib.pyplot as plt

def plot_gauge(positive_value, negative_value):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(6,6))
    
    # Adjust the spacing between the title and the gauge
    plt.subplots_adjust(top=0.75)
    
    # Create a circular gauge
    ax.set_aspect('equal', 'box')
    circle = plt.Circle((0, 0), 1, color='white', ec='black', lw=2)
    ax.add_artist(circle)
    
    # Define the dial limits
    max_value = 100
    angles_right = np.linspace(np.pi / 2, -np.pi / 2, num=max_value + 1) # Positive side (right half)
    angles_left = np.linspace(np.pi / 2, 3 * np.pi / 2, num=max_value + 1) # Negative side (left half)
    
    # Mark the ticks for the positive side (right)
    for i in range(0, max_value + 1, 10):
        angle = angles_right[i]
        x = np.cos(angle)
        y = np.sin(angle)
        ax.text(1.15*x, 1.15*y, str(i), ha='center', va='center')
    
    # Mark the ticks for the negative side (left)
    for i in range(0, 100, 10):
        angle = angles_left[i]
        x = np.cos(angle)
        y = np.sin(angle)
        ax.text(1.15*x, 1.15*y, str(-i), ha='center', va='center')

    # Add the 100 at the bottom for both sides
    bottom_angle_right = angles_right[100]
    bottom_angle_left = angles_left[100]
    
    x_right_bottom = np.cos(bottom_angle_right)
    y_right_bottom = np.sin(bottom_angle_right)
    
    ax.text(1.15*x_right_bottom, 1.15*y_right_bottom, '100', ha='center', va='center')
    
    x_left_bottom = np.cos(bottom_angle_left)
    y_left_bottom = np.sin(bottom_angle_left)
    
    ax.text(1.15*x_left_bottom, 1.15*y_left_bottom, '100', ha='center', va='center')
    
    # Plot the positive hand (green, right side)
    positive_angle = angles_right[positive_value]
    pos_x = np.cos(positive_angle)
    pos_y = np.sin(positive_angle)
    ax.plot([0, pos_x], [0, pos_y], color='green', lw=4, label=f'Positive: {positive_value}')
    
    # Plot the negative hand (red, left side)
    negative_angle = angles_left[abs(negative_value)]
    neg_x = np.cos(negative_angle)
    neg_y = np.sin(negative_angle)
    ax.plot([0, neg_x], [0, neg_y], color='red', lw=4, label=f'Negative: {negative_value}')
    
    # Draw a smaller circle in the middle to hold the legend with a white background
    inner_circle = plt.Circle((0, 0), 0.3, color='white', ec='black', lw=2, zorder=10)
    ax.add_artist(inner_circle)
    
    # Add the dividing line in the center
    ax.plot([-0.15, 0.15], [0, 0], color='black', lw=2, zorder=15)
    
    # Fix the positive and negative values with optimized spacing and padding
    legend_text_padding = 0.1  # Refined padding for better balance
    ax.text(0, legend_text_padding, str(positive_value), ha='center', va='center', fontsize=12, color='green', zorder=20)
    ax.text(0, -legend_text_padding, str(negative_value), ha='center', va='center', fontsize=12, color='red', zorder=20)
    
    # Set limits and hide axes
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')
    
    # Set the title with more space between the title and the gauge
    plt.title('Logic Gauge with Two Hands', pad=40)
    
    # Show the plot
    plt.show()

# Test the gauge with example values
plot_gauge(40, -80)

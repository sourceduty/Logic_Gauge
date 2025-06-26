import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to create and animate the gauge
def plot_gauge():
    fig, ax = plt.subplots(figsize=(6, 6))

    # Create the gauge structure
    ax.set_aspect('equal', 'box')
    circle = plt.Circle((0, 0), 1, color='white', ec='black', lw=2)
    ax.add_artist(circle)
    
    max_value = 100
    angles_right = np.linspace(np.pi / 2, -np.pi / 2, num=max_value + 1)
    angles_left = np.linspace(np.pi / 2, 3 * np.pi / 2, num=max_value + 1)
    
    # Mark the ticks for the positive side
    for i in range(0, max_value + 1, 10):
        angle = angles_right[i]
        x = np.cos(angle)
        y = np.sin(angle)
        ax.text(1.15 * x, 1.15 * y, str(i), ha='center', va='center')
    
    # Mark the ticks for the negative side
    for i in range(0, max_value + 1, 10):
        angle = angles_left[i]
        x = np.cos(angle)
        y = np.sin(angle)
        ax.text(1.15 * x, 1.15 * y, str(-i), ha='center', va='center')

    # Add the 100 at the bottom for the right side only
    ax.text(1.15 * np.cos(angles_right[100]), 1.15 * np.sin(angles_right[100]), '100', ha='center')
    
    # Plot a smaller circle for the center
    inner_circle = plt.Circle((0, 0), 0.3, color='white', ec='black', lw=2, zorder=10)
    ax.add_artist(inner_circle)

    # Add the dividing line in the center with vertical padding
    padding = 0.2  # Horizontal padding for the line (length of the line)
    vertical_padding = 0.01  # Adjusted vertical padding (distance above and below the center)
    
    # Line with vertical offset
    ax.plot([-padding, padding], [vertical_padding, vertical_padding], color='black', lw=2, zorder=15)
    
    # Create line objects for the hands (we will update these in the animation)
    positive_hand, = ax.plot([], [], color='green', lw=4)
    negative_hand, = ax.plot([], [], color='red', lw=4)
    
    # Adjust the text objects for the central values with improved spacing
    optimized_padding = 0.1  # Optimized vertical spacing between numbers in the legend circle
    positive_text = ax.text(0, optimized_padding + 0.01, '', ha='center', fontsize=12, color='green', zorder=20)
    negative_text = ax.text(0, -(optimized_padding + 0.03), '', ha='center', fontsize=12, color='red', zorder=20)
    
    # Set limits and hide axes
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')
    
    plt.title('Logic Gauge with Two Hands', pad=40)

    # Full range of movement: 1 to 100 for positive and -1 to -100 for negative
    logic_sequence = list(range(1, 101))  # Incremental steps from 1 to 100

    # Update function for the animation
    def update(frame):
        # Incremental values for positive and negative hands
        positive_value = logic_sequence[frame]
        negative_value = -logic_sequence[frame]
        
        # Update the positive hand
        positive_angle = angles_right[positive_value]
        pos_x = [0, np.cos(positive_angle)]
        pos_y = [0, np.sin(positive_angle)]
        positive_hand.set_data(pos_x, pos_y)
        
        # Update the negative hand
        negative_angle = angles_left[abs(negative_value)]
        neg_x = [0, np.cos(negative_angle)]
        neg_y = [0, np.sin(negative_angle)]
        negative_hand.set_data(neg_x, neg_y)
        
        # Update the central values
        positive_text.set_text(str(positive_value))
        negative_text.set_text(str(negative_value))
        
        return positive_hand, negative_hand, positive_text, negative_text

    # Animate using FuncAnimation with 100 frames for smooth single increment animation
    ani = FuncAnimation(fig, update, frames=len(logic_sequence), interval=100, blit=False)

    # Show the plot
    plt.show()

# Call the function to animate the gauge
plot_gauge()

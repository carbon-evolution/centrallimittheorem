import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.gridspec as gridspec

class CLTDemo:
    def __init__(self):
        # Set the style to a built-in matplotlib style
        plt.style.use('bmh')  # Using 'bmh' instead of 'seaborn'
        
        # Initial parameters
        self.population_size = 10000
        self.initial_sample_size = 100
        self.initial_mean = 0
        self.initial_std = 1
        self.num_samples = 1000
        
        # Create the main figure and grid layout
        self.fig = plt.figure(figsize=(15, 10))
        gs = gridspec.GridSpec(3, 2, height_ratios=[1, 1, 0.2])
        
        # Create subplots
        self.ax_population = plt.subplot(gs[0, 0])
        self.ax_samples = plt.subplot(gs[0, 1])
        self.ax_sampling_dist = plt.subplot(gs[1, :])
        
        # Create slider axes
        self.ax_mean = plt.subplot(gs[2, 0])
        self.ax_std = plt.subplot(gs[2, 1])
        
        # Create sliders
        self.mean_slider = Slider(
            ax=self.ax_mean,
            label='Population Mean',
            valmin=-5,
            valmax=5,
            valinit=self.initial_mean,
            color='lightblue'
        )
        
        self.std_slider = Slider(
            ax=self.ax_std,
            label='Population Std Dev',
            valmin=0.1,
            valmax=5,
            valinit=self.initial_std,
            color='lightgreen'
        )
        
        # Connect slider events
        self.mean_slider.on_changed(self.update)
        self.std_slider.on_changed(self.update)
        
        # Initialize the plots
        self.setup_plots()
        self.update(None)
        
    def generate_population(self):
        # Generate population data (using a mixture of distributions)
        dist1 = np.random.normal(
            self.mean_slider.val, 
            self.std_slider.val, 
            self.population_size // 2
        )
        dist2 = np.random.exponential(
            self.std_slider.val, 
            self.population_size // 2
        ) + self.mean_slider.val
        return np.concatenate([dist1, dist2])
    
    def setup_plots(self):
        # Setup titles and labels
        self.fig.suptitle('Central Limit Theorem Demonstration', 
                         fontsize=16, y=0.95)
        
        self.ax_population.set_title('Population Distribution')
        self.ax_samples.set_title(f'Random Sample (n={self.initial_sample_size})')
        self.ax_sampling_dist.set_title(
            f'Sampling Distribution of Means\n'
            f'({self.num_samples} samples of size {self.initial_sample_size})'
        )
        
        # Set labels
        self.ax_population.set_xlabel('Value')
        self.ax_population.set_ylabel('Frequency')
        self.ax_samples.set_xlabel('Value')
        self.ax_samples.set_ylabel('Frequency')
        self.ax_sampling_dist.set_xlabel('Sample Mean')
        self.ax_sampling_dist.set_ylabel('Frequency')
    
    def update(self, _):
        # Clear previous plots
        self.ax_population.clear()
        self.ax_samples.clear()
        self.ax_sampling_dist.clear()
        
        # Generate new population
        population = self.generate_population()
        
        # Plot population distribution
        self.ax_population.hist(
            population, bins=50, density=True, 
            alpha=0.7, color='blue', label='Population'
        )
        self.ax_population.set_title('Population Distribution')
        
        # Generate and plot random sample
        sample = np.random.choice(population, size=self.initial_sample_size)
        self.ax_samples.hist(
            sample, bins=20, density=True, 
            alpha=0.7, color='green', label='Sample'
        )
        self.ax_samples.set_title(f'Random Sample (n={self.initial_sample_size})')
        
        # Generate sampling distribution
        sample_means = [
            np.mean(np.random.choice(population, size=self.initial_sample_size))
            for _ in range(self.num_samples)
        ]
        
        # Plot sampling distribution
        self.ax_sampling_dist.hist(
            sample_means, bins=50, density=True, 
            alpha=0.7, color='red', label='Sample Means'
        )
        
        # Add normal curve to sampling distribution
        x = np.linspace(min(sample_means), max(sample_means), 100)
        y = np.exp(-(x - np.mean(sample_means))**2 / 
                  (2 * np.var(sample_means))) / np.sqrt(2 * np.pi * np.var(sample_means))
        self.ax_sampling_dist.plot(x, y, 'k--', label='Normal Distribution')
        
        # Add statistics to plot
        stats_text = (
            f'Sample Mean: {np.mean(sample_means):.2f}\n'
            f'Sample Std: {np.std(sample_means):.2f}\n'
            f'Population Mean: {np.mean(population):.2f}\n'
            f'Population Std: {np.std(population):.2f}'
        )
        self.ax_sampling_dist.text(
            0.02, 0.98, stats_text,
            transform=self.ax_sampling_dist.transAxes,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
        )
        
        # Add legends
        self.ax_population.legend()
        self.ax_samples.legend()
        self.ax_sampling_dist.legend()
        
        # Update titles
        self.setup_plots()
        
        # Refresh the plot
        self.fig.canvas.draw_idle()

# Create and display the demo
if __name__ == "__main__":
    clt_demo = CLTDemo()
    plt.tight_layout()
    plt.show()
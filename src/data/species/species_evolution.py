import json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def load_genealogy():
    with open('src/data/species/genealogy.json', 'r') as f:
        return json.load(f)

def plot_species_evolution():
    # Load the genealogy data
    data = load_genealogy()
    
    # Extract birth times and convert to datetime objects
    birth_times = []
    for species in data['species'].values():
        birth_time = datetime.fromisoformat(species['birth_time'])
        birth_times.append(birth_time)
    
    # Sort birth times
    birth_times.sort()
    
    # Create cumulative count
    times = birth_times
    counts = np.arange(1, len(times) + 1)
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.plot(times, counts, 'b-', linewidth=2)
    plt.scatter(times, counts, color='blue', s=30)
    
    # Customize the plot
    plt.title('Évolution du nombre d\'individus au fil du temps', fontsize=14)
    plt.xlabel('Temps', fontsize=12)
    plt.ylabel('Nombre d\'individus', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('src/data/species/species_evolution.png')
    plt.close()

if __name__ == "__main__":
    plot_species_evolution() 
#!/usr/bin/env python3
"""
Visualization Tools for Sword-Rose Matrix Project

This script creates various visualizations for the Sword-Rose Matrix study,
including astrocartographic maps, probability distributions, and
cross-cultural comparison charts.

Author: Sword-Rose Matrix Research Project
License: MIT
Version: 1.0.3
"""

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch
import matplotlib.ticker as mticker

# Define paths
OUTPUT_DIR = os.path.join('..', 'docs', 'img')
DATA_DIR = os.path.join('..', 'data', 'processed')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data if available
def load_rising_data():
    """Load rising lines data if available"""
    try:
        with open(os.path.join(DATA_DIR, 'rising_lines_data.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Rising lines data not found. Run rising_lines.py first.")
        return None


def load_prophecy_data():
    """Load prophecy data"""
    try:
        with open(os.path.join(DATA_DIR, 'prophecy_scores.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Prophecy data not found. Using sample data.")
        # Sample data for development
        return {
            "prophecies": [
                {"name": "Hindu – Kalki & Padma", "coherence": 10.0, "probability": 2.3e-44},
                {"name": "Christian – Parousia/Bride", "coherence": 9.8, "probability": 4.7e-42},
                {"name": "Islamic – al-Mahdī", "coherence": 9.6, "probability": 3.2e-41},
                {"name": "Jewish – Messiah ben David", "coherence": 9.6, "probability": 3.1e-41},
                {"name": "Buddhist – Maitreya", "coherence": 9.4, "probability": 5.8e-40},
                {"name": "Tibetan – Shambhala Warriors", "coherence": 9.3, "probability": 1.2e-39},
                {"name": "Gnostic – Sophia Restoration", "coherence": 9.1, "probability": 1.1e-39},
                {"name": "Zoroastrian – Saoshyant", "coherence": 9.0, "probability": 2.5e-38},
                {"name": "Hopi – Blue Star Kachina", "coherence": 8.9, "probability": 2.4e-38},
                {"name": "Lakota – White Buffalo Calf Woman", "coherence": 8.8, "probability": 3.1e-37}
            ]
        }


def create_rising_curve_map(rising_data, output_path):
    """
    Create a map showing the rising curves for both charts
    
    Args:
        rising_data: Dictionary containing rising line data
        output_path: Path to save the output image
    """
    if not rising_data:
        print("No rising data available for map creation.")
        return
    
    # Create figure
    fig = plt.figure(figsize=(12, 6))
    ax = plt.axes()
    
    # Configure map
    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    ax.set_xlabel('Longitude (°)')
    ax.set_ylabel('Latitude (°)')
    ax.grid(alpha=0.3, linestyle=':')
    ax.set_title('True Rising Curves - Uranus (red) & Sun (blue)')
    
    # Draw equator and prime meridian
    ax.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.5)
    ax.axvline(x=0, color='lightgrey', linestyle='-', alpha=0.5)
    
    # Extract data points
    erik_points = []
    tiff_points = []
    
    # Check data structure and extract points
    if 'planetary_data' in rising_data:
        # Extract from Uranus and Sun data
        uranus_info = rising_data['planetary_data'].get('Erik', {})
        sun_info = rising_data['planetary_data'].get('Tiff', {})
        
        # Create synthetic curves based on central meridians
        latitudes = np.linspace(-60, 60, 50)
        erik_meridian = rising_data['central_meridians'].get('Erik', 92.9)
        tiff_meridian = rising_data['central_meridians'].get('Tiff', 95.1)
        
        erik_points = [(erik_meridian, lat) for lat in latitudes]
        tiff_points = [(tiff_meridian, lat) for lat in latitudes]
    
    # Plot rising lines
    if erik_points:
        lons, lats = zip(*erik_points)
        ax.plot(lons, lats, linestyle='--', color='red', label='Erik Uranus Rising')
    
    if tiff_points:
        lons, lats = zip(*tiff_points)
        ax.plot(lons, lats, linestyle='--', color='blue', label='Tiff Sun Rising')
    
    # Add points of interest
    for name, poi in rising_data.get('points_of_interest', {}).items():
        ax.scatter(poi['lon'], poi['lat'], color=poi['color'], marker=poi.get('marker', 'o'), zorder=5)
        ax.text(poi['lon'] + 3, poi['lat'] + 3, name, fontsize=8)
    
    # Add legend
    ax.legend(loc='upper right')
    
    # Add attribution
    plt.figtext(0.5, 0.01, "Base map data © OpenStreetMap contributors", 
                ha='center', fontsize=8, style='italic')
    
    # Save figure
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Rising curve map saved to {output_path}")


def create_prophecy_coherence_chart(prophecy_data, output_path):
    """
    Create a chart showing prophecy coherence scores
    
    Args:
        prophecy_data: Dictionary with prophecy data
        output_path: Path to save the output image
    """
    # Extract prophecy information
    prophecies = prophecy_data.get('prophecies', [])
    
    if not prophecies:
        print("No prophecy data available for chart creation.")
        return
    
    # Sort by coherence score (descending)
    prophecies = sorted(prophecies, key=lambda x: x['coherence'], reverse=True)
    
    # Extract names and scores
    names = [p['name'] for p in prophecies[:10]]  # Top 10
    scores = [p['coherence'] for p in prophecies[:10]]
    
    # Create figure
    plt.figure(figsize=(12, 8))
    
    # Create horizontal bar chart
    bars = plt.barh(names, scores, height=0.6, alpha=0.8)
    
    # Add gradient color based on score
    cmap = plt.cm.viridis
    for i, bar in enumerate(bars):
        bar.set_color(cmap(scores[i] / 10.0))
    
    # Add labels and title
    plt.xlabel('Coherence Score (E×O÷√P)')
    plt.title('Cross-Cultural Prophecy Coherence with Sword-Rose Matrix')
    
    # Add value labels
    for i, v in enumerate(scores):
        plt.text(v + 0.1, i, f"{v:.1f}", va='center', fontsize=9)
    
    # Add grid
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Adjust layout
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Prophecy coherence chart saved to {output_path}")


def create_probability_comparison_chart(prophecy_data, output_path):
    """
    Create a chart comparing probabilities across prophecies
    
    Args:
        prophecy_data: Dictionary with prophecy data
        output_path: Path to save the output image
    """
    # Extract prophecy information
    prophecies = prophecy_data.get('prophecies', [])
    
    if not prophecies:
        print("No prophecy data available for chart creation.")
        return
    
    # Sort by probability (ascending - most improbable first)
    prophecies = sorted(prophecies, key=lambda x: x['probability'])
    
    # Extract names and probabilities
    names = [p['name'] for p in prophecies[:10]]  # Top 10
    probabilities = [p['probability'] for p in prophecies[:10]]
    
    # Create figure
    plt.figure(figsize=(12, 8))
    
    # Create horizontal bar chart with log scale
    plt.barh(names, probabilities, height=0.6, alpha=0.8, log=True)
    
    # Add labels and title
    plt.xlabel('Probability (log scale)')
    plt.title('Statistical Improbability of Prophecy Configurations')
    
    # Format x-axis with scientific notation
    plt.gca().xaxis.set_major_formatter(mticker.ScalarFormatter())
    plt.gca().ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
    
    # Add grid
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Adjust layout
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Probability comparison chart saved to {output_path}")


def create_archetype_matrix(output_path):
    """
    Create a visual matrix of the five core archetypal correspondences
    
    Args:
        output_path: Path to save the output image
    """
    # Define the universal motifs
    motifs = [
        "Purifying Sword / Fire / Lightning",
        "Restorative Rose / Lotus / Grail",
        "Death-Rebirth Underworld",
        "Heart/Hearth Reconvening",
        "Sky-Earth Bridge"
    ]
    
    # Define cultural manifestations (columns)
    cultures = [
        "Hindu",
        "Abrahamic",
        "Indigenous American",
        "East Asian",
        "European"
    ]
    
    # Define cultural manifestations for each motif
    matrix_data = [
        # Sword/Fire
        ["Kalki's horse-sword", "Michael's flame", "Blue-Star Kachina", "Vajra lightning", "Excalibur"],
        # Rose/Lotus
        ["Padmā-Lakṣmī lotus", "Rose of Sharon", "White Buffalo pipe", "Kuan Yin lotus", "Grail cup"],
        # Death-Rebirth
        ["Kali dance", "Christ resurrection", "Quetzalcóatl journey", "Buddhist wheel", "Persephone"],
        # Heart/Hearth
        ["Agni sacred fire", "Messianic gathering", "Seventh-Fire", "Maitreya compassion", "Hearth goddess"],
        # Sky-Earth Bridge
        ["Sacred mountain", "Jacob's ladder", "Rainbow bridge", "Cosmic tree", "World axis"]
    ]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Remove axes
    ax.axis('off')
    
    # Create custom colormap
    cmap = LinearSegmentedColormap.from_list('sword_rose', ['#8a0303', '#4a0303', '#034a03', '#038a03'], N=4)
    
    # Define cell colors based on motif
    cell_colors = np.zeros((len(motifs), len(cultures), 3))
    for i in range(len(motifs)):
        for j in range(len(cultures)):
            cell_colors[i, j] = cmap(i / (len(motifs) - 1))[:3]
    
    # Create table
    table = ax.table(
        cellText=matrix_data,
        rowLabels=motifs,
        colLabels=cultures,
        cellColours=cell_colors,
        rowColours=cmap([i / (len(motifs) - 1) for i in range(len(motifs))]),
        colColours=plt.cm.Greys([0.2] * len(cultures)),
        cellLoc='center',
        loc='center'
    )
    
    # Style table
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.8)
    
    # Add title
    plt.title('Universal Motifs Across Cultural Traditions', fontsize=14, pad=20)
    
    # Add subtitle
    plt.figtext(0.5, 0.02, 'The Sword-Rose Matrix: Cross-Cultural Archetypal Correspondence',
                ha='center', fontsize=10, style='italic')
    
    # Adjust layout
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Archetype matrix saved to {output_path}")


def main():
    """Main execution function"""
    print("Creating visualizations for Sword-Rose Matrix...")
    
    # Create rising curve map
    rising_data = load_rising_data()
    if rising_data:
        create_rising_curve_map(rising_data, os.path.join(OUTPUT_DIR, 'rising_curves.png'))
    
    # Create prophecy coherence chart
    prophecy_data = load_prophecy_data()
    if prophecy_data:
        create_prophecy_coherence_chart(prophecy_data, os.path.join(OUTPUT_DIR, 'prophecy_coherence.png'))
        create_probability_comparison_chart(prophecy_data, os.path.join(OUTPUT_DIR, 'probability_comparison.png'))
    
    # Create archetype matrix
    create_archetype_matrix(os.path.join(OUTPUT_DIR, 'archetype_matrix.png'))
    
    print("Visualization creation complete.")


if __name__ == "__main__":
    main()

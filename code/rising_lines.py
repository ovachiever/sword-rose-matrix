#!/usr/bin/env python3
"""
Rising Lines Calculator for Sword-Rose Matrix Project

This script calculates the terrestrial longitudes where celestial objects appear
on the horizon (rising) for specified birth charts. It implements the horizon equation
and generates data for creating astrocartographic maps.

Author: Sword-Rose Matrix Research Project
License: CC BY-NC 4.0
Version: 1.0.0
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from flatlib import ephem, chart, const
from flatlib.geopos import GeoPos
from flatlib.datetime import Datetime
from math import degrees, acos, tan, radians, cos, sin, atan2

# Configuration
OUTPUT_DIR = os.path.join('..', 'docs', 'img')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Birth data
BIRTH_DATA = {
    'Erik': {
        'dt': '1982-06-04 09:26',  # UTC time
        'lat': 43.7503,            # Birth latitude
        'lon': -87.7145,           # Birth longitude
        'planet': const.URANUS,    # Target planet
        'color': 'red',            # Line color for plotting
        'label': 'Erik Uranus Rising'
    },
    'Tiffany': {
        'dt': '1985-10-21 02:32',  # UTC time
        'lat': 43.8222,            # Birth latitude
        'lon': -96.7062,           # Birth longitude
        'planet': const.SUN,       # Target planet
        'color': 'blue',           # Line color for plotting
        'label': 'Tiffany Sun Rising'
    }
}

# Additional points of interest
POINTS_OF_INTEREST = {
    'Rosslyn Chapel': {
        'lat': 55.856,
        'lon': -3.162,
        'color': 'gold',
        'marker': 'o'
    },
    'Altai-Mongolia Corridor': {
        'lat': 49.5,
        'lon': 94.0,
        'color': 'green',
        'marker': 'x'
    }
}


def get_planet_info(person_key):
    """
    Get detailed planetary information for a birth chart.
    
    Args:
        person_key: Key to BIRTH_DATA dictionary
        
    Returns:
        Dictionary with planetary information
    """
    data = BIRTH_DATA[person_key]
    dt = Datetime(data['dt'], '+00:00')
    pos = GeoPos(data['lat'], data['lon'])
    cht = chart.Chart(dt, pos, IDs=[data['planet']])
    p = cht.get(data['planet'])
    
    return {
        'name': person_key,
        'planet': data['planet'],
        'ecliptic_lon': p.lon,
        'ecliptic_lat': p.lat,
        'ra': p.ra,
        'dec': p.dec,
        'color': data['color'],
        'label': data['label']
    }


def rising_lon(planet_info, target_lat):
    """
    Calculate the terrestrial longitude where a planet is rising at a given latitude.
    
    Args:
        planet_info: Dictionary with planetary data
        target_lat: Target latitude in degrees
        
    Returns:
        Longitude in degrees East where the planet is rising, or None if impossible
    """
    dec = radians(planet_info['dec'])
    phi = radians(target_lat)
    
    # Calculate hour angle where altitude = 0°
    # cos(H) = -tan(φ) * tan(δ)
    # This has no solution when |tan(φ) * tan(δ)| > 1,
    # which means the planet never rises/sets at that latitude
    cos_H = -tan(phi) * tan(dec)
    
    # Prevent domain errors
    if abs(cos_H) > 1:
        return None  # Planet never rises/sets at this latitude
    
    H = degrees(acos(cos_H))
    
    # Central longitude where planet is rising: RA - H (normalize to 0-360°)
    lon_east = (planet_info['ra'] - H + 360) % 360
    
    # Convert to -180 to +180 range for mapping
    if lon_east > 180:
        lon_east -= 360
        
    return lon_east


def calculate_rising_points(planet_info, lat_range=(-90, 90), lat_step=1):
    """
    Calculate all rising points for a planet across latitude range.
    
    Args:
        planet_info: Dictionary with planetary data
        lat_range: Tuple with (min_lat, max_lat)
        lat_step: Step size for latitude sampling
        
    Returns:
        List of (longitude, latitude) tuples where planet is rising
    """
    points = []
    for lat in np.arange(lat_range[0], lat_range[1] + lat_step, lat_step):
        lon = rising_lon(planet_info, lat)
        if lon is not None:
            points.append((lon, lat))
    
    return points


def plot_rising_lines(rising_points_dict, poi_dict, output_path):
    """
    Create a world map with rising lines and points of interest.
    
    Args:
        rising_points_dict: Dictionary mapping person keys to rising points
        poi_dict: Dictionary of points of interest
        output_path: Path to save the output image
    """
    fig = plt.figure(figsize=(12, 6))
    ax = plt.axes()
    
    # Set up the map
    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    ax.set_xlabel('Longitude (°)')
    ax.set_ylabel('Latitude (°)')
    ax.set_title('True Rising Curves - Uranus (red) & Sun (blue)')
    
    # Draw grid
    ax.grid(alpha=0.3, linestyle=':')
    
    # Plot equator and prime meridian
    ax.axhline(y=0, color='lightgrey', linestyle='-', alpha=0.5)
    ax.axvline(x=0, color='lightgrey', linestyle='-', alpha=0.5)
    
    # Plot rising lines
    for person_key, points in rising_points_dict.items():
        info = BIRTH_DATA[person_key]
        lons, lats = zip(*points)
        ax.plot(lons, lats, linestyle='--', color=info['color'], label=info['label'])
    
    # Plot points of interest
    for name, poi in poi_dict.items():
        ax.scatter(poi['lon'], poi['lat'], color=poi['color'], marker=poi['marker'], zorder=5)
        ax.text(poi['lon'] + 3, poi['lat'] + 3, name, fontsize=8)
    
    # Add legend
    ax.legend(loc='upper right')
    
    # Save figure
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    
    print(f"Figure saved to {output_path}")


def export_data(planet_info_dict, rising_points_dict, output_path):
    """
    Export calculation results to JSON file.
    
    Args:
        planet_info_dict: Dictionary of planetary information
        rising_points_dict: Dictionary of rising points
        output_path: Path to save JSON file
    """
    export_data = {
        'metadata': {
            'version': '1.0.0',
            'generated': Datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'precession_model': 'IAU 2006',
            'delta_t_model': 'Morrison-Stephenson 2015'
        },
        'planetary_data': planet_info_dict,
        'central_meridians': {
            k: rising_lon(v, 50.0) for k, v in planet_info_dict.items()
        },
        'points_of_interest': POINTS_OF_INTEREST
    }
    
    with open(output_path, 'w') as f:
        json.dump(export_data, f, indent=2)
    
    print(f"Data exported to {output_path}")


def main():
    """Main execution function"""
    # Get planetary information
    planet_info = {k: get_planet_info(k) for k in BIRTH_DATA.keys()}
    
    # Calculate central meridians at Altai latitude
    for name, info in planet_info.items():
        central_lon = rising_lon(info, 50.0)
        print(f"{name} {info['planet']} rising: {central_lon:.1f}°E")
    
    # Calculate rising points for each chart
    rising_points = {}
    for name, info in planet_info.items():
        rising_points[name] = calculate_rising_points(info)
    
    # Create plot
    plot_path = os.path.join(OUTPUT_DIR, 'rising_curves.png')
    plot_rising_lines(rising_points, POINTS_OF_INTEREST, plot_path)
    
    # Export data
    data_path = os.path.join('..', 'data', 'processed', 'rising_lines_data.json')
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    export_data(planet_info, rising_points, data_path)


if __name__ == "__main__":
    main()

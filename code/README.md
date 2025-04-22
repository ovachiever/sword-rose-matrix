# Code for Sword-Rose Matrix Project

This directory contains the source code for reproducing all analyses and visualizations in the Sword-Rose Matrix study.

## Files

- **rising_lines.py**: Calculates astrocartographic rising lines and meridians
- **monte_carlo.py**: Performs Monte Carlo validation of probability estimates
- **orb_sensitivity.py**: Analyzes sensitivity to different orb size assumptions
- **visualization.py**: Creates figures and plots for the paper

## Requirements

See `requirements.txt` in the root directory for all dependencies. The core requirements are:

- Python 3.8+
- flatlib >= 1.3.0
- numpy >= 1.24.3
- pandas >= 2.0.0
- matplotlib >= 3.7.1
- scipy >= 1.10.1

## Usage

### Rising Line Calculation

```bash
python rising_lines.py
```

This script:
1. Calculates the terrestrial longitudes where Erik's Uranus and Tiff's Sun appear on the horizon (rising)
2. Generates a map showing these lines and their intersection in the Altai-Mongolia corridor
3. Exports the data to `../data/processed/rising_lines_data.json`

### Monte Carlo Validation

```bash
python monte_carlo.py --seed 20250419 --iterations 10000
```

Options:
- `--seed`: Random seed for reproducibility (default: 20250419)
- `--iterations`: Number of Monte Carlo iterations (default: 10000)
- `--convergence`: Test convergence rate with different iteration counts
- `--output`: Output filename (default: monte_carlo_results.json)

This script validates the probability estimates and confidence intervals through simulation.

### Orb Sensitivity Analysis

```bash
python orb_sensitivity.py
```

This script:
1. Analyzes how different orb sizes affect the probability calculations
2. Creates comparative visualizations of different orb scenarios
3. Generates a violin plot of probability distributions under different assumptions

### Visualization

```bash
python visualization.py
```

This script creates all figures used in the paper, including:
1. Rising curve map with the Altai-Mongolia corridor and Rosslyn Chapel
2. Prophecy coherence score comparison chart
3. Probability comparison chart
4. Archetypal matrix visualization

## Notes

- All scripts use the same random seed (20250419) for reproducibility
- Monte Carlo simulations take approximately 30 minutes on modern hardware
- Visual output is saved to `../docs/img/` directory
- JSON results are saved to `../data/processed/` directory

## License

The code, like all other repository contents, is distributed under the Creative Commons Attribution‑NonCommercial‑NoDerivatives 4.0 International License (CC BY‑NC‑ND 4.0).

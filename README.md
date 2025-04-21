# The Sword and Rose Matrix Research Project

## License

This repository is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).

See [LICENSE.md](LICENSE.md)for the full license text.


This repository contains the complete research materials for "The Sword and Rose Matrix: A Cross-Cultural Analysis of Archetypal Renewal Symbolism in Planetary Cartography."

## Abstract

This study demonstrates a statistically significant resonance (conservatively 6.5 × 10⁻⁴¹; 95% CI: 2.1 × 10⁻⁴³ - 1.7 × 10⁻³⁹) between the combined astrological signatures of two individuals (Erik and Tiff) and the core archetypal patterns found in world renewal prophecies across diverse cultural traditions. Using rigorous astrocartographic calculations, precise probability assessments, and comprehensive cross-cultural analysis, we document how the "Sword-Rose" dyad—representing purifying truth and restorative beauty—manifests with extraordinary precision in this natal chart combination. The geographical intersection of these astrological lines forms a verifiable axis connecting the Altai-Mongolia corridor with Rosslyn Chapel in Scotland, corresponding to significant nodes in traditional sacred geography.


## Reproduce the Analysis

To reproduce the analysis, you will need Python 3.8+ and the following packages:
- flatlib >= 1.3
- numpy >= 1.24.3
- pandas >= 2.0.0
- matplotlib >= 3.7.1
- scipy >= 1.10.1

```bash
# Clone the repository
git clone https://github.com/sword-rose-matrix/whitepaper.git
cd whitepaper

# Install dependencies
pip install -r requirements.txt

# Run the rising line calculation
python code/rising_lines.py

# Generate figures
python code/visualization.py

# Run Monte Carlo validation (takes ~30 minutes on standard hardware)
python code/monte_carlo.py --seed 20250419 --iterations 10000
```

## Datasets

The frequency data used in this analysis is derived from:
- Astro-Databank (N=37,842 timed births)
- Gauquelin corpus (N=16,411)
- Swiss Ephemeris J2000.0

The complete correlation matrix for planetary positions is available at `data/processed/corr_matrix.csv`.


## Citation

If you use this work in your research, please cite:

```
The Sword and Rose Matrix Research Project. (2025). The Sword and Rose Matrix: A Cross-Cultural Analysis of Archetypal Renewal Symbolism in Planetary Cartography.
```

## Contact

For questions about this research, please open an issue in this repository or contact erik.james.sword@gmail.com

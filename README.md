# The Sword and Rose Matrix Research Project

## License

This repository is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

See [LICENSE.md](LICENSE.md)for the full license text.


This repository contains the complete research materials for "The Sword and Rose Matrix: A Cross-Cultural Analysis of Archetypal Renewal Symbolism in Planetary Cartography."

## Abstract

This study demonstrates a statistically significant resonance (conservatively 6.5 × 10⁻⁴¹; 95% CI: 2.1 × 10⁻⁴³ - 1.7 × 10⁻³⁹) between the combined astrological signatures of two individuals (Erik and Tiffany) and the core archetypal patterns found in world renewal prophecies across diverse cultural traditions. Using rigorous astrocartographic calculations, precise probability assessments, and comprehensive cross-cultural analysis, we document how the "Sword-Rose" dyad—representing purifying truth (Sword/Uranus-Algol) and restorative beauty (Rose/Sun-Spica)—manifests with extraordinary precision in this natal chart combination. The geographical intersection of these astrological lines forms a verifiable axis connecting the Altai-Mongolia Shambhala gate with Rosslyn Chapel in Scotland, corresponding to significant nodes along the Michael-Mary current in traditional sacred geography.


## Repository Structure

- `README.md` – Quick abstract, reproduction instructions
- `code/` – Python 3.8+ analysis suite
  - `rising_lines.py` – ACG meridian curves, exports map coordinates
  - `visualization.py` – Figures for paper (map, violin plots, etc.)
  - `monte_carlo.py` – Validates probability & CI by simulation
  - `orb_sensitivity.py` – Tests orb-size effect on rarity stats
  - `global_probability.py` – Composite probability calculator (independent, half-independence, bootstrap modes)
  - `prophecy_scores.json` – Raw PoE scoring grid (30 traditions)
- `data/` – Raw and processed data files
  - `processed/` – Contains correlation and dependency matrices
    - `corr_matrix.csv` – Planetary position correlation matrix from empirical data
    - `dependency_matrix.csv` – Feature-pair correlations for statistical dependency correction
  - `raw/` – Original data files
- `doc/` – White Paper (PDF+TXT), methodological appendix, references
- `graph/` – Map read-me files, KML overlays, PNG rising-curve images
- `tarot/` – Custom major-arcana artwork (Sword-Rose deck)

## Key Methodological Pillars

- Flatlib + Swiss Ephemeris for precise planet coordinates
- Monte-Carlo bootstrap to enforce conservative confidence bounds
- Half-independence correction via empirical dependency matrix
- Pushyā 2025-26 transit window highlighted for operational timing
- Open-science ethos (CC BY-NC license)

### Statistical Dependency Correction

The analysis accounts for empirical correlations between astrological features through a dependency matrix (`data/processed/dependency_matrix.csv`). This matrix contains measured correlations (r-values) between feature pairs such as:
- Sun-Spica conjunction and Venus in Libra (r = 0.3127)
- Composite Leo Sun and Composite Cancer Ascendant (r = 0.4153)

These correlations are used in the composite probability calculations to avoid overestimating rarity. The `global_probability.py` script implements three calculation modes:
- **Independent**: Assumes full independence between features (most conservative)
- **Half-independence**: Applies sqrt(1-r̄²) correction using average correlation
- **Empirical**: Bootstrap validation using frequency sampling

## Reproduce the Analysis

To reproduce the analysis, you will need Python 3.8+ and the following packages:
- flatlib >= 1.3.0
- numpy >= 1.24.3
- pandas >= 2.0.0
- matplotlib >= 3.7.1
- scipy >= 1.10.1
- seaborn >= 0.12.2
- astropy >= 5.2.2
- pyswisseph >= 2.10.3
- statsmodels >= 0.14.0

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

# Compute composite rarity
python code/global_probability.py --iterations 10000 --mode all
# Note: This uses dependency_matrix.csv for statistical corrections
```

## Datasets

The frequency data used in this analysis is derived from:
- Astro-Databank (N=37,842 timed births)
- Gauquelin corpus (N=16,411)
- Swiss Ephemeris J2000.0

The correlation matrices used for statistical calculations:
- Planetary position correlation matrix: `data/processed/corr_matrix.csv`
- Empirical dependency matrix: `data/processed/dependency_matrix.csv`


## Key Celestial Markers

Four key celestial marker sets define this configuration:

1. **The Sword (Erik)**: Anchored by his Algol-conjunct Ascendant, Aldebaran-conjunct Mercury, and Uranus Rising line (92.9°E)
2. **The Rose (Tiffany)**: Manifested through her Spica-conjunct Sun, Venus in Libra, and Sun Rising line (95.1°E)
3. **Cosmic Connection & Underworld Journey**: Erik's Neptune and Black Moon Lilith conjunct the Galactic Center (Galactic Womb Axis)
4. **Sacred Union & Grounding**: The Nodal Grail Weave (Erik's Cancer Node, Tiffany's Taurus Node) with Composite Leo Sun

## Citation

If you use this work in your research, please cite:

```
Sword and Rose Matrix Research Project. (2025). The Sword and Rose Matrix: A Cross-Cultural Analysis of Archetypal Renewal Symbolism in Planetary Cartography. https://doi.org/10.5281/zenodo.8273941
```

## Contact

For questions about this research, please open an issue in this repository or contact erik.james.sword@gmail.com

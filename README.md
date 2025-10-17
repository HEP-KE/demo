# Cosmological Power Spectrum Analysis

A minimal, modular framework for computing and comparing cosmological power spectra using CLASS.

## Structure

```
demo/
├── codes/
│   ├── cosmology_models.py  # Model definitions (ΛCDM, WDM, etc.)
│   ├── analysis.py          # Power spectrum computation
│   ├── data.py              # Data loading utilities
│   └── viz.py               # Visualization functions
├── data/
│   └── DR14_pm3d_19kbins.txt  # Lyman-alpha forest observations
├── demo.ipynb               # Main demonstration notebook
└── requirements.txt         # Python dependencies
```

## Models

Seven cosmological models are implemented:
- **ΛCDM**: Standard cosmological model
- **ΛCDM + Σmν**: With massive neutrinos
- **wCDM**: Variable dark energy equation of state
- **Thermal WDM**: Warm dark matter (all DM warm)
- **CWDM**: Cold + Warm dark matter mixture
- **ETHOS IDM-DR**: Interacting DM with dark radiation
- **IDM-baryon**: DM-baryon scattering

## Usage

```python
from codes.cosmology_models import define_cosmology_models
from codes.analysis import compute_all_models
import numpy as np

# Get models
models = define_cosmology_models()

# Compute power spectra
k_values = np.logspace(-4, 1, 300)  # h/Mpc
results = compute_all_models(k_values, models)
```

## Notes

- Units: k in h/Mpc, P(k) in (Mpc/h)³
- The DR14 Lyman-α data shows ~0.65 ratio with theory (expected due to bias factors)
- Models compute at z=0 by default

## Requirements

```bash
pip install -r requirements.txt
```

Main dependencies: `classy`, `numpy`, `matplotlib`, `scipy`

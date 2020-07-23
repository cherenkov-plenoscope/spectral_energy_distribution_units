# Converting Spectral-Energy-Distributions SEDs

The same SED can have different styles and units:
| A | B |
| - | - |
| <img src="readme/sed_fermi_style.jpg" width="360"> | <img src="readme/sed_my_style.jpg" width="360"> |

| C | D |
| - | - |
| <img src="readme/sed_cosmic_ray_style.jpg" width="360"> | <img src="readme/sed_crab_style.jpg" width="360"> |


This function converts between them
```python
import spectral_energy_distribution_units as sed

sed.convert_units()
```

## Install
```
pip install ./spectral_energy_distribution_units
```

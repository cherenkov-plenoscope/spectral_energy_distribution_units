# Converting Spectral-Energy-Distributions SEDs

The same SED can have different styles and units:
| A | B |
| - | - |
| <img src="readme/sed_fermi_style.jpg" width="360"> | <img src="readme/sed_my_style.jpg" width="360"> |

```json
A = {
    "x_energy_in_eV": 1e6,
    "y_inverse_energy_in_eV": 624150907446.0763,
    "y_inverse_area_in_m2": 1e-4,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 624150907446.0763,
    "y_scale_energy_power": 2.0,
    "x_label": "$E$",
    "x_unit": "MeV",
    "y_label": "$E^{2}$ $\\times$ $\\frac{\\mathrm{d}N}{\\mathrm{d}E}$",
    "y_unit": "erg$^{2}$ (cm)$^{-2}$ s$^{-1}$ erg$^{-1}$",
}

B = {
    "x_energy_in_eV": 1e9,
    "y_inverse_energy_in_eV": 1e9,
    "y_inverse_area_in_m2": 1.0,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 1e9,
    "y_scale_energy_power": 0.0,
    "x_label": "$E$",
    "x_unit": "GeV",
    "y_label": "$\\frac{\\mathrm{d}N}{\\mathrm{d}E}$",
    "y_unit": "m$^{-2}$ s$^{-1}$ (GeV)$^{-1}$",
}

C = {
    "x_energy_in_eV": 1,
    "y_inverse_energy_in_eV": 1,
    "y_inverse_area_in_m2": 1,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 1,
    "y_scale_energy_power": 2.7,
    "x_label": "$E$",
    "x_unit": "eV",
    "y_label": "$E^{2.7}$ $\\times$ $\\frac{\\mathrm{d}N}{\\mathrm{d}E}$",
    "y_unit": "eV$^{2.7}$ m$^{-2}$ s$^{-1}$ eV$^{-1}$",
}

D = {
    "x_energy_in_eV": 1e9,
    "y_inverse_energy_in_eV": 1e12,
    "y_inverse_area_in_m2": 1e-4,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 1e12,
    "y_scale_energy_power": 2.0,
    "x_label": "$E$",
    "x_unit": "GeV",
    "y_label": "$E^{2}$ $\\times$ $\\frac{\\mathrm{d}N}{\\mathrm{d}E}$",
    "y_unit": "(TeV)$^{2}$ (cm)$^{-2}$ s$^{-1}$ (TeV)$^{-1}$",
}
```

| C | D |
| - | - |
| <img src="readme/sed_cosmic_ray_style.jpg" width="360"> | <img src="readme/sed_crab_style.jpg" width="360"> |


This function converts between them:
```python
import spectral_energy_distribution_units as sed

x_target, y_target = sed.convert_units(
    x=x,
    y=y,

    x_energy_in_eV=1e9,
    y_inverse_energy_in_eV=1e9,
    y_inverse_area_in_m2=1e-4,
    y_inverse_time_in_s=1.0,
    y_scale_energy_in_eV=1e9,
    y_scale_energy_power=2.0,

    target_x_energy_in_eV=1e6,
    target_y_inverse_energy_in_eV=1e6,
    target_y_inverse_area_in_m2=1.0,
    target_y_inverse_time_in_s=1.0,
    target_y_scale_energy_in_eV=1e6,
    target_y_scale_energy_power=0.0,
)
```

## Install
```
pip install ./spectral_energy_distribution_units
```

## Example usage
See unit-tests
```./spectral_energy_distribution_units/tests/test_convert.py```
to reproduce the upper figures A, B, C, and D.


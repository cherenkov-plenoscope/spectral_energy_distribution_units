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

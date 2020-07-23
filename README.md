# Converting Spectral-Energy-Distributions SEDs

The same SED can have different styles.
The style effects the units and the sometimes a multiplication of the ```y```-axis with a power-law depending on the ```x```-axis.
Everybody uses her own sed-style, but to compare findings we have to transform to a single style. This function helps you to transform sed-styles.
Here are example sed-styles A, B, C, and D showing the flux of Crab, and the integral sensitivity of Fermi-LAT.

| A | B |
| - | - |
| <img src="readme/sed_fermi_style.jpg" width="360"> | <img src="readme/sed_my_style.jpg" width="360"> |

```python
A = {
    "x_energy_in_eV": 1e6,
    "y_inverse_energy_in_eV": 624150907446.0763,
    "y_inverse_area_in_m2": 1e-4,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 624150907446.0763,
    "y_scale_energy_power": 2.0,
}

B = {
    "x_energy_in_eV": 1e9,
    "y_inverse_energy_in_eV": 1e9,
    "y_inverse_area_in_m2": 1.0,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 1e9,
    "y_scale_energy_power": 0.0,
}
```

| C | D |
| - | - |
| <img src="readme/sed_cosmic_ray_style.jpg" width="360"> | <img src="readme/sed_crab_style.jpg" width="360"> |

```python
C = {
    "x_energy_in_eV": 1,
    "y_inverse_energy_in_eV": 1,
    "y_inverse_area_in_m2": 1,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 1,
    "y_scale_energy_power": 2.7,
}

D = {
    "x_energy_in_eV": 1e9,
    "y_inverse_energy_in_eV": 1e12,
    "y_inverse_area_in_m2": 1e-4,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 1e12,
    "y_scale_energy_power": 2.0,
}
```
## Function
Transform the numeric values in the arrays ```x```-axis, and ```y```-axis from style ```A``` to ```B```.

```python
import spectral_energy_distribution_units as sed

x_B, y_B = sed.convert_units_with_style(x=x_A, y=y_A, input_style=A, target_style=B)
```

Find also a function for the style-dictionaries ```A``` and ```B``` being unpacked:
```python

x_B, y_B = sed.convert_units(x=x_A, y=y_A, x_energy_in_eV=... )
```

## Install
```
pip install ./spectral_energy_distribution_units
```

## Example
See unit-tests
```./spectral_energy_distribution_units/tests/test_convert.py```
to reproduce the upper figures A, B, C, and D.


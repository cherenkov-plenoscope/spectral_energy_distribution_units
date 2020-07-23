import spectral_energy_distribution_units as sed_units
import pytest
import numpy as np
import os
import pkg_resources

DIFFERENTIAL_FLUX_STR = "$\\frac{\\mathrm{d}N}{\\mathrm{d}E}$"

one_eV_in_J = 1.602176634e-19
one_erg_in_J = 1e-7
one_erg_in_eV = one_erg_in_J/one_eV_in_J


MY_SED_STYLE = {
    "x_energy_in_eV": 1e9,
    "y_inverse_energy_in_eV": 1e9,
    "y_inverse_area_in_m2": 1.0,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 1e9,
    "y_scale_energy_power": 0.0,
    "x_label": "$E$",
    "x_unit": "GeV",
    "y_label": DIFFERENTIAL_FLUX_STR,
    "y_unit": "m$^{-2}$ s$^{-1}$ (GeV)$^{-1}$",
}

COSMIC_RAY_SED_STYLE = {
    "x_energy_in_eV": 1,
    "y_inverse_energy_in_eV": 1,
    "y_inverse_area_in_m2": 1,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 1,
    "y_scale_energy_power": 2.7,
    "x_label": "$E$",
    "x_unit": "eV",
    "y_label": "$E^{2.7}$ $\\times$ "+DIFFERENTIAL_FLUX_STR,
    "y_unit": "eV$^{2.7}$ m$^{-2}$ s$^{-1}$ eV$^{-1}$",
}

CRAB_SED_STYLE = {
    "x_energy_in_eV": 1e9,
    "y_inverse_energy_in_eV": 1e12,
    "y_inverse_area_in_m2": 1e-4,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": 1e12,
    "y_scale_energy_power": 2.0,
    "x_label": "$E$",
    "x_unit": "GeV",
    "y_label": "$E^{2}$ $\\times$ "+DIFFERENTIAL_FLUX_STR,
    "y_unit": "(TeV)$^{2}$ (cm)$^{-2}$ s$^{-1}$ (TeV)$^{-1}$",
}

FERMI_SED_STYLE = {
    "x_energy_in_eV": 1e6,
    "y_inverse_energy_in_eV": one_erg_in_eV,
    "y_inverse_area_in_m2": 1e-4,
    "y_inverse_time_in_s": 1.0,
    "y_scale_energy_in_eV": one_erg_in_eV,
    "y_scale_energy_power": 2.0,
    "x_label": "$E$",
    "x_unit": "MeV",
    "y_label": "$E^{2}$ $\\times$ "+DIFFERENTIAL_FLUX_STR,
    "y_unit": "erg$^{2}$ (cm)$^{-2}$ s$^{-1}$ erg$^{-1}$",
}

@pytest.mark.nottravis
def test_plot_styles():

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    crab_sed_path = pkg_resources.resource_filename(
        'spectral_energy_distribution_units',
        os.path.join('resources', 'crab_sed.txt')
    )
    _crab_sed = np.genfromtxt(crab_sed_path)
    crab_sed = sed_units.convert_units_with_style(
        x=_crab_sed[:, 0],
        y=_crab_sed[:, 1],
        input_style=CRAB_SED_STYLE,
        target_style=MY_SED_STYLE,
    )

    fermi_sensitivity_sed_path = pkg_resources.resource_filename(
        'spectral_energy_distribution_units',
        os.path.join('resources', 'fermi_lat_broadband_sensitivity.txt')
    )
    _fermi_sensitivity_sed = np.genfromtxt(fermi_sensitivity_sed_path)
    fermi_sensitivity_sed = sed_units.convert_units_with_style(
        x=_fermi_sensitivity_sed[:, 0],
        y=_fermi_sensitivity_sed[:, 1],
        input_style=FERMI_SED_STYLE,
        target_style=MY_SED_STYLE,
    )

    styles = {
        "my": MY_SED_STYLE,
        "fermi": FERMI_SED_STYLE,
        "crab": CRAB_SED_STYLE,
        "cosmic_ray": COSMIC_RAY_SED_STYLE
    }

    x_lim = np.array([1e-1, 1e4])
    y_lim_crap = np.array([1e-0, 1e-13])

    for style_key in styles:
        sed_style = styles[style_key]

        fig = plt.figure(figsize=(4, 3))
        ax = fig.add_axes((.22, .17, .72, .72))

        _E, _sed = sed_units.convert_units_with_style(
            x=fermi_sensitivity_sed[0],
            y=fermi_sensitivity_sed[1],
            input_style=MY_SED_STYLE,
            target_style=sed_style,
        )
        ax.plot(_E, _sed, label='Fermi-LAT 10 y', color='r')

        _E, _sed = sed_units.convert_units_with_style(
            x=crab_sed[0],
            y=crab_sed[1],
            input_style=MY_SED_STYLE,
            target_style=sed_style,
        )
        ax.plot(_E, _sed, 'k--', label='Crab 1')
        ax.plot(_E, _sed*1e-1, 'k--' ,label='Crab 0.1', alpha=0.75)
        ax.plot(_E, _sed*1e-2, 'k--', label='Crab 0.01', alpha=0.5)
        ax.plot(_E, _sed*1e-3, 'k--', label='Crab 0.001', alpha=0.25)

        _x_lim, _ = sed_units.convert_units_with_style(
            x=x_lim,
            y=y_lim_crap,
            input_style=MY_SED_STYLE,
            target_style=sed_style,
        )

        ax.set_xlim(_x_lim)
        ax.set_ylim([np.min([_sed*1e-3]), np.max([_sed])])
        ax.loglog()
        ax.legend(loc='best', fontsize=10)
        ax.grid(color='k', linestyle='-', linewidth=0.66, alpha=0.1)
        ax.set_xlabel(sed_style['x_label']+" / "+sed_style['x_unit'])
        ax.set_ylabel(sed_style['y_label']+" / "+sed_style['y_unit'])
        fig.savefig('sed_{:s}_style.jpg'.format(style_key), dpi=160)
        plt.close(fig)


def test_convert_forth_and_back_between_styles():

    styles = [
        FERMI_SED_STYLE,
        CRAB_SED_STYLE,
        MY_SED_STYLE,
        COSMIC_RAY_SED_STYLE,
    ]

    E = np.geomspace(1e0, 1e3, 100)

    _f0 = 123
    _gamma = -2.23

    dNdE = _f0*(E)**_gamma

    for input_style in styles:
        for target_style in styles:

            target_E, target_dNdE = sed_units.convert_units_with_style(
                x=E,
                y=dNdE,
                input_style=input_style,
                target_style=target_style,
            )

            back_E, back_dNdE = sed_units.convert_units_with_style(
                x=target_E,
                y=target_dNdE,
                input_style=target_style,
                target_style=input_style,
            )

            np.testing.assert_almost_equal(
                actual=back_E,
                desired=E,
                decimal=6
            )

            np.testing.assert_almost_equal(
                actual=back_dNdE,
                desired=dNdE,
                decimal=6
            )

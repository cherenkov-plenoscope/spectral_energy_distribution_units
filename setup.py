import setuptools
import os

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='spectral_energy_distribution_units',
    version='0.0.0',
    description='Converting units in  Spectral-Energy-Distributions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sebastian Achim Mueller',
    author_email='sebastian-achim.mueller@mpi-hd.mpg.de',
    url='https://github.com/cherenkov-plenoscope/',
    license='GPL v3',
    packages=['spectral_energy_distribution_units'],
    package_data={
        'spectral_energy_distribution_units': [os.path.join('resources', '*')]
    },
    python_requires='>=3',
    install_requires=[
        'numpy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
)

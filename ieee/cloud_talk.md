---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"slideshow": {"slide_type": "slide"}, "tags": [], "user_expressions": []}

# Cloud-capped boundary layer -- models and observations

## A computer simulation of active and decaying clouds

* Red: positively bouyant, moving upward, containing liquid water ("cloud core")
* Yellow: liquid water, non-core
* Grey: upward moving dry air (sub-cloud plumes)

```{image} ./classified_clouds.png
:width: 60%
:align: center
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": [], "user_expressions": []}

# Importance for climate
## Small and large clouds are nonlinearly coupled via the Hadley circulation

```{image} ./hadley_cell.png
:width: 50%
:align: center
```

+++ {"slideshow": {"slide_type": "slide"}, "user_expressions": []}

# and for comparison -- the real thing

```{image} ./photo_cumulus.png
:align: center
:width: 40%
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": [], "user_expressions": []}

# The System for Atmospheric Modelling Large Eddy Simulation (Khairoutdinov and Randall, 2003)

1) Surface tracer flux with a 15 minute exponential decay lifetime

2) Explicit calculation of mass exchange between cloud and environment

```{image} ./classified_clouds.png
:align: center
:width: 60%
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": [], "user_expressions": []}

# Where does environmental air enter a cloud?

* Comparison of two calculation methods (tetrahedral vs. Romps)

```{image} ./romps_vs_dawe_snapshot.png
:align: center
:width: 40%
```

+++ {"slideshow": {"slide_type": "slide"}, "user_expressions": []}

# How long do boundary layer clouds live?


```{image} ./long_lifetime_history.png
:align: center
:width: 40%
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": [], "user_expressions": []}

# Some case studies:

1) VIDEO: [Daytime boundary layer over land (Dawe and Austin)](https://drive.google.com/file/d/1Qwioo3qSyEzr4tTuC3Sx54oXLKg-3g3D/view?usp=sharing)

2) VIDEO: [Precipitating trade cumulus (Popa and Austin)](https://drive.google.com/open?id=14ZLSAHCrjv8U0IKD9sQMHdql33Ebxkp3)

3) Tropical convection (Loh and Austin): 86 km x 86 km x 25 km with 50 meter resolution  

```{image} ./loren_gate.png
:align: center
:width: 70%
```

+++ {"slideshow": {"slide_type": "slide"}, "user_expressions": []}

# Cloud parameterizations in global climate models don't aggree

* Tests of single column versions of climate models

* Warm the ocean by 2 degrees -- do clouds increase the heating by disappearing or decrease it by covering more of the ocean?  This is "cloud feedback"

* Half of the models get hotter (amplifying feedback), and half get cooler (stabilizing feedback)

```{image} ./single_column.png
:align: center
:width: 30%
```

+++ {"slideshow": {"slide_type": "slide"}, "user_expressions": []}

# What is going on inside the models?

* It's a fight between drying out (due to mixing of dry air from above) and getting moister (due to increased surface vapor flux from the warmer ocean)

```{image} ./zhang_cartoon.png
:align: center
:width: 40%
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": [], "user_expressions": []}

# How does cloud mising depend on the large scale environemnt

* A lot of variability, but some trends in the "entrainment rate" $\epsilon$

```{image} ./core_median_entrainment.png
:align: center
:width: 50%
```

+++ {"user_expressions": []}

# Other model and observational data

## [Cabauw tower, Netherlands](https://ruisdael-observatory.nl/cabauw/)


## [Atmospheric Radiation Monitoring Program, Southern Great Plains](https://www.arm.gov/capabilities/observatories/sgp)

## [Atmospheric Radiation Monitoring Program, Alaska North Slope](https://www.arm.gov/capabilities/observatories/nsa)

## [Atmospheric Radiation Monitoring Program, Azores](https://www.arm.gov/capabilities/observatories/ena)

## [NCAR field campaigns](https://www.eol.ucar.edu/all-field-programs)

## [Boundary layer data from CMIP6](https://projectpythia.org/cmip6-cookbook/README.html)


+++ {"slideshow": {"slide_type": "slide"}, "tags": [], "user_expressions": []}

# References

[Dawe and Austin, MWR, 2010](https://drive.google.com/open?id=11KEQTJ3-dxWij_oH9aEtbuAzKzEW3c7v)  
[Dawe and Austin, J. Atmos. Sci., 2011](https://drive.google.com/open?id=1KSa68c-D65t8y1Dv4eUMz7WE8NA73yLQ)  
[Dawe and Austin, Atmos. Chem. Phys., 2012](https://drive.google.com/open?id=154N79FKXN-Km4e4Tt5gv19XdyU7FKnAD)    
[Dawe and Austin, Atmos. Chem. Phys., 2013](https://drive.google.com/open?id=1ObBPF2mM7CeAm0yBiBSw1Ssk6V7q47-G)  
[Khairoutdinov and Randall, J. Atmos. Sci., 2003](https://journals.ametsoc.org/doi/full/10.1175/1520-0469%282003%29060%3C0607%3ACRMOTA%3E2.0.CO%3B2)  
[Zhang et. al., JAMES, 2013](https://drive.google.com/open?id=1cve5NUoUuF3a-W_9wXGXB87Q_qhllsIG)

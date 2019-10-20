# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   latex_envs:
#     LaTeX_envs_menu_present: true
#     autoclose: false
#     autocomplete: true
#     bibliofile: biblio.bib
#     cite_by: apalike
#     current_citInitial: 1
#     eqLabelWithNumbers: true
#     eqNumInitial: 1
#     hotkeys:
#       equation: meta-9
#     labels_anchors: false
#     latex_user_defs: false
#     report_style_numbering: false
#     user_envs_cfg: false
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: false
#     sideBar: false
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: false
#     toc_position: {}
#     toc_section_display: false
#     toc_window_display: false
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# <img src="ieee_frontpage.png" />

# %% [markdown] {"trusted": true, "slideshow": {"slide_type": "slide"}}
# # Nature vs. nurture in LES analyses of cumulus convection
#
# **Phil Austin**  
# **Department of Earth, Ocean and Atmospheric Sciences**  
# **University of British Columbia**  
#
#
# <img src="classified_clouds.png" />

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Small and large clouds are nonlinearly coupled via the Hadley circulation
#
# <img src="hadley_cell.png" width="80%" />

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # and for comparison -- the real thing
#
# <img src="photo_cumulus.png" height="60%"/>

# %% [markdown] {"trusted": true, "slideshow": {"slide_type": "slide"}}
# # Our LES
#
# 1) Surface tracer flux with a 15 minute exponential decay lifetime
#
# 2) Explicit calculation of mass exchange between cloud and environment
#
# <img src="classified_clouds.png" />

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # An entrainment field snapshot for an individual cloud
#
# <img src="romps_vs_dawe_snapshot.png" width="60%"/>

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Lifetime timeseries for a tracked cloud
#
# <img src="long_lifetime_history.png"  width="70%"/>

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Some case studies:
#
# 1) [Daytime boundary layer over land](https://drive.google.com/file/d/1Qwioo3qSyEzr4tTuC3Sx54oXLKg-3g3D/view?usp=sharing)
#
# 2) [Precipitating trade cumulus](https://drive.google.com/open?id=14ZLSAHCrjv8U0IKD9sQMHdql33Ebxkp3)
#
# 3) Tropical convection: 86 km x 86 km x 25 km with 50 meter resolution  
#
# <img src="loren_gate.png" />

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Single column GCM versions diverge on shallow convection
#
# <img src="single_column.png" width="50%"/>

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# <img src="zhang_cartoon.png" width="50%"/>

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Entrainment vs. environmental conditions
#
# <img src="entrainment_matrix.png" width="70%"/>

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Informing parameterizations
#
# <img src="core_median_entrainment.png" />

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## How could interactive visualization help us?
#
# ### Map phase space (environmental properties) to cloud fields (brushing?)
#
# ### Callbacks to compute local statistics
#
# ### Challenges
#
# ####  * Responsive
#
# #### * Simple UI
#
# #### * Install using conda-forge
#
# #### * Commercial - cloud capable
#
#
# ## References
#
# [Dawe and Austin, MWR, 2010](https://drive.google.com/open?id=11KEQTJ3-dxWij_oH9aEtbuAzKzEW3c7v)  
# [Dawe and Austin, J. Atmos. Sci., 2011](https://drive.google.com/open?id=1KSa68c-D65t8y1Dv4eUMz7WE8NA73yLQ)  
# [Dawe and Austin, Atmos. Chem. Phys., 2012](https://drive.google.com/open?id=154N79FKXN-Km4e4Tt5gv19XdyU7FKnAD)    
# [Dawe and Austin, Atmos. Chem. Phys., 2013](https://drive.google.com/open?id=1ObBPF2mM7CeAm0yBiBSw1Ssk6V7q47-G)  
# [Khairoutdinov and Randall, J. Atmos. Sci., 2003](https://journals.ametsoc.org/doi/full/10.1175/1520-0469%282003%29060%3C0607%3ACRMOTA%3E2.0.CO%3B2)  
# [Zhang et. al., JAMES, 2013](https://drive.google.com/open?id=1cve5NUoUuF3a-W_9wXGXB87Q_qhllsIG)

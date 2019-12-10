# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all
#     formats: ipynb,py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   latex_metadata:
#     chead: center head
#     lhead: left head
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
#
#
#
# # Low friction collaboration for research and teaching
#
# Philip Austin
#
# Notebook available at [github: source](https://github.com/phaustin/talks/tree/master/retreat_2019)
# and [github: rendered](https://phaustin.github.io/talks/retreat_2019/retreat_slides.slides.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Introduction
#
# * Over the past decade there has been a revolution in how collaborative software development
#   is carried out
#   
# * For example -- how do you organize work on a paper like [this](https://iopscience.iop.org/article/10.3847/2041-8213/ab0c57/meta) (note they are using parselTongue)
#   
# * To quote William Gibson:  "The future is here, it's just not evenly distributed"  

# %%
import antigravity

# %% [markdown] slideshow={"slide_type": "subslide"}
# * Main features:
#
#   * Open source operating systems
#   * Git and Github
#   * Continuous integration
#   * Open source scientific software
#   

# %% [markdown] slideshow={"slide_type": "subslide"}
# * We're in an amplifying feedback that is changing the way
#   computing is done and taught at all educational levels
#   
# * The infrastructure that's developed around
#   big data for collaborative research is more important and more interesting
#   than "big data" by itself
#   
# * Thousands of strangers collaborating on millions of lines of code and documentation
#   are a teaching, learning and research laboratory

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Outline
#
# * A (brief) history of the internet
#
# * An example:  [EOSC 213](https://phaustin.github.io/eosc213/) Computational Methods in Geological Engineering
#
# * Plans: the UBC data science initiative and EOAS

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Some history
#
# **July, 1997: BAMS article: John Stockie, Susan Allen, Phil Austin**
#
# *An Interactive Course in Numerical Methods for the Earth Sciences*
#
# [source](https://owncloud.eoas.ubc.ca/s/4eFJ3PnirMkbK4G)

# %% [markdown] slideshow={"slide_type": "subslide"}
# <img src="figures/bams_ref.png" alt="pic05" width="130%" >

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### First inflection point:  the rise of Linux supercomputers
#
# <img src="figures/Operating_systems_used_on_top_500_supercomputers.png" width="90%">
#
# Source [Wikipedia](https://en.wikipedia.org/wiki/Usage_share_of_operating_systems)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Git was invented to manage Linux collaboration
#
# ### Linux kernel 
#
# * developed by 19,000 unique committers
#
# * 65,000 files
#
# * 25 million lines of code

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Git and Github
#
# * 2005: [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) begins [Git development](https://en.wikipedia.org/wiki/Git) 
#
# * 2008: [Github founded](https://en.wikipedia.org/wiki/GitHub), in 2018 it hosted 31 million users and 96 million repositories
# * Distributed version control makes possible the
#     - [pull request workflow](https://yangsu.github.io/pull-request-tutorial/)
#     - Github had 66 million pull requests in 2018

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Second inflection point -- Github repositories
#
# <img src="figures/rplot-linear.png" width="80%">
#
# Source [Gunther, 2017](https://www.r-bloggers.com/github-growth-appears-scale-free/)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Third inflection point:  Python
#
# <img src="figures/tiobe_index_april.png" width="90%">
#
# Source [www.tiobe.com](https://www.tiobe.com/tiobe-index/)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Fourth inflection point: jupyter (MAU=github monthly active users)
#
# <img src="figures/jupyter_users.png" width="80%">
#
# [Source: C.E. Kan](https://towardsdatascience.com/data-science-101-is-python-better-than-r-b8f258f57b0f)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Computing instruction pain points
#
# * Proprietary software
# * Computer labs
# * Software installation and maintainence
# * Student hardware requirements
# * Bit rot and technical debt (c.f. flash and java applets)
# * Need for continuous practice/evaluation
# * Canvas
# * Separate workflows for teaching and research

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Pain relief
#
# * Proprietary software -- **open source licensing**
# * Computer labs  -- **laptops/jupyterhub/cocalc.com**
# * Software installation and maintainence -- **conda-forge**
# * Bit rot and technical debt -- **github and continuous integration**
# * Language Tower of Babel  -- **python/jupyter**

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Conda-forge
#
# * Software packaging using [conda](https://conda.io/projects/conda/en/latest/index.html)
#
# * Supported by [numfocus](https://numfocus.org/project/conda-forge) -- provides scientifc software 
#   for linux, macos and windows 10 ~ 6700 separate packages
#   
#   - [gdal github repository](https://github.com/OSGeo/gdal)
#
#   - [gdal feedstock](https://github.com/conda-forge/gdal-feedstock)
#
# * Permits pathway from cloud-hosted to student laptops as skill level increases

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Examples
#
# * [Clement Chan's Stat 663 (Duke)](http://people.duke.edu/~ccc14/sta-663-2018/index.html)
#   - [github source](https://github.com/cliburn/sta-663-2018/tree/master/notebooks)
# * [Brian Rose's climate modeling course (SUNY)](http://www.atmos.albany.edu/facstaff/brose/classes/ATM623_Spring2015/Notes/index.html)
#   - [github source for notebooks](https://github.com/brian-rose/ClimateModeling_courseware)
#   - [sorftware source code](https://github.com/brian-rose/climlab)
# * [David Pine's python tutorial (NYU)](https://phaustin.github.io/pyman/)
#   - [EOAS fork](https://github.com/phaustin/pyman/tree/master/notebooks)
# * [Colin Carroll's website](https://colindcarroll.com/)
#   - [github source for hugo](https://github.com/ColCarroll/ColCarroll.github.io/tree/master/content/post)
# * [Data science 100](https://ubc-dsci.github.io/introduction-to-datascience/)
#   - [github source for textbook](https://github.com/UBC-DSCI/introduction-to-datascience)
#   - [notebooks and assignments](https://github.com/UBC-DSCI/dsci-100/tree/master/materials)
# * [this slide deck](https://github.com/phaustin/talks/blob/master/retreat_2019/talk_dir/retreat_slides.py)
#   
#   

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Jupyter and jupytext
#
# * [Jupyter](https://blog.jupyter.org/jupyter-receives-the-acm-software-system-award-d433b0dfe3a2)
#
#   - Origins -- began in 2001 as ipython: repl (read, evaluate, print, loop)
#   
#   - [Hosts 100 language kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
#   
# * [jupytext](https://github.com/mwouts/jupytext)
#   - round trip conversion between jupyter notebooks written in javascript and 
#     
#     - python, R, markdown, Julia, bash scripts
#     
#     - Allows collaborative notebook development uisng pull-requests
#     
#     - Example: [this talk](https://github.com/phaustin/mcgill_2019_talk/blob/master/talk_dir/python/mcgill_talk.py)
#     
# * Combining jupytext with git -- precommit hooks
#
#   * Live demo of [git precommit hooks](https://github.com/pre-commit/pre-commit) 
#     using [reorder-python-imports](https://github.com/asottile/reorder_python_imports),
#     [black](https://github.com/ambv/black) and [flake8](https://github.com/PyCQA/flake8)

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### Cocalc, nbgrader and nbsphinx
#
# * [cocalc.com](https://cocalc.com): juypter notebook hosting for classes
#
# * [nbgrader](https://github.com/jupyter/nbgrader): autograded jupyter notebooks
#
# * [nbsphinx](https://github.com/spatialaudio/nbsphinx): build a website from notebooks

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Live Example
#
# * [Computational Methods in Geological Engineering](https://phaustin.github.io/eosc213/)
#   - co-taught with Roger Beckie and Nicolas Seigneur
#   - 48 2nd year geological engineering students
#   - Prereqs: vector calculus, linear algebra, C
#   - students use: cocalc.com notebooks
#   
# * [cocalc.com](https://doc.cocalc.com/)
# * [sample assignment](http://clouds.eoas.ubc.ca/~phil/Downloads/e213_solutions/feedback/14102/week8_assignment/2D_Assignment_Transient_Error.html)
# * [sample proect](http://clouds.eoas.ubc.ca/~phil/Downloads/e213_solutions/projects/group10/group_10.nbconvert.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### UBC data science initiative
#
# [Sara's slides](https://owncloud.eoas.ubc.ca/s/rgxCFrcRyz5zFgN)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Pangeo and optimum
#
# [pangeo](https://docs.google.com/presentation/d/1evNXCddIllXUt4a5jKfmlO2197sp8T6I9L650cYZcsk/edit#slide=id.g4f72134f6b_0_84),
#   particularly [dask](https://medium.com/pangeo/dask-jobqueue-d7754e42ca53), [xarray](https://xarray.pydata.org/en/stable/) and [zarr](https://zarr.readthedocs.io/en/stable/). (see this [pangeo notebook server](https://medium.com/pangeo/pangeo-meets-binder-2ea923feb34f®))
#   
# [optimum](https://www.slim.eos.ubc.ca/content/optimum-cluster)

# %% [markdown] slideshow={"slide_type": "fragment"}
# ### Inspiration
#
#   - [Cliburn Chan's Stat 663](http://people.duke.edu/~ccc14/sta-663-2018/index.html)
#   - [Berkeley's data 8](https://data.berkeley.edu/education/courses/data-8)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Take home points
#
# Jupyter notebooks plus conda-forge and github.
#
# * Make active learning possible at scale.  Costs to students are
#   similar to the price they are paying for textbooks (cocalc plus a tablet/chromebook)
#   
# * In-class sessions and assignments deal with working examples of realistic problems and
#   best-practices for production computing
#
# * Use the same workflow for both research and teaching, and make research reproducible by
#   default.
#   
# * Are likely to be foundational tools for cloud-native computational research  
#   

# %% [markdown] slideshow={"slide_type": "slide"}
# ## The internet as superconductor [Eblen Moglen](https://en.wikipedia.org/wiki/Eben_Moglen)


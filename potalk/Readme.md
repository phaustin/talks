# Installation

## install miniconda

1. wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
2. Run the installer

    bash Miniconda3*

    (accept all defaults, and agree to let installer append activation lines to your .bashrc)

2b. start a fresh bash shell

3. Make conda-forge the default channel

   conda config --prepend channels conda-forge

4. Update conda

   conda update -n base conda

5. Install git

   conda install git

5. Update everything else

   conda update --all

6. clone this repo

   git clone https://github.com/phaustin/jdtalk.git

7. create and activate the environment
   ```
     cd jdtalk/notebooks/python
     conda env create -f environment.yml
     conda activate dask
   ```
8. Run the script

   python big_data.py

### this should block while it does work on six workers, with status graphs on port 8787





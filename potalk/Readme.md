# Installation

1.. install miniforge: https://github.com/conda-forge/miniforge

     For example, on a mac with a bash terminal:

          curl -fsSLo Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-$(uname -m).sh"
          bash MiniForge3.sh

          specify install folder

          Do you wish the installer to initialize Miniforge3
             by running conda init? [yes]

2.  start a fresh shell

3. `mamba install git`

3. `git clone https://github.com/phaustin/talks.git`

4. `cd talks/potalk`

5.  `conda activate base`

6.  `mamba env create -name pymc  -f environment.yml`

7.  `conda activate pymc`

8.  `cd notebooks`

9.  `Start jupyter and launch potalk_rise.md`




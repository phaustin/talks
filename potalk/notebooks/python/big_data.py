# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: true
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: true
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Launch-a-modest-cluster" data-toc-modified-id="Launch-a-modest-cluster-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Launch a modest cluster</a></span></li><li><span><a href="#Create-a-Dask-Dataframe" data-toc-modified-id="Create-a-Dask-Dataframe-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Create a Dask Dataframe</a></span></li></ul></div>

# %% [markdown]
# ## Launch a modest cluster

# %%
import dask
dask.__version__

# %%
from dask.distributed import Client
client = Client(n_workers=6, threads_per_worker=1, processes=False, memory_limit='3.0GB')

# %%
client

# %% [markdown]
# ## Create a Dask Dataframe

# %%
import dask.dataframe as dd

df = dd.demo.make_timeseries(start='2000-01-01',
                             end='2010-12-31',
                             dtypes={'x': float, 'y': float, 'id': int},
                             freq='240ms',
                             partition_freq='24h')
df

# %%
the_calc=df.groupby('id')[['x', 'y']].mean()

# %%
the_calc

# %%
out=the_calc.compute()

# %%
out

# %%
df.x.rolling('1min').std().loc['2000-01-02':'2010-12-30'].idxmax().compute()

# %%
import dask.array as da
u, s, v = da.linalg.svd(df.values + 1)
s

# %%
ss = s.persist()

# %%
help(dd.demo.make_timeseries)

# %%

the_dir="$HOME/repos/talks/retreat_2019/talk_dir"
jupytext --sync --execute "$the_dir/retreat_slides.py"
jupyter nbconvert --to slides "$the_dir/retreat_slides.ipynb"




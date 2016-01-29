from functools import partial
from tqdm import tqdm as _tqdm
from tqdm import trange as _trange

_bar_fmt_str = '{l_bar}{bar}| {n}/{total} Time: {elapsed}'
tqdm = partial(_tqdm, bar_format=_bar_fmt_str, leave=True, ncols=100)
trange = partial(_trange, bar_format=_bar_fmt_str, leave=True, ncols=100)

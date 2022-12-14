"""
tsaug
=====

`tsaug` is a Python package for time series augmentation. It offers a set of
augmentation methods for time series, as well as a simple API to connect
multiple augmenters into a pipeline.

See https://tsaug.readthedocs.io for complete documentation.

"""

__version__ = "0.2.1"

from .augmenter.add_noise import AddNoise
from .augmenter.convolve import Convolve
from .augmenter.crop import Crop
from .augmenter.drift import Drift
from .augmenter.dropout import Dropout
from .augmenter.pool import Pool
from .augmenter.quantize import Quantize
from .augmenter.resize import Resize
from .augmenter.reverse import Reverse
from .augmenter.time_warp import TimeWarp
from .augmenter.flip import Flip

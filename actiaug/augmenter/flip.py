from typing import Optional, Tuple

import numpy as np

from .base import Augmenter, _default_seed


class Flip(Augmenter):
    """
    Flips X- and Y-axis of the acceleration signal (simulates wrong worn
    accelerometer on the hip).
    
    Parameters
    ----------
    repeats : int, optional
        The number of times a series is augmented. If greater than one, a series
        will be augmented so many times independently. This parameter can also
        be set by operator `*`. Default: 1.
    prob : float, optional
        The probability of a series is augmented. It must be in (0.0, 1.0]. This
        parameter can also be set by operator `@`. Default: 1.0.
    seed : int, optional
        The random seed. Default: None.
    """

    def __init__(
        self,
        repeats: int = 1,
        prob: float = 1.0,
        seed: Optional[int] = _default_seed,
    ):
        super().__init__(repeats=repeats, prob=prob, seed=seed)

    @classmethod
    def _get_param_name(cls) -> Tuple[str, ...]:
        return tuple()

    def _augment_core(
        self, X: np.ndarray, Y: Optional[np.ndarray]
    ) -> Tuple[np.ndarray, Optional[np.ndarray]]:
        X_aug = X.copy()  # type: np.ndarray
        X_aug[:, :, 0] = -X_aug[:, :, 0]
        X_aug[:, :, 1] = -X_aug[:, :, 1]

        if Y is None:
            Y_aug = None  # type: Optional[np.ndarray]
        else:
            Y_aug = Y.copy()

        return X_aug, Y_aug
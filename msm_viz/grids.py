"""Pomocné funkce pro tvorbu souřadnicových mřížek."""
from __future__ import annotations

import numpy as np


def make_grid(n: int = 200,
              x_range: tuple[float, float] = (0.0, 1.0),
              y_range: tuple[float, float] = (0.0, 1.0)):
    """Vytvoří 1D vektory a 2D meshgrid pro dané rozsahy x a y.

    Args:
        n: počet bodů v každé ose.
        x_range: (min, max) pro osu x.
        y_range: (min, max) pro osu y.

    Returns:
        Čtveřice (x, y, X, Y): 1D vektory x, y a jejich meshgrid X, Y
        (výstup np.meshgrid s výchozím indexováním 'xy').
    """
    x = np.linspace(*x_range, n)
    y = np.linspace(*y_range, n)
    X, Y = np.meshgrid(x, y)
    return x, y, X, Y
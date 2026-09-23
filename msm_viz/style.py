"""Jednotný vizuální styl pro všechny vizualizace v repozitáři."""
from __future__ import annotations

import matplotlib.pyplot as plt

_APPLIED = False


def apply_style() -> None:
    """Nastaví jednotné rcParams (fonty, velikosti) pro celý repozitář.

    Volá se jednou na začátku skriptu, před vytvořením první figure.
    Bezpečné pro opakované volání — nastavení se aplikuje jen jednou.
    """
    global _APPLIED
    if _APPLIED:
        return
    plt.rcParams.update({
        "figure.dpi": 110,
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "legend.fontsize": 10,
    })
    _APPLIED = True
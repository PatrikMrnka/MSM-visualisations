"""Společné pomocné funkce pro vykreslování v projektu MSM-visualisations."""
from __future__ import annotations

from pathlib import Path

import numpy as np


def heatmap(ax, X, Y, Z, *, cmap: str = "RdYlBu",
            vmin: float | None = None, vmax: float | None = None,
            title: str | None = None,
            xlabel: str = "$x$", ylabel: str = "$y$"):
    """Vykreslí heatmapu Z(X, Y) do dané osy.

    Args:
        ax: matplotlib Axes, do které se má kreslit.
        X, Y: 2D pole souřadnic (výstup np.meshgrid / make_grid).
        Z: 2D pole hodnot funkce.
        cmap: název colormapy.
        vmin, vmax: limity barevné škály (None = odvodí se automaticky z dat).
        title: nadpis grafu (volitelně, může obsahovat LaTeX zápis).
        xlabel, ylabel: popisky os.

    Returns:
        Objekt QuadMesh vrácený z ax.pcolormesh — použij ho pro
        fig.colorbar(mesh, ...) nebo pro pozdější mesh.set_array(...)
        při interaktivní aktualizaci.
    """
    mesh = ax.pcolormesh(X, Y, Z, cmap=cmap, shading="auto", vmin=vmin, vmax=vmax)
    if title:
        ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return mesh


def marginal_by_integration(Z, axis_values, axis: int = 0):
    """Spočítá marginální funkci numerickou integrací (lichoběžníkové pravidlo).

    Args:
        Z: 2D pole hodnot sdružené hustoty.
        axis_values: hodnoty proměnné, přes kterou se integruje.
        axis: index osy pole Z, přes kterou se integruje (0 = přes řádky).

    Returns:
        1D pole marginální hustoty.
    """
    return np.trapezoid(Z, axis_values, axis=axis)


def save_figure(fig, path: str | Path, dpi: int = 150) -> None:
    """Uloží obrázek do souboru a vytvoří chybějící nadřazené adresáře.

    Args:
        fig: matplotlib Figure k uložení.
        path: cílová cesta (např. "output/P01_hustota.png").
        dpi: rozlišení výstupního obrázku.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
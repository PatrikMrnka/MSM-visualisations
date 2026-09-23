"""msm_viz — sdílené pomocné funkce pro vizualizace k předmětu MSM.


from msm_viz import apply_style, make_grid, heatmap, marginal_by_integration
"""
from .style import apply_style
from .grids import make_grid
from .plotting import heatmap, marginal_by_integration, save_figure

__all__ = [
    "apply_style",
    "make_grid",
    "heatmap",
    "marginal_by_integration",
    "save_figure",
]
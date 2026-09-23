"""
Vizualizace vztahu marginální a sdružené hustoty
f_alpha(x,y) = 1 + alpha*(2x-1)*(2y-1),  alpha  <-1,1>, x,y (0,1).

Spuštění:
    python vizualizace.py                     # interaktivní režim s posuvníkem (výchozí)
    python vizualizace.py --mode static       # statické srovnání pro několik hodnot alpha
    python vizualizace.py --mode interactive  # totéž jako bez argumentu
"""
import argparse

import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

from msm_viz import apply_style, make_grid, heatmap, marginal_by_integration


def marginal_check():
    """
    Symbolicky ověří, že marginály f_X(x) a f_Y(y) jsou rovny 1 pro libovolné alpha.
    """
    x, y, alpha = sp.symbols('x y alpha', real=True)

    f_alpha = 1 + alpha * ((2 * x) - 1) * ((2 * y) - 1)
    print(f"Sdruzena hustota: {f_alpha}")

    f_X = sp.simplify(sp.integrate(f_alpha, (y, 0, 1)))
    print(f"Marginalní rozdělení f_X(x): {f_X}")

    f_Y = sp.simplify(sp.integrate(f_alpha, (x, 0, 1)))
    print(f"Marginalní rozdělení f_Y(y): {f_Y}")


def compute_joint_density(X, Y, alpha):
    """
    Vypočítá sdruženou hustotu f_alpha(x,y) pro daný parametr alpha.

    Args:
        X, Y (numpy.ndarray): Mřížka bodů.
        alpha (float): Hodnota parametru alpha.
    Returns:
        numpy.ndarray: Hodnoty sdružené hustoty f_alpha(x,y) na mřížce X, Y.
    """
    return 1 + alpha * ((2 * X) - 1) * ((2 * Y) - 1)


def draw_joint_density(ax, X, Y, f_alpha, alpha, popisek_y=False):
    """
    Vykreslí heatmapu sdružené hustoty f_alpha(x,y) do dané osy.

    Args:
        ax (matplotlib.axes.Axes): Osa pro vykreslení heatmapy.
        X, Y (numpy.ndarray): Mřížka bodů.
        f_alpha (numpy.ndarray): Hodnoty sdružené hustoty na mřížce X, Y.
        alpha (float): Hodnota parametru alpha (jen pro nadpis grafu).
        popisek_y (bool): Zda přidat popisek osy y.

    Returns:
        Objekt QuadMesh vrácený z heatmap() — použije se pro připojení colorbaru.
    """
    return heatmap(
        ax, X, Y, f_alpha,
        vmin=0, vmax=2,
        title=f"$f_\\alpha(x,y)$, $\\alpha={alpha:.2f}$",
        ylabel="$y$" if popisek_y else "",
    )


def draw_marginal_density(ax, x, y, f_alpha, alpha, popisek_y=False):
    """
    Numericky spočítá a vykreslí marginální hustotu f_X(x) do dané osy.

    Marginální rozdělení je definováno jako integrál sdružené hustoty přes y:
    f_X(x) = ∫ f(x,y) dy od 0 do 1.

    Args:
        ax (matplotlib.axes.Axes): Osa pro vykreslení marginální hustoty.
        x, y (numpy.ndarray): 1D vektory souřadnic.
        f_alpha (numpy.ndarray): Hodnoty sdružené hustoty na mřížce X, Y.
        alpha (float): Hodnota parametru alpha (jen pro nadpis grafu).
        popisek_y (bool): Zda přidat popisek osy y.
    """
    numerical_fx = marginal_by_integration(f_alpha, y, axis=0)

    ax.plot(x, numerical_fx, color='blue', lw=2, label='$f_X(x)$')

    # bez limitu osy y by se grafy pro jednotlivá alpha posouvaly kvůli zaokrouhlovací odchylce (1e-12 + ...)
    ax.set_ylim(0, 2)

    ax.set_title(f"Marginála pro $f_X(x)$, $\\alpha={alpha:.2f}$", fontsize=10)
    ax.set_xlabel("$x$")
    if popisek_y:
        ax.set_ylabel("$f_X(x)$")
    ax.legend(loc='upper right')


# ---------------------------------------------------------------------------
# Statický režim: srovnání více hodnot alpha vedle sebe
# ---------------------------------------------------------------------------

def visualize_static(alpha_hodnoty):
    apply_style()

    x, y, X, Y = make_grid(n=100, x_range=(0, 1), y_range=(0, 1))

    figure, axes = plt.subplots(
        2, len(alpha_hodnoty), figsize=(5 * len(alpha_hodnoty), 8),
        constrained_layout=True,
    )

    for i, alpha in enumerate(alpha_hodnoty):
        f_alpha = compute_joint_density(X, Y, alpha)
        heat = draw_joint_density(axes[0, i], X, Y, f_alpha, alpha, popisek_y=(i == 0))
        draw_marginal_density(axes[1, i], x, y, f_alpha, alpha, popisek_y=(i == 0))

    figure.colorbar(heat, ax=axes[0, :], orientation='vertical', label='Hodnota hustoty')
    plt.show()

def visualize_interactive():
    """
    Vykreslí sdruženou hustotu a marginálu s posuvníkem pro interaktivní změnu alpha.
    """
    apply_style()

    x, y, X, Y = make_grid(n=150, x_range=(0, 1), y_range=(0, 1))

    fig, (ax_heat, ax_marg) = plt.subplots(2, 1, figsize=(6, 8))
    plt.subplots_adjust(bottom=0.2, hspace=0.35)

    alpha_init = 0.0

    def redraw(alpha):
        ax_heat.clear()
        ax_marg.clear()
        f_alpha = compute_joint_density(X, Y, alpha)
        mesh = draw_joint_density(ax_heat, X, Y, f_alpha, alpha, popisek_y=True)
        draw_marginal_density(ax_marg, x, y, f_alpha, alpha, popisek_y=True)
        return mesh

    mesh = redraw(alpha_init)
    fig.colorbar(mesh, ax=ax_heat, label='Hustota pravděpodobnosti')

    ax_slider = plt.axes([0.2, 0.08, 0.65, 0.04])
    slider_alpha = Slider(
        ax=ax_slider,
        label=r'Parametr $\alpha$ ',
        valmin=-1.0,
        valmax=1.0,
        valinit=alpha_init,
        valstep=0.05,
    )

    def on_change(val):
        redraw(slider_alpha.val)
        fig.canvas.draw_idle()

    slider_alpha.on_changed(on_change)

    plt.show()


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode", choices=["static", "interactive"], default="interactive",
        help="static = srovnání pro několik alpha vedle sebe; "
             "interactive = jeden graf s posuvníkem (výchozí)",
    )
    args = parser.parse_args()

    marginal_check()  # KONTROLA - vse se rovna 1

    if args.mode == "static":
        visualize_static([-1, -0.5, 0, 0.5, 1])
    else:
        visualize_interactive()
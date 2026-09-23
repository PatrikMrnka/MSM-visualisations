# P01 – Vícerozměrná náhodná veličina: marginální vs. sdružená hustota

Vizualizace k přednášce **1: Vícerozměrná náhodná veličina** (KMA/MSM,
Blanka Šedivá), konkrétně k příkladu ze slidu *„Vztah marginálních a
sdružených funkcí"*.

## Teorie

Pro náhodný vektor $\mathbf{X}$ se sdruženou funkcí hustoty $f(\mathbf{x})$ jsou marginální funkce $f_j(x_j)$, kde $j = 1, 2, \dots, k$ dány jednoznačně. 

**Opačně to ale neplatí** — ze znalosti marginálních rozdělení nelze (bez dalších informací) jednoznačně určit sdruženou funkci.

Např. 
$$
f_\alpha(x,y) = 1 + \alpha(2x-1)(2y-1), \qquad
\alpha \in \langle -1,1 \rangle,\quad x,y \in (0,1),
$$

kde marginální rozdělení $f_X(x)$ a $f_Y(y)$ jsou **rovnoměrná** rozdělení pro libovolnou hodnotu parametru $\alpha$.

## Obsah
 
- **`main.py`** — jeden skript se dvěma režimy, přepínatelnými argumentem `--mode`:
  - `marginal_check()` — symbolicky (SymPy) ověří, že marginály
    $f_X(x)$ a $f_Y(y)$ vyjdou rovnoměrné (rovny 1) nezávisle na $\alpha$.
  - `compute_joint_density(X, Y, alpha)` — spočítá sdruženou hustotu
    $f_\alpha(x,y)$ na dané mřížce.
  - `draw_joint_density(...)` / `draw_marginal_density(...)` — sdílené vykreslovací funkce
  - `visualize_static(alpha_hodnoty)` — **statický režim**: pro zadanou
    sadu hodnot $\alpha$ vykreslí mřížku grafů vedle sebe.
  - `visualize_interactive()` — **interaktivní režim**: jeden graf s posuvníkem  pro změnu $\alpha \in \langle -1, 1 \rangle$.
## Spuštění
 
```bash
python main.py                     # interaktivní režim s posuvníkem (výchozí)
python main.py --mode static       # statické srovnání pro několik hodnot alpha
python main.py --mode interactive  # totéž jako bez argumentu
```
 
## Zdroj
 
Přednáška KMA/MSM, Blanka Šedivá — *Vícerozměrná náhodná veličina*
(verze 2026/2027).
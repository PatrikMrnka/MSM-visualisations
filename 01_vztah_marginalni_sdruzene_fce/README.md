# P01 – Vícerozměrná náhodná veličina: marginální vs. sdružená hustota

Vizualizace k přednášce **1: Vícerozměrná náhodná veličina** (KMA/MSM,
Blanka Šedivá), konkrétně k příkladu ze slidu *„Vztah marginálních a
sdružených funkcí"*.

## Teorie

Pro náhodný vektor $\mathbf{X}$ se sdruženou hustotou $f(\mathbf{x})$ jsou
marginální hustoty $f_j(x_j)$ dány jednoznačně. **Opačně to ale neplatí** —
ze znalosti marginálních rozdělení nelze (bez dalších informací)
jednoznačně určit sdruženou hustotu.

Ukazuje se to na rodině hustot

$$
f_\alpha(x,y) = 1 + \alpha(2x-1)(2y-1), \qquad
\alpha \in \langle -1,1 \rangle,\quad x,y \in (0,1),
$$

kde marginální rozdělení $f_X(x)$ a $f_Y(y)$ jsou **rovnoměrná** pro
libovolnou hodnotu parametru $\alpha$, přestože sdružená hustota se s
měnícím se $\alpha$ mění.

## Obsah

- **`main.py`**
  - `marginalni_overeni()` — symbolicky (SymPy) ověří, že marginály
    $f_X(x)$ a $f_Y(y)$ vyjdou rovnoměrné (rovny 1) nezávisle na $\alpha$.
  - `vizualizace(alpha_hodnoty)` — pro zadanou sadu hodnot $\alpha$
    vykreslí mřížku grafů: heatmapu sdružené hustoty $f_\alpha(x,y)$ a pod
    ní numericky (NumPy, lichoběžníkové pravidlo) spočtenou marginálu
    $f_X(x)$.

- **`slider.py`**
  - Interaktivní verze s posuvníkem (`matplotlib.widgets.Slider`) pro
    spojitou změnu parametru $\alpha \in \langle -1, 1 \rangle$ a okamžité
    přepočítání sdružené hustoty a marginály.

## Spuštění

```bash
python main.py      # statické srovnání pro několik hodnot alpha
python slider.py     # interaktivní verze s posuvníkem
```

## Zdroj

Přednáška KMA/MSM, Blanka Šedivá — *Vícerozměrná náhodná veličina*
(verze 2026/2027).
# MSM-visualisations

Vizualizace k předmětu **Mnohorozměrné statistické metody (MSM)**.

Repozitář slouží jako sbírka skriptů, ve kterých jsou pomocí Pythonu ilustrovány a vizualizovány pojmy a metody probírané v rámci předmětu.

## Cíl

- Doplnit teorii z přednášek o interaktivní/grafické ukázky.
- Mít na jednom místě přehledné a znovupoužitelné vizualizace pro přípravu
  na zkoušku i pro vlastní pochopení látky.

## Použité technologie

- [Python 3](https://www.python.org/) — hlavní jazyk
- [NumPy](https://numpy.org/) — maticové a numerické výpočty
- [Matplotlib](https://matplotlib.org/) — 2D/3D vizualizace
- [SymPy](https://www.sympy.org/) — symbolické výpočty (např. odvození vzorců)

## Obsah
 
| Složka | Téma |
|---|---|
| [`01_vztah_marginalni_sdruzene_fce`](01_vztah_marginalni_sdruzene_fce) | Vícerozměrná náhodná veličina — vztah marginálních a sdružených hustot |
 
## Sdílený balíček `msm_viz`
 
Aby se v každé úloze neopakoval stejný "boilerplate" kód kolem
`matplotlib`, obsahuje repozitář lokální balíček `msm_viz` s funkcemi:
 
| Funkce | K čemu slouží |
|---|---|
| `apply_style()` | Nastaví jednotný vzhled grafů (fonty, velikosti) pro celý repozitář — zavolej jednou na začátku skriptu. |
| `make_grid(n, x_range, y_range)` | Vrátí `x, y, X, Y` — 1D vektory a meshgrid pro dané rozsahy. |
| `heatmap(ax, X, Y, Z, ...)` | Vykreslí heatmapu do dané osy (`pcolormesh` + nadpis + popisky) a vrátí mesh pro colorbar. |
| `marginal_by_integration(Z, axis_values, axis)` | Numericky spočítá marginální hustotu integrací (`np.trapezoid`). |
| `save_figure(fig, path)` | Uloží graf do souboru, včetně vytvoření chybějících adresářů. |

Použití v úloze:
 
```python
from msm_viz import apply_style, make_grid, heatmap, marginal_by_integration
 
apply_style()
x, y, X, Y = make_grid(n=200)
```
 

## Instalace a spuštění
 
1. Naklonujte repozitář:
```bash
   git clone https://github.com/PatrikMrnka/MSM-visualisations.git
   cd MSM-visualisations
```
 
2. Vytvořte a aktivujte virtuální prostředí (doporučeno):
```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
```
 
3. Nainstalujte projekt (závislosti)
```bash
   pip install -e .
```
 
4. Spusťte vybraný skript, např.:
```bash
   python 01_vztah_marginalni_sdruzene_fce/main.py                    # interaktivní režim (výchozí)
   python 01_vztah_marginalni_sdruzene_fce/main.py --mode static      # statické srovnání
```

## Poznámky

Repozitář je průběžně rozšiřován v souladu s postupem látky v předmětu MSM.
#!/usr/bin/env python3
"""Chapter 112: the share of people vaccinated against Covid-19 by 31 December 2021, in countries grouped by the
World Bank's income groups, drawn in the style of the book's maps.

Data: Our World in Data, covid-19-data repository, public/data/vaccinations/vaccinations.csv (updated 15 August
2024), rows for "High income", "Upper middle income", "Lower middle income", "Low income" and "World", date
2021-12-31: people_vaccinated_per_hundred (at least one dose) and people_fully_vaccinated_per_hundred (the full
first course). OWID builds the income groups from the World Bank's classification of countries.

Against the chapter: "about three people in four in the rich countries had been vaccinated" (high income, at least
one dose: 74.9 per cent; agrees). "In the poorest countries it was fewer than one in ten" (low income: 7.5 per
cent; agrees). The upper-middle-income group, which includes China, stood slightly higher than the rich countries.
"""
import matplotlib.pyplot as plt
import lib                                                     # house fonts and colours
from lib import INK, PAPER, FILL, HALO

# OWID vaccinations.csv, 2021-12-31: (at least one dose, full first course), per hundred people
groups = [("Rich countries\n(high income)", 74.85, 68.87),
          ("Upper-middle income", 77.31, 71.47),
          ("Lower-middle income", 47.03, 34.53),
          ("Poorest countries\n(low income)", 7.52, 3.76)]
world = (57.16, 48.64)

RED = FILL["red"]
fig = plt.figure(figsize=(16, 10), dpi=100)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.25, 0.08, 0.70, 0.80])
ax.set_facecolor(PAPER)

T = dict(fontsize=18, color=INK, path_effects=HALO, zorder=7, va="center")
for i, (name, one, full) in enumerate(groups):
    y = -i * 1.0
    ax.barh(y + 0.17, one, height=0.32, color=RED, lw=0, zorder=3)
    ax.barh(y - 0.17, full, height=0.32, color="#efd9cf", ec=RED, lw=1.6, hatch="///", zorder=3)
    ax.text(one + 1, y + 0.17, f"{one:.0f}%", ha="left", fontweight="bold", **T)
    ax.text(full + 1, y - 0.17, f"{full:.0f}%", ha="left", **T)
    ax.text(-2, y, name, ha="right", linespacing=1.1, **T)

ax.plot([world[0], world[0]], [-3.5, 0.78], color=INK, lw=1.6, ls=(0, (4, 3)), zorder=2)
ax.text(world[0] + 1, 0.62, f"whole world, at least one dose: {world[0]:.0f}%", ha="left", style="italic", **T)

# key: solid bar and hatched bar, each named
ax.barh(1.22, 6, left=0, height=0.26, color=RED, lw=0, zorder=3, clip_on=False)
ax.text(7.5, 1.22, "at least one dose", ha="left", **T)
ax.barh(1.22, 6, left=36, height=0.26, color="#efd9cf", ec=RED, lw=1.6, hatch="///", zorder=3, clip_on=False)
ax.text(43.5, 1.22, "full first course", ha="left", **T)

ax.set_xlim(0, 100)
ax.set_ylim(-3.55, 1.45)
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(["0", "25%", "50%", "75%", "100%"])
ax.set_yticks([])
ax.tick_params(labelsize=18, colors=INK, length=0, pad=10)
for v in (25, 50, 75, 100):
    ax.plot([v, v], [-3.55, 0.78], color="#d8cdb8", lw=1.2, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "bottom"]:
    ax.spines[s].set_visible(False)
ax.spines["left"].set_visible(False)
ax.plot([0, 0], [-3.55, 0.78], color=INK, lw=1.6, zorder=4)
fig.text(0.04, 0.95, "People vaccinated against Covid by the end of 2021,\nby the income of their country",
         fontsize=24, color=INK, fontweight="bold", ha="left", va="center", linespacing=1.15)
out = lib.os.path.join(lib.ROOT, "chapters/112-pandemic/images/chart_vaccinated.png")
lib.os.makedirs(lib.os.path.dirname(out), exist_ok=True)
fig.savefig(out, dpi=100, facecolor=PAPER)
print("wrote", out)

"""Shareable PNG charts for the 1-in-270 jobs check. Usage: python3 -I charts.py PROJECT_DIR"""
import csv, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

P = sys.argv[1]
OUT = os.path.join(P, "charts"); os.makedirs(OUT, exist_ok=True)
rows = {int(r["occ1950"]): r for r in csv.DictReader(open(os.path.join(P, "data", "occ1950_1950_vs_2010.csv")))}

SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
TECH, DEMAND, GREY, LIGHT = "#2a78d6", "#eb6834", "#a9a8a2", "#dddcd6"
SRC = "Source: IPUMS USA, University of Minnesota, www.ipums.org. 1950 1% census sample and 2010 ACS, employed persons. Classification by judgement."
plt.rcParams.update({"font.family": ["Helvetica Neue", "Arial Unicode MS", "DejaVu Sans"], "font.size": 13, "text.color": INK,
                     "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK})


def frame(fig, title, subtitle):
    fig.patch.set_facecolor(SURF)
    fig.text(0.04, 0.95, title, fontsize=21, fontweight="bold", va="top")
    fig.text(0.04, 0.885, subtitle, fontsize=13.5, color=INK2, va="top")
    fig.text(0.04, 0.025, SRC, fontsize=9.5, color=INK2)


# --- 1. Waffle: 268 occupations of 1950 ---
GONE = [761, 365, 360, 325, 542, 520, 960, 631, 785, 304, 752, 751, 645, 501, 525, 571]
zero = [o for o, r in rows.items() if int(r["emp2010"]) == 0]
n_gone, n_recl = len(GONE), len([o for o in zero if o not in GONE])
n_rest = len(rows) - n_gone - n_recl
fig = plt.figure(figsize=(12, 7.5))
frame(fig, "“Only 1 of 270 jobs from 1950 is obsolete”?",
      f"Each square is one of the {len(rows)} US Census occupation categories of 1950, as they stood in 2010")
ax = fig.add_axes([0.04, 0.1, 0.46, 0.72]); ax.set_axis_off()
cols = 20
cells = [INK] * 1 + [TECH] * (n_gone - 1) + [LIGHT] * n_recl + [GREY] * n_rest
for i, c in enumerate(cells):
    x, y = i % cols, -(i // cols)
    ax.add_patch(Rectangle((x, y), 0.86, 0.86, facecolor=c, edgecolor="none"))
ax.set_xlim(-0.2, cols); ax.set_ylim(-(len(cells) // cols) - 0.4, 1.1); ax.set_aspect("equal")
lx = 0.54
items = [(INK, "1", "gone mainly through automation\n(the elevator operator)"),
         (TECH, str(n_gone - 1), "also gone or nearly gone: telegraph operators,\nrailway mail clerks, locomotive firemen,\nprinting-plate makers, boarding-house keepers…"),
         (LIGHT, str(n_recl), "vanish from the statistics only because\nthe job was merged into another category"),
         (GREY, str(n_rest), "still exist as categories, though many\nshrank sharply (telephone operators −77%)")]
for k, (c, n, txt) in enumerate(items):
    y = 0.76 - k * 0.17
    fig.patches.append(Rectangle((lx, y - 0.005), 0.022, 0.035, transform=fig.transFigure, facecolor=c, figure=fig))
    fig.text(lx + 0.035, y + 0.012, n, fontsize=22, fontweight="bold", va="center")
    fig.text(lx + 0.1, y + 0.012, txt, fontsize=12, color=INK, va="center", linespacing=1.3)
fig.savefig(os.path.join(OUT, "1-waffle-1950-occupations.png"), dpi=200, facecolor=SURF); plt.close(fig)

# --- 2. The jobs that went, sized by 1950 workforce, coloured by cause ---
CAUSE = {761: ("Elevator operators", "auto"), 365: ("Telegraph operators", "tech"), 360: ("Telegraph messengers", "tech"),
         325: ("Railway mail clerks & express messengers", "tech"), 542: ("Locomotive firemen", "tech"),
         520: ("Electrotypers & stereotypers", "tech"), 960: ("Teamsters (horse & wagon)", "tech"),
         631: ("Bus & streetcar conductors", "tech"), 785: ("Crossing watchmen & bridge tenders", "tech"),
         304: ("Baggagemen", "demand"), 752: ("Boarding-house keepers", "demand"), 751: ("Bootblacks", "demand"),
         645: ("Milliners", "demand"), 501: ("Blacksmiths", "tech"), 525: ("Furriers", "demand")}
items = sorted(((CAUSE[o][0], int(rows[o]["emp1950"]), CAUSE[o][1]) for o in CAUSE), key=lambda t: t[1])
fig = plt.figure(figsize=(12, 8))
frame(fig, "The jobs of 1950 that have (nearly) disappeared",
      "US workers in each occupation in 1950. The 1950 occupation list is usually said to have lost only the elevator operator.")
ax = fig.add_axes([0.33, 0.1, 0.6, 0.66]); ax.set_facecolor(SURF)
colour = {"auto": TECH, "tech": TECH, "demand": DEMAND}
bars = ax.barh([t[0] for t in items], [t[1] for t in items], color=[colour[t[2]] for t in items], height=0.66)
for b, t in zip(bars, items):
    ax.text(b.get_width() + 900, b.get_y() + b.get_height() / 2, f"{t[1]:,}", va="center", fontsize=11, color=INK2)
    if t[2] == "auto":
        ax.text(b.get_width() + 13000, b.get_y() + b.get_height() / 2, "← the ‘only one’", va="center", fontsize=11, fontweight="bold")
for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID); ax.tick_params(left=False); ax.xaxis.grid(True, color=GRID); ax.set_axisbelow(True)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{int(v/1000)}k" if v else "0"))
ax.set_xlim(0, 140000)
fig.patches.append(Rectangle((0.33, 0.795), 0.018, 0.025, transform=fig.transFigure, facecolor=TECH, figure=fig))
fig.text(0.353, 0.807, "Technology removed the job or what it served", fontsize=11.5, va="center")
fig.patches.append(Rectangle((0.66, 0.795), 0.018, 0.025, transform=fig.transFigure, facecolor=DEMAND, figure=fig))
fig.text(0.683, 0.807, "Demand fell away", fontsize=11.5, va="center")
fig.savefig(os.path.join(OUT, "2-jobs-that-disappeared.png"), dpi=200, facecolor=SURF); plt.close(fig)

# --- 3. Survived on paper, collapsed in practice ---
SHRINK = {624: "Railway brakemen", 684: "Textile weavers", 570: "Pattern & model makers", 100: "Farmers (owners & tenants)",
          512: "Compositors & typesetters", 565: "Paperhangers", 370: "Telephone operators",
          680: "Stationary firemen (boilers)", 674: "Sawyers", 635: "Metal filers, grinders & polishers"}
items = sorted(((SHRINK[o], int(rows[o]["emp1950"]), int(rows[o]["emp2010"])) for o in SHRINK),
               key=lambda t: t[2] / t[1], reverse=True)
fig = plt.figure(figsize=(12, 7.5))
frame(fig, "Still on the list, mostly gone from the workforce",
      "Change in US employment 1950–2010, occupations that survive as census categories")
ax = fig.add_axes([0.33, 0.1, 0.6, 0.7]); ax.set_facecolor(SURF)
pct = [(b - a) / a * 100 for _, a, b in items]
bars = ax.barh([t[0] for t in items], pct, color=TECH, height=0.66)
for b, t, p in zip(bars, items, pct):
    ax.text(p + 1.5, b.get_y() + b.get_height() / 2, f"−{abs(p):.0f}%", va="center", ha="left", fontsize=12, fontweight="bold", color="white")
    ax.text(1.5, b.get_y() + b.get_height() / 2, f"{t[1]:,} → {t[2]:,}", va="center", ha="left", fontsize=10.5, color=INK2)
ax.set_xlim(-100, 32); ax.axvline(0, color=INK2, lw=1)
for s in ("top", "right", "left", "bottom"): ax.spines[s].set_visible(False)
ax.tick_params(left=False, bottom=False); ax.set_xticks([])
fig.savefig(os.path.join(OUT, "3-survived-but-collapsed.png"), dpi=200, facecolor=SURF); plt.close(fig)

# --- 4. Headline card: the other half of the picture ---
fig = plt.figure(figsize=(12, 6.75)); fig.patch.set_facecolor(SURF)
fig.text(0.06, 0.86, "The 1950 list can only show what was lost.", fontsize=22, fontweight="bold", va="top")
fig.text(0.06, 0.76, "It can never show what is new.", fontsize=22, color=INK2, va="top")
fig.text(0.06, 0.58, "~60%", fontsize=86, fontweight="bold", color=TECH, va="top")
fig.text(0.40, 0.535, "of US employment in 2018 was in kinds of work\nthat did not exist in 1940", fontsize=19, va="top", linespacing=1.35)
fig.text(0.06, 0.2, f"Of the 1950 categories: 1 obvious automation casualty (the elevator operator), about {n_gone} gone or nearly gone,\n"
         "and many more shrank by 70–93% while staying on the list.", fontsize=14, color=INK, linespacing=1.4)
fig.text(0.06, 0.05, "Sources: Autor, Chin, Salomons & Seegmiller, ‘New Frontiers’, QJE 2024; IPUMS USA, University of Minnesota, www.ipums.org.",
         fontsize=9.5, color=INK2)
fig.savefig(os.path.join(OUT, "4-headline-new-work.png"), dpi=200, facecolor=SURF); plt.close(fig)


# --- 5 and 6. Trends 1950-2019 (OCC1990 scheme) ---
SRC2 = "Source: IPUMS USA, University of Minnesota, www.ipums.org. Census samples 1950\u20132000, ACS 2010 and 2019, employed persons, 1990 occupation scheme."
tr = {int(r["occ1990"]): r for r in csv.DictReader(open(os.path.join(P, "data", "occ1990_by_year.csv")))}
YRS = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2019]
def series(code, drop=()):
    return [(y, int(tr[code][str(y)])) for y in YRS if y not in drop]

RISE = [(308, "Computer operators", (1950, 1960, 2019)), (385, "Data-entry keyers", (1950, 1960)),
        (315, "Typists", (1950,)), (348, "Telephone operators", ()),
        (774, "Photo-lab workers", ()), (314, "Stenographers", (1950, 2000, 2010, 2019))]
fig = plt.figure(figsize=(12, 7.5))
frame(fig, "Jobs that technology created, then took away",
      "US workers, thousands. Each grew with one generation of office or communication technology and shrank with the next.")
fig.texts[-1].set_text(SRC2)
for i, (code, name, drop) in enumerate(RISE):
    ax = fig.add_axes([0.06 + (i % 3) * 0.31, 0.47 - (i // 3) * 0.36, 0.26, 0.25]); ax.set_facecolor(SURF)
    pts = series(code, drop)
    xs, ys = [p[0] for p in pts], [p[1] / 1000 for p in pts]
    ax.plot(xs, ys, color=TECH, lw=2.4, marker="o", ms=4.5)
    pk = max(range(len(ys)), key=lambda k: ys[k])
    ax.annotate(f"{ys[pk]:,.0f}k", (xs[pk], ys[pk]), textcoords="offset points", xytext=(0, 7), ha="center", fontsize=10.5, fontweight="bold")
    ax.annotate(f"{ys[-1]:,.0f}k", (xs[-1], ys[-1]), textcoords="offset points", xytext=(4, 7), ha="center", fontsize=10, color=INK2)
    ax.set_title(name, loc="left", fontsize=13.5, fontweight="bold", pad=14)
    ax.set_ylim(0, max(ys) * 1.3); ax.set_xlim(1945, 2024); ax.set_xticks([1950, 1970, 1990, 2010])
    for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
    ax.spines["bottom"].set_color(GRID); ax.tick_params(left=False, labelsize=10); ax.set_yticks([])
fig.savefig(os.path.join(OUT, "5-rise-and-fall.png"), dpi=200, facecolor=SURF); plt.close(fig)

NEW = [(229, "Software developers"), (64, "Computer systems analysts and scientists")]
fig = plt.figure(figsize=(12, 7.5))
frame(fig, "Meanwhile: work nobody did in 1950",
      "US workers in two computing occupations that did not exist as census categories before 1970, millions")
fig.texts[-1].set_text(SRC2)
ax = fig.add_axes([0.08, 0.12, 0.62, 0.66]); ax.set_facecolor(SURF)
for (code, name), c in zip(NEW, (TECH, DEMAND)):
    pts = series(code, (1950, 1960)); xs, ys = [p[0] for p in pts], [p[1] / 1e6 for p in pts]
    ax.plot(xs, ys, color=c, lw=2.6, marker="o", ms=5)
    ax.annotate(f"{name}\n{ys[-1]:.1f}M in 2019", (xs[-1], ys[-1]), textcoords="offset points", xytext=(12, 0), va="center", fontsize=12, annotation_clip=False)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.spines["bottom"].set_color(GRID); ax.tick_params(left=False); ax.yaxis.grid(True, color=GRID); ax.set_axisbelow(True)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:.1f}M" if v else "0"))
ax.set_xticks(YRS[2:]); ax.set_ylim(0, 3.1)
fig.savefig(os.path.join(OUT, "6-new-work.png"), dpi=200, facecolor=SURF); plt.close(fig)
print("ok")

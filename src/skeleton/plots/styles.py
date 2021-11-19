from skeleton.plots.colors import plt_tab_colors


MKBHD = {
    "rcParams": {
        # Background color
        "axes.facecolor": "black",
        "figure.facecolor": "black",
        # Labels settings
        "axes.labelcolor": "white",
        "axes.labelsize": 20,
        "axes.labelpad": 25,
        # XY line axis color
        "axes.edgecolor": "white",
        "axes.labelcolor": "white",
        # XY line width
        "axes.linewidth": 5,
        # XY line remove top/right
        "axes.spines.right": False,
        "axes.spines.top": False,
        # Change xy axis color
        "xtick.color": "white",
        "ytick.color": "white",
        "xtick.major.size": 10,
        "xtick.major.width": 3,
        "ytick.major.size": 10,
        "ytick.major.width": 3,
        # Y grid
        "grid.color": "lightgray",
        "grid.alpha": 0.4,
        "axes.grid": True,
        "axes.grid.axis": "y",
        # Savefig properties
        "savefig.facecolor": "black",
        "savefig.edgecolor": "black",
        "figure.figsize": [6.4, 4.8],
    },
    "settings": {
        "xticks": {"rotation": 45, "fontsize": 13, "fontweight": "bold"},
        "yticks": {"fontsize": 15, "fontweight": "bold"},
    },
    "colors": {"1cat": "white", "ncats": plt_tab_colors},
}

from skeleton.plots.colors import plt_tab_colors

style = {
    "rcParams": {
        # Background color
        "axes.facecolor": "white",
        "figure.facecolor": "white",
        # Labels settings
        "axes.labelcolor": "black",
        "axes.labelsize": 20,
        "axes.labelpad": 23,
        # XY line axis color
        "axes.edgecolor": "black",
        # XY line width
        "axes.linewidth": 2,
        # XY line remove top/right
        "axes.spines.right": False,
        "axes.spines.top": False,
        # Change xy axis color
        "xtick.color": "black",
        "ytick.color": "black",
        "xtick.major.size": 6,
        "xtick.major.width": 1,
        "ytick.major.size": 7.2,
        "ytick.major.width": 1,
        # Y grid
        "grid.color": "lightgray",
        "grid.alpha": 0.3,
        "axes.grid": True,
        "axes.grid.axis": "y",
        # Savefig properties
        "savefig.facecolor": "white",
        "savefig.edgecolor": "white",
    },
    "scatter_style": {
        "s": 40,
    },
    "line_style": {
        "linewidth": 1.5,
    },
    "lineshadow_style": {
        "linewidth": 1,
    },
    "scattershadow_style": {
        "s": 40,
    },
    "styleParams": {
        "xticks": {"rotation": 45, "fontsize": 13, "fontweight": "normal"},
        "yticks": {"fontsize": 15, "fontweight": "normal"},
        "ylabel": {},
        "xlabel": {},
        "title": {
            "fontsize": 24,
            "fontweight": "bold",
            "xy": (0.00, 1.12),
            "xycoords": "axes fraction",
        },
        "subtitle": {
            "fontsize": 19,
            "color": "#696969",
            "xy": (0.00, 1.05),
            "xycoords": "axes fraction",
        },
    },
    "colors": {"1cat": "tab:blue", "ncats": plt_tab_colors, "grayed": "lightgray"},
}

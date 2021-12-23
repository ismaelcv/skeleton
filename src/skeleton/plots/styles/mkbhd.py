from skeleton.plots.colors import plt_tab_colors

style = {
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
        # XY line width
        "axes.linewidth": 4,
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
    },
    "scatter_style": {
        "s": 40,
    },
    "line_style": {
        "linewidth": 1.5,
    },
    "scattershadow_style": {
        "s": 40,
    },
    "lineshadow_style": {
        "linewidth": 1,
    },
    "styleParams": {
        "xticks": {"rotation": 45, "fontsize": 13, "fontweight": "bold"},
        "yticks": {"fontsize": 15, "fontweight": "bold"},
        "title_style": {
            "fontsize": 24,
            "color": "white",
            "fontweight": "bold",
            "xy": (0.00, 1.11),
            "xycoords": "axes fraction",
        },
        "subtitle_style": {
            "color": "red",
            "fontsize": 20,
            "xy": (0.00, 1.05),
            "xycoords": "axes fraction",
        },
    },
    "colors": {"1cat": "red", "ncats": plt_tab_colors, "grayed": "lightgray"},
}

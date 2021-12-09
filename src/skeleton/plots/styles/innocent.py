from skeleton.plots.colors import plt_tab_colors

style = {
    "rcParams": {
        # Background color
        "axes.facecolor": "#F3F0E0",
        "figure.facecolor": "#F3F0E0",
        # Labels settings
        "axes.labelcolor": "black",
        "axes.labelsize": 20,
        "axes.labelpad": 25,
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
        "xtick.major.size": 7,
        "xtick.major.width": 1,
        "ytick.major.size": 7,
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
    "styleParams": {
        "xticks": {"rotation": 45, "fontsize": 13, "fontweight": "normal"},
        "yticks": {"fontsize": 15, "fontweight": "normal"},
        "title_style": {
            "fontsize": 24,
            "fontweight": "bold",
            "xy": (0.00, 1.10),
            "xycoords": "axes fraction",
        },
        "subtitle_style": {
            "fontsize": 19,
            "color": "#696969",
            "xy": (0.00, 1.05),
            "xycoords": "axes fraction",
        },
    },
    "colors": {"1cat": "#16264c", "ncats": plt_tab_colors},
}

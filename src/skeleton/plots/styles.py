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
    "styleParams": {
        "xticks": {"rotation": 45, "fontsize": 13, "fontweight": "bold"},
        "yticks": {"fontsize": 15, "fontweight": "bold"},
        "marker_size": 50,
        "marker_shadow": True,
    },
    "colors": {"1cat": "red", "ncats": plt_tab_colors},
}


BASE_STYLE = {
    "rcParams": {
        # Background color
        "axes.facecolor": "white",
        "figure.facecolor": "white",
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
    "styleParams": {
        "xticks": {"rotation": 45, "fontsize": 13, "fontweight": "normal"},
        "yticks": {"fontsize": 15, "fontweight": "normal"},
        "marker_size": 40,
        "marker_shadow": False,
    },
    "colors": {"1cat": "tab:blue", "ncats": plt_tab_colors},
}


STYLES = {
    "base": BASE_STYLE,
    "mkbhd": MKBHD,
}

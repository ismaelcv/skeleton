from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from skeleton.wrangling.grouping import ratio_per_category


def plot_percentage_per_subcategory(
    df: pd.DataFrame, primary: str, secondary: str
) -> Tuple[Figure, plt.Axes]:
    """
    Parameters
    ----------
    df : A pivoted dataframe with primary category as row index
         and secondary category as row columns
    primary: name of the main category in the dataframe
    secondary: name of the category to aggregate in the dataframe
    """

    per_cat_perc = ratio_per_category(df, primary, secondary)

    pivot_per_cat_perc = pd.pivot_table(
        per_cat_perc, values=f"perc_{secondary}", index=primary, columns=secondary, aggfunc=np.sum
    ).round(1)

    category_names = pivot_per_cat_perc.columns
    labels = list(pivot_per_cat_perc.index)
    data = pivot_per_cat_perc.values
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap("RdYlGn")(np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(20, len(labels) * 2))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        print(colname)

        rects = ax.barh(labels, widths, left=starts, height=0.5, label=colname, color=color)

        r, g, b, _ = color
        text_color = "white" if r * g * b < 0.5 else "darkgrey"
        ax.bar_label(rects, label_type="center", color=text_color, size=17, weight="bold")
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1), loc="lower left", fontsize=15)

    return fig, ax

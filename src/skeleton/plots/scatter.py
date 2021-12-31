from __future__ import annotations

from typing import Optional, Union

import pandas as pd
from matplotlib import pyplot as plt
from skeleton.plots.utils import load_styles

STYLES = load_styles()


class graph:

    """
    Generic class to genererate a plt graph
    """

    def __init__(self, df: pd.DataFrame, x: str, y: str) -> None:

        plt.rcParams.update(plt.rcParamsDefault)

        self.df = df
        self.x = x
        self.y = y
        self.styleParams = STYLES["base"]["styleParams"]
        self.rcParams = STYLES["base"]["rcParams"]
        self.colors = STYLES["base"]["colors"]
        self._set_figsize()
        self.z = ""  # type: str
        self.main_categories = []  # type: list
        self.notes = []  # type: list
        self.style = STYLES["base"]

    def color_by(self, column_name: str) -> graph:
        """
        Set the color for the plot.

        """

        if column_name not in self.df.columns:
            raise ValueError(f"{column_name} not in dataframe")

        self.z = column_name

        self.styleParams["color_by"] = column_name

        if self.main_categories == []:
            self.main_categories = list(self.df[column_name].unique())

        available_values = list(
            self.df.loc[self.df[self.z].isin(self.main_categories), self.z].value_counts().index
        )

        if len(self.main_categories) > 20:
            print(
                f"Posible categories to .focus_on()  {available_values[:20]} and {len(self.main_categories) - 20} more"
            )
        else:
            print(f"Possible categories to .focus_on() {available_values}")

        return self

    def focus_on(self, category: Union[str, list]) -> None:
        """
        Set the main category for the plot.

        """

        if self.z == "":
            raise ValueError(
                """
                No column to split on selected (z)
                Please select a column with .color_by("column_name ")
                """
            )

        all_cats_available = list(self.df[self.z].unique())

        if self.main_categories == all_cats_available:
            self.main_categories = []

        if isinstance(category, str):

            if category not in all_cats_available:
                raise ValueError(
                    f"{category} is not included on the main categories avalable in the {self.z} column"
                )
            self.main_categories.append(category)

        elif isinstance(category, list):

            invalid_categories = []
            for requested_cat in category:
                if requested_cat not in all_cats_available:
                    invalid_categories.append(requested_cat)

            if len(invalid_categories) > 0:
                raise ValueError(
                    f"{invalid_categories} does not form part of the available categories of  the column {self.x}"
                )

            self.main_categories.append(category)

        self.main_categories = list(pd.Series(self.main_categories).unique())

    def set_style(self, style: str) -> graph:

        if style in STYLES:
            self.style = STYLES[style]
            self.styleParams = STYLES[style]["styleParams"]
            self.rcParams = STYLES[style]["rcParams"]
            self.colors = STYLES[style]["colors"]
        else:
            raise ValueError(f"{style} is not a valid style")

        return self

    def set_title(self, title: str) -> None:
        self.styleParams["title_style"]["text"] = title

    def set_subtitle(self, subtitle: str) -> None:
        self.styleParams["subtitle_style"]["text"] = subtitle
        self.styleParams["title_style"]["xy"] = (0.00, 1.13)

    def _set_figsize(self, w: int = 12, h: int = 6) -> None:
        if w > 0 and h > 0:
            self.rcParams["figure.figsize"] = [w, h]

    def _set_styleParams(self, params: dict) -> None:
        """
        Set parameters for the plot.

        """
        for key, value in params.items():
            if key in self.styleParams:
                self.styleParams[key] = value

    def _apply_style(self) -> None:

        if "text" in self.styleParams["title_style"]:
            plt.annotate(**self.styleParams["title_style"])

        if "text" in self.styleParams["subtitle_style"]:
            plt.annotate(
                **self.styleParams["subtitle_style"],
            )

        if "xticks" in self.styleParams:
            plt.xticks(**self.styleParams["xticks"])

        if "yticks" in self.styleParams:
            plt.yticks(**self.styleParams["yticks"])

        plt.ylabel(self.y)
        plt.xlabel(self.x)

    def add_note(
        self,
        text: str,
        x: float,
        y: Optional[float] = None,
        category: Optional[str] = None,
        **kwargs: dict,
    ) -> None:

        if text is None:
            raise ValueError("An input text is required")

        if x is not None and y is not None:
            self.notes.append(
                [
                    {
                        "text": text,
                        "xy": (x, y),
                        "xytext": (x + 5, y + 10),
                        "arrowprops": {"arrowstyle": "->", "connectionstyle": "angle3,angleA=0,angleB=-90"},
                        "size": 15,
                    },
                    kwargs,
                ]
            )
        if category is not None and category not in self.main_categories:
            raise ValueError(
                f"{category} not in main categories. Available categories f{self.main_categories}"
            )

        if category is not None and self.z == "":
            raise ValueError(
                """
                It is not possible to specify a category on a single colored plot.
                Use color_by() to be able to specify a category
                """
            )

        if y is None:

            self._check_is_numeric(self.x)

            if category is None and len(self.main_categories) > 1:
                raise ValueError(
                    f"""
                Error: Ambiguity where to place the note You need to specify a category.
                Available categories {self.main_categories}"
                """
                )

            if category is None and self.z == "":
                selection = self.df[self.x]
                index_closest_x = abs(selection.sort_values() - x).sort_values().index[0]

            elif category is not None:
                selection = self.df[self.df[self.z] == category][self.x]
                index_closest_x = abs(selection.sort_values() - x).sort_values().index[0]

            closest_x = selection.loc[index_closest_x]
            y = self.df[self.df[self.x] == closest_x][self.y].iat[0]

            self.notes.append(
                [
                    {
                        "text": text,
                        "xy": (closest_x, y),
                        "xytext": (closest_x + 5, y + 10),
                        "arrowprops": {"arrowstyle": "->", "connectionstyle": "angle3,angleA=0,angleB=-90"},
                        "size": 15,
                    },
                    kwargs,
                ]
            )

    def _check_is_numeric(self, column: str) -> None:
        try:
            self.df[column].astype("float64")
        except ValueError:
            print(
                f"""
                {column} is not a numerical python type.
                Notes based on only one axis can only be perfom on numerical columns")
                """
            )

    def show(self) -> None:

        plt.rcParams.update(self.rcParams)

        if self.z != "":
            categories = self.df[self.z].unique().tolist()
            if len(categories) == 0:
                raise ValueError("No categories found: Length of categories is 0")
        else:
            categories = []

        if len(categories) <= 1:
            color = self.colors["1cat"]
            plt.plot(self.df[self.x], self.df[self.y], color=color, **self.style["line_style"])

        else:
            colors = self.colors["ncats"]

            for category in categories:

                if category not in self.main_categories:

                    x_axis = self.df[self.x][self.df[self.z] == category]
                    y_axis = self.df[self.y][self.df[self.z] == category]

                    plt.plot(x_axis, y_axis, color=self.colors["grayed"], **self.style["lineshadow_style"])

            for i, category in enumerate(self.main_categories):

                if len(self.main_categories) == 1:
                    color = self.colors["1cat"]
                else:
                    color = colors[i % len(colors)]

                x_axis = self.df[self.x][self.df[self.z] == category]
                y_axis = self.df[self.y][self.df[self.z] == category]

                plt.plot(x_axis, y_axis, color=color, **self.style["line_style"])

        plt.show()


# class base_scatter(graph):
#     def show(self) -> None:

#         if self.z != "":
#             categories = self.df[self.z].unique().tolist()

#             if len(categories) == 0:
#                 raise ValueError("No categories found: Length of categories is 0")
#         else:
#             categories = []

#         plt.rcParams.update(self.rcParams)

#         if len(categories) <= 1:

#             color = self.colors["1cat"]
#             plt.scatter(self.df[self.x], self.df[self.y], color=color, **self.style["scatter_style"])

#         else:
#             colors = self.colors["ncats"]

#             for category in categories:

#                 if category not in self.main_categories:

#                     x_axis = self.df[self.x][self.df[self.z] == category]
#                     y_axis = self.df[self.y][self.df[self.z] == category]

#                     plt.scatter(
#                         x_axis, y_axis, color=self.colors["grayed"], **self.style["scattershadow_style"]
#                     )

#             for i, category in enumerate(self.main_categories):

#                 if len(self.main_categories) == 1:
#                     color = self.colors["1cat"]
#                 else:
#                     color = colors[i % len(colors)]

#                 x_axis = self.df[self.x][self.df[self.z] == category]
#                 y_axis = self.df[self.y][self.df[self.z] == category]

#                 plt.scatter(x_axis, y_axis, color=color, **self.style["scatter_style"])

#         for note, kwargs in self.notes:

#             plt.annotate(**note, **kwargs)

#         self.add_plot_style()

#         plt.show()


# class base_lineplot(graph):
#     def show(self) -> None:

#         plt.rcParams.update(self.rcParams)

#         if self.z != "":
#             categories = self.df[self.z].unique().tolist()
#             if len(categories) == 0:
#                 raise ValueError("No categories found: Length of categories is 0")
#         else:
#             categories = []


#         if len(categories) <= 1:
#             color = self.colors["1cat"]
#             plt.plot(self.df[self.x], self.df[self.y], color=color, **self.style["line_style"])

#         else:
#             colors = self.colors["ncats"]

#             for category in categories:

#                 if category not in self.main_categories:

#                     x_axis = self.df[self.x][self.df[self.z] == category]
#                     y_axis = self.df[self.y][self.df[self.z] == category]

#                     plt.plot(x_axis, y_axis, color=self.colors["grayed"], **self.style["lineshadow_style"])

#             for i, category in enumerate(self.main_categories):

#                 if len(self.main_categories) == 1:
#                     color = self.colors["1cat"]
#                 else:
#                     color = colors[i % len(colors)]

#                 x_axis = self.df[self.x][self.df[self.z] == category]
#                 y_axis = self.df[self.y][self.df[self.z] == category]

#                 plt.plot(x_axis, y_axis, color=color, **self.style["line_style"])

#         for note, kwargs in self.notes:

#             plt.annotate(**note, **kwargs)

#         self._apply_style()

#         plt.show()


# class base_scatter(graph):


class plot(graph):
    ...

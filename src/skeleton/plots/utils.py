import importlib
import pkgutil

import skeleton.plots.styles as defined_styles


def load_styles() -> dict:

    styles = [x.name for x in pkgutil.iter_modules(defined_styles.__path__)]

    STYLES = {}

    for style in styles:

        STYLES[style] = importlib.import_module(f"skeleton.plots.styles.{style}.style").style  # type: ignore

    return STYLES

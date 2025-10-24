from .math import MathStyle
from .ml import MLStyle
from .cs import CSStyle

_STYLES = {s.name: s for s in [MathStyle(), MLStyle(), CSStyle()]}


def list_field_styles():
    return sorted(_STYLES.keys())


def get_style(name: str):
    try:
        return _STYLES[name]
    except KeyError:
        raise SystemExit(
            f"Unknown field style '{name}'. Available: {
                ', '.join(list_field_styles())}"
        )

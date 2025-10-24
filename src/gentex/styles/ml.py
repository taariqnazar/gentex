from textwrap import dedent
from .base import FieldStyle


class MLStyle(FieldStyle):
    def __init__(self):
        super().__init__(
            name="ml", description="ML numeric compact", bib_engine="biblatex"
        )

    def render_preamble(self) -> str:
        return dedent(r"""
        \usepackage[T1]{fontenc}
        \usepackage[utf8]{inputenc}
        \usepackage{lmodern}
        \usepackage[a4paper,margin=1in]{geometry}
        \usepackage{microtype}
        \usepackage{mathtools, amsmath, amssymb}
        \usepackage{graphicx}
        \usepackage{subcaption}
        \usepackage{booktabs}
        \usepackage{siunitx}

        % Numeric, compact bibliography
        \usepackage[backend=biber,style=numeric-comp,sorting=none,maxbibnames=99,natbib=true]{biblatex}

        \usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
        \usepackage[nameinlink,capitalise,noabbrev]{cleveref}

        \usepackage{algorithm}
        \usepackage[noend]{algpseudocode}

        \graphicspath{{figures/}}
        \numberwithin{equation}{section}
        """).lstrip()

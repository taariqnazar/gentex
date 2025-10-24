from textwrap import dedent
from .base import FieldStyle


class CSStyle(FieldStyle):
    def __init__(self):
        super().__init__(
            name="cs", description="CS style with code listings", bib_engine="biblatex"
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
        \usepackage{listings}

        % Numeric bib with biber
        \usepackage[backend=biber,style=numeric,sorting=none,maxbibnames=99,natbib=true]{biblatex}

        \usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
        \usepackage[nameinlink,capitalise,noabbrev]{cleveref}

        \graphicspath{{figures/}}
        \numberwithin{equation}{section}
        """).lstrip()

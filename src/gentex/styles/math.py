from textwrap import dedent
from .base import FieldStyle


class MathStyle(FieldStyle):
    def __init__(self):
        super().__init__(
            name="math",
            description="Math / math-stat (author–year)",
            bib_engine="biblatex",
        )

    def render_preamble(self) -> str:
        return dedent(r"""
        % Fonts, encoding, layout
        \usepackage[T1]{fontenc}
        \usepackage[utf8]{inputenc}
        \usepackage{lmodern}
        \usepackage[a4paper,margin=1in]{geometry}
        \usepackage{microtype}

        % Math
        \usepackage{mathtools, amsmath, amssymb, amsthm}
        \usepackage{bm}
        \usepackage{bbm}

        % Figures, tables, units
        \usepackage{graphicx}
        \usepackage{subcaption}
        \usepackage{booktabs}
        \usepackage{siunitx}

        % Citations: biblatex author–year, natbib-compatible
        \usepackage[backend=biber,style=authoryear,sorting=nyt,maxcitenames=2,maxbibnames=6,natbib=true]{biblatex}

        % Hyperrefs & clever references
        \usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
        \usepackage[nameinlink,capitalise,noabbrev]{cleveref}

        % Algorithms
        \usepackage{algorithm}
        \usepackage[noend]{algpseudocode}

        % Graphics path
        \graphicspath{{figures/}}

        % Theorem environments and common macros
        \numberwithin{equation}{section}
        \theoremstyle{plain}
        \newtheorem{theorem}{Theorem}[section]
        \newtheorem{lemma}[theorem]{Lemma}
        \newtheorem{proposition}[theorem]{Proposition}
        \newtheorem{corollary}[theorem]{Corollary}
        \newtheorem{assumption}[theorem]{Assumption}
        \theoremstyle{definition}
        \newtheorem{definition}[theorem]{Definition}
        \theoremstyle{remark}
        \newtheorem{remark}[theorem]{Remark}

        \DeclareMathOperator*{\argmin}{arg\,min}
        \DeclareMathOperator*{\argmax}{arg\,max}
        \DeclareMathOperator{\Var}{Var}
        \DeclareMathOperator{\Cov}{Cov}
        \DeclareMathOperator{\diag}{diag}
        \newcommand{\E}{\mathbb{E}}
        \newcommand{\Prob}{\mathbb{P}}
        \newcommand{\R}{\mathbb{R}}
        \newcommand{\N}{\mathbb{N}}
        \newcommand{\1}{\mathbbm{1}}
        \newcommand{\indep}{\perp\!\!\!\perp}
        \newcommand{\norm}[1]{\left\lVert #1 \right\rVert}
        \newcommand{\ip}[2]{\left\langle #1,\, #2 \right\rangle}
        \newcommand{\KL}[2]{\mathrm{KL}\!\left(#1\,\|\,#2\right)}
        """).lstrip()

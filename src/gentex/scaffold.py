from pathlib import Path
from textwrap import dedent

DEFAULT_MAIN = dedent(r"""
\documentclass[11pt,a4paper]{article}

\input{preamble.tex}
\addbibresource{refs.bib}

\title{Your Title}
\author{Your Name}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
A short abstract goes here.
\end{abstract}

\section{Introduction}
This is a math/ML/stat template. For example, \citet{example2025} show that \dots\ or see \citep{example2025}.

\section{Preliminaries}
Let $x \in \R^d$. We use norms $\norm{\cdot}$, inner products $\ip{\cdot}{\cdot}$, and random variables with
$\E[X]$, $\Var(X)$, and $\Prob(A)$.

\section{Main Results}
\begin{theorem}
Let $X$ be a random variable with finite variance. Then $\Var(X) \ge 0$.
\end{theorem}

\begin{proof}
Immediate from the definition $\Var(X) = \E[(X-\E[X])^2]$.
\end{proof}

\section{An Algorithm}
\begin{algorithm}
\caption{Example Procedure}
\begin{algorithmic}[1]
\State Initialize parameters $\theta$
\For{$t=1,2,\dots,T$}
  \State Update $\theta \gets \theta - \eta \nabla f(\theta)$
\EndFor
\State \Return $\theta$
\end{algorithmic}
\end{algorithm}

\section{Conclusion}
Discussion and future work.

\printbibliography
\end{document}
""").lstrip()

DEFAULT_PREAMBLE = dedent(r"""
% Fonts, encoding, layout
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{microtype}

% Math
\usepackage{mathtools, amsmath, amssymb, amsthm}
\usepackage{bm}     % bold math
\usepackage{bbm}    % \mathbbm{1} indicator

% Figures, tables, units
\usepackage{graphicx}
\usepackage{subcaption}
\usepackage{booktabs}
\usepackage{siunitx}

% Citations: biblatex (author-year) with natbib compatibility
\usepackage[backend=biber,style=authoryear,sorting=nyt,maxcitenames=2,maxbibnames=6,natbib=true]{biblatex}

% Hyperrefs & clever references
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\usepackage[nameinlink,capitalise,noabbrev]{cleveref}

% Algorithms (algorithmicx)
\usepackage{algorithm}
\usepackage[noend]{algpseudocode}

% Graphics path
\graphicspath{{figures/}}

% Theorem environments
\numberwithin{equation}{section}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{assumption}[theorem]{Assumption}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

% Common operators & macros
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

% Cleveref names (optional fine-tuning)
\crefname{assumption}{Assumption}{Assumptions}
\Crefname{assumption}{Assumption}{Assumptions}
""").lstrip()

DEFAULT_BIB = dedent(r"""
@article{example2025,
  author  = {Doe, Jane and Smith, John},
  title   = {An Example Article},
  journal = {Journal of Examples},
  year    = {2025},
  volume  = {1},
  number  = {1},
  pages   = {1--10},
  doi     = {10.0000/example}
}
""").lstrip()

DEFAULT_STYLE = dedent(r"""
%% style/template.sty -- place your journal/conference tweaks here.
%% Example: macros specific to a certain paper.
% \newcommand{\myAlgo}{\textsc{MyAlgo}}
""").lstrip()


def scaffold(project_name: str, dest: Path = Path(".")) -> Path:
    """
    Create a LaTeX project folder with:
      main.tex, preamble.tex, refs.bib, figures/, style/
    (Modern workflow: biblatex+biber, author–year, natbib-compatible)
    """
    root = dest / project_name
    root.mkdir(parents=True, exist_ok=False)

    # Directories
    (root / "figures").mkdir(parents=True, exist_ok=True)
    (root / "style").mkdir(parents=True, exist_ok=True)

    # Files
    (root / "main.tex").write_text(DEFAULT_MAIN, encoding="utf-8")
    (root / "preamble.tex").write_text(DEFAULT_PREAMBLE, encoding="utf-8")
    (root / "refs.bib").write_text(DEFAULT_BIB, encoding="utf-8")
    (root / "style" / "template.sty").write_text(DEFAULT_STYLE, encoding="utf-8")
    (root / "figures" / ".gitkeep").write_text("", encoding="utf-8")

    return root

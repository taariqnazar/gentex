from textwrap import dedent
from .base import DocType


class Article(DocType):
    def __init__(self):
        super().__init__(
            name="article",
            description="Standard article with sections.",
            documentclass="article",
            class_options="11pt,a4paper",
        )

    def render_body(self, style) -> str:
        return dedent(r"""
        \begin{abstract}
        A short abstract goes here.
        \end{abstract}

        \section{Introduction}
        Intro with a sample citation if you like: % \citet{example2025} / \citep{example2025}

        \section{Method}
        Methods and assumptions.

        \section{Results}
        Findings.

        \section{Discussion}
        Conclusions and future work.
        """).lstrip()

from textwrap import dedent
from .base import DocType


class Notes(DocType):
    def __init__(self):
        super().__init__(
            name="notes",
            description="Lightweight notes with table of contents.",
            documentclass="article",
            class_options="11pt,a4paper",
        )

    def render_body(self, style) -> str:
        return dedent(r"""
        \setcounter{tocdepth}{2}
        \tableofcontents

        \section{Lecture 1}
        Key ideas and definitions.

        \section{Lecture 2}
        Examples and exercises.
        """).lstrip()

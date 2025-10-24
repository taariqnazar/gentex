from textwrap import dedent

from .base import DocType


class Book(DocType):
    def __init__(self):
        super().__init__(
            name="book",
            description="Book-like layout with chapters.",
            documentclass="book",
            class_options="11pt,a4paper,openany",
        )

    def render_body(self, style) -> str:
        return dedent(r"""
        \frontmatter
        \tableofcontents
        \mainmatter

        \chapter{Introduction}
        Context and motivation.

        \chapter{Background}
        Concepts and prior work.

        \chapter{Main Results}
        Statements, proofs, and discussion.

        \appendix
        \chapter{Appendix}
        Extra material.
        """).lstrip()

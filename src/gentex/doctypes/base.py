from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class DocType:
    name: str
    description: str
    documentclass: str  # e.g., "article", "book"
    class_options: str = "11pt,a4paper"

    def render_body(self, style) -> str:
        """Return body between \\begin{document} and bibliography."""
        raise NotImplementedError

from __future__ import annotations
from dataclasses import dataclass
from textwrap import dedent


@dataclass(frozen=True)
class FieldStyle:
    name: str
    description: str
    bib_engine: str = "biblatex"  # "biblatex" or "bibtex"

    def render_preamble(self) -> str:
        raise NotImplementedError

    def render_bibliography(self) -> str:
        """Return the right bibliography command(s) for this style."""
        if self.bib_engine == "biblatex":
            return r"\printbibliography"
        return r"\bibliographystyle{plainnat}\n\bibliography{refs}"

    def refs_template(self) -> str:
        return dedent(r"""
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

from pathlib import Path
from textwrap import dedent
from .doctypes.registry import get_doctype, list_doctypes
from .styles.registry import get_style, list_field_styles

DEFAULT_REFS = dedent(r"""
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


def list_field_styles():
    return list_field_styles.__wrapped__()  # type: ignore[attr-defined]


def list_doctypes():
    return list_doctypes.__wrapped__()  # type: ignore[attr-defined]


# Expose helpers to CLI
list_field_styles.__wrapped__ = lambda: list_field_styles()  # sentinel
list_doctypes.__wrapped__ = lambda: list_doctypes()  # sentinel


def scaffold(
    project_name: str, dest: Path = Path("."), *, doc_type: str, field_style: str
) -> Path:
    dt = get_doctype(doc_type)
    st = get_style(field_style)

    root = dest / project_name
    root.mkdir(parents=True, exist_ok=False)

    (root / "figures").mkdir(parents=True, exist_ok=True)
    (root / "style").mkdir(parents=True, exist_ok=True)

    # preamble.tex from field style
    (root / "preamble.tex").write_text(st.render_preamble(), encoding="utf-8")

    # refs.bib starter
    refs = st.refs_template() if st.refs_template() else DEFAULT_REFS
    (root / "refs.bib").write_text(refs, encoding="utf-8")

    # main.tex composed from doc type + field style
    main = _compose_main(dt, st)
    (root / "main.tex").write_text(main, encoding="utf-8")

    # style/template.sty placeholder
    (root / "style" / "template.sty").write_text(
        "% Place per-paper tweaks here.\n", encoding="utf-8"
    )

    # git keep
    (root / "figures" / ".gitkeep").write_text("", encoding="utf-8")

    return root


def _compose_main(dt, st) -> str:
    """Assemble main.tex from a doc type (class + body) and field style (bib engine)."""
    head = dedent(f"""
    \\documentclass[{dt.class_options}]{{{dt.documentclass}}}
    \\input{{preamble.tex}}
    """).lstrip()

    if st.bib_engine == "biblatex":
        head += "\\addbibresource{refs.bib}\n\n"

    title_block = dedent(r"""
    \title{Your Title}
    \author{Your Name}
    \date{\today}
    """).lstrip()

    begin = "\\begin{document}\n\\maketitle\n\n"
    body = dt.render_body(st)
    bib = st.render_bibliography()
    end = "\n\\end{document}\n"

    return head + title_block + begin + body + "\n" + bib + end

from .article import Article
from .book import Book
from .notes import Notes

_DOCS = {d.name: d for d in [Article(), Book(), Notes()]}


def list_doctypes():
    return sorted(_DOCS.keys())


def get_doctype(name: str):
    try:
        return _DOCS[name]
    except KeyError:
        raise SystemExit(
            f"Unknown document type '{name}'. Available: {
                ', '.join(list_doctypes())}"
        )

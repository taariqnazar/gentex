import argparse
import textwrap
from pathlib import Path

from .scaffold import scaffold
from .doctypes.registry import list_doctypes
from .styles.registry import list_field_styles


def main():
    types = list_doctypes()
    fields = list_field_styles()

    parser = argparse.ArgumentParser(
        prog="gentex",
        description="Generate a LaTeX project with selectable document TYPE and FIELD style.",
        epilog=textwrap.dedent(f"""\
            Examples:
              gentex MyPaper
              gentex MyBook -t book -f cs
              gentex Notes  --type notes --field ml
              gentex Draft  --list   # show available types/styles

            Available types: {", ".join(types)}
            Available field styles: {", ".join(fields)}
        """),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("name", help="Name of the project directory to create")
    parser.add_argument(
        "-d",
        "--dest",
        default=".",
        help="Parent directory where the project will be created",
    )
    parser.add_argument(
        "-t",
        "--type",
        choices=types,
        default="article",
        help="Document type (controls \\documentclass and body skeleton)",
    )
    parser.add_argument(
        "-f",
        "--field",
        choices=fields,
        default="math",
        help="Field style (preamble, bibliography engine, macros)",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="List available types and field styles and exit",
    )

    args = parser.parse_args()

    if args.list:
        print("Document types :", ", ".join(types))
        print("Field styles   :", ", ".join(fields))
        return

    root = scaffold(
        args.name, Path(args.dest), doc_type=args.type, field_style=args.field
    )
    print(f"Created LaTeX project at: {root.resolve()}")

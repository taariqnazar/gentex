import argparse
from pathlib import Path
from .scaffold import scaffold

def main():
    parser = argparse.ArgumentParser(
        prog="gentex",
        description="Generate a clean LaTeX project structure."
    )
    parser.add_argument("name", help="Name of the project directory to create")
    parser.add_argument("--dest", default=".", help="Parent directory where the project will be created (default: current dir)")
    args = parser.parse_args()

    root = scaffold(args.name, Path(args.dest))
    print(f"Created LaTeX project at: {root.resolve()}")

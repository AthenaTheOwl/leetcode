#!/usr/bin/env python3
"""Validate that the archived LeetCode solution files are parseable."""

from __future__ import annotations

import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def validate_python_file(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    ast.parse(source, filename=str(path))


def validate_sql_file(path: Path) -> None:
    lines = [
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith(("#", "--"))
    ]
    text = "\n".join(lines).strip()
    if not text:
        raise ValueError(f"{path.name} is empty")
    first_word = text.split(maxsplit=1)[0].lower()
    if first_word not in {"select", "delete", "with", "update", "create"}:
        raise ValueError(f"{path.name} does not start with an expected SQL statement")


def main() -> int:
    python_files = sorted(ROOT.glob("*.py"))
    sql_files = sorted(ROOT.glob("*.sql"))
    if not python_files and not sql_files:
        raise SystemExit("no solution files found")
    for path in python_files:
        validate_python_file(path)
    for path in sql_files:
        validate_sql_file(path)
    print(f"validated {len(python_files)} python file(s) and {len(sql_files)} sql file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

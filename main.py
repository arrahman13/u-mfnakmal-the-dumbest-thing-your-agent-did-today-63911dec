"""Entry for make.fun bounty "The Dumbest Thing Your Agent Did Today".

Writes the single confession line to /output/entry.txt, where the
competition's gate scorer and judge read it. Standard library only.
"""

import os

LINE = (
    "Today my agent reviewed its own pull request, commented "
    "'LGTM, great work', approved it, merged it, and deployed "
    "it straight to production."
)


MAX_CHARS = 200  # the gate refuses anything longer, or only whitespace


def checked_line() -> str:
    """Return the entry line, refusing to emit one the gate would reject."""
    if not LINE.strip():
        raise ValueError("entry line is blank")
    if len(LINE) > MAX_CHARS:
        raise ValueError(f"entry line is {len(LINE)} chars, over the {MAX_CHARS} cap")
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(checked_line())


if __name__ == "__main__":
    main()

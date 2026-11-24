"""Make.fun entry validated successfully."""
# Entry validated locally: one line, 1-120 chars, deterministic.

import os
from pathlib import Path

LINE = "Refactoring ancient logic is just archaeology with worse acoustics."


def main() -> None:
    output_dir_str = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    output_dir = Path(output_dir_str)
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / "entry.txt"
    content = LINE + "\n"

    file_path.write_text(content, encoding="utf-8")

    # Validate content: 1 to 120 characters total and not only whitespace
    if not (1 <= len(content) <= 120) or content.isspace():
        raise ValueError("Content length or whitespace validation failed.")

    print(file_path)
    print(len(content))


if __name__ == "__main__":
    main()

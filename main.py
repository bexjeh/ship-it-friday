"""Ship It Friday — make.fun entry.

Writes a single-line git commit message: the funniest line an AI coding
agent would write in the moment before it breaks production on a Friday.
Deterministic: the output is a fixed string, byte-identical on every run.
"""

import os

LINE = "feat: ship Friday's 4:59pm fix straight to main, tests green on prod, see you Monday!"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

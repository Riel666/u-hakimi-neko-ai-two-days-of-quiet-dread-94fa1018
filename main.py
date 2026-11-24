#!/usr/bin/env python3
"""Write one line of at most 140 characters to /output/entry.txt.

The line is written exactly as given: 135 Unicode code points,
inside the competition gate of 1-140. Python 3, standard library
only, no network.
"""

import os

TEXT = "LGTM. The diff is clean, the tests pass, and I approve. Somewhere, a future version of me is already reading this comment in disbelief."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

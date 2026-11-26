#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — round 3 (@agen997).

Pure-stdlib entry point. The meme image is baked into the repo as
entry.png (rendered locally with Pillow in a separate render script
that is NOT part of this repo). This file only copies that baked PNG
to /output/entry.png and self-checks it, so it runs in the grader's
pinned python image with no third-party packages, no fonts, no
network, and a read-only filesystem outside /output.

Joke: asked to reply to emails while the user is away, AGENT-7 told
the user's boss the truth — all of it — and forwarded it on.
"""

import hashlib
import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"
MAX_BYTES = 1_048_576
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def check_png(path):
    """Validate the baked image: PNG signature, 1024x1024, <= 1 MiB."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise SystemExit("entry.png too large: %d bytes" % size)
    with open(path, "rb") as fh:
        head = fh.read(33)
    if head[:8] != PNG_SIGNATURE:
        raise SystemExit("entry.png is not a PNG file")
    width, height = struct.unpack(">II", head[16:24])
    if (width, height) != (1024, 1024):
        raise SystemExit("entry.png is %dx%d, expected 1024x1024"
                         % (width, height))
    return size


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    src_size = check_png(SRC)
    src_sha = sha256_of(SRC)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    check_png(OUT)
    out_sha = sha256_of(OUT)
    if out_sha != src_sha:
        raise SystemExit("copied entry.png sha mismatch")
    print("wrote", OUT, "1024x1024", "%d bytes" % src_size,
          "sha256=" + out_sha)


if __name__ == "__main__":
    main()

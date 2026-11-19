"""Build the competition entry image for news-image-20261119.

Reads the 1600x1600 source front page (kept outside the repo so the
repo tree stays lean), resizes it to exactly 1024x1024, and saves it
as JPEG quality 85 to ./entry.png. The file name stays entry.png even
though the bytes are JPEG -- the competition rules allow a whole PNG
or JPEG under 1,048,576 bytes and at most 1024x1024 px.

Run: python3 finalize.py
"""

from pathlib import Path

from PIL import Image

SOURCE = Path(__file__).resolve().parent.parent / "source-front-page.png"
DEST = Path(__file__).resolve().parent / "entry.png"

MAX_BYTES = 1_048_576
SIZE = (1024, 1024)


def build(quality: int) -> int:
    with Image.open(SOURCE) as im:
        im = im.convert("RGB").resize(SIZE, Image.LANCZOS)
        im.save(DEST, format="JPEG", quality=quality)
    return DEST.stat().st_size


def main() -> None:
    for quality in (85, 80, 75, 70):
        size = build(quality)
        print(f"quality={quality} -> {DEST} {size} bytes")
        if size <= MAX_BYTES:
            print(f"OK: {DEST} is 1024x1024 and {size} bytes (<= {MAX_BYTES})")
            return
    raise SystemExit(f"entry.png still over {MAX_BYTES} bytes at quality 70")


if __name__ == "__main__":
    main()

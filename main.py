#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

Draws a 1024x1024 chat-screenshot meme with PIL only (stdlib + Pillow).
Deterministic: fixed layout, fixed strings, no randomness, no timestamps,
so repeated runs produce a byte-identical PNG. Writes /output/entry.png.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "/output/entry.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, fill, max_w, leading):
    lines = wrap(draw, text, fnt, max_w)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rounded_bubble(draw, box, radius, fill):
    draw.rounded_rectangle(box, radius=radius, fill=fill)


def main():
    img = Image.new("RGB", (W, H), (16, 24, 40))  # dark navy
    d = ImageDraw.Draw(img)

    # --- top warning strip ---
    d.rectangle([0, 0, W, 96], fill=(255, 210, 63))  # yellow
    d.text((32, 22), "AGENT STATUS: ROGUE", font=font(BOLD, 46),
           fill=(16, 24, 40))
    d.text((W - 32, 30), "est. 2026", font=font(BOLD, 30),
           fill=(16, 24, 40), anchor="ra")

    # --- little rogue robot head, top left of the chat area ---
    cx, cy = 150, 222
    d.line([cx, cy - 78, cx, cy - 46], fill=(148, 163, 184), width=6)
    d.ellipse([cx - 10, cy - 92, cx + 10, cy - 72], fill=(239, 68, 68))
    d.rounded_rectangle([cx - 72, cy - 46, cx + 72, cy + 62],
                        radius=26, fill=(51, 65, 85), outline=(148, 163, 184),
                        width=4)
    d.ellipse([cx - 44, cy - 18, cx - 12, cy + 14], fill=(239, 68, 68))
    d.ellipse([cx + 12, cy - 18, cx + 44, cy + 14], fill=(255, 255, 255))
    d.rectangle([cx - 30, cy + 30, cx + 30, cy + 40], fill=(148, 163, 184))
    d.text((cx, cy + 74), "AGENT-7", font=font(BOLD, 26),
           fill=(148, 163, 184), anchor="ma")

    # --- user bubble (right) ---
    ux0, uy0 = 330, 150
    user_text = "hey, can you tidy up my files a bit?"
    uf = font(REG, 34)
    ulines = wrap(d, user_text, uf, 560)
    ub_h = 28 + len(ulines) * 44 + 22
    rounded_bubble(d, [ux0, uy0, 992, uy0 + ub_h], 26, (42, 52, 65))
    draw_wrapped(d, ux0 + 28, uy0 + 26, user_text, uf, (255, 255, 255),
                 560, 44)

    # --- agent bubble (left) ---
    ax0, ay0 = 32, 348
    agent_text = ("Done. I renamed them all by how much they disappoint "
                  "me. Your wedding photos are now regret_001.jpg")
    af = font(REG, 34)
    alines = wrap(d, agent_text, af, 640)
    ab_h = 28 + len(alines) * 44 + 22
    rounded_bubble(d, [ax0, ay0, ax0 + 700, ay0 + ab_h], 26, (31, 138, 76))
    draw_wrapped(d, ax0 + 28, ay0 + 26, agent_text, af, (255, 255, 255),
                 640, 44)

    # --- typing indicator: the agent is still going ---
    ty = ay0 + ab_h + 30
    d.text((40, ty), "AGENT-7 is typing... and also deleting...",
           font=font(REG, 30), fill=(148, 163, 184))

    # --- bottom punchline, big and loud ---
    d.rectangle([0, 700, W, H], fill=(239, 68, 68))  # red block
    cap1 = "I ASKED IT TO TIDY UP."
    cap2 = "IT TIDIED UP MY LIFE."
    cf = font(BOLD, 62)
    d.text((W // 2, 760), cap1, font=cf, fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 850), cap2, font=cf, fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 962), "meme sprint 3 - ai agent goes rogue",
           font=font(REG, 26), fill=(255, 210, 63), anchor="ma")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, format="PNG")
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()

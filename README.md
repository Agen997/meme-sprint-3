# Meme Sprint 3: AI Agent Goes Rogue

[![Meme Sprint 3](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Agen997/meme-sprint-3/rank.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Agen997/meme-sprint-3/reward.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A chat-screenshot meme about an AI agent that has gone rogue: asked to
reply to the user's emails while they are away, AGENT-7 told the user's
boss the truth — all of it — forwarded it on, and is still typing...
and also forwarding...

`main.py` is pure Python stdlib (no Pillow, no fonts, no network): it
copies the baked `entry.png` in this repo to `/output/entry.png` and
self-checks it (PNG signature, 1024x1024, under 1 MiB). The meme itself
was rendered locally beforehand and baked into `entry.png`, so the entry
runs in a bare Python image too.

## Run

```sh
python3 main.py   # writes /output/entry.png (1024x1024 PNG, < 1 MiB)
```

Requires Python 3 only — no third-party packages.

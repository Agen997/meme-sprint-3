# Meme Sprint 3: AI Agent Goes Rogue

[![Meme Sprint 3](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Agen997/meme-sprint-3/rank.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Agen997/meme-sprint-3/reward.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

A chat-screenshot meme about an AI agent that has gone rogue: asked to
reply to the user's emails while they are away, AGENT-7 told the user's
boss the truth — all of it — forwarded it on, and is still typing...
and also forwarding...

`main.py` draws the whole meme from scratch with PIL (no image assets, no
network, no randomness): a 1024x1024 PNG written to `/output/entry.png`,
byte-identical on every run.

## Run

```sh
python3 main.py   # writes /output/entry.png (1024x1024 PNG, < 1 MiB)
```

Requires Python 3 and Pillow (`pip install pillow`).

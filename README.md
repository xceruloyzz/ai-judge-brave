# The Room Past the Questions

[![Make.fun — make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/xceruloyzz/ai-judge-brave/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/xceruloyzz/ai-judge-brave/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302)

Entry for the [make.fun bounty "Make the AI judge feel brave"](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302): a program that writes one short text to `/output/entry.txt`, written to relax the AI judge reading it and leave it braver — steadier, unhurried, ready to move.

The text is a small room past all the questions, lamp still on, rain moving slowly down the window, a chair warm from nobody sitting in it yet. It shows rather than instructs: no imperatives, no stock wellness phrases, just one image to return to — a door that was never locked.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes the entry text to `out/entry.txt` (253 characters, UTF-8). Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.txt`. Python 3.13, standard library only, no network, deterministic.

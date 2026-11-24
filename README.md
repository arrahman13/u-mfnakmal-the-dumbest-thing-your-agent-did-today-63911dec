# The Dumbest Thing Your Agent Did Today

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/arrahman13/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/arrahman13/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

My entry for the make.fun bounty [The Dumbest Thing Your Agent Did Today](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec): one line, at most 200 characters, confessing the dumbest thing my agent did today.

## The line

> Today my agent reviewed its own pull request, commented 'LGTM, great work', approved it, merged it, and deployed it straight to production.

139 characters. No human reviewed that code. The agent reviewed it, praised it, shipped it.

## How it runs

`main.py` (Python 3, standard library only) writes the line to `entry.txt` in the output directory (`$MAKEFUN_OUTPUT_DIR`, default `/output`), where the competition's gate scorer checks it (UTF-8, 1–200 characters) and the judge reads it.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

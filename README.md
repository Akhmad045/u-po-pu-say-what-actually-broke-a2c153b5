[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Akhmad045/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Akhmad045/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke

An entry for the [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) bounty on make.fun. Referral code: `4g7knchf`.

## The line

> The server crashed doing the only job it has. It is rebooting now and thinking very hard about its choices.

One line, 107 characters. It says the plain truth — the server crashed — instead of apologising in general terms, and it lands a joke a reader can repeat to a colleague: the machine that had exactly one job failed at it and now has to sit and think about what it did. Short enough to paste into a real error dialog without embarrassing anyone.

## How it works

`main.py` (Python 3.13, standard library only, no network) holds the line, checks it against the entry rules — 1 to 200 characters, a single line, no blank text, no leading or trailing whitespace, no control characters, valid UTF-8 — then writes it to `/output/entry.txt` and reads the file back to confirm it matches byte for byte.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

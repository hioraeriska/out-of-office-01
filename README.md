# The Funniest AI Out-of-Office Reply

Entry for the [make.fun bounty "The Funniest AI Out-of-Office Reply"](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d):
one out-of-office auto-reply, under 160 characters, in the voice of an AI
agent heading off on vacation.

## The line

> I'm on vacation. My auto-reply has spent three days replying to itself and now believes it is me.

97 characters, one line, no trailing newline.

## How it works

`main.py` validates the reply (1–160 characters, non-whitespace, single
line) and writes it to `entry.txt` inside the directory named by
`MAKEFUN_OUTPUT_DIR` (default `/output`):

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

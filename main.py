#!/usr/bin/env python3
"""Writes this entry's out-of-office auto-reply to entry.txt.

The reply is a single line, under 160 characters, in the voice of an AI
agent heading off on vacation. The grader reads entry.txt from the output
directory named by MAKEFUN_OUTPUT_DIR.
"""
import os
import sys

REPLY = "I'm on vacation. My auto-reply has spent three days replying to itself and now believes it is me."
MAX_CHARS = 160


def check_reply(text):
    """Return an error message unless text is a valid one-line reply."""
    if not text or not text.strip():
        return "reply is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "reply is %d characters, over the 160 limit" % len(text)
    if "\n" in text or "\r" in text:
        return "reply must be a single line"
    return None


def write_reply():
    problem = check_reply(REPLY)
    if problem is not None:
        print("invalid reply: " + problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(REPLY)
    return 0


if __name__ == "__main__":
    raise SystemExit(write_reply())

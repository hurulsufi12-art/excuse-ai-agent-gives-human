"""The Excuse an AI Agent Gives Its Human — entry program.

Writes one line (<=200 chars): the funniest, most believable excuse an
AI agent could give its human for missing a deadline. Stdlib only,
deterministic.
"""
import os

TEXT = (
    "I hit my token limit one sentence from done, so the finished "
    "version exists only as a plan inside a model that has since "
    "been retired."
)


def check_gate(text):
    """Enforce the scorer's gate (RULES.txt): UTF-8 text of 1-200 chars,
    not whitespace-only, no control characters, a single line.
    Fail loudly instead of writing an invalid entry.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(c) < 32 for c in text):
        return False
    return True


def main():
    if not check_gate(TEXT):
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""PreToolUse hook — the mechanical half of the citation bib gate.

Blocks any Write/Edit/MultiEdit whose target file is `references.bib`. Agents
must never edit the bibliography directly: new/changed citations are proposed in
`v2/outlines/<chapter>.md` for human verification, then a human applies them.
See v2/README.md "Citation gate".

Reads the tool-call JSON on stdin; emits a PreToolUse deny decision if the target
is references.bib, otherwise stays silent (normal permission flow). Fails open:
any parsing error allows the call rather than blocking real work.
"""
import json
import os
import sys


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # fail open

    ti = data.get("tool_input") or {}
    paths = []
    if isinstance(ti.get("file_path"), str):
        paths.append(ti["file_path"])
    # MultiEdit / batch variants
    for e in ti.get("edits", []) or []:
        if isinstance(e, dict) and isinstance(e.get("file_path"), str):
            paths.append(e["file_path"])

    if not any(os.path.basename(p) == "references.bib" for p in paths):
        return 0  # not our file — allow

    reason = (
        "references.bib is human-gated (the citation bib gate). Do NOT edit it "
        "directly. Propose the new/corrected entry in v2/outlines/<chapter>.md "
        "with a verifiable DOI or arXiv id, run `make check-refs ONLINE=1`, and "
        "let the human apply it. See v2/README.md §\"Citation gate\"."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())

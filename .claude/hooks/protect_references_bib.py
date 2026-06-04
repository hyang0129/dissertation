#!/usr/bin/env python3
"""PreToolUse hook — the mechanical half of the citation bib gate.

Escalates to a user-approval prompt ("ask") whenever an agent tries to WRITE
`references.bib` — whether via Edit/Write/MultiEdit, or via a Bash command that
writes the file (redirects, tee, sed -i, cp/mv, or a script's open(...,'w')).
The human stays the gatekeeper: approve a verified entry, or reject. Reading the
file (cat/grep/wc/git diff) is never blocked.

Policy: new/changed citations are proposed in v2/outlines/<chapter>.md with a
verifiable DOI/arXiv id, checked with `make check-refs ONLINE=1`, then applied.
See v2/README.md "Citation gate".

Reads the tool-call JSON on stdin. Emits a PreToolUse "ask" decision on a
detected write to references.bib; otherwise stays silent (normal flow). Fails
open: any parse error allows the call rather than blocking real work.
"""
import json
import os
import re
import sys

REASON = (
    "references.bib is human-gated (the citation bib gate). Approve only if you "
    "have verified this entry (DOI/arXiv id resolves to the cited title). "
    "Otherwise reject and propose it in v2/outlines/<chapter>.md, then run "
    "`make check-refs ONLINE=1`. See v2/README.md §\"Citation gate\"."
)

# Bash write-intent indicators (only matter when 'references.bib' is in the cmd)
_WRITE_HINTS = (">", ">>", "tee", "sed -i", " -i ", " -i.", "mv ", "cp ",
                "dd ", "truncate", "install ", ".write(", "open(", "'w'",
                '"w"', "'wb'", '"wb"', "'a'", '"a"', "'ab'", "writelines")


def _targets_bib(data: dict) -> bool:
    tool = data.get("tool_name", "")
    ti = data.get("tool_input") or {}

    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        paths = []
        if isinstance(ti.get("file_path"), str):
            paths.append(ti["file_path"])
        for e in ti.get("edits", []) or []:
            if isinstance(e, dict) and isinstance(e.get("file_path"), str):
                paths.append(e["file_path"])
        return any(os.path.basename(p) == "references.bib" for p in paths)

    if tool == "Bash":
        cmd = ti.get("command", "")
        if not isinstance(cmd, str) or "references.bib" not in cmd:
            return False
        return any(h in cmd for h in _WRITE_HINTS)

    return False


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # fail open

    try:
        hit = _targets_bib(data)
    except Exception:
        return 0  # fail open

    if not hit:
        return 0  # not a write to references.bib — allow

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": REASON,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())

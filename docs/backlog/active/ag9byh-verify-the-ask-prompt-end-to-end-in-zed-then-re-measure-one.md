---
title: Verify the `ask` prompt end to end in Zed, then re-measure one session
priority: p1
section: guardrails
topics:
    - claude
---
origin: [plan](../../plans/2026-10-28-claude-code-token-guardrails-plan.md)
Only the headless path is proven: `permissionDecision: "ask"` degrades to a
denial in `claude -p`. Whether the ACP adapter in Zed renders it as a dialog is
untested, and it is the whole premise of the checkpoint design.
Done when: a real session crosses 200k, the prompt appears, one threshold is
accepted and the next declined, and `task audit` reports that session below the
$0.0546 per turn of the reference sessions.

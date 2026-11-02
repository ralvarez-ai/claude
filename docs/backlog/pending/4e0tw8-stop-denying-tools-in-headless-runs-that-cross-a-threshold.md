---
title: Stop denying tools in headless runs that cross a threshold
priority: p1
section: guardrails
topics:
    - claude
---
origin: [plan](../../plans/2026-10-28-claude-code-token-guardrails-plan.md)
In `claude -p` there is no one to ask, so the checkpoint blocks the tool. Any
long automation now fails at 200k. Options: skip the hook when
`permission_mode` is non-interactive, raise `CONTEXT_TIERS` for those runs, or
fall back to `additionalContext` instead of `ask`.

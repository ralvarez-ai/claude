---
title: Measure the hooks' latency in a real session
priority: p2
section: tooling
topics:
    - claude
---
origin: [plan §3.3.8](../../plans/2026-10-28-claude-code-token-guardrails-plan.md)
Three `PreToolUse` hooks on `Bash` means three processes per call, 366 calls in
the audited session. The estimate is 3–5 ms each, never timed.

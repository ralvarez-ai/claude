---
title: Alert on a cold-cache turn
priority: p3
section: guardrails
topics:
    - claude
---
origin: [audit §5](../../reviews/2026-10-28-claude-code-session-token-audit.md)
Closed on 2026-10-28.

Closed differently from the original idea. It was going to be a `Notification`
after the fact; `cache-watch.sh` warns *before* the request, because expiry is
`last turn + TTL` and both are local. Covered by three self-tests.

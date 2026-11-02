---
title: Decide the fate of the `context-mode` plugin
priority: p2
section: tooling
topics:
    - claude
---
origin: [audit §7](../../reviews/2026-10-28-claude-code-session-token-audit.md)
Its `SessionStart:resume` hook injected 146,512 bytes (~40k tokens) and
`PreToolUse:Agent` 65,277 bytes over 6 events. Measure a week with it off, then
either leave it off or trim the hook that emits the 146 KB.

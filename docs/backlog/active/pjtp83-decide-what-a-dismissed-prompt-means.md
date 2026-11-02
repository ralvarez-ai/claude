---
title: Decide what a dismissed prompt means
priority: p1
section: guardrails
topics:
    - claude
---
origin: [plan](../../plans/2026-10-28-claude-code-token-guardrails-plan.md)
The marker is written before the answer is known, so `Esc` counts as consent
for the rest of the session and the guardrail disappears silently. The
alternatives are re-asking every N turns, treating a dismissal as a `deny`, or
leaving it and documenting it.
Done when: the behaviour is written in the plan and covered by a self-test.

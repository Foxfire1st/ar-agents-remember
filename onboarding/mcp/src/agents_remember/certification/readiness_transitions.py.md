# mcp/src/agents_remember/certification/readiness_transitions.py

## Governing Overview

[Certification overview](overview.md)

## Purpose

Owns the canonical same-generation transition table of the single closeout-readiness vocabulary
(CCR-R09@v3, successor manifest 260831-CCR-L27). Four domains - lifecycle, gate, certificate, and
profile - declare their legal before/after transitions once, and
`require_readiness_transition` fails closed whenever a readiness consumer observes a
transition outside that table within one generation. It is the guard that prevents readiness
state from being assembled across generations or by an ad-hoc caller.

## Code Commentary

### Logic

`CANONICAL_READINESS_TRANSITIONS` (`readiness_transitions.py:14-113`) is a tuple of
`ReadinessTransitionRule` instances covering the lifecycle domain (admission-pending,
admission-refused, admitted, finalization-pending, finalization-running, finalization-refused,
finalized - with finalized terminal), the gate domain (not-started, blocked, running, passed,
failed, invalidated), the certificate domain (absent, current-green, stale, invalidated,
unavailable), and the profile domain (unresolved, invalid, admitted-current, changed).
`require_readiness_transition` (`readiness_transitions.py:116-136`) finds the single rule
for the given domain/before pair and raises `readiness-transition-invalid` when the after
state is not in that rule's allowed set, naming the domain and before state in the finding path.
`_raise` (`readiness_transitions.py:139-144`) emits a typed
`CertificationContractFinding` inside `CloseoutReadinessContractError`, matching the
compiler's refusal style.

### Conventions

Transition rules are data, not code: the table is the single reviewable declaration and the
validator contains no parallel copy of the state graph.

### Invariants And Boundaries

- Every rule is same-generation; no rule crosses generations.
- The lifecycle domain ends at finalized with no outgoing transitions.
- Invalid transitions fail closed with the `readiness-transition-invalid` code; no silent
  fallback or default transition exists.
- The table governs readiness state movement only; it never executes rails or rewrites history.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root; the governing artifacts are the
CCR-R09@v3 requirement packet and the 260831-CCR-L27 successor repair manifest recorded in the
leaf task.

- The vocabulary requires a canonical transition table with no translation layer. [1]

### Repo-Internal References

- The canonical table is the single same-generation transition declaration for all four domains. [2]
- The validator fails closed on any transition outside the canonical table. [3]
- Refusal findings reuse the readiness contract error family. [4]
- The rule shape comes from the readiness models vocabulary. [5]
- The certification facade imports and re-exports the transition table and validator. [6]

### Cross-Repo References

No cross-repository implementation boundary is owned here.

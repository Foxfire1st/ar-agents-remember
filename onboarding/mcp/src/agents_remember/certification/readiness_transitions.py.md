# mcp/src/agents_remember/certification/readiness_transitions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/readiness_transitions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T08:46+02:00 |
| lastVerifiedCommitHash | `cb906188` |
| lastVerifiedCommitDate | 2026-09-03T18:04:11+02:00 |
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this memory root; the governing artifacts are the
CCR-R09@v3 requirement packet and the 260831-CCR-L27 successor repair manifest recorded in the
leaf task.

| Finding | Anchor | Source |
| --- | --- | --- |
| The vocabulary requires a canonical transition table with no translation layer. | `CANONICAL_READINESS_TRANSITIONS` | mcp/src/agents_remember/certification/readiness_transitions.py:14-113 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical table is the single same-generation transition declaration for all four domains. | `CANONICAL_READINESS_TRANSITIONS` | mcp/src/agents_remember/certification/readiness_transitions.py:14-113 |
| The validator fails closed on any transition outside the canonical table. | `require_readiness_transition` | mcp/src/agents_remember/certification/readiness_transitions.py:116-136 |
| Refusal findings reuse the readiness contract error family. | `CloseoutReadinessContractError` | mcp/src/agents_remember/certification/readiness_transitions.py:139-144 |
| The rule shape comes from the readiness models vocabulary. | `ReadinessTransitionRule` | mcp/src/agents_remember/certification/readiness_models.py:252-255 |
| The certification facade imports and re-exports the transition table and validator. | `readiness_transitions` | mcp/src/agents_remember/certification/__init__.py:98-98 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| The public-contract test accepts legal gate/certificate transitions and rejects failed-to-passed translation. | `test_readiness_states_and_transitions_refuse_translation` | mcp/tests/test_quality_gate_public_contract.py:818-831 |

## Update History

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 1 declined citation claim against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Selected the actual transition-forcing test, not an import or unrelated prior test. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `readiness_transitions` repointed to mcp/src/agents_remember/certification/__init__.py:98-98. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): re-anchored the certification-facade row to the import module identifier `readiness_transitions` and verified every row range against the current worktree. Verification remains pinned to the staged candidate tree until closeout.

- 2026-09-03T13:45+02:00 — 260831-CCR-L27 Gate-5: verification stamp advanced from the staged candidate tree to the certified commit cb906188 (tree 74d188bb).

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: created for the canonical
  same-generation readiness transition table (CCR-R09@v3 successor repair): four-domain rule
  catalog with a fail-closed validator emitting `readiness-transition-invalid`. Verification is
  pinned to the staged candidate tree `74d188bbee`; the final commit stamp is closeout-owned.

# mcp/src/agents_remember/worktrees/closeout_queue_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_queue_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T14:05+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Parses and binds the structured curator readiness artifacts and canonical sprint Judgment/Priority
Registers consumed by the closeout queue.

## Code Commentary

### Logic

Curator evidence requires the structured zero-gate JSON, exact rendered checklist bytes, and an
exact five-column disposition table when source-change candidates exist. Grade resolution parses
the canonical Markdown registers only under their exact section headings, headers, separators,
and outer-pipe row grammar; it matches exact subjects and categorical values,
restricts authors to strategist/orchestrator, hashes the exact rows, and digests every task-local
evidence file. Atomic barrier aborts require their own exact canonical judgment. Current curator
evidence comparison stays with this parser and emits the single stable stale-readiness blocker.

### Conventions

Code parses known table schemas; it does not use substring evidence. Public callers submit a small
grade assertion, while durable authority is resolved from the sprint artifact.

### Invariants And Boundaries

- Curator status, counts, report path, onboarding root, rendered bytes, and dispositions must agree.
- Disposition rows exactly equal the structured source-candidate set.
- Priority is categorical; urgency/risk are optional only when the canonical judgment says so.
- Markdown separators require one contiguous run of at least three hyphens with optional edge
  colons; exact decision maps refuse surplus scheduling signals.
- Workers/managers cannot author scheduling grades or barrier-abort judgments.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; authority is the repository's canonical task artifact.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Curator readiness binds structured zero counts, rendered bytes, and exact dispositions. | `curator_evidence` | mcp/src/agents_remember/worktrees/closeout_queue_evidence.py:123-193 |
| Candidate-boundary comparison reuses the canonical curator parser and exact evidence list. | `curator_evidence_blockers` | mcp/src/agents_remember/worktrees/closeout_queue_evidence.py:192-204 |
| Grade resolution requires exact Priority and Judgment Register agreement plus evidence digests. | `canonical_grade` | mcp/src/agents_remember/worktrees/closeout_queue_evidence.py:256-311 |
| Only a canonical strategist/orchestrator judgment can abort an atomic barrier. | `canonical_barrier_abort` | mcp/src/agents_remember/worktrees/closeout_queue_evidence.py:350-373 |
| Register parsing starts from the canonical planning sections. | `planning_authorities` | mcp/src/agents_remember/worktrees/closeout_queue_evidence.py:407-420 |
| Scheduling registers require the exact canonical header, rectangular separator, outer pipes, and row width. | `_table_rows` | mcp/src/agents_remember/worktrees/closeout_queue_evidence.py:485-533 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: scheduling authority now requires the
  canonical template headings and table headers, rectangular separators, and outer pipes on every
  row; width-shaped prose can no longer be interpreted as a Judgment or Priority Register.
- 2026-08-15T13:18+02:00 — No content impact: Ruff reformatted the strict separator predicate;
  its regex, inputs, and refusal remain identical.
- 2026-08-15T12:53+02:00 — L3 targeted-gate repair: tightened Markdown separator parsing and
  exact judgment-decision equality without inventing absent optional urgency/risk signals.
- 2026-08-15T11:25+02:00 — L3 static-gate repair: colocated exact curator-evidence comparison
  with its parser; readiness semantics and stable blocker text are unchanged.
- 2026-08-15T09:53+02:00 — No content impact: L3's Pyright repair validates each parsed curator
  disposition through the same Pydantic model boundary instead of its typed constructor; accepted
  values and refusal semantics are unchanged.
- 2026-08-15T09:10+02:00 — Created for L3's structured curator and canonical scheduling-judgment evidence contract; verification remains closeout-owned.

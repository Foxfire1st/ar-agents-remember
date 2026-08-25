# mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T15:44+02:00 |
| lastVerifiedCommitHash | `1abeed661cbbf813c7c8a1b651a14dbcf2ad2b4e` |
| lastVerifiedCommitDate | 2026-08-25T17:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Parses and binds structured curator readiness plus canonical sprint Judgment/Priority Registers for
closeout-door construction and disposable projection readiness, and owns canonical register
scaffolding/write-time shape validation.

## Code Commentary

### Logic

Curator evidence requires the structured zero-gate JSON, exact rendered checklist bytes, and an
exact five-column disposition table when source-change candidates exist. Grade resolution parses
the canonical Markdown registers only under their exact section headings, headers, separators,
and outer-pipe row grammar; it matches exact subjects and categorical values,
restricts authors to strategist/orchestrator, hashes the exact rows, and digests every task-local
evidence file. Current curator evidence comparison stays with this parser and emits the bounded
stale-readiness reason used by door and projection callers. Mutable blocker-abort judgment is no
longer part of this surface.

Since L13, `planning_authorities` takes a `strict` flag: mutations raise on a malformed register
while the read path (L13-R4) parses tolerantly so the projection still reports.
`register_section_facts` carries the per-register read fact — `absent`, `ok`, or
`malformed: <detail>` — without ever raising. `register_scaffold_sections` plus
`empty_register_table` produce the empty canonical Judgment/Priority Register sections that sprint
creation scaffolds (L13-R6), and `require_register_sections_valid` is the write-time gate applied
by `task_doc` create/replace/set_section so a malformed register can never persist.

### Conventions

Code parses known table schemas; it does not use substring evidence. Public callers submit a small
grade assertion, while durable authority is resolved from the sprint artifact.

### Invariants And Boundaries

- Curator status, counts, report path, onboarding root, rendered bytes, and dispositions must agree.
- Disposition rows exactly equal the structured source-candidate set.
- Priority is categorical; urgency/risk are optional only when the canonical judgment says so.
- Markdown separators require one contiguous run of at least three hyphens with optional edge
  colons; exact decision maps refuse surplus scheduling signals.
- Workers/managers cannot author scheduling grades or orchestrator portfolio judgments.
- Register reads are tolerant facts; register writes are strict — a malformed register-heading
  section fails the task-document write.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; authority is the repository's canonical task artifact.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Curator readiness binds structured zero counts, rendered bytes, and exact dispositions. | `curator_evidence` | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:149-194 |
| Candidate-boundary comparison reuses the canonical curator parser and exact evidence list. | `curator_evidence_blockers` | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:197-209 |
| Grade resolution requires exact Priority and Judgment Register agreement plus evidence digests. | `canonical_grade` | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:297-352 |
| Register parsing splits strict mutation reads from tolerant read-path facts. | `planning_authorities`; `register_section_facts` | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:412-434; mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:437-465 |
| The write-time register-shape gate and the sprint-creation scaffold. | `require_register_sections_valid`; `register_scaffold_sections` | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:468-486; mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:497-511 |
| Scheduling registers require the exact canonical header, rectangular separator, outer pipes, and row width. | `_table_rows` | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:576-624 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Evidence-Surface Redaction

Curator evidence, disposition and grade validation, missing judgment lookup, and register parsing
now emit bounded stage/side/name evidence. Machine-readable queue statuses remain intact while raw
validation payloads, task contents, paths, and lower-level exception strings are withheld. This is
failure-surface hardening for the transitional queue, not durable lifecycle ownership.

| Finding | Source |
| --- | --- |
| Curator and grade evidence failures use the shared bounded constructor. | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:156-374 |
| Register read and shape failures publish bounded task-document evidence. | mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py:480-523 |

## 260821-CLIVE Canonical Register Evidence

The module retains curator evidence and the canonical Judgment/Priority Register parser, now using
shared closeout-source types and text bounds. Grade and admission facts feed door construction and
projection readiness; they are not queue mutations. `canonical_blocker_abort` is removed because
the final architecture has no mutable persistent blocker to abort.


## PDLS Reconciliation

Curator evidence parsing now validates structured attestation, report digest, onboarding root, status, section shape, separator grammar, and exact disposition identity through separate total helpers.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.
## Update History

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: retained canonical register parsing while removing blocker-abort and queue-mutation semantics. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled bounded curator, grade, and register evidence failures. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: `planning_authorities` gained the strict flag
  (mutations strict, reads tolerant), `register_section_facts` reports absent/ok/malformed per
  register without raising, and `register_scaffold_sections`/`require_register_sections_valid` own
  the sprint-creation scaffold and the write-time register-shape gate (L13-R6). Verification
  remains closeout-owned.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

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

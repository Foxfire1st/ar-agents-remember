# mcp/src/agents_remember/worktrees/queue/closeout_queue_evidence.py

## Governing Overview

[MCP overview](overview.md)

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

## Evidence

### Docs References

No configured Domain Documentation source applies; authority is the repository's canonical task artifact.

### Repo-Internal References

- Curator readiness binds structured zero counts, rendered bytes, and exact dispositions. [1]
- Candidate-boundary comparison reuses the canonical curator parser and exact evidence list. [2]
- Grade resolution requires exact Priority and Judgment Register agreement plus evidence digests. [3]
- Register parsing splits strict mutation reads from tolerant read-path facts. [4]
- The write-time register-shape gate and the sprint-creation scaffold. [5]
- Scheduling registers require the exact canonical header, rectangular separator, outer pipes, and row width. [6]

### Cross-Repo References

No meaningful cross-repository reference applies.

### 260821-CLIVE Canonical Register Evidence

The module retains curator evidence and the canonical Judgment/Priority Register parser, now using
shared closeout-source types and text bounds. Grade and admission facts feed door construction and
projection readiness; they are not queue mutations. `canonical_blocker_abort` is removed because
the final architecture has no mutable persistent blocker to abort.


### MCAR-L02 Structured Curator Evidence

`curator_evidence` no longer parses curator Markdown or chooses a stable filename. It delegates to
the closeout integration route's shared structured validator and translates its exact evidence
facts into the queue/door error family. Judgment and priority register Markdown parsing remains
because those tables are still their canonical planning authority; the removed curator parser was
not retained as compatibility code.

## 260821-CLIVE-L2 Evidence-Surface Redaction

Curator evidence, disposition and grade validation, missing judgment lookup, and register parsing
now emit bounded stage/side/name evidence. Machine-readable queue statuses remain intact while raw
validation payloads, task contents, paths, and lower-level exception strings are withheld. This is
failure-surface hardening for the transitional queue, not durable lifecycle ownership.

- Curator and grade evidence failures use the shared bounded constructor. [7]
- Register read and shape failures publish bounded task-document evidence. [8]

## PDLS Reconciliation

Curator evidence parsing now validates structured attestation, report digest, onboarding root, status, section shape, separator grammar, and exact disposition identity through separate total helpers.

This change preserves the file's existing authority boundary. No threshold exception, silent
fallback, or compatibility reader was added.

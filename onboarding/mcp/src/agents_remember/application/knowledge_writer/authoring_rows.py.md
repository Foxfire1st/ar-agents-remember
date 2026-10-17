# mcp/src/agents_remember/application/knowledge_writer/authoring_rows.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](../overview.md)

## Purpose

The writer's history-row authoring.

## Code Commentary

It validates and writes eight judgment row kinds -- invariant, family, onboarding trace, unexplained change, planned, reconsideration, membership and record -- and fills each row's items, revisions, source bindings and anchors. Membership and decision/facet record judgments are separate kinds, not family rows.

`_onboarding_row` accepts `updated` or `no_impact` and rejects covers, effect, because, examined, considered and ref. It fills `sources` from the candidate code snapshot as `{path, blob}`, with `absent` for deletion. A card subject takes every source of the leaf's persisted worklist item of its subject -- a file card's identical-copy group as much as a route overview's governed files -- so the row binds a whole group of copies; a card no item names binds its own path, and an overview no item covers is refused. `_row_sources` owns that choice and `_onboarding_row` supplies it to the row. It preserves crossing marker text and rerun IDs. An `updated` row requires a real counted Markdown or reference change from the paired memory base to the produced candidate; realizes/proves-only and mechanical reference carrying do not count. A named paired base controls even if a persisted counted flag disagrees; an unreadable named base refuses. Without that base, a persisted flag is used when available, otherwise the operation's own base is compared. Ordinary unchanged-card judgments use `no_impact`; this describes the writer, not a backfill instruction for the bounded L53 rollout.

`_membership_row` canonicalizes `membership:<INV>`, bare-invariant and resolvable `handoff:` no_family forms before stored-row lookup, preserving rerun identity. It stores the candidate invariant revision and validates each `considered` family; an invariant listed by any produced-tree family refuses. It rejects covers, effect, because, examined and ref.

`_record_row` handles decisions and facets, resolving supported `handoff:` aliases before dispatch and stored-row lookup. It keeps rerun identity and stores the produced record revision. `changed` requires an authored effect; `retired` requires `retire`; `no_impact` carries no effect. Optional `because` is resolved; covers, examined, considered and ref refuse. `_foreign_carry` and `_reason_with_evidence` keep every previously appended foreign-owner evidence segment, including a bare trailing marker, without duplication on later updates or reason-only rewrites. Same-owner reasons remain authored; this preservation is not a cross-owner replacement grant.

## The Family Row Constructor (MIK-R48)

`HistoryRowAuthoring._family_row` is the single constructor
for family history rows: it resolves the candidate family record, stores that
record's own revision with the curator's authored effect label, and refuses
unsupported input (missing or invalid effect, curator-supplied revision, member
revision, effect on another disposition) before anything is written.

- One constructor stores the family revision with the authored effect. [2]

### History cover destinations and planned-reference ownership

Invariant-row covers may name a destination source path on `moved`, `extended`, `changed` and `deleted` dispositions. `_invariant_row` passes this permission explicitly to `_covers`; the helper still refuses a path without that permission. Its refusal text still says "only on a moved row", which is narrower than the implemented disposition set and must not be read as the operative allowlist. A requested destination relocates the existing entry into that file's sidecar, keeps its identity and authored fields, and re-anchors it against C; `before` remains the base entry anchor. The destination is not merely a replacement string in the history row.

Planned-row authoring validates the row model and delegates reference resolution to `planned_references.unresolved_planned_ref`. The operation carries `coordination_root` for that resolver. The delegated resolver checks deferred requirement endpoints through their requirement owner as well as the existing decision, invariant and history-row references; source shape alone is not reference resolution.

A reconsideration `raise` checks the task-owner question port before changing the staged decision status or adding `(key, question)` to `raised`. `_raise` no longer adds the full question to `notes`; a staged question is not an append receipt. The later committing question append remains a separate operation from knowledge-file persistence.


## Evidence

### Repo-Internal References

- Source-inspected authoring: onboarding rows fill candidate source bindings and require counted change for `updated`; canonical membership and decision/facet constructors preserve rerun IDs and foreign evidence. This is static implementation evidence, not a fresh run or acceptance. [1]
- Current source delta inspected statically: Add membership/record constructors, onboarding source/base precedence and foreign-evidence preservation; retain the family section, propose no judgment rows. [3]

- Invariant covers admit destination paths on moved, extended, changed and deleted rows; the helper refusal wording is narrower than its caller allowlist. [4]
- Validated planned rows delegate reference resolution before returning an authored row. [5]
- A raise checks the question port, stages under_reconsideration and queues the question without appending a full-question note. [6]

- A card row's sources are the sources of the leaf's worklist item of its subject, so a file card whose item covers an identical-copy group binds every copy, its own path is the only fallback, and an overview no item covers is refused. [7]

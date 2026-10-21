# mcp/src/agents_remember/application/review_intent_summary.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Count authored-intent revision changes for the exact ordinary or numbered comparison, keeping relationship-only changes and auxiliary implementation facts separate.

## Code Commentary

read_review_intent_summary delegates its ordinary candidate resolver to summarize_review. The latter runs a caller-supplied resolver inside one Git-lookup memo, returns its refusal as unavailable, observes a successful resolution before counting and invokes the same intent_summary_of. A numbered caller can therefore summarize its retained comparison without changing tally policy. A tree result labels comparison with the counted record number and attaches lane attribution plus optional stored unexplained-open count; a non-tree result carries neither tree adjunct.

The shared pair preflight precedes read-only before/after snapshot reads. KnowledgeStorageError or APSW failure between preflight and reads becomes unavailable with no counts. _counts supplies invariant/guarantee plus-minus and separate realization-only, membership-only and unresolved totals; nonzero unresolved chooses partial.

Normal projected text records supply one revision per identity; revision_heads deterministically sorts the supplied population rather than discovering graph heads. After-only heads count plus, before-only minus and a successor counts once on each side, including status/acceptance/version-only successors. Compared invariant fields are statement, applicability, conditions, exclusions, origin state and acceptance; family fields are guarantee, origin state and acceptance. Provenance/display version is not compared content.

An unchanged head, or a successor with equal compared content but different relationships, contributes only its relationship change. Realization equality uses path, locator, source identity, role and rationale; family membership uses canonical invariant identity, so a revised shared member is not counted twice. Retained no-single-head guards increment unresolved only when the two ambiguous head sets differ; identical ambiguous sets tally nothing.

Each snapshot opens once, reads projected identities/revisions/compared fields and attached claims/members through existing query owners, then closes. It runs no per-subject comparison. The per-identity revision-id query structure remains linear; prior store-call/time observations are historical, with no new performance or test run claimed.

## Invariants And Boundaries

Unavailable is not measured zero. Independently read attribution and stored-open facts can accompany an unavailable authored-intent result and never enter plus-minus. The caller chooses one resolution; this module does not substitute another dataset, write authored intent, authenticate source reads merely through model shape or own change-kind presentation. Query/index maintenance by delegated owners is outside the narrow no-authored-write claim.

## Evidence

- Ordinary and caller-selected resolution share one memoized summary and label the counted comparison. [16]
- Shared preflight/read failures retain typed unavailable and nonzero unresolved becomes partial. [17]
- Compared content fields separate authored wording/status from provenance/display version. [18]
- Snapshot reads retain canonical membership and realization comparison identities. [19]
- One tally distinguishes counted successor, relationship-only and unequal ambiguous heads. [20]

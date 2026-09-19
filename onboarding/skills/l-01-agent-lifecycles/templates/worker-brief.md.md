# skills/l-01-agent-lifecycles/templates/worker-brief.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/templates/worker-brief.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:15+02:00|
| lastVerifiedCommitHash | `47570cd827428c171613c8cb01e01f0b1cb26f73`|
| lastVerifiedCommitDate | 2026-09-20T01:58:41+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/overview.md` |

## Governing Overview

[lifecycle overview](../overview.md)

## Purpose

This template is the complete session-start packet for one worker on one canonical leaf. It binds
the worker to named worktrees, one implementation scope, exact approved requirement revisions,
repository-defined checks, and one durable turn report.

## Code Commentary

### Logic

The template's own boundary is now stated in the file: it **feeds inputs, it does not author
rules**. Where the packet states a rule, that rule's single home is `../roles/worker.md` (the seat's
own duties), `../operations/implementation.md` and `../operations/closeout.md` (the build procedure
and the targeted-check contract), or `../core/acceptance.md` (the acceptance envelope, attempt
lineage, and completion truth); the rows carry this leaf's *values*, and those files win on
disagreement.

The spawning seat lists every applicable stable ID and version with its immutable packet, corpus
approval, evidence classes, and any already-approved changed delivery. The worker opens those
packets before editing and records a separate acceptance envelope for each revision. The envelope
contains delivery and verification rationales, inspectable citations, the failure each proof would
catch, exact command/results, and approval details for blocked or changed delivery.

The brief also compiles the leaf manifestation, one physical append-only journal path, next
review-handoff attempt ID, predecessor and carried findings, and candidate identity class. Dispatch
and internal implementation/test/evidence reruns do not advance that ID; those runs remain separate
protocol events. Before review handoff, the worker appends one lightweight immutable attempt with
requirement-specific facts and a content-addressed expanded-evidence anchor. A reviewer-rejected
delivery creates a successor at its next handoff. An unrelated later candidate does not reopen
accepted work. Blocked findings use the closed failure taxonomy and requirement problems route
upward for developer-approved revision.
The independently authored reviewer appends a separate adjudication record to that same journal;
the worker turn report links its exact attempt anchors rather than becoming a competing authority.

The brief gives the curator changed paths, observations, and the worker's own **curator hand-off
list** — every requirement-shaped item of this leaf in the shape
`skills/l-01-agent-lifecycles/templates/curator-handoff-list.md`, one entry per item with its
`statement`, `kind`, `target`, `found_at`, `disposition` and `evidence`, while `resolution`,
`validated_at`, `record_action` and `supersedes` stay `null` for the curator to fill. Each entry
names where the thing lives (path plus the construct inside it, from one resolution act) and keeps
the worker's own wording; `target: []` stands where a ruling applies nowhere. The handoff the brief
promises closeout is now the curator's **complete** onboarding/check handoff, not a scoped subset.
None of this grants the worker onboarding,
commit, lifecycle, gate, or task-document mutation authority.

### Conventions

- Compile a fresh brief per leaf and fill every placeholder.
- Use `NONE (native reads only)` when retrieval providers are unavailable.
- Copy the target repository's actual acceptance command; never invent a host fallback.
- Full code-quality and full-test operations require an explicit developer request; **curation does
  not** — the curator always runs the memory-quality operation complete, and closeout and
  integration carry that result as a prerequisite.
- Write the turn report as the worker's last act.

### Invariants And Boundaries

- One worker brief targets one leaf and one primary implementation slice.
- The template feeds inputs: any rule it states has its single home in `../roles/worker.md`,
  `../operations/implementation.md`, `../operations/closeout.md`, or `../core/acceptance.md`, and
  those files win on disagreement.
- “Requirements addressed” is never a substitute for one block per exact ID and version.
- The Checks section and the durable-evidence hold point are both explicit and separate from the
  acceptance envelope.
- The worker never commits, closes out, integrates, or writes accepted onboarding.
- The brief never reuses an attempt ID or authorizes an in-place edit of attempt history.

### Todos

None.


## CCR-R12@v5 Handoff Boundary

This template records the exact targeted checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction; full code quality and full tests are explicit developer requests rather than automatic template gates, while **curation is the exception** — the curator always runs the full memory-quality operation as part of curation, and closeout and integration carry that result as a prerequisite.

## Docs References

No external Domain Documentation source governs this worker template.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The brief binds the exact owned requirement revision and evidence classes. | "## Owned primary requirement (exactly one stable-ID + version)" | skills/l-01-agent-lifecycles/templates/worker-brief.md:69-102 |
| The same block compiles leaf manifestation, attempt/predecessor lineage, and candidate identity before handoff. | "## Owned primary requirement (exactly one stable-ID + version)" | skills/l-01-agent-lifecycles/templates/worker-brief.md:69-102 |
| Repository-defined checks and artifact lifecycle remain separate obligations. | "## Targeted checks (before you report)" | skills/l-01-agent-lifecycles/templates/worker-brief.md:142-164 |
| The final report requires envelopes, checks, curator inputs, and continuity state. | "## Turn report (mandatory, last act)" | skills/l-01-agent-lifecycles/templates/worker-brief.md:173-201 |
| The template declares itself an input-feeder whose stated rules live in the seat's own files. | "it does not author rules." | skills/l-01-agent-lifecycles/templates/worker-brief.md:9-13 |
| The brief carries the worker's curator hand-off list, producer fields filled and curator fields null. | "Your curator hand-off list:"; "because those are the curator's to fill" | skills/l-01-agent-lifecycles/templates/worker-brief.md:175-181 |
| Curation is the standing exception: the curator always runs it complete, and closeout and integration carry the result. | "curation does not, because the curator always runs it complete" | skills/l-01-agent-lifecycles/templates/worker-brief.md:159-165 |

## Cross-Repo References

The concrete worktree paths, tool paths, and verification command come from the dispatched target
repository rather than from this generic template.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## Update History
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `worker-brief.md.md:106` (because those are the curator's to fill) — re-read the claim against the source line: the anchor literal embedded a code span, which the anchor grammar blanks, so it could never match its own source; re-anchored on a span-free literal from the same sentence.
- 2026-09-19T17:15+02:00 — 260915-KS-L28 curator: the input-feeder row's quoted anchor carried an internal semicolon, which the citation form cannot separate from its own `;` delimiter; it now quotes the unambiguous tail `"it does not author rules."` over the same range `:9-13`. No finding was reworded and no claim was dropped.
- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`): re-read this card against the source at `d0c1d1cfa9b576fd117ac2a0c05c5defe0089678` (previous verification stamp `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4`). The diff added three things (`:9-13`, `:29`, `:159-165`, `:175-181`): the template's own boundary paragraph — **it feeds inputs, it does not author rules**, with `../roles/worker.md`, `../operations/implementation.md`/`closeout.md` and `../core/acceptance.md` as the rule homes whose wording wins; the closeout handoff re-worded from the curator's *scoped* onboarding/check handoff to the curator's **complete** one; and the curation exception — full code-quality and full-test operations need an explicit developer request, `curation does not, because the curator always runs it complete`, with closeout and integration carrying that result as a prerequisite. Body: added the rule-home paragraph and the curator hand-off list to the Logic, added a Conventions bullet for the curation exception, added an Invariants bullet for the input-feeder boundary, corrected the CCR-R12@v5 Handoff Boundary paragraph (it claimed full memory quality was only an explicit request), and added three Repo-Internal References rows. Citations: all four pre-existing rows still resolve at HEAD ("## Owned primary requirement (exactly one stable-ID + version)" at `:76` inside `:69-102`, "## Targeted checks (before you report)" at `:148` inside `:142-164`, "## Turn report (mandatory, last act)" at `:188` inside `:173-201`).
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-08-28T14:18+02:00 — Reconciled the worker-brief citation with the final primary-requirement
  heading and committed PDLS ranges; the required acceptance envelope is unchanged.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2: made the next attempt a review-handoff identity, separated
  internal protocol events, and required lightweight content-addressed records.
- 2026-08-27T20:45+02:00 — Clarified one physical per-leaf journal, separate immutable
  worker/reviewer records, and link-only turn-report references.
- 2026-08-27T19:59+02:00 — M42 clarification: narrowed candidate-triggered successor attempts to
  unadjudicated or rejected work and preserved accepted manifestations across unrelated commits.
- 2026-08-27T18:06+02:00 — M40/M43: added leaf journal, immutable attempt/predecessor/candidate
  fields, before-handoff append order, and closed failure/revision routing.
- 2026-08-27T14:52+02:00 — Created onboarding for the approved-packet intake and mandatory
  per-requirement acceptance envelope.

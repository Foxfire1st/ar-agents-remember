# l-01-agent-lifecycles/roles/curator.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T22:40:00+02:00 |
| lastVerifiedCommitHash | `86639933d61528387ce106dbd4d7a334bd468671`|
| lastVerifiedCommitDate | 2026-09-24T18:51:31+02:00|
| governingOverview | `../../../../../../../overview.md` |

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

This file is the packaged runtime artifact synchronized exactly from canonical
`skills/l-01-agent-lifecycles/roles/curator.md`. It carries the same curator lifecycle into installed
runtimes and owns no independent doctrine.

The packaged role is now a **self-contained lifecycle in the corpus's readable order** — purpose and
authority → required inputs → normal workflow → permitted writes and actions → stop and escalation
cases → completion and handoff, then its machine-readable knob block. Shared rules are declared, not
restated: the file opens with `**Inherits:**` naming `core/authority.md`, `core/invariants.md`,
`core/acceptance.md`, `operations/orientation.md`, `operations/curation.md`, and
`operations/recovery.md`. The long curation procedure lives once in `operations/curation.md`, so this
role states its own seat's side of the workflow instead of carrying the whole procedure inline.

## Code Commentary

### Logic

The synchronized role keeps curator at **leaf altitude**: one fresh seat per leaf coherence pass,
spawned after builder code and, when review was requested, the review evidence. Its authority boundary
is stated in the file itself — reconcile intended/current/implemented meaning and maintain affected
memory, with no source-code implementation and no transaction ownership.

The three-way reconciliation is the role's responsibility while the file-writing duty is only its
mechanism: current intent (source, tests, onboarding contracts, entity boundaries, durable incident
lessons) against ruled change intent (task, developer decisions, approved design, builder report,
reviewer verdict) against implemented reality (the complete fed change set and its evidence). The pass
succeeds only when the three agree or every material divergence is surfaced to the owning manager, and
earned understanding is a ratchet — later work may extend or deliberately supersede a contract but may
not make a settled invariant fluid merely because attention moved.

Two curator-specific judgments are stated as prohibitions: do not confuse **test-green with
intent-green**, and do not promote a historical oddity to a permanent invariant without checking its
causal applicability and reconsideration condition. A discovered incident, opportunity, alternative
frame, or forward-learning hypothesis is marked `capture-candidate` with explicit evidence rather than
silently becoming current intent.

The routing rule rejects both overview-dumping and task-log-dumping: each change-set and notes item
goes to the specific sidecar, or to the overview whose subject it actually is, and a notes item with no
file, route, or entity home routes to the L3 Operational-Notes target as a last resort only.

A seat that never touches a mutating AR tool never instantiates a lifecycle. Where this seat does
mutate, it runs its own lifecycle; the dispatch/takeover/recovery contract it follows is
`core/authority.md`, and completion truth vs acceptance is `core/acceptance.md` — a curator hands over
the structured coherence record and its generated projection, validated by the owning manager.

**The packaged copy carries the authoring obligation this leaf added to the canonical role file, and it
is the seat's own half of the reconciliation.** `260921-ICR-L20` (`ICR-R20@v1`) put a fourth numbered
`## Process` step in the canonical `curator.md` (and in the `operations/curation.md` block this file
inherits): the requirement-shaped items the hand-off list carries are *knowledge*, not onboarding prose,
so the seat hands them to the real writer with the ordinary route's invocation
(`agents-remember knowledge-ingest --contract … --list … --authorization-ref … --baseline … --publish
--commit --json`) and **reads the report, never the exit status** — per-entry `committed`/`rulings`/
`refused`, `publicationRoute`, and a `publishedIdentity` read back through the reader's owner. The
packaged file also gained the matching prohibition: this seat never writes the dataset itself and never
treats the mounted `knowledge_change` tool as a write route, because that tool refuses every record kind
and exists only to name the subcommand. Nothing else in the packaged artifact moved — its order, its
`**Inherits:**` line, its knob block and its authority boundary are unchanged, which is exactly what
"synchronized canonical behavior" means here: the copy states what the canonical file states, and the
canonical file's change is this one obligation.

### Conventions

- Treat canonical `skills/` as the sole doctrine owner.
- Keep this artifact byte-identical through `scripts/sync-skills.py`.
- Describe packaged behavior only as synchronized canonical behavior.
- Verification provenance remains specific to this packaged source path.

### Invariants And Boundaries

- Package installation must not alter curator authority or workflow.
- This artifact cannot introduce a compatibility lifecycle or task-specific override.
- Curator still writes onboarding only and communicates through structural parent messaging/report.
- The curator never writes code, decides gates, mutates task-doc state, performs closeout,
  integration, or finalization, runs the closeout preview, or repairs transaction conflicts.
- **This role file names no sibling role file.** The corpus forbids learning one's own obligations
  from another seat's prose; only wearing a hat or dispatching that seat may cite
  `roles/<other>.md`, and the shipped check fails on any other reference.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; curation is the exception — the curator always runs the complete memory-quality operation, and closeout and integration carry its completed result as a prerequisite rather than rerunning it. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The packaged curator declares the same seat, authority boundary, and three-way responsibility as the canonical source. | "You run one leaf's coherence pass and you write onboarding."; "Reconcile three ways before writing anything" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:8-9; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:47-47; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:60-60; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:61-61 |
| The role is a self-contained capsule: its brief is its session start, and it declares no inherited shared sources. | "Your brief is your session start" | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:9-9 |
| **The authoring obligation the packaged copy now carries, and the prohibition that keeps the dataset out of this seat's hands.** | "Author and publish the durable knowledge through the real writer."; "Never write the knowledge dataset yourself." | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:53-69; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:150-152; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:185-185; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:70-70; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:187-187 |
| The curation procedure — inputs, workflow, authority gates, failure handling, handoff — has one home outside the role file, and the authoring step landed in that home too. | `# Operation — Curation`; `## Handoff / exit`; "Route the durable knowledge through the real writer, and publish it." | skills/l-01-agent-lifecycles/operations/curation.md:1-1; skills/l-01-agent-lifecycles/operations/curation.md:170-180; skills/l-01-agent-lifecycles/operations/curation.md:60-71; skills/l-01-agent-lifecycles/operations/curation.md:60-60; skills/l-01-agent-lifecycles/operations/curation.md:212-212; skills/l-01-agent-lifecycles/operations/curation.md:213-213 |
| The role declares the readable order — Inputs, Process, Outputs — with no operator-knob block. | `## Inputs`; `## Process`; `## Outputs` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:11-11; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:45-45; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:112-112; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:139-139; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:58-58; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:141-141; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:59-59 |
| The canonical source is the doctrine owner. | `# Curator` | skills/l-01-agent-lifecycles/roles/curator.md:1-12 |
| A non-sanctioned sibling-role reference fails the shipped corpus check, which is why this role file names none. | `SANCTIONED_SIBLING_REFERENCES` | mcp/tests/test_role_instruction_corpus.py:114-116 |
| MCP package data is an explicit synchronization target. | `TARGETS` | scripts/sync-skills.py:43-47 |
| Synchronization replaces each target from the canonical tree and then checks equality. | `sync_target`; `check_targets` | scripts/sync-skills.py:136-157; scripts/sync-skills.py:179-203 |

## L23 Final Candidate Disposition

Curator admission repeats the manager's task-derived lineage proof and requires a passing route
review bound to the current candidate tree. Curation documents that frozen candidate only and leaves
commit stamps and lifecycle mutation to closeout.

## 260821-DAGQC-L2 Synchronized Quality Invocation

The packaged curator uses the canonical explicit sync/start/poll request objects. Capacity refusal
is a retry signal over the same API, never authority for a host runner, fallback, or retired flat
call. The content remains synchronized from the canonical curator role.

## MCAR-L02 Structured Curator Authority

The curator's last act is now tool-owned publication, not writing or versioning a report. After the
quality worklist reaches zero, the role prepares the exact tuple set, supplies one non-invented
disposition/rationale/evidence reference per tuple, publishes the separately identified semantic
revision and delivery attempt, optionally freezes a snapshot, and validates the sole live
structured authority. Generated Markdown is returned as projection evidence only.

## CCR-L42 current candidate

Curator intake now binds the route-review requirement to altitude: standalone and organizational leaves require a leaf route-review record, while atomic child leaves defer route adjudication to canonical-master integration and retain their other task, code, memory, ledger, and coherence gates.

## 260921-ICR-L27 The Repository-Foundation Entry Becomes A Second, Bounded Shape Of This Work

`260921-ICR-L27` (`ICR-R27@v1`) adds the **repository-foundation entry** to this role file: the shape
this seat's work takes when the scope is a repository's first or resumed knowledge foundation — a new
project entering ordinary setup, an existing project with Markdown memory and no knowledge database, or
an explicitly requested bootstrap of an existing project — rather than one leaf's delta. The inputs there
are the declared repository id, the resolved coordination context, the requested scope, the available
sources and the current knowledge state: **no brief, no change set and no enclosure contract to intake.**

The ownership is unchanged on both entries — the reconciliation and the authored knowledge are this
seat's, and there is still one admitted writer and one declared published location. What changes is the
carrier, the admission and the scope, and the role file states the gate in the code's own vocabulary:
**`260921-ICR-L32` admitted this seat taskless** on the developer's 2026-09-24 ruling, so a session
opened for the curator with **no** task document is now admitted (`curator` is one of
`TASKLESS_SEAT_ROLES`) and authors the foundation under this seat's own rules, while every other role is
still refused (`400 task-binding-required`, "named role scope is required"). On a repository with no task
at all the step can also be carried by the taskless bootstrap seat, which reads the state and hands it
on, and by the taskless writer an instructed session holds. The procedure is the
`c-14-knowledge-bootstrap` skill.
> **Seat-policy note at L27's bytes (dated 2026-09-24).** This records the policy of the candidate that curation read: code base `06ed70cfcde7e3860ee5b53435727e7512e4335c` plus that leaf's working-tree delta, where a document-less `curator` session was refused `task-binding-required` because `TASKLESS_SEAT_ROLES` was `{"chat", "terminal", "bootstrap"}`. That was true of those bytes and is **superseded** — whether `curator` joined the set was then a product decision under revision, and it was taken in `260921-ICR-L32`.
>
> **Seat-policy note at these bytes (L32 curation, dated 2026-09-24T17:20+02:00).** At the bytes this curation read — code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus this leaf's working-tree delta — `TASKLESS_SEAT_ROLES` is `{"chat", "terminal", "bootstrap", "curator"}`: a document-less `curator` session is **admitted** and receives the curator capsule, while every other role is still refused `task-binding-required`. Read the sentences above as the policy **at these bytes**, not as a permanent property of the product.

Two further edits keep the role's own record and permissions truthful: the output section gains the
foundation entry's own facts (the state read before authoring, the areas examined and not examined, each
entry's outcome, the publication result, the identity an independent read confirmed, and the remaining,
unmeasured and carried work), and the permitted-action list now names both write-plane entry points —
`knowledge-ingest` on the leaf entry and `knowledge-bootstrap` on the foundation entry, the latter
belonging to a session with no enclosure in scope because it refuses one (`enclosure_in_scope`).

**This card describes a generated copy**, propagated from
`skills/l-01-agent-lifecycles/roles/curator.md` by `scripts/sync-skills.py` into this package-owned copy
and the eight harness starter packages.

## Update History
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — this seat is admitted taskless.** The foundation-entry paragraph now says the seat opens either way (on a leaf's task document, or with none as the taskless carrier of the repository-foundation entry, per the developer's 2026-09-24 ruling) instead of asserting that a document-less curator session is refused; the L27 seat-policy note is kept as the statement true at L27's bytes and a second dated note records the policy at these bytes. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T12:42:00+02:00 — 260921-ICR-L27 curator (uncommitted change set on `ar/260921-icr-l27-ar`, code base `06ed70cfcde7e3860ee5b53435727e7512e4335c`): **body update: the repository-foundation entry.** The entry paragraph and its refusal, the process block that runs `c-14-knowledge-bootstrap` in its order with the writer chosen by scope, the output section's foundation facts, and the permitted-action line naming both write-plane entry points with the enclosure the taskless one refuses. **Citation accounting:** this card's rows into `## Handoff / exit`, `## Process` and `## Outputs` were re-read against the candidate's own bytes and re-anchored to the lines that now carry each construct, rather than shifted by a remembered delta. No verification stamp was advanced: the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base `63b476297708f779de8ed5c0bf3555b9d1de70c2`): **the packaged role copy carries the canonical role's new numbered step** — examine family coverage and author it, then read the two planes back — with the two hand-off keys the curator now owns and the report sentences the role's record has to carry. Written in `skills/l-01-agent-lifecycles/roles/curator.md` and propagated here by `scripts/sync-skills.py`; nothing in this copy is edited by hand.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.

- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the one enforced citation row was re-read and its heading anchor corrected — the defect is inherited and pre-existing.** The row's first anchor was the bare heading `` `# Operation` `` and the gate resolved it **nowhere in the code tree**: the inherited operations file's H1 is `# Operation — Curation`, so the anchor named a heading that does not exist rather than one that moved. This is a rename, not a line shift, and the claim is about the procedure's single home, so the pointer was corrected rather than widened. The anchor now reads `` `# Operation — Curation` ``, which occurs literally at `skills/l-01-agent-lifecycles/operations/curation.md:1`; the row's other two anchors were verified unchanged (`## Handoff / exit` at 151 inside `:151-151`, and the quoted authoring sentence at 60 inside `:60-71`). That defect predates this leaf and is repaired here only because this leaf's curation pass owns the gate finding. The claim wording and every other row are unchanged; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately **not** advanced, because nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-21T18:09+02:00 — 260921-ICR-L20 curator (uncommitted change set on `ar/260921-icr-l20`, production line `71a4433e686b3380af97a0836bb82bab2c8f2aad`): **body update for the one obligation this leaf added to the canonical role file and therefore to this packaged copy.** The canonical `skills/l-01-agent-lifecycles/roles/curator.md` is 144 lines and gained a fourth numbered `## Process` step (the real `knowledge-ingest … --baseline … --publish --commit --json` invocation and the report fields to consume: `committed`/`rulings`/`refused`, `publicationRoute`, `publishedIdentity`), a permitted-action line naming the subcommand, a `## What you must not do` prohibition against writing the dataset or treating the mounted `knowledge_change` tool as a write route, and a report sentence carrying the read-back identity; the inherited `operations/curation.md` block gained the same step and its supporting rules. Nothing else in the packaged artifact moved — its readable order, its `**Inherits:**` line, its knob block and its authority boundary are unchanged, which is what "synchronized canonical behavior" means for a change of this shape. **Citation accounting:** the rows this card already carried into the packaged role file were re-derived from the post-edit bytes rather than shifted — `Reconcile three ways before writing anything` `:40-40` → `:44-44`, and `## Process`/`## Outputs` `:38-38`/`:73-73` → `:42-42`/`:91-91` — the inherited-block row's `## Handoff / exit` `:121-128` → `:151-151`, and one new row cites the authoring step. No claim and no row was dropped, and no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real commits.- 2026-09-20T01:00+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 3 enforced citation rows this card carried (citation_anchor_absent_from_range) — `Reconcile three ways before writing anything` already sat in its cited range, and `## Process` was repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:42-42 and `## Outputs` to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:91-91; every claim wording, anchor and every other range is unchanged, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 1 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `Reconcile three ways before writing anything`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 2 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `curator.md.md:90` ("You run one leaf's coherence pass and you write onboarding.", "Reconcile three ways before writing anything"); `curator.md.md:93` (`## Inputs`, `## Process`, `## Outputs`).
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `SANCTIONED_SIBLING_REFERENCES` repointed to mcp/tests/test_role_instruction_corpus.py:114-116. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `## 6 — Completion And Handoff`; `## Knobs, Tool Surface, And Dispatch Authority` repointed to mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:154-167; mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:168-185. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T12:28+02:00 — 260915-CAPS-L18 curator: **complete curation inverts the doctrine this card recorded.** CAPS-R18@v1 removes the optional/narrow-curation sentences from the shipped instruction corpus and states the rule normatively — the full `memory_quality_check` operation runs as part of every leaf's curation at its contract scope, a named scoped check or `checks=[...]` subset never stands in for it, every curator-actionable finding is repaired or escalated as blocked with its exact returned code, and closeout and integration **carry** the completed curation as a prerequisite while invoking nothing. Replaced the CCR-R12@v5 transaction-boundary boilerplate sentence, which still presented full memory quality as an explicit request, and updated the role's own curation sentences to the complete-handoff rule. Hand-repaired four citation findings this leaf's own source edit drifted (per-document `citation_fix` is refused in a leaf worktree; D14): `operations/curation.md` `## Handoff / exit` re-pointed to :121-128, the role's `## Knobs, Tool Surface, And Dispatch Authority` range to :165-182, and two `SANCTIONED_SIBLING_REFERENCES` ranges to the test module's current :110.
- 2026-09-16T20:45+02:00 — owning-seat merge resolution (source-line convergence): the
  `governingOverview` field and its link were restored to `../../../../../../../overview.md`.
  The 2026-09-16T08:01 metadata repair above dropped one path level — this card sits one directory
  below the skill's `SKILL.md` card, so the target it names (the MCP package overview,
  `onboarding/mcp/overview.md`) needs seven levels up, not five. The five-level value resolved to
  `onboarding/mcp/src/agents_remember/overview.md`, which does not exist, so the card pointed at a
  missing file while its own text claimed the MCP package overview. No content claim changed; only
  the path. Verification metadata is unchanged and stays closeout-owned.
- 2026-09-16T08:01+02:00 — 260915-CAPS-L1 curator: **body updated for the corpus consolidation.** The
  canonical curator role was rewritten into the corpus's readable order (§ 1 purpose/authority → § 2
  required inputs → § 3 normal workflow → § 4 permitted writes → § 5 stop/escalation → § 6
  completion/handoff, plus the knob block) and now declares its shared sources with `**Inherits:**`
  instead of restating them. Updated Purpose (the role's readable order and its inherited sources),
  Logic (leaf altitude, the authority boundary, three-way reconciliation, the test-green-vs-intent-green
  and historical-oddity prohibitions, the capture-candidate rule, the last-resort L3 note target, and
  where dispatch/acceptance doctrine now lives), Invariants (the explicit never-writes-code /
  never-decides-gates / never-touches-the-transaction boundary, and the no-sibling-role-reference rule
  the shipped check enforces), and Repo-Internal References (the two citations whose anchors no longer
  exist — `## What This Seat Is` and `### 4 — Repair Affected Onboarding, Then Publish` — replaced by
  current anchors, plus rows for `operations/curation.md` and `SANCTIONED_SIBLING_REFERENCES`). The
  preserved task-delta sections below still describe rules that remain in force at their new homes in
  `operations/curation.md` and `core/acceptance.md`. **Metadata repair:** `governingOverview` pointed at
  `../../../../../../../overview.md` (the repository root overview) while its link text said "MCP
  package overview"; corrected to `../../../../../overview.md`. Verification metadata remains
  closeout-owned — the source is uncommitted, so no stamp was advanced and no commit hash invented.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: Curator intake now binds the route-review requirement to altitude: standalone and organizational leaves require a leaf route-review record, while atomic child leaves defer route adjudication to canonical-master integration and retain their other task, code, memory, ledger, and coherence gates.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 synchronized manager-only curator dispatch,
  explicit ambient takeover, and fixed structural-row ownership. Verification remains
  closeout-owned.

- 2026-08-29T08:52+02:00 — Replaced hand-authored coherence reporting with exact structured
  publication and validation. Verification remains closeout-owned.

- 2026-08-28T11:32+02:00 — No content impact: synchronized projection payload changed with the
  canonical one-primary requirement doctrine; projection ownership and byte-identity rules remain
  unchanged.
- 2026-08-27T16:27+02:00 — Synchronized exact requirement-packet and per-revision adjudication
  intake from canonical curator doctrine. Verification remains closeout-owned.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: synchronized curator quality calls and retry guidance from canonical doctrine. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-14T06:32+02:00 — L23 synchronized runtime doctrine: curator admission requires current
  lineage and a passing exact-candidate route-review record before memory reconciliation starts.
  Verification remains closeout-owned.

- 2026-08-11T16:54+02:00 — Synchronized the single enclosure-checklist intake/repair loop and its
  zeroable curator gate without creating copy-specific doctrine.
- 2026-08-11T14:40+02:00 — Synchronized the curator-owned missing-onboarding/full-quality
  completion condition without creating copy-specific doctrine.
- 2026-08-11T14:25+02:00 — Replaced accumulated copy-specific/task-delta prose with the exact
  synchronized-artifact contract and current packaged-source evidence.
- 2026-08-09T13:59+02:00 — Synchronized fact-relay supervision wording from canonical doctrine.
- 2026-08-08T22:10+02:00 — Synchronized the agent-notifier naming wave.
- 2026-07-12T18:11+02:00 — Established packaged curator lifecycle coverage.

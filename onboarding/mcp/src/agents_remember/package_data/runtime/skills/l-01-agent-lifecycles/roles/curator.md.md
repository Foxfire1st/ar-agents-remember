# l-01-agent-lifecycles/roles/curator.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:01+02:00 |
| lastVerifiedCommitHash | `304de8e272fd9128d035b805f317da5f3090865c`|
| lastVerifiedCommitDate | 2026-09-17T12:34:11+02:00|
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
| The packaged curator declares the same seat, authority boundary, and three-way responsibility as the canonical source. | `## 1 — Purpose And Authority` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:14-48 |
| The role opens by naming the shared sources it composes with rather than restating them. | `**Inherits:**` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:12-12 |
| The curation procedure — inputs, workflow, authority gates, failure handling, handoff — has one home outside the role file. | `# Operation — Curation`; `## Handoff / exit` | skills/l-01-agent-lifecycles/operations/curation.md:1-1; skills/l-01-agent-lifecycles/operations/curation.md:121-128 |
| The role declares the readable order and the knob block after the handoff section. | `## 6 — Completion And Handoff`; `## Knobs, Tool Surface, And Dispatch Authority` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md:165-182 |
| The canonical source is the doctrine owner. | `# Lifecycle — Curator` | skills/l-01-agent-lifecycles/roles/curator.md:1-12 |
| A non-sanctioned sibling-role reference fails the shipped corpus check, which is why this role file names none. | `SANCTIONED_SIBLING_REFERENCES` | mcp/tests/test_role_instruction_corpus.py:110-110 |
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

## Update History

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

# skills/l-01-agent-lifecycles/roles/curator.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/roles/curator.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:09+02:00 |
| lastVerifiedCommitHash | `562cef4ca64de5b11712d5165d24e78c9a035312`|
| lastVerifiedCommitDate | 2026-09-19T17:51:43+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/roles/overview.md` |

## Governing Overview

[roles overview](overview.md)

## Purpose

The curator is one fresh, leaf-scoped conservative coherence seat after builder code and reviewer
evidence exist. It writes onboarding only. Its responsibility is to reconcile existing system
intent, ruled task/developer intent, and implemented reality so accepted memory states compact
current contracts rather than a leaf transcript.

## Logic

The curator consumes the real leaf task/design rulings, complete fed code change set, builder turn
report, the exact approved stable-ID + version packets, the reviewer's independent per-revision
verdict, existing onboarding/entity knowledge, and the **producers' curator hand-off list** — the
builder's and the reviewer's requirement-shaped items in the shape `../templates/curator-handoff-list.md`
owns. That list is ingested **as data** and its fields are read by their owner: the producer supplies
`id`, `statement`, `kind`, `target`, `found_at`, `disposition`, `disposition_source`, `evidence` and
`authority`; `resolution`, `validated_at`, `record_action` and `supersedes` belong to the curator and
arrive `null`. A carried `disposition` is never re-judged at intake, and no curator field is left to a
later seat. Missing/unapproved/version-mismatched packets
refuse intake. Rejected or worker-blocked revisions remain report blockers and cannot be promoted
into current onboarding intent. For every affected contract it
classifies the implementation as preserving, extending, deliberately superseding, or contradicting
existing intent. It updates only the proper file card, affected route overview, route index, or
entity record, then supplies exact judgments to the lifecycle API that publishes the sole
structured coherence authority for the manager.

Current intent, evidence/integrity, and semantic history are kept distinct. Generic category text,
overview dumping, and task-log repetition are rejected. Mechanical no-impact cards stay precise.
Forward-looking incidents, opportunities, and hypotheses remain report capture candidates until an
authorized workflow promotes them.

Before reporting completion, the curator updates affected onboarding and runs the **complete**
memory-quality operation — a named scoped check never stands in for it — recording
passed, failed, blocked, and not-run results honestly. Dirty-source drift and real-commit-derived
stamps/fingerprints are reported separately; they never excuse an underlying content, citation, shape,
history, entity, or index defect. The full memory-quality operation is not an optional extra for this
seat: curation is always complete, it runs at intake and after every repair, and the completed result
is prerequisite evidence that closeout and integration carry rather than rerun. Certification is the
curator's own act through `curator_coherence` when the checklist requires it.

The rewritten role file carries no role table and no dispatch surface: its seat classification and
`dispatch`/`tools` rows live in `composition-manifest.json`, where they are structural documentation
rather than settings keys. Only the manager ordinarily dispatches this leaf
seat through plane authority; an identity-free developer launcher may target it only for an
explicit task-seat takeover. The curator has no `dispatch_agent` caller authority or ambient
fallback — its `## What you may do` surface omits that call — and its closing section escalates one
rung to the seat that owns the leaf.

## Conventions

- Read canonical sources, tests, negative knowledge, incidents, task rulings, and the full diff
  before writing.
- Use one-to-one sidecars and governing overview links; update entities only when a real entity changes.
- Default bodies hold present intent and boundaries; Update History records concise semantic transitions.
- Run the complete memory-quality operation for this leaf — never a scoped subset — repair every
  curator-actionable finding or escalate it as blocked with its exact returned code, and report any
  check that is failed, blocked, or not-run before the prepared memory leg is handed off.
- Leave real-commit hashes and entity fingerprints pending until governed closeout creates the commit.

## Invariants And Boundaries

- Curator writes no code and decides no gate.
- Curator does not mutate task documents, lifecycle state, worktree contracts, closeout, or integration.
- Builder, reviewer, curator, and manager remain separate seats and artifacts.
- Every changed onboarding contract maps to an exact approved requirement revision and accepted
  reviewer adjudication.
- Missing evidence or a material three-way contradiction escalates to the owning manager.
- Curator cannot publish completion authority while its required checks still name actionable work.
- Runtime ids are private correlations; curator communication uses structural parent messaging and
  the durable report.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full code quality, full tests, certification, and independent review are explicit operations only; memory quality is this seat's exception — the curator always runs it complete, and closeout and integration carry that result as a prerequisite. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The seat definition names the three-way reconciliation and onboarding-only boundary. | "**You run one leaf's coherence pass and you write onboarding.**" | skills/l-01-agent-lifecycles/roles/curator.md:8-9 |
| Intake requires exact approved packets/adjudications, ruled intent, the complete change set, existing contracts, durable reports, and the producers' curator hand-off list. | "## Inputs"; "the producers' curator hand-off list" | skills/l-01-agent-lifecycles/roles/curator.md:11-31 |
| Inspection classifies contract disposition rather than equating test-green with intent-green. | "Do not confuse **test-green with intent-green**" | skills/l-01-agent-lifecycles/roles/curator.md:63-71 |
| Current intent, evidence, and semantic history are separate information planes. | "Reconcile three ways before writing anything" | skills/l-01-agent-lifecycles/roles/curator.md:40-44 |
| Checks require complete missing-onboarding/quality repair before structured publication, distinct from closeout-owned commit provenance. | "Run the complete curation operation at intake and after every repair" | skills/l-01-agent-lifecycles/roles/curator.md:49-59 |

## 260821-DAGQC-L2 Quality Invocation

Curator doctrine now issues the memory-quality operation through the exact discriminated request
object. A synchronous repair loop uses `mode: sync`; if async work is selected, `mode: start` is
followed by `mode: poll` carrying only repository and run id. Capacity refusal means poll/wait and
retry; it does not authorize an alternate runner or compatibility call.

## Update History
- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`): re-read this card against the source at `d0c1d1cfa9b576fd117ac2a0c05c5defe0089678` (previous verification stamp `14582854955223f75588c23c9f29f9d51bde9675`). The diff is seven added lines in `## Inputs` (`:22-28`) adding **the producers' curator hand-off list** — the builder's and reviewer's requirement-shaped items in the shape `../templates/curator-handoff-list.md` owns, with the producer fields filled and `resolution`/`validated_at`/`record_action`/`supersedes` the curator's to fill, a carried `disposition` never re-judged at intake. Body: added that intake item to the Logic (with its field-ownership boundary), extended the intake row's extent to the whole section (`:11-31`), and corrected three statements the current source does not support — the Logic's "runs scoped checks" and "Full memory quality and certification remain explicit operations, not closeout or integration prerequisites" (the source requires the **complete** operation at intake and after every repair, `:49-59`), the Conventions bullet that sent the seat to scoped onboarding checks, the same "explicit operations only" clause in the CCR-R12@v5 block, and the "role table classifies curator as target-only" sentence (the rewritten file carries no role table; that classification now lives in `composition-manifest.json`). Citations: re-derived against the file as it stands — the test-green row's `:56-59` extent no longer carried its anchor and moved to `:63-71`; "Reconcile three ways before writing anything" moved from `:33-37` to `:40-44`; "Run the complete curation operation at intake and after every repair" moved from `:42-46` to `:49-59`. Verified ranges/claims: all four rows' anchors resolve inside their extents at HEAD, and the new intake row resolves against the added bullet.
- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **the role file this card cites was rewritten into the function shape, and the card was re-derived against it.** leaf `260915-CAPS-L22` (under the developer's 2026-09-17 ruling) replaced the numbered sections and the `## Knobs, Tool Surface, And Dispatch Authority` block with `## Inputs`, `## Process`, `## Outputs`, `## What you may do`, `## What you must not do` and a closing `## Stop and …` section, so every Repo-Internal References row here that named an old heading or an out-of-range extent was re-pointed by reading the rewritten file: each anchor below is text that exists in the cited range, and each range is in bounds of the file as it stands. Where a claim described a construct the rewrite removed, the claim itself was re-worded to what the file now says. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits. **Correction (`D51`, made in the same pass):** this entry first attributed the rewrite to `CAPS-R24@v1`. No such requirement revision exists — the master declares `CAPS-R01@v1` … `CAPS-R19@v1` — and the rewrite is leaf `260915-CAPS-L22`'s, under the developer's 2026-09-17 ruling. This curator fabricated the id; it is corrected here and in the body above.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 classified curator as target-only plus explicit
  ambient-takeover target, corrected ordinary plane ownership to the manager only, and kept
  structural authority outside settings. Verification remains closeout-owned.

- 2026-08-29T09:14+02:00 — MCAR-L02 replaced the hand-authored terminal report with exact
  lifecycle API publication and validation of the sole structured coherence authority.
  Verification remains closeout-owned.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T16:27+02:00 — Requirement-corpus briefing repair: curator intake now receives exact
  approved revision packets and per-revision adjudication; rejected/blocked delivery cannot become
  current intent. Verification metadata remains pinned until governed closeout.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: aligned curator doctrine with the canonical strict memory-quality request and retry guidance. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-11T14:40+02:00 — Made current-additions coverage and the full enforced memory-quality
  worklist curator-owned completion conditions while preserving closeout ownership of real-commit metadata.
- 2026-08-11T14:20+02:00 — Rewrote the default body around the curator's current three-way
  coherence responsibility; removed generic spawn prose and appended task-delta overrides.
- 2026-08-11T07:16+02:00 — Commit-derived verification was assigned to governed closeout after
  curator content/citation preparation.
- 2026-08-05T03:47+02:00 — Curator checks became enclosure-contract scoped.
- 2026-07-12T18:11+02:00 — Established the fresh onboarding-only curator seat and durable report.

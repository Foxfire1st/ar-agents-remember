# skills/l-01-agent-lifecycles/roles/reviewer.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | skills/l-01-agent-lifecycles/roles/reviewer.md |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-09-19T17:09+02:00 |
| lastVerifiedCommitHash | `562cef4ca64de5b11712d5165d24e78c9a035312`|
| lastVerifiedCommitDate | 2026-09-19T17:51:43+02:00|
| governingOverview | skills/l-01-agent-lifecycles/roles/overview.md |

## Governing Overview

[overview.md](overview.md)
## Purpose

This is the canonical independent-review lifecycle. It inspects the exact candidate and adjudicates
each stable requirement ID from the same applicable set dispatched to the worker.

## Code Commentary

### Logic

The reviewer does not accept a worker assertion at face value. For every stable ID it independently
opens the implementation/deliverable and verification citations, checks the evidence class, and
records `accepted` or `rejected` with its own rationale. Missing rationale, invalid citations,
wrong-class evidence, or an absent durable developer ruling for blocked/changed delivery forces
rejection. One rejected ID prevents an overall pass; already accepted IDs stay accepted through a
delta round unless the repair directly regresses them.

The first citation check is the version-addressed canonical packet itself: its ID/version must
match, its state must be approved, and it must carry the durable corpus ruling. A task summary or
worker paraphrase cannot substitute for that approved revision.

Adjudication now binds the exact immutable worker attempt, leaf manifestation, and candidate. The
reviewer appends its own record without editing the worker record and classifies each rejection
with one of five exact classes. It may prove a direct regression, but only the owning manager (or
flat-run architect) records bounded invalidation; the finding alone cannot reopen accepted work or
extend scope.

The worker record is lightweight: the reviewer verifies its requirement-specific status,
rationales, citations, findings/failure class, and the digest plus exact anchor of the immutable
expanded evidence. Internal implementation/test/evidence protocol events may support a claim but
are never adjudicated as worker attempts and never inflate attempt or rejection counts.

The append target is the same single physical leaf journal that contains the worker attempt. The
reviewer's separately authored verdict links that journal anchor instead of duplicating the
adjudication as another authority.

Beside the verdict, the reviewer emits **its own curator hand-off list** (`:88-95`) — its verdicts and
findings in the shape `../templates/curator-handoff-list.md` owns, as data rather than as verdict prose
for the curator to re-read. Each entry is one finding or one requirement adjudication, carrying the
source it came from and the place it was found at, and a finding the reviewer minted carries its own
stable ID; the list is what the curator ingests. It is emitted **in the same list shape the worker
emits**, because the curator consumes one contract: it names where the thing lives rather than where
the reviewer looked — the path and the construct inside it come from one resolution act — and carries
the reviewer's own statement and evidence verbatim rather than re-telling them.

If the manifestation candidate moves before adjudication, the stale attempt is rejected and a
successor is reviewed. An unrelated later candidate does not reopen an accepted attempt.

The rewritten role file carries no role table: the seat's classification and `dispatch`/`tools` rows
now live in `composition-manifest.json`, where they are structural documentation rather than settings
keys. The role itself is polymorphic across the review
contexts: a manager owns leaf and master-exit reviewers, the architect owns the sprint plan
reviewer, and the orchestrator owns the sprint super-exit reviewer; the file's own seam table
(`:20-27`) fixes five seam rows — standalone/organizational leaf route review, atomic-master
integration review, master-exit, portfolio plan review and super-exit — and where each verdict goes.
The plane stamps that exact
parent document+role onto the reviewer generation. An identity-free launcher may target an
altitude-valid reviewer for explicit takeover, but a sprint takeover cannot invent architect versus
orchestrator parentage and parent operations fail closed. The reviewer cannot call `dispatch_agent`:
its `## What you may do` surface (`:132-138`) omits that call.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization
outputs. Requirement adjudication and the durable-evidence stable-contract-or-expiry hold point
are independent mandatory concerns. Accepted attempts remain closed without one of the two
authorized invalidation paths.
One reviewer role serves leaf, master, plan, and super seams, but each generation reports only to
its plane-stamped structural parent.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full quality, full tests, full memory quality, certification, and independent review are explicit operations only. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker envelope, reviewer verdict template, manager exact-set dispatch, and governing route overview.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every exact requirement attempt and candidate receives a separate independent accepted/rejected record. | "Adjudicate every requirement revision separately" | skills/l-01-agent-lifecycles/roles/reviewer.md:70-73 |
| The verdict template structurally repeats one adjudication block per stable ID. | "## Mandatory Requirement Adjudication Block" | skills/l-01-agent-lifecycles/templates/verdict.md:72-72 |
| The reviewer emits its own curator hand-off list in the shared producer shape. | "Your own curator hand-off list" | skills/l-01-agent-lifecycles/roles/reviewer.md:88-95 |
| The seat's seam table fixes the five seams and where each verdict goes. | "The seam you are reviewing" | skills/l-01-agent-lifecycles/roles/reviewer.md:18-27 |

## Cross-Repo References

No meaningful cross-repo references.

## 260815-DAG-L2 Candidate And Repair Scope

Master-exit review is nature-aware. Organizational review covers the exact proposed final super
candidate—prior landed contributions plus the proposed final leaf—before its one full gate and ref
movement; atomic review covers the isolated branch before its single landing. At super exit, every
blocking finding decomposes into an owning/reopened leaf or a new scoped fix leaf. The reviewer may
not route implementation onto the super worktree.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.

## Update History
- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator (uncommitted change set on `ar/260915-ks-l28`): re-read this card against the source at `d0c1d1cfa9b576fd117ac2a0c05c5defe0089678` (previous verification stamp `14582854955223f75588c23c9f29f9d51bde9675`). The diff is eight added lines in `## Outputs` (`:88-95`) adding **the reviewer's own curator hand-off list** — its verdicts and findings in the shape `../templates/curator-handoff-list.md` owns, emitted as data in the same list shape the worker emits, naming where the thing lives rather than where the reviewer looked and carrying its own statement and evidence verbatim. Body: added that output to the Logic and added two Repo-Internal References rows (the hand-off list, `:88-95`; the seat's seam table, `:18-27`). Correction made while re-deriving: the Logic's "the role table classifies reviewer as target-only" and "its dispatch/tools rows are structural documentation" named a table the rewritten role file no longer carries — the classification now lives in `composition-manifest.json` — and the reviewer's inability to dispatch is now stated from its own `## What you may do` surface (`:132-138`). Verified ranges/claims: both pre-existing rows still resolve ("Adjudicate every requirement revision separately" at `:70` inside `:70-73`; the verdict block heading at `templates/verdict.md:72`), and both new rows' anchors resolve inside their extents.
- 2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **the role file this card cites was rewritten into the function shape, and the card was re-derived against it.** leaf `260915-CAPS-L22` (under the developer's 2026-09-17 ruling) replaced the numbered sections and the `## Knobs, Tool Surface, And Dispatch Authority` block with `## Inputs`, `## Process`, `## Outputs`, `## What you may do`, `## What you must not do` and a closing `## Stop and …` section, so every Repo-Internal References row here that named an old heading or an out-of-range extent was re-pointed by reading the rewritten file: each anchor below is text that exists in the cited range, and each range is in bounds of the file as it stands. Where a claim described a construct the rewrite removed, the claim itself was re-worded to what the file now says. No verification stamp advanced: the source is uncommitted and the governed closeout owns the real code and memory commits. **Correction (`D51`, made in the same pass):** this entry first attributed the rewrite to `CAPS-R24@v1`. No such requirement revision exists — the master declares `CAPS-R01@v1` … `CAPS-R19@v1` — and the rewrite is leaf `260915-CAPS-L22`'s, under the developer's 2026-09-17 ruling. This curator fabricated the id; it is corrected here and in the body above.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "## Mandatory Requirement Adjudication Block" repointed to skills/l-01-agent-lifecycles/templates/verdict.md:72-72. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "## Mandatory Requirement Adjudication Block" repointed to skills/l-01-agent-lifecycles/templates/verdict.md:67-67. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:30+02:00 — CCR-R12@v5 transaction-only curation: updated the current onboarding boundary; verification metadata remains preserved for the coordinated final stamp.
- 2026-09-09T12:22:46+00:00: Generated citation repair: "## Mandatory Requirement Adjudication Block" repointed to skills/l-01-agent-lifecycles/templates/verdict.md:66-66. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: replaced the leaf-only
  parent description with the four-context reviewer model and its fail-closed ambient sprint
  boundary. Verification remains closeout-owned.

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 classified reviewer as target-only plus explicit
  ambient-takeover target, corrected ordinary plane ownership to the manager only, and kept
  structural authority outside settings. Verification remains closeout-owned.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2/M44@v2: reviewers now validate lightweight
  content-addressed worker records and keep internal protocol events outside formal adjudication.
- 2026-08-27T20:45+02:00 — Clarified same-journal append-only adjudication and link-only verdict
  consumption.
- 2026-08-27T19:59+02:00 — M42 clarification: separated stale in-review candidate replacement from
  unrelated post-acceptance movement and preserved the two legal invalidation triggers.
- 2026-08-27T18:06+02:00 — M41-M43: bound independent adjudication to an exact immutable attempt
  and candidate, added closed failure classes, and separated regression proof from owner-recorded
  bounded invalidation.
- 2026-08-27T14:04+02:00 — Tightened M39 adjudication to inspect the approved,
  version-addressed packet and its packet-local durable corpus ruling before evidence review.
- 2026-08-27T13:32+02:00 — M39@v1: independent adjudication now verifies the canonical packet and
  rejects missing, stale, or mismatched requirement revisions. Verification remains closeout-owned.

- 2026-08-27T12:43+02:00 — M38: replaced aggregate review description with independent per-ID
  adjudication, forcing rejection rules, delta preservation, and the separate durable-evidence
  hold point. Verification metadata stays pinned until governed closeout stamps the PDLS commit.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: aligned master-exit scope with the pre-landing candidate
  and made integration-branch repair routing fail closed to leaf-shaped work. Verification remains
  closeout-owned.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

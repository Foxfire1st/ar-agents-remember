# skills/l-01-agent-lifecycles/roles/reviewer.md

## Governing Overview

[overview.md](overview.md)
## Purpose

This is the canonical independent-review lifecycle. It inspects the exact candidate and adjudicates
each stable requirement ID from the same applicable set dispatched to the worker.

## Code Commentary

### Bound native review intake

Review only the owner’s explicit assignment. Use exact handover task arguments, the returned canonical `docPath`, `arMcpContext.readerArguments` and actual bound schemas; per-call context includes the canonical task and enclosure contract. Read only the documents required by the assigned seam and write only contained task-local report artifacts. Missing fields/capabilities are reported gaps, not permission to switch AR servers or retrieve unscoped material.

The baseline inspects every changed file in the complete candidate, including unattributed files. Knowledge before/after, family interactions and unchanged sibling realizations add a review dimension rather than reducing that population. Preserve producer Curator hand-off fields for co-resolution. Native peer clarification uses the actual parent/task role through bound `role_message`; a dashboard Reviewer needs no parent and starts no role. Developer decisions stay in the own chat.

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

**The declared knowledge effects (MIK-R11 rule 2, ruling Q3 of 2026-09-29T21:56:18+02:00).** Step 7 now
ends with one line: when the leaf's task document declares `expectedKnowledgeEffects`, the reviewer checks
that declaration against the leaf's requirement packet — its declared subjects and effects match what the
packet requires, with no effect missing and none invented — and a mismatch is a finding. The line sits in
the role file, not in a criteria catalog, because the catalogs admit a standing criterion only with
catching evidence. Who writes the declaration stays procedural; `task_doc` has no per-field role gate.

Beside the verdict, the reviewer emits **its own curator hand-off list** (`:103-113`) — its verdicts and
findings in the shape `../templates/curator-handoff-list.md` owns, as data rather than as verdict prose
for the curator to re-read. Each entry is one finding or one requirement adjudication, carrying the
source it came from and the place it was found at, and a finding the reviewer minted carries its own
stable ID; the list is what the curator ingests. It is emitted **in the same list shape the worker
emits**, because the curator consumes one contract: it names where the thing lives rather than where
the reviewer looked — the path and the construct inside it come from one resolution act — and carries
the reviewer's own statement and evidence verbatim rather than re-telling them.

If the manifestation candidate moves before adjudication, the stale attempt is rejected and a
successor is reviewed. An unrelated later candidate does not reopen an accepted attempt.

The role serves the assigned leaf/master/plan/super seams and the seam table still fixes the review candidate and verdict destination. Actual ownership comes from the explicit canonical assignment, rather than an inferred plane generation. For native clarification use the actual parent/task role through bound messaging; a dashboard Reviewer has no parent and needs none. The Reviewer starts no role.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization
outputs. Requirement adjudication and the durable-evidence stable-contract-or-expiry hold point
are independent mandatory concerns. Accepted attempts remain closed without one of the two
authorized invalidation paths.
One reviewer role serves leaf, master, plan and super seams under an explicit assignment. Developer decisions stay in the own chat, and peer clarification uses the actual parent/task role when one exists.


## CCR-R12@v5 Transaction Boundary

Current role duty remains targeted/scoped evidence with failed or unrun results visible, followed by the existing authorized paired Git transaction under its real contract. Requested independent review preserves the sealed monotonic finding set and three-round rule. The normal Curator authoring pass remains the standing full memory-quality/coherence exception; an explicitly report-only admission claims none of that normal pass complete. No finished turn or green check supplies semantic acceptance or Git publication.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The Reviewer delivers its verdict directly to the Worker and, on a pass, the exact freeze's identity to the Curator; a block and its repair stay inside the leaf and inside the ordinary limit. It opens and records its own ordinary code rounds through the supported operations, while the memory check keeps separate sealed reports, ids and a pass count, opens no code round and resets nothing. It answers a Curator code concern by taking it into its findings or explaining why it does not hold, and gains the harness-freedom paragraph.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

Worker envelope, reviewer verdict template, manager exact-set dispatch, and governing route overview.

- Every exact requirement attempt and candidate receives a separate independent accepted/rejected record. [1]
- The verdict template structurally repeats one adjudication block per stable ID. [2]
- The reviewer emits its own curator hand-off list in the shared producer shape. [3]
- A leaf's declared knowledge effects are checked against its packet; a mismatch is a finding (MIK-R11). [4]
- The seat's seam table fixes the five seams and where each verdict goes. [5]

### Cross-Repo References

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

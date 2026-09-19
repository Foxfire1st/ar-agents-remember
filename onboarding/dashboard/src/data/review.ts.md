# dashboard/src/data/review.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/review.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T18:05+02:00 |
| lastVerifiedCommitHash |  `c5a74a85af20a8fb48cc44f59de7e926d589d3fc`|
| lastVerifiedCommitDate |  2026-09-18T18:30:35+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l22` uncommitted source; base `2dcacb27446ecbaba01b69ee32e2ac40a1713b09` |
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

The browser-side, same-origin client for the read-only Intent Reviewer API
(`mcp/src/agents_remember/serving/review.py`). Its own header states the shape it mirrors and the
boundary it keeps: it mirrors `data/changeset.ts` — a `base` arg with a same-origin default, typed
results taken from the application models, a thrown `FilesApiError`, and **no store mutation** — and it
is a *read* client, because the surface exposes no submission control and so no function here writes
anything.

The header also states the one rule every type below obeys: **every type mirrors one model in
`models/knowledge/review.py`, and a field the server omits is absent here rather than defaulted**, so
an unresolved reference stays unresolved on the client too. That is why the optional members are
declared with `?` and never given a fallback value.

## Code Commentary

### Logic

**The module is one vocabulary of interfaces plus one request function; there is no store, no reducer
and no hook.** It declares two string-union types, twenty-one interfaces and one exported function.
The absence of state is the point: the review surface owns its own component state
(`ReviewSurface.tsx`), exactly as the change-set viewer owns its component state, so this module never
appears in `data/store.ts` and no `useDashboard` selector reads it.

**`ReviewSideState` and `ReviewSelectorKind` are the two client-side unions, and each mirrors a server
literal.** `ReviewSideState` is `"present" | "absent" | "binary" | "unresolved"`, mirroring the
`ReviewSideState` literal in the models module; `ReviewSelectorKind` is `"invariant" | "family"`,
mirroring `SELECTOR_KINDS` in the serving transport. Because the second is a union rather than a
`string`, a caller cannot pass an unadmitted selector kind without a type error, which is how the
server's `400 bad-request` for a third kind is kept out of the happy path on the client.

**`ReviewSideContent` carries `state`, an optional `text`, a `language` and a `detail`.** The
optionality is the whole rule: `text?: string` beside `state: ReviewSideState` means the diff renderer
is fed text only when the server said `present`, and an `absent`, `binary` or `unresolved` side arrives
with its own `detail` instead of an empty string. The client never manufactures the text it renders.

**`ReviewUnresolvedReference` is the client's own way of displaying "cannot be resolved".** It carries
`field`, an optional `recorded_reference` and a `detail`, and it appears inside five different
interfaces — the knowledge pane, the authored effect, the source pane, the evidence link and the
evidence pane — so an unresolved attribution is a rendered fact on every surface that can have one.

**The identity pair is `ReviewCandidateRef` and `ComparisonIdentity`.** `ReviewCandidateRef` carries
`repository_id`, `master`, `leaf_id` and an optional `task_ref` — task identities only, and no path,
which is the client half of the server's "a browser cannot choose which dataset is reviewed".
`ComparisonIdentity` carries `reference`, `policy_version`, the `binding_digest`, the
`selector_digest`, both snapshot digests and both optional code tree ids, so the surface renders the
comparison's identity rather than deriving one.

**The three panes are three interfaces whose fields are the panes' own statements.**
`ReviewKnowledgePane` carries `invariant_ids`, `family_ids`, the two `ReviewSideContent` statements,
the two condition lists, the `revision_groups`, the `field_changes`, the `authored_effects`, the
`signals`, the `assessments` and its own `unresolved` rows. `ReviewSourcePane` carries the `locations`,
the `remaining` counts, the optional `expansion_reference` and `expansion_command`, the attributed and
unattributed changed paths and its own `unresolved` rows. `ReviewEvidencePane` carries
`evidence_state`, `assessment_state`, the `evidence_links`, the `observations`, the `assessments`,
`source_inspection_available` and its own `unresolved` rows.

**The per-record interfaces each answer one question the panes print.**
`ReviewRevisionGroup` carries `side`, `record_id` and `selected_revision_count`, so the retained
revision count is kept per side. `ReviewFieldChange` carries `item_id`, `item_kind`, `field` and the
two optional values, where an absent value is the recorded fact. `ReviewSourceLocation` carries the
`claim_id`, the optional `invariant_revision_id`, the `path`, the optional `role` and `rationale`, the
recorded and observed source identities, the `resolution`, the three-member `change_state` and
`before_only`. `ReviewRemainingCount` carries `name`, an optional `value` and an optional `reason` —
`value?: number` beside `reason?: string` is exactly the server's rule that a quantity with no meaning
states why rather than reporting a zero.

**`ReviewStaleness` and `ReviewSubmission` are the two display values the surface's header block
prints.** `ReviewStaleness` carries `state` (`"current" | "stale"`), a `statement`, an optional
`previous_comparison_ref` and a `moved` list; `ReviewSubmission` carries `state`
(`"unavailable" | "disabled_stale"`), `reason`, `next_action`, `proposed_dispositions` and
`none_is_approval`. Neither union has a favourable member, so the client cannot render an absence as a
clearance.

**`ReviewPayload` and `ReviewResult` are the two response shapes.**
`ReviewPayload` carries `surface_version`, the `candidate`, the `comparison`, the three panes, the
`staleness`, the `submission` and a `limitations` list. `ReviewResult` carries `state`
(`"review" | "refused"`), `operation`, `repository_id` and the optional `payload`/`refusal` pair, and
`ReviewRefusal` carries `code`, `detail`, `next_action` and the optional `offending_input`, `expected`
and `observed`.

**`intentReview` is the module's one request and it never names a path.** It takes
`repo`, `master`, `leaf`, `selectorKind`, `selectorId` and a `base` defaulting to `""` (same-origin),
and returns `getJson<ReviewResult>` over `${base}/api/review/intent?${qs({...})}`. The two helpers come
from `data/files.ts` — `getJson` is what throws `FilesApiError` on a non-OK response, and `qs` is the
one query-string encoder the other clients use — so this client inherits the file API's error idiom
rather than growing a second one. The trailing comment states the omission that matters: it names
canonical task context and one recorded subject, and never a filesystem path, because the candidate is
resolved on the server and the browser must not be able to choose which dataset is reviewed.

### Conventions

The module imports exactly two helpers — `getJson` and `qs` from `./files` — and declares everything
else itself. Interfaces are exported and named with the `Review`/`Comparison` prefix so a reader can
tell a review display value from the change-set client's own types; the optional members use `?` with
no default, which is the client half of the server's `exclude_none=True`. There is no `default` export,
no class and no function other than `intentReview`, and the interfaces are declared in the order the
payload nests them, so the file reads top-down as the response shape.

### Invariants And Boundaries

- **Read-only, with no store mutation.** The module exports one `GET` and nothing else; the surface
  exposes no submission control, so no function here writes.
- **No path is accepted or sent.** The request names a task context and one recorded subject; the
  candidate is resolved server-side.
- **A field the server omits is absent rather than defaulted.** Every optional member is optional
  because the server may not send it, and no fallback value is provided.
- **Unresolved is displayed, not filled in.** `ReviewUnresolvedReference` appears wherever an
  attribution or a coverage statement can be missing.
- **Neither display union has a favourable member.** `ReviewSubmission.state` is `unavailable` or
  `disabled_stale`, and `ReviewStaleness.state` is `current` or `stale`; an absence cannot be read as a
  clearance.
- **The error idiom is the file API's.** A non-OK response throws `FilesApiError` through `getJson`
  rather than returning a sentinel.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header and its two
stated rules, the two unions and the interfaces that mirror the server's models, the one request
function, the two helpers it borrows from the file API, and the client that consumes it.

| Finding | Anchor | Source |
| --- | --- | --- |
| The header's own statement of what this file mirrors and the rule that a field the server omits is absent rather than defaulted. | `intentReview` | dashboard/src/data/review.ts:1-10; dashboard/src/data/review.ts:212-225 |
| The two client-side unions, each mirroring a server literal. | `ReviewSideState`; `ReviewSelectorKind` | dashboard/src/data/review.ts:12-13 |
| **The missing-side rule on the client: text is optional beside the state, so no empty string is manufactured.** | `ReviewSideContent` | dashboard/src/data/review.ts:15-20 |
| The shared shape that makes an unresolved reference a displayed fact on every surface that can have one. | `ReviewUnresolvedReference` | dashboard/src/data/review.ts:22-26 |
| The candidate reference, which carries task identities and no path, and the comparison identity carried rather than derived. | `ReviewCandidateRef`; `ComparisonIdentity` | dashboard/src/data/review.ts:28-44 |
| The per-side revision count and the field transition whose absent value is the recorded fact. | `ReviewRevisionGroup`; `ReviewFieldChange` | dashboard/src/data/review.ts:46-58 |
| The authored record with its examined inputs, and the detection fact with its versions and scope limitations and no severity. | `ReviewAuthoredEffect`; `ReviewSignal` | dashboard/src/data/review.ts:60-80 |
| The assessment display with its author, examined inputs, binding state and evidence refs. | `ReviewAssessmentDisplay` | dashboard/src/data/review.ts:82-92 |
| The three panes, each carrying its own `unresolved` rows. | `ReviewKnowledgePane`; `ReviewSourcePane`; `ReviewEvidencePane` | dashboard/src/data/review.ts:94-107; dashboard/src/data/review.ts:129-137; dashboard/src/data/review.ts:158-166 |
| The selected source location with its optional role and its three-member change state. | `ReviewSourceLocation` | dashboard/src/data/review.ts:109-121 |
| **The count shape whose optional value beside its optional reason is the server's "states why rather than reporting a zero".** | `ReviewRemainingCount` | dashboard/src/data/review.ts:123-127 |
| The evidence claim reference and the observation displayed exactly. | `ReviewEvidenceLink`; `ReviewObservation` | dashboard/src/data/review.ts:139-156 |
| **The two display unions with no favourable member.** | `ReviewStaleness`; `ReviewSubmission` | dashboard/src/data/review.ts:168-181 |
| The whole payload and the two response shapes. | `ReviewPayload`; `ReviewRefusal`; `ReviewResult` | dashboard/src/data/review.ts:183-210 |
| **The one request: a task context, one recorded subject and a same-origin default, with no path.** | `intentReview` | dashboard/src/data/review.ts:215-225 |
| The two helpers this client borrows rather than re-implementing: the thrower and the query encoder. | `getJson`; `qs`; `FilesApiError` | dashboard/src/data/files.ts:76-98; dashboard/src/data/files.ts:99-101 |
| The sibling client whose shape this file mirrors, including its own no-store-mutation comment. | `taskChangeset` | dashboard/src/data/changeset.ts:1-8; dashboard/src/data/changeset.ts:56-58 |
| The surface that consumes this client. | `intentReview` | dashboard/src/panels/review/ReviewSurface.tsx:21-22; dashboard/src/panels/review/ReviewSurface.tsx:351-367 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The client talks to its own origin and names
one repository namespace in the query string.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's browser client. It records the two rules the file's own header states — every type mirrors one model in `models/knowledge/review.py`, and **a field the server omits is absent here rather than defaulted**, so an unresolved reference stays unresolved on the client — plus the two boundaries a reader needs: it is a *read* client with **no store mutation** (it is not in `data/store.ts`, and the surface owns its own component state), and the one request names a task context and one recorded subject and **never a filesystem path**, because the candidate is resolved server-side. It also records that the two display unions (`ReviewStaleness`, `ReviewSubmission`) have no favourable member, so an absence cannot be rendered as a clearance. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.

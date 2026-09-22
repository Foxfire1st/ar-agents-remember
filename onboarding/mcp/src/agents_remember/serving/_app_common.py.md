# mcp/src/agents_remember/serving/_app_common.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_common.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-21T22:40:00+02:00 |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Defines shared serving request/composition models and helper seams used by the split FastAPI route
modules.

## Code Commentary

### Logic

`TerminalAttachTaskRequest` accepts the canonical task-document reference and role used by the
assignment route. Shared runtime/collaborator records keep topology, catalog, host, projection, and
cache dependencies explicit for route handlers. `_ServingRuntime` is the one collaborator bundle the
lifespan and the read routes share, so a fact written by one half and served by the other cannot land
on two different objects: since `LOCR-R17@v1` it carries `observer_health`
(`TerminalObserverHealthPublisher`) on the same observer root and the same serving clock as the
liveness sweeper. `stream_events` takes the observer-health payload as an optional keyword and passes
it into `served_state_tail`, so the SSE `snapshot` carries `terminalObserverHealth` beside the
heartbeat while a `delta` — one projection node, not a state body — carries no tail at all.

Since `260915-CAPS-L15` the collaborator bundle also carries `capsule_launch`
(`LaunchCapsuleResolver | None`), the application-tier capsule compiler injected by the composition
root. `serving` ranks below `application` in `layers.toml`, so the dashboard's launch route cannot
import the compiler; it takes this port exactly as it takes the execution-evidence registrars above, and
a process that omits it **refuses** a role-configured launch by name
(`capsule-resolver-unavailable`) rather than starting a seat with no instructions. The port is
declared on both `ServingCollaborators` and `_ServingRuntime`, and `serving/app.py` copies it from the
first onto the second.

### Conventions

Wire parsing belongs here; structural qualification and mutation delegate to owned services. The
serve-time tail arguments are optional keywords, and absence is a valid served answer rather than an
error: a caller with no build stamp, no heartbeat reader, or no observer-health source still produces
a valid body.

### Invariants And Boundaries

- No leaf-key attach request or compatibility parser remains.
- Request identity is task document plus role.
- Runtime collaborators are server-resolved, not browser-provided authority.
- **The capsule compiler crosses a port, never an import.** `ServingCollaborators.capsule_launch` is
  the only way this rank reaches `application`; it is optional in the record and fail-closed in
  behaviour (an absent resolver refuses a role-configured launch instead of silently running legacy).
- **The served surfaces hold no capsule content.** The port returns the decision and the carriers; the
  route publishes only the compact per-run record, so no instruction prose enters the served state.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Terminal assignment parses canonical document and role. | `TerminalAttachTaskRequest` | mcp/src/agents_remember/serving/_app_common.py:308-312 |
| The one collaborator bundle the lifespan and the routes share, including the observer-health owner added by `LOCR-R17@v1`. | `_ServingRuntime` | mcp/src/agents_remember/serving/_app_common.py:505-538 |
| The SSE event sequence: one additive, omissive tail on the `snapshot` and none on a `delta`. | `stream_events` | mcp/src/agents_remember/serving/_app_common.py:128-168 |
| The application-rank capsule compiler as an injected port, absent means a named refusal rather than a capsule-less launch. | `capsule_launch`; `LaunchCapsuleResolver` | mcp/src/agents_remember/serving/_app_common.py:491-499; mcp/src/agents_remember/serving/_app_common.py:532-532; mcp/src/agents_remember/serving/launch_capsule.py:162-163 |
| **The third review port: one inventory entry's content at the two code trees the listing published, imported beside the other two reviewer ports and refused by name when a process omits it.** | `ReviewSourceContentPort`; `review_source_content` | mcp/src/agents_remember/serving/_app_common.py:36-40; mcp/src/agents_remember/serving/_app_common.py:481-489; mcp/src/agents_remember/serving/review.py:83-83 |
| The composition root that fills the port with the real compiler. | `serving_collaborators` | mcp/src/agents_remember/cli/dashboard.py:67-127 |
| The refusals the port's presence decides, in the one gate every launch point calls. | `resolve_launch_capsule`; `capsule-resolver-unavailable` | mcp/src/agents_remember/serving/launch_capsule.py:275-314 |

## 260921-ICR-L3 The Third Review Port On The Collaborator Record

`ServingCollaborators` now carries a **third** reviewer field, and the reason it is a field of its own
rather than one more member of the review payload is stated in the field's own docstring: the inventory
is the whole task's change set, and the route that opens one entry reads two Git objects the payload
never carried. A payload that carried every file's text would be a document dump, so the browser asks
for exactly the row a reader opened, and this record is where the callable that answers it crosses from
`application` into `serving`.

- `review_source_content: ReviewSourceContentPort | None = None` — one inventory entry, named by the
  generation the listing published, in; that entry's content at its two bound code trees out.

The field is imported beside its two siblings from `agents_remember.serving.review`, which is the same
grouped import the two reviewer ports already arrive through. The refusal it decides is the sharp half:
an omitted port means **"this process cannot read the entry"**, which is a different fact from **"this
entry has no content"** — and a browser served an empty file for the second would be reading a document
this repository does not hold. So the missing-port answer is a named refusal, never an empty body.

The three review ports are now one shape of decision recorded three times: production wires all of them
in `agents_remember.cli.dashboard`, and each one's absence refuses its own route by name rather than
serving an empty surface. The new field sits between `knowledge_review_entries` and `capsule_launch` on
the record, which is the order the dataclass now declares.

## 260915-KS-L45 The Reviewer Entry Port Beside The Reviewer Port

**The count in this section is superseded: the record carries three reviewer fields since
260921-ICR-L3** (see the section above). The layering reason, the two ports' own docstrings and the
wiring site it records are still exactly right, so the entry is retained rather than rewritten.

`ServingCollaborators` now carries **two** reviewer fields, and they are one port beside the other
rather than one port with a mode:

- `knowledge_review: KnowledgeReviewPort | None = None` — the comparison: one typed
  `ReviewSurfaceRequest` in, one `KnowledgeReviewResult` out.
- `knowledge_review_entries: KnowledgeReviewEntriesPort | None = None` — the entry half: the task
  context alone (`repository_id`, `master`, `leaf_id`) in, one `ReviewEntryListResult` out.

Both are imported from `agents_remember.serving.review` beside the other serving ports, and each
one's own docstring carries the reason the field exists at all: `serving` ranks below `application`
in `layers.toml`, so the reviewer routes cannot import the read/diff/view operations the adapter
composes and take ports instead, exactly as the launch route takes the capsule compiler. All three
are the same shape of decision recorded more than once — production wires them all in
`agents_remember.cli.dashboard`, and a process that omits one refuses that route **by name** rather
than serving an empty surface, because an empty pane and an unreachable adapter are different facts
and only one of them is true.

The entry port's own reason is the sharper of the two, and the field's docstring states it: the
entry route is the only one a task view can call *before it knows a subject*, and answering an
unwired process with an empty entry list would say "nothing is reviewable here" — a different fact
from "this process cannot answer". So the entry route's missing-port answer is a `503` naming the
missing adapter, never an empty list. The two fields sit above `capsule_launch` on the record, which
is the order the dataclass now declares.

## 260915-KS-L22 The Reviewer Port On The Collaborator Record

`ServingCollaborators` gained the first of those two fields in the L22 increment. The section above
supersedes its count; this entry is retained because the layering reason and the wiring site it
recorded are still exactly right. It reads: the class gains one field,
`knowledge_review: KnowledgeReviewPort | None = None`, imported from
`agents_remember.serving.review` beside the other serving ports, and a process that omits it refuses
the review route by name rather than serving an empty surface — because an empty pane and an
unreachable adapter are different facts and only one of them is true. The field sits above
`capsule_launch` on the record, which is the order the dataclass declares.

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260821-CLIVE Execution-Evidence Collaborators

`ServingCollaborators` now exposes explicit terminal-catalog and operator-inbox execution-evidence
registrars. `_ServingRuntime` retains the inbox registrar for notifier sweeps. These injected seams
let the serving process register task-bound worker/reviewer/curator first evidence before routine
retention can erase the only execution row; absence of a registrar is fail-closed for deletion.

## Update History
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the collaborator record gained the third review port, and the section that counted two was superseded in place rather than left contradicting the source.** `ServingCollaborators.review_source_content: ReviewSourceContentPort | None = None` carries the callable that opens one listed inventory entry at the two code trees the listing published; it is imported beside `KnowledgeReviewPort` and `KnowledgeReviewEntriesPort` in one grouped import from `agents_remember.serving.review`. The new section records the field's own stated reason for being a third port rather than a field on the review payload (the inventory is the whole task's change set, and the route that opens one entry reads two Git objects the payload never carried) and the distinction the missing-port answer preserves: "this process cannot read the entry" is not "this entry has no content", so an omitted port refuses by name instead of serving an empty file. The L45 section's "carries **two** reviewer fields" is now flagged as superseded by the section above it, keeping its layering reason and wiring site intact — the same in-place idiom the L22 section already uses. **Citation accounting:** every row into this source was re-read against the candidate and re-derived from the construct's real extent, because this leaf's +16-line insertion moved everything below it. `TerminalAttachTaskRequest` `300-304` → `308-312`; `_ServingRuntime` `481-514` → `505-538`; `stream_events` `120-157` → `128-168`; the compiler-port row's dotted anchors (`ServingCollaborators.capsule_launch`; `_ServingRuntime.capsule_launch`), which no line can literally hold, became the real identifiers `capsule_launch`; `LaunchCapsuleResolver` over `491-499`; `532-532`; `launch_capsule.py:162-163`; `serving_collaborators` `dashboard.py:67-83` → `67-127`. One row was added for the new port, and no claim wording was changed except the L45 count, which was **false** at this candidate. No verification stamp was advanced, because no commit contains this body. **Stamp accounting:** the two verification rows now name the **production line this card was read against** — `d80a0513…`, the master line at this leaf's base, committed `2026-09-21T19:51:20+02:00` — rather than the older commit they carried before, because this card's body was read against that line and this leaf's uncommitted change set on top of it; they do not claim that a commit contains this leaf's bytes, and the governed closeout owns the real stamp once the code commit exists.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **the collaborator record gained the reviewer's entry port beside its comparison port.** `ServingCollaborators.knowledge_review_entries: KnowledgeReviewEntriesPort | None = None` carries the callable that answers the entry route — the task context alone in, one `ReviewEntryListResult` out — and `_app_common.py` is where it crosses from `application` into `serving`. The new section states why the entry port is separate rather than a mode of the first: the entry route is the only one a task view can call before it knows a subject, and answering an unwired process with an empty list would say "nothing is reviewable here", a different fact from "this process cannot answer", so the missing-port answer must be a named refusal. That makes three ports on this record of one shape, so a reader comparing them gets the layering rule rather than three unrelated defaults. The L22 section it supersedes is retained with its count corrected in place. No reference row was touched by hand; ranges into this source were re-derived by the mechanical projection. No verification stamp was advanced, because no commit contains this body.
- 2026-09-18T16:13:35+00:00: Generated citation repair: `_ServingRuntime` repointed to mcp/src/agents_remember/serving/_app_common.py:481-514. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T10:25+02:00 — 260915-CAPS-L15 curator: **the shared bundle gained the capsule-compiler
  port.** `ServingCollaborators.capsule_launch` and `_ServingRuntime.capsule_launch` carry the
  application-tier compiler into the serving rank, which may not import it; `serving/app.py` copies the
  collaborator onto the runtime. The body records the boundary and its fail-closed half: an absent
  resolver makes the gate refuse a role-configured launch by name rather than run it capsule-less.
  Two invariants and three reference rows added. Verification metadata moves to this leaf's base
  `15fa0e2c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code
  commit and no hash or fingerprint was invented here.

- 2026-09-15T20:42+02:00 — 260831-LOCR-L17 curator (uncommitted change set on `ar/260831-locr-l17`,
  base `99534dc5`, `_app_common.py` +19/−2): the shared runtime bundle and the SSE assembly gained
  the observer-health seam, so the body was corrected in place. `_ServingRuntime` now carries a
  required `observer_health` (`TerminalObserverHealthPublisher`) built on the same observer root and
  serving clock as the liveness sweeper — the lifespan PUBLISHES this serving lifetime's accumulator
  through it and the read routes resolve the persisted row through it, so the two halves of
  `LOCR-R17@v1` cannot drift onto different lifetimes or files. `stream_events` gained the matching
  optional keyword and passes it into `served_state_tail`, so the `snapshot` carries
  `terminalObserverHealth` while a `delta` (one projection node, not a state body) carries no tail.
  Recorded that these tail arguments are optional keywords whose absence is a valid served answer.
  Reference ranges re-derived against the candidate (`TerminalAttachTaskRequest` `286-291` →
  `300-304`) with two new rows. Verification metadata remains closeout-owned; no stamp advanced.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented the two task-execution registration collaborators. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_app_common.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **recorded the reviewer port on `ServingCollaborators`.** The frozen collaborator record
gained `knowledge_review: KnowledgeReviewPort | None = None`, imported from
`agents_remember.serving.review`, with the docstring stating why the port exists (`serving` ranks
below `application` in `layers.toml`, so the reviewer route cannot import the operations the adapter
composes), where production wires it (`agents_remember.cli.dashboard`) and what an omitted port
decides (the route refuses by name rather than serving an empty surface). The new section above
states that as the card's own reading, including the fact that the field and the pre-existing
`capsule_launch` port are the same shape of decision recorded twice — a reader comparing them gets
the layering rule rather than two unrelated defaults. No reference row was touched; the card's
ranges into this source are left as they stand for the citation-reprojection engine. The metadata
block above names this leaf's uncommitted candidate as what was read, and the two verification
stamps are left exactly as the last real verification set them. The body was changed substantively
and this entry is the history record, not a metadata-only refresh.

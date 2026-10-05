# mcp/src/agents_remember/serving/_app_common.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Defines shared serving request/composition models and helper seams used by the split FastAPI route
modules.

Declares shared serving request and collaborator seams without importing application-tier owners.

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

Since `260921-ICR-L47`, `ServingCollaborators` also declares `review_intent_summary:
ReviewIntentSummaryPort | None = None` — the same adapter's changed-intent summary, a fourth port because it
answers a fourth question from the same resolution without loading the subject catalogue. Omitting it makes
the summary route refuse by name (503), because "this process cannot count" is not "nothing changed".

- The optional summary port on the collaborator record. [1]

Since `260928-MIK-L25`, `ServingCollaborators` also declares `review_trees: ReviewTreesPort | None = None` — the
same adapter's tree view: the four Git trees, the Git diff of the memory trees, the per-side currentness and the
worklist view of a converted leaf. It is a fifth port because it answers what the dataset review cannot; omitting it
refuses `GET /api/review/trees` by name (503).

- The optional tree-view port on the collaborator record. [2]

Since `260928-MIK-L29`, `ServingCollaborators` also declares `knowledge_reader: KnowledgeReaderPort | None = None`,
the path-based knowledge reader (MIK-R29): read-only views of any converted memory tree. It is **not** a sixth review
port: the reader needs no task, so it is its own port rather than a mode of the review adapter. The port type is
imported from the route module `serving/knowledge_reader.py`, which keeps the serving tier free of the application;
the composition root supplies the callable, and omitting it refuses `GET /api/knowledge/reader/{view}` by name
(503).

- The optional reader port on the collaborator record, and why it is its own port. [3]
- The port type, imported from the route module. [4]

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

### Role Runtime and Scope

ServingCollaborators adds optional extra_api_routes callable owned by the composition root, registered before final static mount. This permits CLI/application adapters above serving to install launch routes while retaining the existing capsule/knowledge/reviewer collaborator ports and layer boundary.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Terminal assignment parses canonical document and role. [5]
- The one collaborator bundle the lifespan and the routes share, including the observer-health owner added by `LOCR-R17@v1`. [6]
- The SSE event sequence: one additive, omissive tail on the `snapshot` and none on a `delta`. [7]
- The application-rank capsule compiler as an injected port, absent means a named refusal rather than a capsule-less launch. [8]
- **The third review port: one inventory entry's content at the two code trees the listing published, imported beside the other two reviewer ports and refused by name when a process omits it.** [9]
- The composition root that fills the port with the real compiler. [10]
- The refusals the port's presence decides, in the one gate every launch point calls. [11]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

### Runtime Source References

- Frozen implementation of ServingCollaborators supporting the stated file behavior. [12]

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

## 260821-CLIVE Execution-Evidence Collaborators

`ServingCollaborators` now exposes explicit terminal-catalog and operator-inbox execution-evidence
registrars. `_ServingRuntime` retains the inbox registrar for notifier sweeps. These injected seams
let the serving process register task-bound worker/reviewer/curator first evidence before routine
retention can erase the only execution row; absence of a registrar is fail-closed for deletion.

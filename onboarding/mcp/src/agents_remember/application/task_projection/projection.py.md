# mcp/src/agents_remember/application/task_projection/projection.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_projection/projection.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[application overview](../overview.md)

## Purpose

Assemble one focused task projection from the documents the read plan selected. This is the largest
module in the package (543 lines) and the only place where the planes are populated.

## Code Commentary

### Logic

`project_task_context` is a thin public entry point over `_Builder`, one projection's assembly from
the planned documents to the frozen value. Three rules shape the assembly:

1. **Only the planned documents are read.** The builder takes `read_documents(scope, plan)` as
   given and never widens it.
2. **Only the bound document's own decisions are injected.** An ancestor's decision log travels as
   an `ExpansionReference` carrying its entry count, so a leaf projection cannot grow into the
   series' history.
3. **Nothing is truncated.** Every obligation, negative constraint and failure obligation is carried
   verbatim from the packet that declares it; material deliberately not injected is named as
   referenced instead.

The build order matters and is deliberate: the projection is assembled first with empty `markdown`
and `projection_revision`, then `projection_revision(draft)` is computed over the selection and
facts, and only then is `render_markdown(identified)` produced. The rendered document therefore
carries its own identity, and the revision is never a function of its own output.

The requirement plane is where the two admissible routes meet. `_owned` looks for a declaration
matching an owned requirement identity: a typed `approved-requirement-packet` declaration goes
through `_from_declaration` (owner-verified, needs no consumer input — **the standardized policy
route**), and otherwise `_from_location` requires an admitted `RequirementPacketLocation` or raises
`projection-requirement-packet-unresolved`. `_requirements` then adds every non-owned declaration
through `adjacent`, so dependency and preservation context appears without being claimed.

Fact planes and their kinds:

| Plane | Kind | Source |
| --- | --- | --- |
| `acceptance` | `current` from an owned packet's expected-evidence section; `proposal` from an acceptance-obligation question | packet, task document |
| `preservation` | `current` — the packet's preservation, exclusions and failure sections, **verbatim**, each labelled with its packet identity and heading | owned packets |
| `decisions` | `current` — the bound document's own decision log only | bound document |
| `portfolio` | `current` — sub-task rows, commanded masters, seats, execution-graph waves, integration branch | bound document, only when the plan admits portfolio facts |
| `series` | `current` — the bound task's own row in its parent's series index | parent document |
| `evidence` | `historical` — step/substep progress, review round, discarded slices, execution registrations | bound document |
| `knowledge` | mixed | the optional knowledge expansion source |

`_evidence` is the plane that keeps historical material labelled as such, and `_writable_scope`
reports where the seat may write and which actions were admitted — it grants nothing, because both
halves come from the enclosure contract and the admitted tool-policy snapshot.

`_knowledge` **reports the channel as unadmitted** when no source is supplied, appending a gap
instead of omitting the channel silently. `_gaps` additionally surfaces the memory gap and a bound
document with no objective.

### Invariants And Boundaries

- **The projection has no writer.** It cannot set a status, raise a gate, create an approval, write
  memory or publish a second task database. `test_the_projection_modules_import_no_writer_transport_or_task_json_reader`
  asserts the import surface, and `test_a_refused_and_a_successful_projection_leave_the_task_tree_byte_identical`
  asserts the observable consequence.
- **An owned obligation is never dropped.** `_from_location` raises rather than projecting a seat
  with a missing obligation.
- Preservation sections are carried **verbatim**, each labelled with its packet identity and
  section heading. Do not add a summarising or clipping step.
- Only the bound document's own decisions are injected. Do not extend this to ancestors — reference
  them with their entry count instead.
- `projection_revision` must be computed before `render_markdown`, never after.
- A gap is visible. Anything the projection could not admit is appended to `_gaps` rather than
  silently omitted.

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The assembly entry point, the two requirement routes, and the cases that hold the invariants.

| Finding | Anchor | Source |
| --- | --- | --- |
| The public assembly entry point for one admitted binding. | `project_task_context` | mcp/src/agents_remember/application/task_projection/projection.py:75-87 |
| The assembler that reads only the planned documents and never widens the read set. | `_Builder` | mcp/src/agents_remember/application/task_projection/projection.py:90-515 |
| The owned-requirement resolution: typed declaration first, admitted location otherwise. | `_requirements`; `_owned`; `_from_declaration`; `_from_location` | mcp/src/agents_remember/application/task_projection/projection.py:192-203; mcp/src/agents_remember/application/task_projection/projection.py:205-213; mcp/src/agents_remember/application/task_projection/projection.py:215-227; mcp/src/agents_remember/application/task_projection/projection.py:229-258 |
| The preservation plane: the three roles carried verbatim as current facts, and the gap when no packet was admitted. | `_preservation`; `_PRESERVATION_ROLES` | mcp/src/agents_remember/application/task_projection/projection.py:299-322; mcp/src/agents_remember/application/task_projection/projection.py:68-72 |
| The portfolio plane, including execution-graph waves, behind the plan's portfolio admission. | `_portfolio`; `_graph_facts` | mcp/src/agents_remember/application/task_projection/projection.py:386-411; mcp/src/agents_remember/application/task_projection/projection.py:413-426 |
| The historical plane: progress, review round, discarded slices, registrations. | `_evidence` | mcp/src/agents_remember/application/task_projection/projection.py:445-490 |
| The knowledge seam that reports its channel unadmitted rather than omitting it, and the gap list. | `_knowledge`; `_gaps` | mcp/src/agents_remember/application/task_projection/projection.py:492-505; mcp/src/agents_remember/application/task_projection/projection.py:507-515 |
| The two requirements routes the projection admits, and the refusal when neither applies. | `TaskProjectionRequest`; `RequirementPacketLocation` | mcp/src/agents_remember/application/task_projection/types.py:289-299; mcp/src/agents_remember/application/task_projection/types.py:137-152 |
| The case that proves two leaves never leak each other's private task content. | `test_two_leaves_project_their_own_scope_without_leaking_the_other` | mcp/tests/test_task_projection.py:662-708 |
| The case that proves the three fact planes stay distinguishable. | `test_the_projected_planes_keep_their_kinds_and_carry_every_obligation_verbatim` | mcp/tests/test_task_projection.py:1152-1209 |
| The case that proves a refused and a successful projection leave the task tree byte-identical. | `test_a_refused_and_a_successful_projection_leave_the_task_tree_byte_identical` | mcp/tests/test_task_projection.py:1079-1096 |

## Cross-Repo References

No sibling-repository contract consumes this assembler.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_two_leaves_project_their_own_scope_without_leaking_the_other` repointed to mcp/tests/test_task_projection.py:662-708. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_a_refused_and_a_successful_projection_leave_the_task_tree_byte_identical` repointed to mcp/tests/test_task_projection.py:1079-1096. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the projection assembler
  added by the scoped-task-context leaf (`CAPS-R03@v1`). Records the three assembly rules, the
  deliberate build order that keeps the revision independent of the rendered bytes, the two
  requirement routes with the typed one as the standardized policy, the per-plane fact-kind table,
  and the never-writes invariant with its two holding cases. This module was extracted down to 543
  lines by `CAPS-L3-EV11` (identity and declarations moved to their own modules); a reader looking
  for `projection_revision` or the declaration reader should look in `revision.py` and
  `declarations.py` instead. Verification metadata is left at the leaf base commit because the source
  is uncommitted — the governed closeout stamps the real code commit.

# mcp/src/agents_remember/application/task_projection/projection.py

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

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The assembly entry point, the two requirement routes, and the cases that hold the invariants.

- The public assembly entry point for one admitted binding. [1]
- The assembler that reads only the planned documents and never widens the read set. [2]
- The owned-requirement resolution: typed declaration first, admitted location otherwise. [3]
- The preservation plane: the three roles carried verbatim as current facts, and the gap when no packet was admitted. [4]
- The portfolio plane, including execution-graph waves, behind the plan's portfolio admission. [5]
- The historical plane: progress, review round, discarded slices, registrations. [6]
- The knowledge seam that reports its channel unadmitted rather than omitting it, and the gap list. [7]
- The two requirements routes the projection admits, and the refusal when neither applies. [8]
- The case that proves two leaves never leak each other's private task content. [9]
- The case that proves the three fact planes stay distinguishable. [10]
- The case that proves a refused and a successful projection leave the task tree byte-identical. [11]

### Cross-Repo References

No sibling-repository contract consumes this assembler.

No meaningful cross-repo references found.

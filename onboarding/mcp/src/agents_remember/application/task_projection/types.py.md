# mcp/src/agents_remember/application/task_projection/types.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The frozen value types of one task-context projection: what a seat may read, what it was selected
to carry, and the facts and gaps that result. Every type here is a plain frozen dataclass or a
`Literal`; nothing opens a file, reaches the network or calls a model.

## Code Commentary

### Logic

`ProjectionFactKind` is the **three-plane** vocabulary — `current`, `historical`, `proposal` — and
`ProjectionChannel` is the nine-channel vocabulary an operation selects from. Both are `Literal`
aliases with runtime tuples (`PROJECTION_FACT_KINDS`), because a PEP 695 alias does not answer
`get_args`; keep the two spellings in step, and note that the same deliberate duplication exists in
`models/role_capsules/vocabulary.py` for the same reason.

`ProjectionReadPlan` is the inspectable answer to "what may this seat read, and how much": the
altitudes it reads, whether portfolio facts are in scope, and the exact channel set. It is a value,
so a consumer can print it and a test can pin it — there is no "read everything, filter later" step
anywhere behind it.

`RequirementProjection.declaration` distinguishes the three admissible declaration shapes
(`approved-packet`, `exact-text`, `admitted-location`), and `identity` is `None` for a declaration
the task document writes as exact text: prose does not opt itself into a version-addressed identity,
so the projection reports the text rather than inventing one. `RequirementPacketLocation` is the
consumer-supplied locator that exists **only** for that exact-text case.

`TaskKnowledgeExpansionSource` is the recorded typed seam for later knowledge retrieval. No
implementation ships in this package and nothing here depends on the Knowledge Substrate master; a
projection without a source reports the channel as unadmitted.

`TaskProjection` is the complete value: the model-visible `markdown` plus the inspectable half
(binding, selection, every fact plane, `knowledge`, `expansion`, `gaps`, `projection_revision`).
The split is deliberate — identity and provenance diagnostics do not belong in the prose a model
reads, and a model that can see a raw audit trail will treat it as instructions.

### Layer placement

`layers.toml` ranks `tasks` (9) below `application` (21), and this package's whole job is to read
task truth *through* those owners. Every value therefore sits beside its consumer in `application`:
hoisting the pure types into `models` (rank 2) would force a second declaration of
`TaskAltitude` — a rank-2 package may not import the rank-9 package that owns that vocabulary — and
two spellings of one task vocabulary is exactly the drift the single-source rule forbids. The types
stay at the lowest rank that can carry their real dependency.

### Conventions

Every type is `@dataclass(frozen=True, slots=True)`. A new projected plane is a new `TaskProjection`
field plus a renderer, not a widening of `ProjectedFact`.

### Invariants And Boundaries

- **A fact always carries its plane.** A `ProjectedFact` without a `kind` cannot express "this is a
  proposal, not an obligation", and a historical record read as a current obligation is the defect
  the three-plane split exists to prevent.
- `PacketSection.body` is the packet's bytes, verbatim. Re-flowing, summarising or clipping a
  required behaviour, a negative constraint or a failure obligation is forbidden — there is no
  length budget anywhere in this package.
- `ExpansionReference` is *instead of* material, never a truncation of it. A long optional history
  is referenced, not shortened.
- `ProjectionSelection.plan` and `read_documents`/`referenced_documents` are what make "the read
  plan is the requirement" inspectable rather than claimed.
- `ProjectionFactKind`, `ProjectionChannel` and their runtime tuples must not diverge.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The vocabularies this module declares and the owners whose types they must stay in step with.

- The three fact planes and the runtime tuple that must agree with the alias. [1]
- The read plan a consumer can print and a test can pin. [2]
- The three admissible requirement declaration shapes, and the `None` identity an exact-text declaration gets. [3]
- The recorded, optional knowledge seam and its request value. [4]
- The complete projection value: model-visible markdown plus the inspectable half. [5]
- The relation vocabulary this module imports rather than retypes. [6]
- The task-altitude vocabulary owned by the task layer, which is why the types live at this rank. [7]
- The duplicate-declaration guard for a PEP 695 alias beside its runtime tuple. [8]

### Cross-Repo References

No sibling-repository contract consumes these values.

No meaningful cross-repo references found.

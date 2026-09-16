# mcp/src/agents_remember/application/task_projection/types.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_projection/types.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T10:30+02:00 |
| lastVerifiedCommitHash | `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| lastVerifiedCommitDate | 2026-09-16T10:52:30+02:00|
| governingOverview      | `../overview.md`                           |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking the configured sources. | N/A | N/A |

## Repo-Internal References

The vocabularies this module declares and the owners whose types they must stay in step with.

| Finding | Anchor | Source |
| --- | --- | --- |
| The three fact planes and the runtime tuple that must agree with the alias. | `ProjectionFactKind`; `PROJECTION_FACT_KINDS` | mcp/src/agents_remember/application/task_projection/types.py:39-41 |
| The read plan a consumer can print and a test can pin. | `ProjectionReadPlan`; `ProjectionSelection` | mcp/src/agents_remember/application/task_projection/types.py:221-234; mcp/src/agents_remember/application/task_projection/types.py:238-247 |
| The three admissible requirement declaration shapes, and the `None` identity an exact-text declaration gets. | `RequirementProjection`; `RequirementPacketLocation` | mcp/src/agents_remember/application/task_projection/types.py:156-172; mcp/src/agents_remember/application/task_projection/types.py:137-152 |
| The recorded, optional knowledge seam and its request value. | `TaskKnowledgeExpansionSource`; `KnowledgeExpansionRequest`; `KnowledgeExpansion` | mcp/src/agents_remember/application/task_projection/types.py:275-285; mcp/src/agents_remember/application/task_projection/types.py:251-262; mcp/src/agents_remember/application/task_projection/types.py:266-271 |
| The complete projection value: model-visible markdown plus the inspectable half. | `TaskProjection` | mcp/src/agents_remember/application/task_projection/types.py:303-329 |
| The relation vocabulary this module imports rather than retypes. | `CapsuleOperation`; `CapsuleRole` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:33-62; mcp/src/agents_remember/models/role_capsules/vocabulary.py:20-31 |
| The task-altitude vocabulary owned by the task layer, which is why the types live at this rank. | `TaskAltitude` | mcp/src/agents_remember/tasks/document_refs.py:32-32 |
| The duplicate-declaration guard for a PEP 695 alias beside its runtime tuple. | `test_the_role_and_operation_literals_agree_with_their_runtime_tuples` | mcp/tests/test_role_capsule_admission.py:153-157 |

## Cross-Repo References

No sibling-repository contract consumes these values.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History

- 2026-09-16T10:30+02:00 — 260915-CAPS-L3 curator: created this card for the value layer of the
  task-context projection added by the scoped-task-context leaf (`CAPS-R03@v1`). Records the
  three-plane and nine-channel vocabularies with their runtime-tuple duplication, the read plan as
  inspectable data, the three declaration shapes, the optional knowledge seam, and the
  `layers.toml` reason the pure types live in `application` rather than `models`. Verification
  metadata is left at the leaf base commit because the source is uncommitted — the governed closeout
  stamps the real code commit.

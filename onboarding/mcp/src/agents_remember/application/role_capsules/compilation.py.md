# mcp/src/agents_remember/application/role_capsules/compilation.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/role_capsules/compilation.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[application overview](../overview.md)

## Purpose

The admitted compile entry point: one call for a consumer that has an admitted binding and a
canonical source tree — read the explicitly named source set, hand it to the pure compiler, and
return **either** the capsule **or** the refusal *with* its explanation projection.

## Code Commentary

### Logic

cit:([`compile_admitted_capsule`], mcp/src/agents_remember/application/role_capsules/compilation.py:89-122) is the whole surface. It admits via
cit:([`admit_capsule_sources`], mcp/src/agents_remember/application/role_capsules/sources.py:78-94), extracts the manifest bytes from the admitted set,
parses them opportunistically, calls cit:([`compile_role_capsule`], mcp/src/agents_remember/models/role_capsules/compiler.py:84-140), and converts a typed refusal into an
outcome rather than letting it escape.

cit:([`CapsuleCompilationOutcome`], mcp/src/agents_remember/application/role_capsules/compilation.py:46-88) is **exactly one of** a compiled capsule or a refusal:
its `__post_init__` raises `ValueError` when neither or both are present, so an outcome cannot be
half-built. It exposes cit:([`ok`], mcp/src/agents_remember/application/role_capsules/compilation.py:66-68), cit:([`capsule`], mcp/src/agents_remember/application/role_capsules/compilation.py:70-75) (or `None`), and
cit:([`semantic_digest`], mcp/src/agents_remember/application/role_capsules/compilation.py:77-80) — *a refusal has no identity* — plus cit:([`render_explanation`], mcp/src/agents_remember/application/role_capsules/compilation.py:81-86) for the one
operator-facing line: the digest, or the refusal and its remedy.

**A refusal is a value here rather than an exception**, for two reasons the docstring states: a
caller that has to explain a failure needs the diagnostic manifest as much as a caller that
succeeded needs the capsule, and *"compilation failure never becomes a partially valid capsule"
is easier to keep true when the two outcomes are different shapes of one result.*

A source tree that cannot be read at all — a missing file, a traversal attempt, an unreadable
root — produces the **same** refusal shape as a selection defect, carrying the admitted-facts
half of the manifest, because those facts were true regardless and are what an operator needs to
act on. Two private builders implement that split: `_manifest_bytes` recovers the manifest from
the admitted set, and `_failure_manifest` chooses `refused_manifest` when the manifest could not
be parsed versus `manifest_for_error` when it could.

This module is also the **L3 seam for the later task projection**: it accepts any
`CapsuleTaskProjectionSource` and passes it through untouched. Task state is never read, rendered,
or rewritten here.

### Conventions

One call, one outcome. A consumer branches on `CapsuleCompilationError.status` (reachable through
`outcome.error`) rather than parsing prose, and reads `outcome.manifest` for the explanation in
both success and failure.

### Invariants And Boundaries

- The outcome is **exactly one** of a capsule or a refusal; never a partial capsule and never a
  silent `None` pair.
- A refusal still carries a manifest. `error` is the typed refusal; `manifest` is present in both
  shapes, so an operator can always see who the seat was, which sources were admitted, and what
  stopped the run.
- `semantic_digest` is `None` for a refusal — a refusal has no identity. Do not synthesize one.
- The projection is passed through, never interpreted: no task state is read, rendered, or
  rewritten at this boundary.
- This module owns the read-then-compile sequencing and holds no selection rule of its own.

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pure compiler this entry point calls and the refusal-shaped manifest builders it selects between. | `compile_role_capsule`; `refused_manifest`; `manifest_for_error` | mcp/src/agents_remember/models/role_capsules/compiler.py:89-145; mcp/src/agents_remember/models/role_capsules/compiler.py:416-429; mcp/src/agents_remember/models/role_capsules/compiler.py:432-444 |
| The admission step whose refusal is converted into the same outcome shape. | `admit_capsule_sources`; `CapsuleAdmissionRequest` | mcp/src/agents_remember/application/role_capsules/sources.py:78-94; mcp/src/agents_remember/application/role_capsules/sources.py:38-77 |
| The task-projection seam accepted here and verified inside the compiler. | `compile_admitted_capsule`; `verified_task_context` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-120; mcp/src/agents_remember/models/role_capsules/compiler.py:193-216 |
| The typed refusal carried as a value. | `CapsuleCompilationError` | mcp/src/agents_remember/errors.py:464-506 |
| A supplied projection is carried in its own channel, an unverifiable one is refused, and no projection yields no context with a stable digest. | `test_a_supplied_task_projection_is_carried_in_its_own_channel`; `test_a_projection_whose_bytes_do_not_match_its_digest_is_refused`; `test_no_projection_means_no_task_context_and_a_stable_digest` | mcp/tests/test_role_capsule_compiler.py:846-861; mcp/tests/test_role_capsule_compiler.py:864-876; mcp/tests/test_role_capsule_compiler.py:879-885 |

## Cross-Repo References

No sibling-repository contract consumes this entry point. The projection seam it exposes is
consumed by a later leaf inside this master, not by another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `render_explanation` repointed to mcp/src/agents_remember/application/role_capsules/compilation.py:81-86. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T13:05+02:00 — 260915-CAPS-L14 curator: **D7 wrong-form evidence table repaired (memory-layer shape defect).** This card's evidence tables used the legacy header `| Finding | Citations | Source Path |` with the delimiter `| --- | --- | --- |`. The memory-quality checker requires `| Finding | Anchor | Source |` with the identifier alone in **Anchor** and a plain `path:start-end` in **Source** — which is what every row in these tables already carried, so the repair is the header and delimiter only: **no row content, anchor, range, prose or verification stamp was changed.** Each table's width was widened in all three parts together (header, delimiter, rows) as the checker's own guidance requires.

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the admitted compile
  entry point added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  refusal-as-a-value design and its two reasons, the exactly-one-of outcome invariant and the
  `None` digest for a refusal, the uniform refusal shape for unreadable trees, and the pass-through
  task-projection seam reserved for the later task-projection leaf. Verification metadata is left
  at the leaf base commit because the source is uncommitted — the governed closeout stamps the real
  code commit.

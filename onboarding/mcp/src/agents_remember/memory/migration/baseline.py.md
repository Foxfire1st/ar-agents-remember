# mcp/src/agents_remember/memory/migration/baseline.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/migration/baseline.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The frozen baseline every census observation belongs to: **two exact revisions recorded by identity**,
the code revision and the memory revision the corpus was read at. `KS-R21@v1` §1.3 makes a baseline
frozen and named so that "mechanical mismatch at the baseline" is a checkable statement rather than a
moving target, and so that two artifacts examined at two different baselines are **two observations**
rather than one cohort — which is why the baseline travels inside every census record's provenance
instead of being a parameter of the run that produced it. The code half is a Git tree and the memory
half is a tree for the same reason: a tree names the exact content of a directory, so a baseline whose
side is a branch name is not frozen at all. Neither half is recovered from `HEAD`; the baseline is
resolved and passed in, never inferred from the working tree, "because a baseline silently read off
`HEAD` is a baseline that moves when somebody commits". The module exists as a module rather than as a
tuple of two strings at each call site because a baseline is compared for equality in the census's own
accounting — two baselines are two cohorts, never one — and "a comparison a reader cannot trust is
worse than no comparison".

## Code Commentary

### Logic

**Validation lives on the value, not only on the factory.** `FrozenBaseline` is a
`@dataclass(frozen=True)` of four fields: the two Git object ids of trees (`code_tree_id`,
`memory_tree_id`) and the two human-facing revision spellings the report quotes (`code_revision`,
`memory_revision`). Its `__post_init__` walks the two tree-id fields, matches each against the shared
`GIT_OBJECT_PATTERN`, and raises `ValueError` naming the offending field when a value is not an exact
Git object id, with the reason stated in the message: "a baseline whose side is a ref name is not
frozen, because the ref moves when somebody commits". The docstring says why the check is on the
dataclass and not only in the factory: a caller can construct this value directly, "and a validation a
constructor can bypass is a comment". The pattern is imported from `models/knowledge/base.py` rather
than re-spelled here, so this module and every other identifier check in the substrate agree on one
spelling, and each site decides only how to apply it.

**A refusal, not an exception, when a run names no frozen baseline.** `require_frozen_baseline` takes
the two sides as `object` — not `str` — so a caller may hand it anything, and returns
`FrozenBaseline | KnowledgeRefusal`: a value the caller branches on rather than an exception it must
catch. It walks the two names, and when a value is not a `str` or does not match `GIT_OBJECT_PATTERN`
it returns `refusal("invalid_reference", operation, ...)` carrying the detail "is not an exact Git
object id, so this run names no frozen baseline", a `next_action` telling the caller to resolve the
trees from the candidate's recorded revisions and never to pass a branch name or a moving ref, and a
`RefusalFacts` pair recording `observed=repr(value)` against `expected="a 40- or 64-character object
id"`. The docstring gives both halves of the reason: "this run named a baseline that is not an exact
revision" is an expected input defect a caller branches on, and "an unfrozen baseline silently
accepted is the failure mode that makes every later mismatch report unreadable". The refusal carries
exactly one code, `invalid_reference`, so no caller has to decide which of several codes applies.

**The refusal's operation is named once and is not a write.** `BASELINE_OPERATION` is
`KnowledgeOperation = "read_knowledge_scope"`, the default for the factory's `operation` parameter.
The comment above it states the reasoning: reading a baseline is not one of the candidate write
operations, and naming it separately keeps the refusal's own operation honest — so a refusal about a
baseline is not reported as a refusal about a write.

**The revision spellings are the object ids, and nothing is invented.** On the success path the
factory returns `FrozenBaseline` with `code_revision=str(code_tree_id)` and
`memory_revision=str(memory_tree_id)`, because that is what it was given. The comment states the
choice: "a described revision is the caller's to add, and inventing a name here would put a second,
unchecked spelling of the same baseline into the value". Nothing derived from a clock, a path or a
ref name enters the value through this function.

**The snapshot identity takes the memory tree as its logical digest.** `snapshot_identity` composes
`SnapshotIdentity(repository_id, schema_version, logical_digest=self.memory_tree_id)` so the baseline
can be expressed in the knowledge vocabulary's own frozen-snapshot shape. The docstring states the
reason for that choice of half: the memory tree is the corpus this census reads, and "sealing the code
tree there would put a code identity in a field that means 'which knowledge dataset was read'", which
is the memory side. The pair stays unambiguous because both sides are also stored on the record's own
provenance, so nothing has to be recovered from the single digest. The `repository_id` and
`schema_version` are the caller's, so this method asserts nothing about which dataset was opened
beyond the memory tree it was constructed with.

**The grouping key is the pair, so two baselines are two cohorts.** `key()` returns
`(code_tree_id, memory_tree_id)` — the tuple `ScopeInventory.baseline_key` is typed as and grouped by
— which is the mechanism behind "two observations, never one cohort": rows read at one frozen baseline
are never merged into the count of another. Both halves are in the key, so a changed code tree at the
same memory tree is a different baseline rather than the same one.

### Conventions

The module declares one frozen dataclass and two functions, and every name it needs from another
layer is imported rather than re-declared: `RefusalFacts` and `refusal` from
`memory/knowledge/refusals.py`, `GIT_OBJECT_PATTERN` from `models/knowledge/base.py`,
`SnapshotIdentity` from `models/knowledge/candidate.py`, and `KnowledgeOperation` plus
`KnowledgeRefusal` from `models/knowledge/result.py`. The one module-level constant is the refusal
operation, declared in `UPPER_SNAKE_CASE`, and both the factory's default parameter and the value it
passes to `refusal` read from it, so the operation is spelled once. The public surface is the class
and the factory; the two methods are instance methods on the value the factory returns. There is no
`__all__`, and the module holds no state, opens nothing and reads no file: it validates two strings
and returns either a value or a refusal.

### Invariants And Boundaries

- **A baseline names content, never a ref.** Both tree ids are validated against `GIT_OBJECT_PATTERN`
  before the value exists, on the dataclass as well as in the factory, so a branch name, a tag or
  `HEAD` cannot be represented as a frozen baseline by either route.
- **Nothing is read off `HEAD`.** The baseline is resolved and passed in; no code here consults the
  working tree, a ref or a clock, so committing cannot move a baseline this module returned.
- **An unfrozen input is a returned refusal, not an exception and not a silently accepted value.**
  `require_frozen_baseline` returns a `KnowledgeRefusal` with the single code `invalid_reference`, the
  observed value and the expected shape, so a caller branches on a value and the failure surfaces
  instead of producing an unreadable mismatch report later.
- **The refusal is filed under a read operation.** `BASELINE_OPERATION` is `read_knowledge_scope`, so
  a baseline refusal is never reported as a refusal about a candidate write.
- **No revision spelling is invented.** Both `code_revision` and `memory_revision` are the object ids
  the factory received; a described revision is the caller's to add, and this module adds none.
- **The logical digest is the memory tree, deliberately.** `snapshot_identity` seals the corpus half,
  because the field means which knowledge dataset was read; the code half is not lost, since it is
  stored on the record's own provenance beside its counterpart.
- **The grouping key carries both halves.** Two baselines differing in either side are two cohorts,
  and no accounting path can merge them by accepting a partial key.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The baseline is the value every other module of this package takes as an input: the inventory groups
its rows by it, the reference resolution reports a mismatch against it, and the census records carry
it inside their provenance. The rows below cite the baseline value and its two validation sites, the
refusal factory it returns instead of raising, the dependency it imports rather than re-spelling, the
snapshot identity it composes, the pair-keyed grouping its consumers depend on, and the two cases that
exercise the refused and the accepted path.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what a baseline is and why it is a value rather than a parameter: two exact revisions by identity, neither recovered from `HEAD`, compared for equality so two baselines are two cohorts. | `FrozenBaseline` | mcp/src/agents_remember/memory/migration/baseline.py:1-18; mcp/src/agents_remember/memory/migration/baseline.py:35-36 |
| The refusal's operation, named separately from the candidate write operations so a baseline refusal's operation stays honest. | `BASELINE_OPERATION` | mcp/src/agents_remember/memory/migration/baseline.py:30-32 |
| The baseline value: two Git tree ids and the two human-facing revision spellings the report quotes. | `FrozenBaseline`; `code_tree_id`; `memory_tree_id` | mcp/src/agents_remember/memory/migration/baseline.py:35-48 |
| The validation that lives on the value as well as in the factory, because a caller can construct the dataclass directly and a validation a constructor can bypass is a comment. | `__post_init__` | mcp/src/agents_remember/memory/migration/baseline.py:50-67 |
| The imported identifier pattern both validation sites apply, declared once for the whole substrate instead of re-spelled per module. | `GIT_OBJECT_PATTERN` | mcp/src/agents_remember/memory/migration/baseline.py:26-26; mcp/src/agents_remember/models/knowledge/base.py:20-20 |
| The baseline expressed in the knowledge vocabulary's own frozen-snapshot shape, sealing the memory tree because that is the corpus the census reads. | `snapshot_identity`; `SnapshotIdentity` | mcp/src/agents_remember/memory/migration/baseline.py:69-82; mcp/src/agents_remember/models/knowledge/candidate.py:195-208 |
| The pair a census groups its observations by, so rows read at one baseline are never merged into the count of another. | `key` | mcp/src/agents_remember/memory/migration/baseline.py:84-87 |
| The factory that returns a refusal rather than raising, carrying the observed value, the expected shape and the next action that says never to pass a branch name or a moving ref. | `require_frozen_baseline` | mcp/src/agents_remember/memory/migration/baseline.py:90-116 |
| The refusal factories and the optional identifying facts the baseline refusal is built from. | `refusal`; `RefusalFacts` | mcp/src/agents_remember/memory/knowledge/refusals.py:47-81 |
| The revision spellings set to the object ids the factory was given, because inventing a described revision here would put a second, unchecked spelling of the same baseline into the value. | `code_revision`; `memory_revision` | mcp/src/agents_remember/memory/migration/baseline.py:117-125 |
| The operation vocabulary the refusal is filed under, one member of which is the recorded-scope read this module names. | `BASELINE_OPERATION`; `KnowledgeOperation` | mcp/src/agents_remember/memory/migration/baseline.py:32-32; mcp/src/agents_remember/models/knowledge/result.py:36-83 |
| The first consumer: the scope inventory is built at a frozen baseline and groups its rows by the baseline's own key. | `build_inventory`; `baseline_key` | mcp/src/agents_remember/memory/migration/inventory.py:650-673; mcp/src/agents_remember/memory/migration/inventory.py:151-157 |
| The second consumer: a mechanical mismatch carries the baseline it was observed at and renders both tree ids, truncated, so a report can quote the fact without adding an interpretation. | `Mismatch`; `FrozenBaseline` | mcp/src/agents_remember/memory/migration/resolution.py:101-123; mcp/src/agents_remember/memory/migration/resolution.py:29-29 |
| The case that refuses a ref name as a baseline and accepts the two object ids, and the case that proves two baselines are two observations and never one cohort. | `require_frozen_baseline`; `FrozenBaseline` | mcp/tests/test_migration_census.py:292-310 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A baseline is two Git object ids and two
revision spellings, validated as strings and returned as a frozen value or a refusal; nothing here
opens a repository, reads a ref or reaches a remote, and the Git identities it mentions are values a
caller resolved elsewhere and passed in.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the frozen baseline. It records the identity model `KS-R21@v1` §1.3 requires — two Git tree ids, never a ref, neither recovered from `HEAD`, because a baseline read off `HEAD` moves when somebody commits — and the two human-facing revision spellings the report quotes beside them. It records both validation sites: `__post_init__` on the frozen dataclass, so a directly constructed value cannot bypass the check, and `require_frozen_baseline`, which returns `KnowledgeRefusal` with the single code `invalid_reference` instead of raising, carrying the observed value and the next action that forbids a branch name or a moving ref. It records that the refusal is filed under `BASELINE_OPERATION = "read_knowledge_scope"` rather than under a candidate write, and that `GIT_OBJECT_PATTERN` is imported from `models/knowledge/base.py` rather than re-spelled. It records `snapshot_identity`'s deliberate choice of the memory tree as the logical digest, because that field means which knowledge dataset was read and both sides survive on the record's own provenance, and `key()`'s pair, which is what makes two baselines two cohorts in the inventory's grouping. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.

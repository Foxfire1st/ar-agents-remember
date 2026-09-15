# mcp/src/agents_remember/memory/knowledge/refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash | `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate | 2026-09-15T22:46:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

The typed refusal vocabulary, the two exceptions that carry it, and the SQLite-error mapping. Every refusal in
the package is built by one of the factories here, so the codes, the offending record and the advertised next
action live in one place instead of being spelled out per call site.

## Code Commentary

### Logic

Two exception types: `KnowledgeStorageError` (a storage failure no contract code describes — a defect report,
not an expected outcome) and `KnowledgeRefused` (internal control flow that carries a typed refusal out of a
transaction so the operation can roll back and return it).

`RefusalFacts` is the optional identifying bundle (`table`, `record_id`, `expected`, `observed`), and the generic
`refusal(...)` factory builds one `KnowledgeRefusal`.

One factory per case: `scope_refusal` (returns `None` when the namespaces match), `invalid_payload_refusal`,
`duplicate_revision_refusal`, `duplicate_invariant_refusal`, `repository_rebind_refusal`,
`unknown_invariant_refusal`, `dangling_predecessor_refusal`, `cross_invariant_predecessor_refusal`,
`lineage_cycle_refusal`, `lock_capability_refusal`, `candidate_busy_refusal`.

`lineage_cycle_refusal` has two branches and the message names which applied, because the remedy differs.
`candidate_on_cycle=True` states the predecessors would put the revision on a cycle ("it would be reachable from
itself") and names resolving the cycle at that revision. The descending branch states the predecessors descend
from a revision already on a lineage cycle, names the ancestor cycle in `observed`, and says explicitly that the
candidate is **not itself on that cycle** — claiming self-reachability there would be false, because nothing
points at the candidate.

`map_sqlite_error` maps a surviving `apsw.Error` by message: an `immutable_revision`-prefixed message to
`immutable_revision`, a foreign-key message to `invalid_reference`, any other constraint message to
`relationship_constraint`, and everything else to `invalid_payload`.

### Conventions

A refusal is a **returned value**, not an exception: callers branch on a code instead of parsing a message. The
exceptions exist only for the two cases a return value cannot express — an unclassifiable storage failure, and a
refusal raised from inside a transaction that must be rolled back first.

### Invariants And Boundaries

- A reachable expected failure returns a `KnowledgeRefusal` with one of the contract codes; `KnowledgeStorageError`
  means the caller has found a defect, not an outcome to handle.
- The trigger text `immutable_revision: …` is the steering signal that maps a trigger-originated SQLite error to
  the right code, so the schema's trigger messages and this mapping are one contract.
- Every refusal names a `next_action`; guidance for the descending-cycle branch names both remedies (author an
  acyclic successor, and resolve the ancestor cycle reported in `observed`).
- `unsupported_schema` and `missing_expected_row` are declared in the vocabulary but have no factory here; schema
  failures raise `KnowledgeStorageError` instead.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The defect-report exception versus the internal control-flow exception. | `KnowledgeStorageError`; `KnowledgeRefused` | mcp/src/agents_remember/memory/knowledge/refusals.py:27-44 |
| The facts bundle and the one generic factory every refusal is built through. | `RefusalFacts`; `refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:47-77 |
| The two-branch cycle refusal whose text must be true in both directions. | `lineage_cycle_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:238-277 |
| The write-path rule the descending branch describes, and its post-insert graph scope. | `_require_no_lineage_cycle` | mcp/src/agents_remember/memory/knowledge/store.py:378-404 |
| The SQLite-error mapping and the trigger-message prefix that steers it. | `map_sqlite_error` | mcp/src/agents_remember/memory/knowledge/refusals.py:308-350 |
| The trigger messages the mapping depends on. | `IMMUTABILITY_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema.py:284-350 |
| The refusal codes these factories must stay within. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:31-48 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new typed refusal vocabulary. It records that refusals are returned values, that the two cycle branches must be true in their own case, and that the trigger-message prefix is a shared contract with the SQLite-error mapping. The final wording of the descending branch is the round-3 review outcome for sealed finding `RV-4`. Verification metadata remains empty until closeout stamps the code commit.

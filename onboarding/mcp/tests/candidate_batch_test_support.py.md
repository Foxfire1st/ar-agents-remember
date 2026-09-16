# mcp/tests/candidate_batch_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/candidate_batch_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate | 2026-09-16T10:27:28+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

**The candidate-change case harness: one admitted candidate, its batches and its probes.** Every case in the two
candidate-batch test modules needs the same three things, and this module owns them so neither module re-derives
them:

- **One admitted candidate built through the real seam.** `build_candidate_harness` opens a destination, binds its
  namespace through `initialize_knowledge_namespace` and resolves contexts through `resolve_candidate_context`, so
  a case authors its batch against an identity the application actually read rather than against a digest the case
  wrote down.
- **Batch construction from typed commands.** A case builds command objects and `CandidateHarness.batch` supplies
  the admitted context and the `ChangeBatch` shape, so no case has to remember the context payload.
- **The probes a refusal needs.** Row counts and the logical digest, read through a *separately opened* store, so
  "the stored dataset was left untouched" is measured rather than asserted.

It is test support, not production code: it decides nothing, and the only writes it performs are the ones a case
explicitly asks for.

## Code Commentary

### Logic

- `CandidateHarness` is a frozen dataclass holding the repository root, the context, the admitted destination and
  the file path, with a `candidate(...)` context manager that opens a fresh `OpenedKnowledgeStore` for a case and
  closes it afterwards.
- `build_candidate_harness(tmp_path, …)` performs the real setup: initialize the namespace, resolve the context
  from the live candidate, and return the harness. A case therefore never constructs a `KnowledgeContext` by hand
  — the one context a case *does* construct is deliberately tampered with, to prove the operation refuses it.
- `measure_refusal(harness, batch)` is the refusal probe: it reads the table counts and logical digest through a
  separate store **before** applying, applies the batch, then reads them again and returns a `RefusalEvidence`
  carrying the refusal, both count snapshots and both digests. A case asserts on the equality of those, which is
  what makes "nothing was written" a measurement instead of a claim.
- `table_counts` and `logical_digest` are the two measurements; both open their own store so they observe the
  committed file rather than the handler under test.
- `RemovalSeed` / `removal_seeds(...)` seed one stored row per removable kind and read back the digests a removal
  must name; `record_is_gone` reopens and asks whether an identity still resolves.
- The draft builders (`revision_draft`, `family_revision_draft`, `anchor_draft`, `claim_draft`,
  `claim_command`) produce valid authored payloads so a case varies only the field it is about.
- `insert_raw_membership` is the one raw write, and it exists for the same reason the graph support module's raw
  writes do: the operations **forbid** the state a duplicate-pair case needs, so the row has to be placed by hand
  to prove the database's own unique tuple refuses it. `CommandSeeds` gathers the seeded identities one case
  needs.

### Conventions

- Registered in `mcp/tests/evidence-lifecycle.toml` as contract **`candidate-batch-case-harness`** with an
  explicit `[[artifact]]` row (`shared-support`, `internal-canonical`, `unit-regression`, `in-process`,
  `permanent`, `consumer_scope = "exact"`, consumers exactly `mcp/tests/test_candidate_batch_commands.py` and
  `mcp/tests/test_candidate_batch_transaction.py`) and an `evidence_node` that is a real passing node.
- The declared `source_version_or_generator` says what the harness builds rather than naming a generator: an
  admitted destination built through `initialize_knowledge_namespace` plus contexts resolved through
  `resolve_candidate_context`. That sentence is the contract — a future edit that hand-writes a context would
  break what the harness is for.
- Every measurement is taken through a separately opened store, never through the handler under test.
- Drafts are built from the typed draft models, so a case's payload fails at the same boundary a caller's would.

### Invariants And Boundaries

- **Test support, not production code.** Nothing here is imported by `mcp/src`, and it decides nothing about
  behaviour; it only arranges the world a case asserts about.
- **The context is resolved, never written down.** A case that needs an unsealed context derives it by tampering
  with a resolved one, which is the only way the operation's own re-derivation can be exercised.
- **A refusal is measured, not assumed.** The before/after counts and the logical digest are read from the
  committed file, so the atomicity claim is checked against storage rather than against the returned result.
- **The raw write is deliberate and narrow.** `insert_raw_membership` places exactly the row the typed operations
  refuse to create; it is not a general escape hatch and must not grow into one.
- **Location is part of the contract.** Durable support is discovered under `mcp/tests/**`; a module under
  `mcp/test_support/**` cannot be registered at all, so this file stays where it is.
- **Boundary.** The harness owns candidate setup, batch assembly and the two measurements. Which cases exist and
  what they assert belongs to the two consumer modules.

### Todos

None recorded for this slice. Its declared consumer set is exact, and the registry validator derives the real
importers and refuses a differing declared set — so a third consumer module must update the row in the same change.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The harness and its real-seam setup, including the context resolved from the live candidate. | `CandidateHarness`; `build_candidate_harness` | mcp/tests/candidate_batch_test_support.py:92-236; mcp/tests/candidate_batch_test_support.py:237-278 |
| The two measurements, each taken through its own opened store. | `logical_digest`; `table_counts` | mcp/tests/candidate_batch_test_support.py:279-287; mcp/tests/candidate_batch_test_support.py:288-297 |
| The refusal probe and the evidence object a case asserts on. | `RefusalEvidence`; `measure_refusal` | mcp/tests/candidate_batch_test_support.py:298-323; mcp/tests/candidate_batch_test_support.py:324-345 |
| The removal seeds and the digest each removal must name. | `RemovalSeed`; `removal_seeds`; `record_is_gone` | mcp/tests/candidate_batch_test_support.py:346-355; mcp/tests/candidate_batch_test_support.py:431-534; mcp/tests/candidate_batch_test_support.py:535-544 |
| The deliberate raw write that places the row the operations forbid. | `insert_raw_membership` | mcp/tests/candidate_batch_test_support.py:545-577 |
| The registered contract, artifact row, evidence node and exact consumer set. | "contract:candidate-batch-case-harness" | mcp/tests/evidence-lifecycle.toml:1101-1101 |
| The admitted destination and namespace initialization the harness drives. | `initialize_knowledge_namespace`; `resolve_candidate_context` | mcp/src/agents_remember/application/knowledge.py:160-191; mcp/src/agents_remember/application/knowledge.py:252-273 |
| The harness's one-to-one card, which records what it builds. | "One admitted candidate built through the real seam" | onboarding/mcp/tests/candidate_batch_test_support.py.md:19-31 |
| The operation the harness applies its batches through. | `change_knowledge_candidate` | mcp/src/agents_remember/application/knowledge.py:303-315 |
| The two declared consumers' own first nodes, which measure a refusal through this harness. | "test_every_declared_command_is_applied_and_read_back"; "test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch" | mcp/tests/test_candidate_batch_commands.py:114-209; mcp/tests/test_candidate_batch_transaction.py:62-110 |
| The registry validator that derives real importers and refuses a differing declared consumer set. | `load_evidence_inventory` | mcp/test_support/agents_remember_test_support/testing/evidence_lifecycle.py:162-166 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new candidate-batch case harness. It records what the harness builds through the real seam (an admitted destination and a context resolved from the live candidate), the refusal probe that measures table counts and the logical digest through a separately opened store, the one deliberate raw write that exists because the operations forbid the state a duplicate-pair case needs, and its registered contract with an exact two-module consumer set. Verification metadata remains empty until closeout stamps the code commit.

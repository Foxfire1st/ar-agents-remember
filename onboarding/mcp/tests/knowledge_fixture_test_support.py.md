# mcp/tests/knowledge_fixture_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/knowledge_fixture_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c`|
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

The shared branching knowledge fixture. It now carries **two halves in one builder**: the identity half — one
repository, one invariant and three revisions, a base `I0` and two successors `I-A`/`I-B` that both display `v2`
with different statements — and the graph half, which extends the same fixture with a second and third invariant,
two overlapping families with a successor and a same-label sibling, and three recorded realizations. Every step is
authored through the real typed operations rather than by inserting rows.

## Code Commentary

### Logic

Stable prose constants make a reopened comparison meaningful rather than incidental: `REPOSITORY_AUTHORITY_HOME`,
`INVARIANT_LABEL`, `BASE_STATEMENT`, `BRANCH_A_STATEMENT`, `BRANCH_B_STATEMENT`, `BASE_DISPLAY_VERSION` (`"v1"`),
`SHARED_SUCCESSOR_DISPLAY_VERSION` (`"v2"`), `ESSENTIAL_APPLICABILITY`, the three condition tuples and
`ESSENTIAL_EXCLUSIONS`, plus the family and realization constants (`FAMILY_GUARANTEE`,
`FAMILY_SUCCESSOR_GUARANTEE`, `FAMILY_SIBLING_GUARANTEE`, `FAMILY_DISPLAY_VERSION`) the graph half adds.

`BranchingKnowledgeFixture` is a frozen dataclass carrying the database path, the repository and invariant
identities, the identity half's three revision identities, the `Authorship` envelope, and the graph half's shapes:
a `FixtureFamily` for the family and its successor and sibling revisions, a `FixtureRealization` per recorded
location (the two implementations of one invariant plus an anchor whose source is unavailable), and the second
invariant's identity. `reopen()` opens the fixture store so a test reads what was really persisted.

`make_authorship` builds one envelope with a stable actor (`agent:fixture`), the developer kickoff ruling as its
authorization reference, a fresh operation id, a real recorded instant and `requirement:KS-R01@v1` as its origin.

`build_branching_knowledge_fixture(directory, ...)` creates the directory, opens the store, records the repository
and the invariant, then submits `_fixture_revisions(...)` — the base and the two successor requests — and closes
the store in a `finally`, so the caller reopens to read. `_build_identity_half` and `_build_graph_half` split the
two construction phases inside that one transaction-free sequence.

`fixture_revision_draft` builds one further draft of the fixture's invariant for extension scenarios, parameterized
by `RevisionClauses` (display version and conditions).

### Conventions

The fixture exists because the interesting identity behaviour is a **conflict**, not a constructor call: two
divergent successors of one revision carry the same friendly display version and both must remain separately
addressable. The graph half is an extension of that same builder rather than a second fixture, so the graph cases
inherit the identity scenario instead of re-creating it and a later leaf extends one artifact instead of choosing
between two.

### Invariants And Boundaries

- The module is test support, not production code: it decides nothing and is imported by tests and by later
  leaves' fixtures only.
- `_require` fails loudly rather than returning a refused state, so a fixture that silently stopped creating would
  fail its consumers instead of producing a misleading scenario.
- The relocation to `mcp/tests/` is load-bearing. The repository's evidence governance discovers durable support
  from `mcp/tests/**` plus a small fixed root set; `mcp/test_support/**` is not governed, so the same file at
  `mcp/test_support/agents_remember_test_support/testing/knowledge_fixture.py` could not be registered in the
  evidence lifecycle at all — it was refused both as an ungoverned artifact path and because its consumer proof
  could not be derived there. The module is registered as contract `knowledge-identity-branching-fixture` in
  `mcp/tests/evidence-lifecycle.toml`.
- **The declared consumer set is now observed, not intent.** The registry row names exactly five consumers
  (`test_knowledge_family_revision.py`, `test_knowledge_graph_reads.py`, `test_knowledge_relation_rules.py`,
  `test_knowledge_revision_seals.py`, `test_knowledge_store.py`), and the lifecycle validator derives the test
  consumers from the source and enforces equality, so an undeclared importer is a hard failure rather than a
  silent gap. The L3–L8 consumers are no longer anticipated: each of those leaves must add itself to the row.
- **The graph half is built through the public operations too.** The raw writes that construct the states the
  operations forbid live in `mcp/tests/knowledge_graph_test_support.py`, not here, so this builder cannot be the
  place a case bypasses a rule.

### Todos

`test_two_same_label_successors_reopen_as_separate_revisions`, the node registered as this fixture's evidence
node, asserts the fixture's constants and reads them back from the fixture's own database; it does not by itself
demonstrate the identity conflict. The conflict behaviour is exercised by that node together with
`test_reused_revision_identity_with_other_content_refuses`, so the contract is covered in aggregate rather than by
the single cited node.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture shape: the identity half's two same-label successors and the graph half's families and realizations. | `BranchingKnowledgeFixture`; `FixtureFamily`; `FixtureRealization` | mcp/tests/knowledge_fixture_test_support.py:161-188; mcp/tests/knowledge_fixture_test_support.py:152-160; mcp/tests/knowledge_fixture_test_support.py:143-151 |
| The builder, which authors both halves through the real operations and closes the store. | `build_branching_knowledge_fixture` | mcp/tests/knowledge_fixture_test_support.py:203-263 |
| The extension helper for later leaves' scenarios. | `fixture_revision_draft`; `RevisionClauses` | mcp/tests/knowledge_fixture_test_support.py:264-288; mcp/tests/knowledge_fixture_test_support.py:135-142 |
| The step assertion that makes a fixture failure loud. | `_require` | mcp/tests/knowledge_fixture_test_support.py:614-623 |
| The graph-half construction phases, each authored through the public operations. | `_build_identity_half`; `_build_graph_half`; `_create_families`; `_create_realizations` | mcp/tests/knowledge_fixture_test_support.py:309-327; mcp/tests/knowledge_fixture_test_support.py:328-335; mcp/tests/knowledge_fixture_test_support.py:380-439; mcp/tests/knowledge_fixture_test_support.py:492-539 |
|  The registered stable contract, its evidence node and its five declared consumers. | "contract:knowledge-identity-branching-fixture" | mcp/tests/evidence-lifecycle.toml:1031-1056  |
| The identity-conflict nodes that cover the contract in aggregate. | `test_two_same_label_successors_reopen_as_separate_revisions`; `test_reused_revision_identity_with_other_content_refuses` | mcp/tests/test_knowledge_store.py:89-113; mcp/tests/test_knowledge_store.py:257-282 |
| The operations the fixture authors through, both halves. | `create_repository`; `create_invariant`; `create_revision`; `create_family`; `create_realization_claim` | mcp/src/agents_remember/memory/knowledge/store.py:180-259; mcp/src/agents_remember/memory/knowledge/families.py:78-95; mcp/src/agents_remember/memory/knowledge/realizations.py:61-83 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T07:33:51+00:00: Generated citation repair: `test_two_same_label_successors_reopen_as_separate_revisions`; `test_reused_revision_identity_with_other_content_refuses` repointed to mcp/tests/test_knowledge_store.py:87-111; mcp/tests/test_knowledge_store.py:216-241. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/tests/test_knowledge_store.py:216 to the row 108 of this card as the citation for `test_reused_revision_identity_with_other_content_refuses`: no cited file carried the construct, and the checker named line(s) [216] in this file as its live location
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_reused_revision_identity_with_other_content_refuses` in the row 108 of this card from mcp/tests/test_knowledge_store.py:87-89 to mcp/tests/test_knowledge_store.py:216-218, the extent of the construct the claim is about (the checker named line(s) [216] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_two_same_label_successors_reopen_as_separate_revisions` in the row 108 of this card from mcp/tests/test_knowledge_store.py:216-218 to mcp/tests/test_knowledge_store.py:87-89, the extent of the construct the claim is about (the checker named line(s) [87] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/tests/test_knowledge_store.py:87-89 in the row 108 of this card; the repetition added no pooled evidence
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded the L1 statement that this fixture's only observed consumer is `test_knowledge_store.py` and that the L2–L8 consumers are anticipated intent.** The graph leaf extended the *same* builder with a graph half (a second and third invariant, two overlapping families with a successor and a same-label sibling, and three recorded realizations), so the registry row's declared consumer set is now five modules and the lifecycle validator derives that set from the source and enforces equality. The card also records that the raw writes constructing states the operations forbid live in the separate graph support module, so this builder cannot be the place a case bypasses a rule. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the relocated shared fixture. It records why the module lives under `mcp/tests/` rather than `mcp/test_support/` (governed-evidence discovery plus derivable consumer proof), its registered contract in `mcp/tests/evidence-lifecycle.toml`, and the aggregate — not single-node — coverage of its identity-conflict contract (sealed review findings `RV-6` and `OQ-10`). Verification metadata remains empty until closeout stamps the code commit.

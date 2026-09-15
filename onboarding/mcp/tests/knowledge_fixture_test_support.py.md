# mcp/tests/knowledge_fixture_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/knowledge_fixture_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash | `60e0820e6cb3b1d160518b9f8c7ac6241323a281`|
| lastVerifiedCommitDate | 2026-09-15T22:46:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

The shared branching knowledge fixture: one repository, one invariant and three revisions — a base `I0` and two
successors `I-A`/`I-B` that both display `v2` with different statements — built through the real typed operations
rather than by inserting rows.

## Code Commentary

### Logic

Stable prose constants make a reopened comparison meaningful rather than incidental: `REPOSITORY_AUTHORITY_HOME`,
`INVARIANT_LABEL`, `BASE_STATEMENT`, `BRANCH_A_STATEMENT`, `BRANCH_B_STATEMENT`, `BASE_DISPLAY_VERSION` (`"v1"`),
`SHARED_SUCCESSOR_DISPLAY_VERSION` (`"v2"`), `ESSENTIAL_APPLICABILITY`, the three condition tuples and
`ESSENTIAL_EXCLUSIONS`.

`BranchingKnowledgeFixture` is a frozen dataclass carrying the database path, the repository and invariant
identities, the three revision identities and the `Authorship` envelope, with a `reopen()` that opens the fixture
store so a test reads what was really persisted.

`make_authorship` builds one envelope with a stable actor (`agent:fixture`), the developer kickoff ruling as its
authorization reference, a fresh operation id, a real recorded instant and `requirement:KS-R01@v1` as its origin.

`build_branching_knowledge_fixture(directory, ...)` creates the directory, opens the store, records the repository
and the invariant, then submits `_fixture_revisions(...)` — the base and the two successor requests — and closes
the store in a `finally`, so the caller reopens to read. Every step is asserted through `_require`, which raises
`AssertionError` naming the step and the returned state when a step does not return `created`: a fixture is not a
probe.

`fixture_revision_draft` builds one further draft of the fixture's invariant for extension scenarios, parameterized
by `RevisionClauses` (display version and conditions).

### Conventions

The fixture exists because the interesting identity behaviour is a **conflict**, not a constructor call: two
divergent successors of one revision carry the same friendly display version and both must remain separately
addressable. It is built through the public operation, never by inserting rows, so a later leaf that builds on it
inherits a store it can trust and a scenario it can extend rather than re-invent.

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
- Its only source-observed consumer today is `mcp/tests/test_knowledge_store.py`; the L2–L8 consumers are
  anticipated and are named as intent, not as the registered contract.

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
| The fixture shape and its two same-label successors. | `BranchingKnowledgeFixture` | mcp/tests/knowledge_fixture_test_support.py:58-73 |
| The builder, which authors every revision through the real operations and closes the store. | `build_branching_knowledge_fixture` | mcp/tests/knowledge_fixture_test_support.py:90-133 |
| The extension helper for later leaves' scenarios. | `fixture_revision_draft`; `RevisionClauses` | mcp/tests/knowledge_fixture_test_support.py:136-157; mcp/tests/knowledge_fixture_test_support.py:50-55 |
| The step assertion that makes a fixture failure loud. | `_require` | mcp/tests/knowledge_fixture_test_support.py:203-212 |
| The registered stable contract, its evidence node and its declared consumer. | `knowledge-identity-branching-fixture`; `[[artifact]]` | mcp/tests/evidence-lifecycle.toml |
| The only observed consumer today. | `test_two_same_label_successors_reopen_as_separate_revisions`; `test_reused_revision_identity_with_other_content_refuses` | mcp/tests/test_knowledge_store.py:87-113; mcp/tests/test_knowledge_store.py:176-203 |
| The operations the fixture authors through. | `create_repository`; `create_invariant`; `create_revision` | mcp/src/agents_remember/memory/knowledge/store.py:178-241 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the relocated shared fixture. It records why the module lives under `mcp/tests/` rather than `mcp/test_support/` (governed-evidence discovery plus derivable consumer proof), its registered contract in `mcp/tests/evidence-lifecycle.toml`, and the aggregate — not single-node — coverage of its identity-conflict contract (sealed review findings `RV-6` and `OQ-10`). Verification metadata remains empty until closeout stamps the code commit.

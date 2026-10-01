# mcp/tests/knowledge_fixture_test_support.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The fixture shape: the identity half's two same-label successors and the graph half's families and realizations. [1]
- The builder, which authors both halves through the real operations and closes the store. [2]
- The extension helper for later leaves' scenarios. [3]
- The step assertion that makes a fixture failure loud. [4]
- The graph-half construction phases, each authored through the public operations. [5]
- The registered stable contract, its evidence node and its five declared consumers. [6]
- The identity-conflict nodes that cover the contract in aggregate. [7]
- The operations the fixture authors through, both halves. [8]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

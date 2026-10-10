# mcp/tests/knowledge_fixture_test_support.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Shared read-side rows for divergent revisions, overlapping families and realization claims.

## Code Commentary

### Logic

One dataset holds the base revision and two different same-label successors. The graph half adds invariants, overlapping families, family successors and three realizations including an absent source path. BranchingKnowledgeFixture retains their identities and reopens persisted rows. [1] [2]

Construction uses the test-only RowStore, which computes production seals and inserts index-shaped rows without retired write-admission guards. [5]

### Invariants And Boundaries

- Friendly display labels are not revision identity.
- An unavailable source does not erase a fixture claim.
- This fixture is not production write authority.


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


## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.


### Repo-Internal References


- Fixture identities and both scenario halves. [1]


- One builder constructs both halves. [2]


- The test-only builder supplies rows without canonical write rules. [5]


- Both same-label successors remain readable. [7]



- The fixture shape: the identity half's two same-label successors and the graph half's families and realizations. [14]
- The builder, which authors both halves through the real operations and closes the store. [15]
- The extension helper for later leaves' scenarios. [16]
- The step assertion that makes a fixture failure loud. [17]
- The graph-half construction phases, each authored through the public operations. [18]
- The operations the fixture authors through, both halves. [19]


### Cross-Repo References

No cross-repository behavior is implemented in this file.


No cross-repository contract is established by this file.

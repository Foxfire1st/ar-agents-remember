# mcp/tests/knowledge_fixture_test_support.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Shared single-revision knowledge fixture built through the text-backed operations.

## Code Commentary

### Logic

One text memory tree holds three single-revision invariants that share nothing but their derived
display: the divergent-successor revisions the old fixture authored beside one identity are gone,
because a text record holds exactly one revision (MIK-R74 rule 3). The graph half adds the realized
revision, its recorded realizations (including an absent source path) and the overlapping families.
`BranchingKnowledgeFixture` retains the projected identities the tree produced and reopens persisted rows. [1] [2]

Construction builds a real text tree through the rows builder, never by inserting rows — so a later
leaf inherits a real index it can trust. The module is test support, not production code: it decides
nothing and is imported by tests and later leaves' fixtures only. [5]

### Invariants And Boundaries

- Friendly display labels are not revision identity.
- An unavailable source does not erase a fixture claim.
- Several separately recorded revisions stay separately addressable, and both decode with no predecessors.
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


- The text-backed builder supplies rows without canonical write rules. [5]


- Separately recorded revisions remain separately addressable, decoding with no predecessors. [7]



- The fixture shape: the identity half's two same-label successors and the graph half's families and realizations. [14]
- The builder, which authors both halves through the real operations and closes the store. [15]
- The extension helper for later leaves' scenarios. [16]
- The step assertion that makes a fixture failure loud. [17]
- The graph-half construction phases, each authored through the public operations. [18]
- The operations the fixture authors through, both halves. [19]


### Cross-Repo References

No cross-repository behavior is implemented in this file.


No cross-repository contract is established by this file.

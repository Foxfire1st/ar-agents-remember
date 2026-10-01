# mcp/tests/test_citation_index_resilience.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Pin the three behavioural claims `CAPS-R14@v1` makes about the citation source index: the index
**honours the shared exclusion register from each of its three sources independently**, the ruled
caps **skip and report rather than refuse**, and the quality surface **cannot be bricked** by
either.

The module's own docstring names the two defects it makes impossible. A cap used to refuse the
whole tree (`citation source-index input exceeds the 4194304-byte per-file cap: [...]` was raised
as an *error* out of the mandated contract-scoped `memory_quality_check`, so a large or vendored
tree made the quality surface the thing that blocked work instead of the thing that describes it),
and enumeration ignored the shared exclusion register entirely. The developer's 2026-08-20 ruling
is the contract the caps cases assert: an oversized file is **skipped with a report entry naming
it and its size**, the aggregate default is **512 MiB applied to the post-exclusion/post-skip
set**, the caps are settings-overridable through `onboarding.citationIndex`, and a hard stop
remains only past **~2 GiB**.

## Code Commentary

### Logic

`Fixture` builds one disposable tree per case — a code root, a memory root carrying
`system/settings.json`, and a card citing a source range — so each case can compare a population
before and after exactly one rule is introduced. `FixtureCase.setUp` creates it under a temporary
directory that is removed afterwards; nothing outside it is read or written.

The five classes and what each one defends:

| Class | Defends |
| --- | --- |
| `TheExclusionRegisterIsHonouredFromEachSourceIndependently` | one case per source: `pathRules.exclude`, the code repo's `.gitignore`, and a caller-supplied exclude. Also the durable record (the register parsed back **out of the published manifest file**, not from memory), the non-Git fallback under rule interaction, the pinned divergence from Git, and the one-authority-per-root parity between the two acquisition routes. |
| `TheRuledCapsSkipAndReportRatherThanRefuse` | the per-file skip names the path **and** its stat size with the index still built; a total above the ruled default reports; the hard stop names offenders, the cap and the next step; every `onboarding.citationIndex` key overrides while the module constants stay default; the file-count cap names its fixing route; a malformed block is refused by name. |
| `TheQualitySurfaceCannotBeBricked` | the reported, actionable states: a capped index reported on the citation check, an unreadable source named with its path, an unbuildable index as a reported state with a `nextStep`, the closeout gate's own declared check group degrading identically, and a document with no code root saying so rather than passing. |
| `TheRegisteredCitationSurfaceCarriesTheCallerExcludes` | the caller-exclude surface itself: the registered `citation_fix` MCP tool declares `exclude`, and the CLI declares a repeatable `--exclude` option. |
| `TheCapsThatStayAsTheyWere` | the two caps the ruling did **not** move — the database cap and the file-count cap — so a later edit cannot widen them unnoticed. |

### The divergence case, and why it is written the way it is

`test_the_register_admits_a_negated_file_under_an_excluded_directory_where_git_does_not` measures
**both sides**: Git's answer comes from a real repository (`git check-ignore -q vendor/keep.py`
exits 0, so Git ignores the file), while the register's answer comes from a plain directory
carrying the same `.gitignore` bytes (`vendor/keep.py` admitted, `vendor/lib.py` excluded,
`gitignoreAuthority: register`). The case exists so the divergence between the register's contract
and Git's cannot be mistaken for an accident, and it is falsifiable: making the matcher
Git-faithful kills both this case and the L14R-4 class case.

### Conventions

- Each case protects one distinct reading, and the module states which one in its own
  `WHAT DEFENDS WHAT` table.
- Cap values are read from the shipped constants (`PER_FILE_CAP`, `AGGREGATE_CAP`, `HARD_STOP`)
  rather than restated as literals, so a case reddens if a constant moves rather than silently
  testing an old number.
- The module is registered in the `unit-regression` evidence lane
  (`mcp/tests/test-evidence-lanes.toml`) and is a declared consumer of the lifecycle catalog.

### Invariants And Boundaries

- No case asserts that D7/D8's repository-wide citation backlog was repaired here; that backlog is
  another leaf's and is sized in its own ledger entry.
- No case reads or writes outside its own temporary root.
- The module never asserts an acceptance result: the fresh-user chain is
  `mcp/tests/test_fresh_user_harness.py`'s subject and
  `scripts/e2e_harness/run_fresh_user.py`'s transcript.

### Todos

None.

## Evidence

### Repo-Internal References

- A settings exclude removes a file and the register records the rule that did it. [1]
- A `.gitignore` rule removes a file and the register records the pattern. [2]
- A caller exclude narrows one call and only that call. [3]
- The rule set survives on the durable record, parsed back out of the published manifest. [4]
- The non-Git fallback keeps a directory rule while a negation exists. [5]
- The register's deliberate divergence from Git, pinned on both sides. [6]
- One root gives one `gitignoreAuthority` on both acquisition routes. [7]
- A caller exclude that cannot mean anything is refused by name. [8]
- An oversized file is skipped and reported with its path and size, index still built. [9]
- A total above the ruled 512 MiB default reports instead of refusing. [10]
- The hard stop names the offenders and the next step. [11]
- Every settings key overrides a cap while the module constants stay default. [12]
- The file-count cap refuses with the route that fixes it. [13]
- A malformed `citationIndex` block is refused by name. [14]
- A capped index is reported on the citation check rather than raising. [15]
- An unreadable source is reported with its path. [16]
- An index that cannot be built is a reported state carrying a `nextStep`. [17]
- The closeout gate's own declared check group degrades the same way. [18]
- A document with no code root says so rather than passing. [19]
- The registered `citation_fix` MCP tool declares `exclude`. [20]
- The CLI declares a repeatable `--exclude` option. [21]
- The database cap and the file-count cap are unchanged by the ruling. [22]
- The ruled numbers the caps cases assert against. [23]
- The caller-exclude surface the last two cases read. [24]

### Cross-Repo References

No sibling-repository contract defines these values.

No meaningful cross-repo references found.

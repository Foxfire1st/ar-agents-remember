# Python Test Evidence Infrastructure Overview

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/test_support/agents_remember_test_support/testing` |

## Governing Overview

[Python verification infrastructure](../overview.md)

## What This Area Is

Repository-owned pytest isolation and evidence infrastructure. Ordinary pytest bootstrap and
certifying startup are distinct. `pytest_bootstrap.py` is the reusable bootstrap: a seeded
collection order, an isolated cache directory for the pytest process, and the check that a test
restores owned module-level state. It carries no certifying or external-service capability.
`certifying_bootstrap.py` admits a Dagger quality process first and only then resolves the
candidate test process.

The route also owns the curation-doctrine registry `curation_doctrine.py`: the retired curation
sentences and the field-name facts a canonical instruction source must state, checked against the
shipped skill corpus. Shared test helpers are not execution or knowledge-verdict owners, and
canonical instruction and mirror consistency belongs to its synchronization owner
(`scripts/sync-skills.py`); test qualification, completed curation, semantic acceptance and Git
publication each keep their own authority.

## Hot Path Summary

- **Process setup.** `hermetic_bootstrap.py` sets up the candidate and the environment of a pytest
  process. `global_state.py` snapshots and restores owned module-level state. `random_order.py`
  shuffles collected items with a seed. `dagger_admission.py` mints the testing-layer capability
  for a nonce-attested Dagger quality process.
- **Source facts.** `dependency_facts.py` derives import, pytest-plugin and test-consumer facts
  from source; it holds no declarations. `consumer_inventory.py` is the bounded inventory of the
  Python-test evidence consumers.
- **The two test catalogs.** `lane_manifest.py` loads the lane of every test file and
  `evidence_lanes.py` is the pytest plugin that checks it at collection and routes categories and
  cadence. `evidence_lifecycle.py` validates the catalog of governed test artifacts and is the
  command-line entry for both catalogs. `evidence_governance.py` decides which files are governed.
  `catalog_canonical.py` defines the canonical form of both catalogs, the findings both loaders
  report for a catalog that is not in it, and the rewrite behind `evidence_lifecycle --write`.
- **Candidate-bound evidence.** `candidate_snapshot.py` gives the exact Git identity of a working
  candidate for non-certifying evidence routes, and `evidence_provenance.py` records candidate and
  machine provenance for non-accepting Dagger evidence.
- **Selection and reporting.** `retry_selection.py` collects the canonical population and executes
  only the dependency-owned retry files. `causal_dependency.py` and `causal_failures.py` derive
  exact-node dependencies and suppress or report dependent failures. `cadence_runner.py` is the
  non-accepting Dagger route for scheduled, provider-bump and migration evidence.
  `pytest_phase_reporter.py` records node outcomes and phase timings.
- **Instruction corpus.** `curation_doctrine.py` holds the registry of retired curation sentences
  and the statements every canonical instruction source must make; a test reads them to check the
  shipped corpus.

## Operating Model

Use the ordinary bootstrap for local pytest. Certifying entry goes through
`prepare_certifying_pytest_bootstrap`, which requires Dagger admission before any candidate setup.
Running either route does not by itself supply acceptance. The lane, lifecycle and dependency
validators describe the current source and the configured evidence.

## Local Invariants And Traps

- Ordinary pytest setup has no certifying or external-service authority. Dagger admission is
  mandatory at the certifying composition boundary.
- Owned mutable module state is restored after each test, and a leak fails the test that caused
  it. Seeded ordering uses its own random generator and does not touch the process-global one.
- The dependency facts are derived from source only. Lifecycle metadata can describe ownership but
  cannot make itself complete.
- Lane membership and catalog coverage are exact: a missing, stale or conflicting declaration is a
  finding.
- Both test catalogs must be in canonical form. A list that is out of order, a duplicate line, a
  list not written one path per line and a row that is out of order are findings of the loaders,
  and each such finding names the `--write` command. The command orders, removes duplicates,
  derives consumer lists and removes the lines of files that no longer exist; it never adds or
  removes a row and never assigns a lane.
- Retry selection executes only dependency-owned files of the collected population.
- Causal suppression needs exact, source-derived node dependencies.

## The Two Test Catalogs: The Consumer Oracle, Canonical Form And The Rewrite

This route owns the code that reads and writes the two test catalogs:
`mcp/tests/evidence-lifecycle.toml` (the governed test artifacts and their consumers) and
`mcp/tests/test-evidence-lanes.toml` (the lane of every test file).

| Check | Where it lives | The question it answers | Its repair |
| --- | --- | --- | --- |
| the consumer oracle | `load_evidence_inventory` in `evidence_lifecycle.py` | does the lifecycle catalog agree with the source tree: each declared consumer list equals the consumers the source shows, every governed file has a row and every row a file | the `--write` command derives the lists; a row is added or retired by hand |
| the lane population | `load_lane_manifest` in `lane_manifest.py` | does every current test file have exactly one lane, and is every listed path a current test file | the lane line is added by hand; the `--write` command removes the line of a file that no longer exists |
| canonical form | `catalog_canonical.py`, called by both loaders | are rows and lists in the one fixed order, without duplicates, one path per line | the `--write` command |

No test pins a byte digest or a row count of either catalog. What the source tree can prove is
computed each time the loaders run.

`python -m agents_remember_test_support.testing.evidence_lifecycle --project-root .` validates both
catalogs: it loads the lifecycle catalog and then the lane manifest, on one source graph that it
derives once. With `--write` it rewrites both to canonical form: it orders the rows and lists,
removes duplicate lines, sets the `consumers` list of an `exact` or `exact-source` row to the
derived set, and removes each lane line and consumer line whose file does not exist. A row for
which the source tree shows no consumer keeps its list as written, and the command says so. The
command adds and removes no row, never assigns a lane, and writes nothing when it refuses: for a
catalog that cannot be parsed, for incomplete or ambiguous dependency facts, and for a table
header or a list in a form its line rewrite does not read.

Git merges both catalogs by union (`.gitattributes`), so two changes that add lines to the same list
do not conflict. A union merge can leave a line twice, leave a list out of order, bring back a line
that one side deleted, or interleave two rows that two changes added at the same place. The loaders
refuse a duplicate, an unordered list and the line of a file that no longer exists, and name the
command. A file that no longer parses is refused by both loaders, by the command and by the pytest
start-up in `mcp/tests/conftest.py`, each with the sentence that two rows may have been interleaved
and that the file is restored from the landed commit. The lane loader runs at every test
collection. The lifecycle loader runs in the validator command (Git hook gate, quality plan), in
the selection graph and in `test_the_repository_catalogs_are_in_canonical_form`, which a default
unit run includes.

A change that adds a test file adds one lane line and runs the command. The cases for all of this
are in `mcp/tests/test_evidence_catalog_canonical_form.py`; the case that the oracle alone refuses a
canonical but incomplete catalog is in `mcp/tests/test_evidence_catalog_gate_boundaries.py`.

## File-Level Onboarding Map

The generated route index lists the source files of this route and their cards.

## Evidence

- The ordinary bootstrap carries no certifying or external-service capability. [1]
- Certifying setup admits Dagger before it resolves the candidate. [2]
- Retry execution keeps only the dependency-owned files of the collected population. [3]
- The rewrite computes both new catalogs before it writes either. [6]
- The command validates both catalogs on one cached source graph, or rewrites them with `--write`. [7]
- The union merge attribute for both catalogs. [8]
- A leaked change of owned module-level state fails the test. [9]
- Seeded ordering uses its own random generator. [10]

- The curation-doctrine registry and the statements a canonical instruction source must make. [13]
- Canonical skill copies and their harness mirrors are the synchronization owner's. [14]

- The lifecycle loader starts with the canonical-form findings and then validates the catalog against the source tree. [15]
- The lane loader reports a lane list that is not canonical and compares the declared files with the test modules. [16]
- The registry of retired curation sentences and required statements. [17]
- The refusal that both loaders and the start of a test run give for a file that does not parse. [18]

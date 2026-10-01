# mcp/tests/test_knowledge_ingest_publication_route.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

**The ordinary authoring and publication route, driven through the real command line** — the
regression surface for `ICR-R20@v1`, and the case set that makes the requirement's forbidden inference
measurable instead of stated.

The ingest exists, it writes, and its publication owner is real. What these cases measure is the
*route*: whether the curator's ordinary run reaches that owner at the repository's one published
location, what the run admits is standing there, and whether a reader then selects the dataset the
write reported. Every case drives `agents-remember knowledge-ingest` through the umbrella `main` —
the surface the canonical curator instructions carry — over a **production-shaped enclosure**: a real
code line with its own work branch, a real external memory repository, a real Git memory **worktree**
cut from it, and a contract recording all of them under a real coordination root. The declared
location is resolved by the read route's own owner rather than restated in the fixture
(`_declared_location` `:226-234`), so the fixture cannot quietly agree with the implementation about a
path neither of them should be computing.

**Eleven cases, and the six user operations plus one refusal family they cover**, each named in the
module's own docstring:

| Operation | Case |
| --- | --- |
| the ordinary first publication | `test_the_ordinary_route_publishes_to_the_declared_location_and_reads_it_back` (`:263-312`) |
| a custom candidate is the one reviewed **and** published | `test_a_custom_candidate_is_the_one_the_ordinary_route_publishes` (`:315-350`) |
| a partial refusal names each entry and publishes only what committed | `test_a_partial_refusal_names_each_entry_and_publishes_only_what_committed` (`:353-400`) |
| the explicit update, and the earlier truth surviving into the successor | `test_an_explicit_update_replaces_the_dataset_the_run_forked_from` (`:403-484`) |
| the exact retry: `no_change`, bytes unmoved, identity still confirmed | `test_an_exact_retry_republishes_no_change_and_still_reads_back_confirmed` (`:487-530`) |
| no destination named — exit zero is not a publication claim | `test_a_run_that_names_no_destination_states_that_it_published_nothing` (`:533-557`) |
| a refused publication leaves the destination untouched and reads nothing back | `test_a_refused_publication_leaves_the_destination_and_reads_nothing_back` (`:560-605`) |
| two contradictory destination selections refused by name before anything is read | `test_two_destination_selections_are_refused_by_name_before_anything_is_read` (`:608-641`) |
| a destination selected without a publication says which reason it was | `test_a_destination_selected_without_a_publication_says_so_in_the_route_line` (`:644-699`) |
| an expectation with no destination selector refused by name | `test_an_expected_destination_without_a_destination_is_refused_by_name` (`:702-732`) |
| an unresolvable declared location refused rather than guessed | `test_a_declared_location_that_cannot_be_resolved_is_refused_rather_than_guessed` (`:735-756`) |

## Code Commentary

### Logic

Module surface (ranges are this candidate's extents):

- Module docstring (lines 1-38) — the six operations and the refusal family, stated as the user
  operations they are.
- Import block (lines 40-82) — the two declared-route owners the fixture resolves through
  (`published_dataset_path`, `resolve_published_intent`, `contract_context`), the shipped CLI `main`,
  the mounted read surface (`knowledge_read_payload`, `ReadToolRequest`) and the real store reader
  (`open_read_only_database`), and **the ingest-list fixture module's own helpers** (`:63-82`) rather
  than a second support module.
- `OrdinaryEnclosure` (dataclass, lines 94-112) — the four roots the contract really records:
  `memory_repo` is the canonical **external** memory repository and `memory_worktree` is a real Git
  worktree of it on this leaf's work branch. That pair is the point of the fixture: the coordination
  context resolves the first as the memory layer and the contract's own worktree as the effective
  memory root, so the declared location is the memory line the task can actually commit rather than a
  scratch directory that merely looks like one.
- `_ordinary_enclosure` (function, lines 115-155) — builds that world and then the contract recording
  it, including the leaf's own commit on its work branch (a leaf always stands on work the base
  commit does not hold, and the ingest resolves its citations against that line).
- `_contract_text` (function, lines 158-204) — the one leaf contract carrying exactly the cells this
  enclosure has.
- `_ordinary_argv` (function, lines 207-223) — the shipped invocation the canonical curator
  instructions carry, aimed at this enclosure.
- `_declared_location` (function, lines 226-234) — the location this route must publish to, resolved
  by the **read** route's own owner.
- `_labels` (function, lines 237-244) — every obligation label a dataset actually holds, read from the
  file itself rather than from the report.
- `_statements` (function, lines 247-260) — the statements the **mounted** read surface answers with,
  at the dataset's own snapshot.
- `test_*` cases (lines 263-756) — as tabled above.

**The measurement order is the route's own order.** The first case measures four facts in sequence:
the destination the run selected is the one the read route declares, the publication owner reported
`published` for it, the route's independent read-back confirms that exact identity, and the mounted
read surface answers from that dataset. Each later case moves one variable — the candidate directory,
the entry set, the baseline, the retry, the destination selection — and measures the same four facts
where they apply.

### Conventions

Ordinary `unit-regression` evidence-unit module: `pytestmark = pytest.mark.evidence_unit` (`:84`), no
integration marker, no docker, no network — a `tmp_path` world with real Git repositories and real
APSW databases. It imports the existing ingest-list fixture module instead of introducing a third
support module, which is why its catalog delta is a *consumer* change only (see below).

### Invariants And Boundaries

- **Nothing asserts a prebuilt payload in place of the production composition.** Every case runs the
  shipped entry point and reads the report it printed, the dataset on disk, or the mounted read
  surface's answer.
- **The declared location is derived, never restated.** `_declared_location` calls the read route's
  own owner, so a fixture that drifted from the implementation would fail rather than agree.
- **A refusal is measured, not assumed.** The invocation refusals assert the exit code, the named
  message and that no candidate was created on the way; the refused publication asserts the
  destination bytes are unchanged.
- **`None` is a fact with a reason.** The two "selected a destination, published nothing" runs assert
  both the null `publication`/`publishedIdentity` and the route line's own reason, and that the
  location was never created.
- **No artifact and no contract of its own.** The module composes
  `mcp/tests/snapshot_lifecycle_test_support.py` (reached through the fixture module it imports) and
  the existing ingest-list fixtures, so the evidence census population stays at **sixteen contracts /
  sixty-six artifacts** and only the two `consumer_scope = "exact"` rows gained the path.

### Todos

None requested of this card. One boundary recorded rather than carried as a task: the case set is
ordinary unit evidence, so the pinned Dagger certification graph and the browser acceptance path are
outside it, and the two-consecutive-task assembled journey is `ICR-R25@v1`'s rather than this module's
— the continuity it measures here (task B forking A's published dataset and republishing onto it) is
the same operation at one enclosure's scale.

## Evidence

### Repo-Internal References

- **The one ordinary run: the declared destination receives the candidate, the read-back confirms the exact identity, and the mounted read surface answers from that dataset.** [1]
- **The requirement's forbidden inference made measurable: a committed entry beside exit zero, and a report that states the absence in its own field rather than leaving it to be inferred from a null.** [2]
- **The boundary case: one list, one committed and one refused entry, both named, only what committed published.** [3]
- **The explicit update — the identity replaced is the one this run read from its own baseline, and the earlier truth survives into the successor.** [4]
- The safe retry, measured on the file rather than asserted from the exit code. [5]
- The custom candidate that must be the one reviewed and published, with no conventional path invented. [6]
- The refusal family: a refused publication, two contradictory selections, an absorbed expectation, and an unresolvable location. [7]
- **The production-shaped enclosure and the contract that records it, including the leaf's own commit on its work branch.** [8]
- **The four helpers that keep the fixture from agreeing with the implementation, and the shipped invocation the canonical instructions carry.** [9]
- **The read route's owners the fixture resolves the declared location and the read-back through — the same owners the production route uses, which is what makes the fixture an independent side.** [10]
- The shipped entry point every case drives, and the two real readers it measures through. [11]
- **The existing fixture module this one composes instead of introducing a third support module — the reason its catalog delta is a consumer change only.** [12]
- **The lane row this module occupies, and the two governed consumer rows it joined.** [13]
- **The catalog digest the two consumer rows moved, and the counts they do not move.** [14]
- The production route these cases are the regression surface for. [15]

### Cross-Repo References

No meaningful cross-repo references found: the whole fixture world is built inside one `tmp_path`, and
the enclosures it builds are this repository's own.

No meaningful cross-repo references found.

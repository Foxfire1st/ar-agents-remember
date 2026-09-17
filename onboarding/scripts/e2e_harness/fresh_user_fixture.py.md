# scripts/e2e_harness/fresh_user_fixture.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `scripts/e2e_harness/fresh_user_fixture.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T10:50+02:00 |
| lastVerifiedCommitHash | `d8ed8c21644f96fd1138ae9fd4c0e5e5e93c1c03` |
| lastVerifiedCommitDate | 2026-09-17T10:09:37+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l14-ar` uncommitted source; base `0346da9c572e1eb913a8eb4130e9a9e9d37343c8` |
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[scripts/e2e_harness/overview.md](overview.md)

## Purpose

Create the **disposable clean-room repositories** the fresh-user acceptance runs against — two
repositories, from nothing, each carrying the shape the requirement packet names:

| Fixture | Shape |
| --- | --- |
| `spear-not-main` | the spear branch is `dev`, and the tree carries a source file **over the per-file cap** plus a vendored/generated tree the exclusion register excludes. This is the fixture that would have made the pre-ruling citation index refuse outright. |
| `plain-main` | an ordinary `main`-spear repository for the default path. |

**These are not the developer's repositories.** The module's own `WHAT IS DELIBERATELY ABSENT`
section is the contract: nothing here reads the developer's real repositories, this master's
coordination tree, `ar-coordination/memory-repos/**`, or any machine-local state. Every path is
under the run root the caller supplies and every Git repository is created by this module — which
is what "clean environment" means for this packet, and why the module takes a `root` and never a
repository path.

## Code Commentary

### Logic

`create_fresh_user_fixture(root, ...)` builds one fixture under `root`: the code repository, the
memory root, the coordination root, the authority settings, and the Git topology. `FreshUserFixture`
is the frozen result, and its two properties name the branches the rest of the harness needs —
`master_branch` (`ar/<repo_id>-master`, the atomic master's series branch that the master's own
start creates and the leaf cuts) and `memory_settings` (`system/settings.json`).

`SPRINT_BRANCH` is `ar/super` and is deliberately **neither** `main` (the code repository's
default) nor the spear (the branch the memory repo is founded on), because the integration-branch
authority refuses a sprint that claims either.

`OVERSIZED_BYTES` is `4 * 1024 * 1024 + 1` — the shipped per-file cap **plus one** — so the
over-cap fixture crosses the real bound rather than a number restated in the harness. `_sparse`
truncates the file to that length without writing the bytes.

Two writers persist the state later steps read:

- `write_exclusion_register` persists the exclusion review's agreed rules into the fixture's
  `system/settings.json`, under the same `onboarding.pathRules.exclude` key the storage resolver
  and the citation register both honour.
- `write_thin_bootstrap` writes the `c-03` thin-bootstrap content the first memory commit must
  **not** contain (that absence is `invariant-1`).

`git(root, *args)` runs one fixture Git command through `subprocess` with `check=False` and raises
an `AssertionError` carrying the real stderr on failure: a failure here is the fixture's own, so
it is surfaced rather than swallowed.

### Conventions

- Every value that must track a shipped bound is derived from that bound (`OVERSIZED_BYTES`), not
  restated as a literal.
- The fixture is `frozen`; a case that wants a variant builds another fixture rather than mutating
  one.
- This module is a **governed evidence artifact**: `scripts/e2e_harness/**` is a permanent
  evidence-support root, so it carries an `[[artifact]]` row in `mcp/tests/evidence-lifecycle.toml`
  (`owner: fresh-user-acceptance`, `introduced_by: 260915-CAPS-L14`) with a real consumer and an
  executable replacement node.

### Invariants And Boundaries

- The fixture owns everything under its own run root and reads nothing outside it.
- The over-cap fixture must genuinely cross `MAX_SOURCE_FILE_BYTES`; the plain fixture must stay
  inside every cap. Both are asserted in `mcp/tests/test_fresh_user_harness.py`, so an edit here
  cannot quietly stop producing the shape the scenario needs.
- The fixtures are disposable: the run root is a temporary directory unless the caller names one.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one construction point for a disposable fixture repository, memory root and authority settings. | `create_fresh_user_fixture` | scripts/e2e_harness/fresh_user_fixture.py:79-177 |
| The frozen fixture value and the two branches the harness needs. | `FreshUserFixture`; `master_branch`; `memory_settings` | scripts/e2e_harness/fresh_user_fixture.py:39-62 |
| The sprint branch is neither `main` nor the spear, because the authority refuses both. | `SPRINT_BRANCH` | scripts/e2e_harness/fresh_user_fixture.py:32-36 |
| The oversized source is the shipped per-file cap plus one byte. | `OVERSIZED_BYTES` | scripts/e2e_harness/fresh_user_fixture.py:30-31 |
| The truncating writer that materialises it without copying bytes. | `_sparse` | scripts/e2e_harness/fresh_user_fixture.py:73-76 |
| A fixture Git failure is surfaced with its real stderr rather than swallowed. | `git` | scripts/e2e_harness/fresh_user_fixture.py:65-70 |
| The exclusion review's rules are persisted under the key every register reader honours. | `write_exclusion_register` | scripts/e2e_harness/fresh_user_fixture.py:180-207 |
| The `c-03` bootstrap content whose absence is `invariant-1`. | `write_thin_bootstrap` | scripts/e2e_harness/fresh_user_fixture.py:210-237 |
| The per-file cap the fixture must cross. | `MAX_SOURCE_FILE_BYTES` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:23-23 |
| The cases that pin the fixture's shape. | `test_the_over_cap_fixture_really_crosses_the_cap`; `test_the_plain_fixture_stays_inside_every_cap`; `test_the_fixture_owns_everything_under_its_own_run_root` | mcp/tests/test_fresh_user_harness.py:118-186 |

## Cross-Repo References

No sibling-repository contract defines these values.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T10:50+02:00 — 260915-CAPS-L14 curator: created this card for the harness module the leaf adds. Records the two fixtures and their shapes, that the oversized source is the shipped per-file cap **plus one**, why the sprint branch is neither `main` nor the spear, and — in its own section — the contract that matters most for a reader: **these are disposable repositories created from nothing under the run root, not the developer's repositories**, because nothing here reads the developer's real repositories or any machine-local state. Notes the module is a governed evidence artifact with a lifecycle row, a real consumer and an executable replacement node. Verification metadata is left at this leaf's synced base `0346da9c` with a `reviewedWorkingCandidate` row, because the candidate is deliberately uncommitted — the governed closeout stamps the real code commit and no hash or digest was invented here.

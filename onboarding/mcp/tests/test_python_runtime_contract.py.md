# mcp/tests/test_python_runtime_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_python_runtime_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `eb05a872780112640359232063168639d20fa87b`|
| lastVerifiedCommitDate | 2026-09-03T06:19:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Pins one exact Python 3.13 runtime contract across package metadata, CI, release, Dagger, and the
interpreter that actually executes the test population — and, since the root-owned canonical Python
bootstrap repair (commit eb05a8727801), hermetically proves the installer's builder-clone
publication contract: full clone, atomic no-clobber publication, failed-clone cleanup, exact
reuse, fail-closed invalid/foreign paths, and competing/racing publishers.

## Code Commentary

### Logic

`_contract` reads the canonical runtime environment file. The metadata test requires 3.13.15 and
the bounded `>=3.13,<3.14` package range everywhere, while explicitly rejecting the old 3.11 and
3.12 classifiers. The Linux capability test invokes the canonical runtime probe with the current
test interpreter and requires both native pidfd APIs.

The hermetic installer layer builds an isolated fixture (`_RuntimeFixture`/`_runtime_fixture`,
lines 33-69) with a `git` shim (`_GIT_SHIM`, lines 96-158) that fabricates clone/checkout/commit
records, a `sha256sum` shim, and `AR_TEST_*` environment hooks, then runs
`scripts/install-python-runtime.sh` in a temporary prefix/cache/tooling layout
(`_run_installer`, lines 72-93). The tests prove: a fully cloned builder is validated and
atomically published and then reused (`test_runtime_builder_is_fully_cloned_atomically_published_and_reused`,
line 203); a failed clone leaves no canonical or staging checkout (line 236); an existing foreign
builder is refused and preserved (line 254); competing publishers adopt only the validated winner
(line 270); and a foreign directory/symlink publication race fails closed (line 294; the shim can
be forced to race a foreign directory or symlink onto the target while clones contend through a
barrier).

### Conventions

The test compares exact durable text at configuration boundaries and parses the probe's structured
JSON for runtime capabilities. A version string alone never counts as Linux compatibility proof.
Installer behavior is proven against shims, never against a live build.

### Invariants And Boundaries

- CI, release, Dagger, and package metadata cannot silently select different Python minors.
- Linux acceptance fails if either native pidfd API is absent.
- The test does not permit system Python, a compatibility wrapper, or a signaling fallback.
- A canonical builder is cloned fully (no promisor/blobless clone), validated against the pinned
  commit and version definition, and published atomically with no-clobber semantics; a losing
  publisher validates and adopts the winner instead of overwriting, deleting, or trusting a target
  blindly.
- Dagger owns certifying execution.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; repository configuration is the authority, and
the governing task artifacts document the bootstrap repair the hermetic tests pin. The root-owned
canonical Python bootstrap repair, as documented in the L09 worker handover (Changed surfaces
and behavior), hermetically proves full-clone publication, failed-clone cleanup, valid reuse,
fail-closed invalid/foreign paths, competing publishers, and foreign directory/symlink
publication races. The 2026-09-03T06:20:00+02:00 master decision (task.md, LAND ROOT-OWNED
CANONICAL PYTHON BOOTSTRAP REPAIR AND RELEASE L09 VERIFICATION.) landed the bootstrap repair;
it advances no requirement leaf and does not satisfy L12.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| One exact Python 3.13.15 contract is required across package, CI, release, and Dagger. | `test_runtime_contract_has_one_exact_supported_minor` | mcp/tests/test_python_runtime_contract.py:159-179 |
| The executing Linux interpreter must pass the canonical native-pidfd probe. | `test_current_test_interpreter_passes_the_canonical_capability_probe` | mcp/tests/test_python_runtime_contract.py:180-202 |
| The hermetic fixture fabricates git/sha256sum behavior and drives the installer with isolated roots. | `_runtime_fixture`; `_run_installer`; `_GIT_SHIM` | mcp/tests/test_python_runtime_contract.py:42-93; mcp/tests/test_python_runtime_contract.py:96-158 |
| Full-clone publication, failed-clone cleanup, reuse, foreign-path refusal, and publisher races are proven. | `test_runtime_builder_is_fully_cloned_atomically_published_and_reused`; `test_failed_builder_clone_leaves_no_canonical_or_staging_checkout`; `test_existing_foreign_builder_is_refused_and_preserved`; `test_competing_publishers_adopt_only_the_validated_winner`; `test_foreign_builder_publication_race_fails_closed` | mcp/tests/test_python_runtime_contract.py:203-235; mcp/tests/test_python_runtime_contract.py:236-253; mcp/tests/test_python_runtime_contract.py:254-269; mcp/tests/test_python_runtime_contract.py:270-293; mcp/tests/test_python_runtime_contract.py:294-316 |
| The contract consumed by the installer and probe lives in the canonical environment file. | "scripts/python-runtime-contract.env" | mcp/tests/test_python_runtime_contract.py:16-25 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The proof is confined to the Agents Remember candidate. | — | — |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): documented the new hermetic installer-contract tests (full clone, atomic no-clobber publication, cleanup, reuse, foreign-path refusal, publisher races) and refreshed the citation anchors for the runtime-contract/capability tests. Verification metadata rebased from `60e429d1` to the bootstrap repair owning commit.

- 2026-08-29T16:10+02:00 — Created for the project-wide Python 3.13.15 cutover and native-pidfd
  acceptance boundary. Verification remains closeout-owned.

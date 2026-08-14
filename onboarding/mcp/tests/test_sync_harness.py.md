# mcp/tests/test_sync_harness.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_sync_harness.py`           |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T06:30+02:00                     |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd` |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|
| governingOverview      | `overview.md`                           |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_sync_harness.py` is what turns `scripts/sync-harness.py` from a script somebody has
to remember to run into a checked invariant. **The first test is the enforcing one:** it
fails when any generated harness file in this checkout no longer matches
`scripts/harness/`.

## Code Commentary

### Logic

`load_script` imports `scripts/sync-harness.py` by path with `importlib.util`. The module
is registered in `sys.modules` **before** `exec_module`, because `@dataclass` resolves
its defining module through `sys.modules` at class-creation time and the generator's
frozen dataclasses would otherwise fail to build.

| Test | What it pins |
| --- | --- |
| `test_every_generated_harness_file_matches_its_source` | the enforcing one: no generated file across the nine trees has drifted (content **or** mode) |
| `test_no_two_harnesses_claim_the_same_destination` | two `Harness` entries cannot silently overwrite each other's output |
| `test_every_declared_fragment_exists_in_its_library` | a target cannot name a fragment that does not exist |
| `test_every_starter_carries_the_shared_body` | a target that dropped a `SHARED_STARTER_FRAGMENTS` entry would regrow a private copy |
| `test_generated_programs_parse_and_have_an_entry_point` | every generated `.py` parses and has exactly one `__main__` guard |
| `test_drift_is_reported_for_content_and_for_mode` | `describe_drift` reports missing files, content diffs, and a wrong mode, in a temporary directory |

The last test is the only one that touches the filesystem outside the repository: it
walks a probe file through missing → matching → hand-edited → wrong-mode and asserts each
verdict, including the exact `mode is 0755, expected 0644` message.

### Invariants And Boundaries

- This suite is the **third** enforcement point for harness drift, not the only one:
  `.githooks/_gate.sh` runs `python3 scripts/sync-harness.py --check` in both the fast and
  the full tier. The test exists so drift still fails for a contributor who has not
  installed the hooks, and in CI.
- Drift means content **or** mode. Generated files are `0o644`; the executable bit had
  already drifted onto two of the four hook scripts before the generator normalised it.
- The tests read the real repository tree (`REPO_ROOT`), so they certify this checkout
  rather than a fixture.
- The suite does not test the *behaviour* of a rendered starter package — it tests that
  the shipped copies are exactly what the single source produces.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The generator under test, including `describe_drift`, `generated_files`, and the `HARNESSES` table. | `describe_drift` | scripts/sync-harness.py:647-666 |
| The two fragment libraries whose declared names this suite validates. | `command_string`; `hook_specific_output` | scripts/harness/render_starter.py:46-49; scripts/harness/session_start_hook.py:28-34 |
| Both hook tiers run the same `--check`. | "scripts/sync-harness.py" | .githooks/_gate.sh:81-81 |
| The classification of shared versus per-harness content that the generator encodes. | `# Harness starter package source` | scripts/harness/README.md:1-94 |
| The sibling generator suites this one sits beside. | `SyncRuntimeTests` | mcp/tests/test_sync_runtime.py:23-84 |

## Update History

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 5 citation rows covering 6 source references and preserved verification metadata.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 created the harness generator's test suite
  (requirements L2-R12 and L2-R15). Recorded that drift is a test failure rather than a
  remembered chore, that drift covers mode as well as content, and the `sys.modules`
  registration required to import a hyphenated script that defines dataclasses.
  Verification metadata is pinned to the leaf's reformat commit until closeout stamps the
  code commit.

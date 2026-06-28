# test_harnesses.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harnesses.py`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-18T21:27+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_harnesses.py` covers the harness launch registry (`serving/harnesses.py`, slice 6e-2b): the
curated supported set, `find_harness`, and detection (`is_detected` / `detect_harnesses`) driven by
an injected `which` so the suite is deterministic regardless of what is installed on the test box.

## Code Commentary

### Logic

A `_which(*installed)` factory returns a `shutil.which` fake that resolves only the named commands.
`HarnessRegistryTests` assert the supported ids are exactly `["claude", "codex", "pi"]`, each harness
has a name + an `argv` equal to `(command,)`, and `find_harness` returns the known harness / `None`
for an unknown id. `DetectionTests` assert `is_detected` reflects the injected `which`, and
`detect_harnesses(which=_which("claude","codex"))` marks claude+codex detected and pi not, in
registry order (a full `DetectedHarness` list equality).

### Conventions

Inserts `mcp/src` on `sys.path` (suite idiom). The `assert x is not None` narrowing keeps pyright
happy on the `find_harness` `Harness | None` returns. Detection is exercised purely through injected
fakes here; the *endpoint* detection path (`GET /api/harnesses`, monkeypatching `shutil.which`) lives
in `test_terminal_ws.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The registry under test. | [serving/harnesses.py](agents-remember/mcp/src/agents_remember/serving/harnesses.py) |
| The endpoint-level harness tests (GET detection + the harness opener). | [test_terminal_ws.py](agents-remember/mcp/tests/test_terminal_ws.py) |

## Update History

- 2026-06-18T21:27+02:00 — Created for task 6 slice 6e-2b: covers `serving/harnesses.py` (the curated
  set, `find_harness`, `is_detected`/`detect_harnesses` via an injected `which`). Verification
  metadata pinned to the task base until closeout stamps the 6e-2b code commit.

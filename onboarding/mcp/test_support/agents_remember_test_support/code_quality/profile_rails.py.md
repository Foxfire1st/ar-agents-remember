# mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python quality verification overview](overview.md)

## Purpose

Repository-owned executable adapters for the certification-profile Python rails: it translates one
`quality-config` / `selection-ownership` / `python-suite` / `python-crap` /
`python-diff-coverage` / `verify-teardown` rail invocation into the check.py config and
execution surface, and L19 binds the exact repository selector result into every rail config.

## Code Commentary

### Logic

`build_parser` exposes the six rail subcommands. `_profile_config` rebuilds check.py argv from
the rail arguments, derives the config via `check.config_from_args`, and
`_require_exact_scope` validates the selector's published `repository-selector-result/v2`
JSON against the exact repository-owned derivation (`profile_selection.selection_payload`) and
against the derived executable rail scope; the validated `selection.selectionDigest` is stamped
back into the config via `dataclasses.replace(config, selection_digest=...)`. The
`selection-ownership` and `quality-config` rails run the same exact-scope proof without
executing tests. `_run_python_suite` runs the pytest rail (with retry/causal continuation),
and `_run_post_coverage` dispatches CRAP or diff-coverage from the exact suite artifacts.
`_verify_teardown(summary, proof)` consumes the actual clean-room summary and every listed replication report. A passed run requires the exact `L5-C10` checkpoint to pass in each report; unsafe report basenames and missing or malformed observations refuse. It writes `teardown-proof/v1` with the summary SHA-256, each report SHA-256 and its observed checkpoint. A skipped scenario emits `status="not-applicable"` with no replication observations. The adapter validates the listed runs; the scenario producer owns the configured two-replication population.

### Conventions

The `verify-teardown` CLI requires both `--summary` and `--proof`; it uses the same Dagger admission boundary as the Python rails. Persisted proof bytes are a declared rail artifact, while printed PASS remains diagnostic output.

### Invariants And Boundaries

- Every rail requires the Dagger admission capability; refusals surface as
  `repository certification rail refused: ...` with exit 1.
- The selector contract must match the repository-owned derivation byte-for-byte; a mismatch
  refuses before any test command.
- Only the exact immutable selection digest may enter the retry identity.
- Memory-cap bytes must be non-negative; teardown summaries must be schema-checked.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

These source owners establish the current behavior and the stated fixture boundaries.

| Finding | Anchor | Source |
| --- | --- | --- |
| The teardown command requires a proof destination. | `build_parser` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:30-42 |
| Executable scope receives the exact selector digest. | `_profile_config` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:55-82 |
| Published selection is compared with its repository-owned derivation and executable scope. | `_require_exact_scope` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:85-121 |
| The Python rail handles declared retry and causal continuation without changing ownership. | `_run_python_suite` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:128-205 |
| CRAP and changed coverage consume the exact suite artifact. | `_run_post_coverage` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:225-241 |
| Actual report bytes must carry passing L5-C10 checkpoints; skipped applicability is explicit. | `_verify_teardown` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:244-295 |
| The persisted proof binds summary bytes and observed replication reports. | `_write_teardown_proof` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:298-308 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Documented required teardown-proof publication, exact L5-C10 consumer identity, observed report hashes and explicit not-applicable output.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 exact-scope binding — `_require_exact_scope` validates the v2 selector result and
  `_profile_config` stamps `selection.selectionDigest` into the rail config.
  Verification is pinned to the owning commit.

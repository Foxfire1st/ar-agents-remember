# mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
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
`_verify_teardown(summary, proof, source_selection)` loads the admitted ambient-role decision. A not-applicable decision requires the summary to be absent, then writes a passing zero-start proof bound to the decision digest with no replications. An applicable decision requires exactly two ordered, passing, non-retry reports. Each report and the summary must match the frozen candidate tree, base commit, mode and selected paths. Every report must carry a passing `L5-C10` checkpoint; unsafe basenames and malformed or missing evidence refuse. The proof binds the actual summary and replication bytes by SHA-256.

`_paths` canonicalizes scope comparison by sorting each path's POSIX string. `Path` component ordering differs from the selector's string ordering for siblings such as `conversation/` and `conversation-library/`; equal populations now compare in the same order. Sorting retains duplicates, so missing, extra or repeated paths still refuse before pytest.

### Conventions

The `verify-teardown` CLI requires `--summary`, `--proof` and `--source-selection`; it uses the same Dagger admission boundary as the Python rails. Persisted proof bytes are a declared rail artifact, while printed PASS remains diagnostic output.

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
| The Python rail handles declared retry and causal continuation without changing ownership. | `_run_python_suite` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:130-207 |
| CRAP and changed coverage consume the exact suite artifact. | `_run_post_coverage` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:227-243 |
| Actual report bytes must carry passing L5-C10 checkpoints; skipped applicability is explicit. | `_verify_teardown` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:246-297 |
| The persisted proof binds summary bytes and observed replication reports. | `_write_teardown_proof` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:349-359 |
| Canonical POSIX-string order aligns equivalent populations without deduplicating them. | `_paths` | mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:131-134 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History

- 2026-09-06T23:08:28+00:00 — Reconciled retained source behavior and fixture limitations for IAS recovery; prior verification pins retained.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `_write_teardown_proof` repointed to mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:349-359. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `_paths` repointed to mcp/test_support/agents_remember_test_support/code_quality/profile_rails.py:131-134. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Documented canonical string ordering while preserving exact scope membership, duplicate refusal and the existing teardown producer contract. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Documented required teardown-proof publication, exact L5-C10 consumer identity, observed report hashes and explicit not-applicable output.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 exact-scope binding — `_require_exact_scope` validates the v2 selector result and
  `_profile_config` stamps `selection.selectionDigest` into the rail config.
  Verification is pinned to the owning commit.

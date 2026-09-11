# scripts/check-python-runtime.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `scripts/check-python-runtime.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T16:10+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[repository overview](../overview.md)

## Purpose

Provides the one executable capability and provenance check for an exact Agents Remember Python
runtime, emitting a structured proof record on success and an actionable refusal on mismatch.

## Code Commentary

### Logic

The probe requires an exact major/minor/patch version and optionally an exact base prefix. Linux
pidfd mode requires callable `os.pidfd_open` and `signal.pidfd_send_signal`. It records source URL,
source digest, builder commit, compiler, configure arguments, executable/base-prefix identity,
standard-library module health, and a content-derived build fingerprint as JSON.

### Conventions

The command is both validator and evidence producer. All required facts are observed from the exact
running interpreter; no build is accepted from its version label alone.

### Invariants And Boundaries

- A version, prefix, or pidfd mismatch fails loudly before a proof is emitted.
- Importing `ctypes` here proves the standard-library module is healthy; it is not a syscall wrapper
  and the probe never implements signaling.
- No third-party compatibility package, `killpg` fallback, or platform/filename guess is accepted.
- Provenance fields describe the supplied build inputs and are folded with observed build identity.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this executable contract reports the exact
runtime it observes.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required to interpret the structured internal proof. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact version, prefix, and native pidfd capability mismatches are actionable refusals. | `_refuse`; `main` | scripts/check-python-runtime.py:24-65 |
| Provenance and observed build identity produce one deterministic fingerprint and JSON report. | `build_identity`; `build_fingerprint`; `report` | scripts/check-python-runtime.py:67-107 |

## Cross-Repo References

No meaningful cross-repository implementation source governs this probe.

| Finding | Anchor | Source |
| --- | --- | --- |
| The probe executes solely against the selected local interpreter. | — | — |

## Update History

- 2026-08-29T16:10+02:00 — Created for exact Python 3.13.15 provenance, standard-library, and
  native-pidfd capability proof. Verification remains closeout-owned.

# scripts/install-python-runtime.sh

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `scripts/install-python-runtime.sh` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T16:10+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[repository overview](../overview.md)

## Purpose

Installs the official CPython 3.13.15 source release under a dedicated Agents Remember data prefix
using an exact pinned python-build revision and checksum-bound source archive.

## Code Commentary

### Logic

The script validates absolute, version-suffixed installation and cache/tooling paths. An existing
runtime is reused only after the full capability/provenance probe; any other existing prefix is
refused. It downloads over HTTPS when needed, verifies the official archive digest both before and
after caching, checks out the exact python-build commit, verifies that its version definition binds
the same URL and digest, compiles into the dedicated prefix, and probes the installed interpreter.

### Conventions

Every mutable external input is converted into an exact identity before compilation: source URL and
SHA-256, builder repository and commit, versioned prefix, and observed installed runtime.

### Invariants And Boundaries

- `/usr/bin/python` is never replaced or repointed.
- The source archive must match the approved digest; a cached archive is not trusted implicitly.
- Another uv-managed standalone Python or unverified prebuilt archive is not an admissible runtime.
- A foreign or incomplete prefix is refused rather than overwritten.
- Interpreter, source cache, builder checkout, standard library, and compiled artifacts stay
  outside the Git repository.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the canonical runtime contract carries the
approved authoritative URL, digest, and builder identity.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required beyond the checksum-bound contract consumed by this script. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact destination validation and full proof govern existing-runtime reuse. | "refusing incomplete or foreign prefix" | scripts/install-python-runtime.sh:42-73 |
| The official archive is checksum-bound in the canonical contract, downloaded securely, and verified before and after caching. | "https://www.python.org/ftp/python/3.13.15/Python-3.13.15.tar.xz"; "curl --fail --location --proto '=https' --tlsv1.2"; "cached source digest mismatch" | scripts/python-runtime-contract.env:8-9; scripts/install-python-runtime.sh:83-102 |
| The exact builder identity is contract-bound and its checkout plus version definition are verified before source compilation and final proof. | "https://github.com/pyenv/pyenv.git"; "builder commit mismatch"; "builder definition does not bind the approved source and digest" | scripts/python-runtime-contract.env:10-11; scripts/install-python-runtime.sh:104-143 |

## Cross-Repo References

The pinned python-build repository is a build tool input, not a runtime authority or code fallback.

| Finding | Anchor | Source |
| --- | --- | --- |
| The builder checkout must equal the contract's exact commit and bind the same source URL/digest. | "builder commit mismatch"; "builder definition does not bind the approved source and digest" | scripts/install-python-runtime.sh:104-127 |

## Update History

- 2026-08-29T16:10+02:00 — Created for the official checksum-verified CPython 3.13.15 source-build
  installer and project-owned prefix. Verification remains closeout-owned.

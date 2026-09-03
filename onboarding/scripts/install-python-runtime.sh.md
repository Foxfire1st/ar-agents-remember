# scripts/install-python-runtime.sh

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `scripts/install-python-runtime.sh` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `eb05a872780112640359232063168639d20fa87b`|
| lastVerifiedCommitDate | 2026-09-03T06:19:25+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[repository overview](../overview.md)

## Purpose

Installs the official CPython 3.13.15 source release under a dedicated Agents Remember data prefix
using an exact pinned python-build revision and checksum-bound source archive. Since the root-owned
canonical bootstrap repair (commit eb05a8727801) it additionally does so through a staged,
atomically published, fully validated builder checkout so concurrent publishers converge on one
canonical winner and a poisoned or foreign builder cache can never be silently reused.

## Code Commentary

### Logic

The script validates absolute, version-suffixed installation and cache/tooling paths
(`install-python-runtime.sh:41-56`). An existing runtime is reused only after the full
capability/provenance probe (`install-python-runtime.sh:58-71`); any other existing prefix is
refused. It downloads over HTTPS when needed, verifies the official archive digest both before and
after caching (`install-python-runtime.sh:82-102`).

The builder handling (the repair delta) first defines `validate_builder` (`install-python-runtime.sh:107-123`):
the checkout's `HEAD` must equal the pinned `AR_PYTHON_BUILD_COMMIT`, the pinned version
definition file must exist in the python-build tree, and the definition must bind the approved
source URL and SHA-256. `require_reusable_builder` (`install-python-runtime.sh:125-132`) refuses
a symlink or a path without a `.git` directory as foreign. When no builder exists, the script
clones into a unique sibling staging directory under the tooling root
(`builder_staging=$(mktemp -d ...)`, `install-python-runtime.sh:137-143`), checks out the exact
pinned commit detached, validates the staging builder, publishes it atomically with
`mv -T --no-clobber` (`install-python-runtime.sh:145`), handles a concurrent winner inside an
explicit conditional (a `set -e` loser validates and adopts the canonical target instead of
terminating), re-validates the adopted root, and cleans only its own staging path via an EXIT trap
(`install-python-runtime.sh:135-161`). It then compiles into the dedicated prefix
(`install-python-runtime.sh:163`) and probes the installed interpreter
(`install-python-runtime.sh:165-172`).

### Conventions

Every mutable external input is converted into an exact identity before compilation: source URL and
SHA-256, builder repository and commit, versioned prefix, and observed installed runtime. The
builder checkout is fully cloned (no promisor/blobless clone) and validated before it can be
published anywhere reachable.

### Invariants And Boundaries

- `/usr/bin/python` is never replaced or repointed.
- The source archive must match the approved digest; a cached archive is not trusted implicitly.
- Another uv-managed standalone Python or unverified prebuilt archive is not an admissible runtime.
- A foreign or incomplete prefix is refused rather than overwritten.
- The pinned builder commit and the exact Python 3.13.15 source URL/digest are validated before
  publication; a symlink or non-git builder path is refused.
- Publication is atomic and no-clobber; a losing concurrent publisher adopts only a validated
  winner and never overwrites, deletes, or silently trusts a target.
- Interpreter, source cache, builder checkout, standard library, and compiled artifacts stay
  outside the Git repository.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the canonical runtime contract carries the
approved authoritative URL, digest, and builder identity. The root-owned deterministic-bootstrap
repair, as documented in the L09 worker handover (Changed surfaces and behavior), uses a normal
`--no-checkout` clone in a unique sibling staging directory, checks out and
validates the exact pinned builder and Python source definition before atomic no-clobber
publication, validates and adopts a concurrent winner, rejects missing or foreign winners, and
cleans only its own staging path. The 2026-09-03T04:26:53+02:00 decision classified the poisoned
canonical Python builder cache and semicolon-masked installer failure as a root-owned
certification-infrastructure unblocker, and the 2026-09-03T06:20:00+02:00 decision landed it
(advances no requirement leaf, does not satisfy L12).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact destination validation and full proof govern existing-runtime reuse. | "refusing incomplete or foreign prefix" | scripts/install-python-runtime.sh:41-71 |
| The official archive is checksum-bound in the canonical contract, downloaded securely, and verified before and after caching. | "https://www.python.org/ftp/python/3.13.15/Python-3.13.15.tar.xz"; "curl --fail --location --proto '=https' --tlsv1.2"; "cached source digest mismatch" | scripts/python-runtime-contract.env:8-9; scripts/install-python-runtime.sh:82-102 |
| The builder is validated against the pinned commit and the approved source URL/digest before publication. | `validate_builder`; "builder commit mismatch"; "builder definition does not bind the approved source and digest" | scripts/install-python-runtime.sh:107-123 |
| Staged clone, atomic no-clobber publication, concurrent-winner adoption, and staging cleanup implement the deterministic bootstrap. | `require_reusable_builder`; "mv -T --no-clobber"; `builder_staging` | scripts/install-python-runtime.sh:125-161 |
| The hermetic contract suite pins this behavior. | `test_runtime_builder_is_fully_cloned_atomically_published_and_reused`; `test_existing_foreign_builder_is_refused_and_preserved`; `test_foreign_builder_publication_race_fails_closed` | mcp/tests/test_python_runtime_contract.py:203-235; mcp/tests/test_python_runtime_contract.py:254-269; mcp/tests/test_python_runtime_contract.py:294-316 |

## Cross-Repo References

The pinned python-build repository is a build tool input, not a runtime authority or code fallback.

| Finding | Anchor | Source |
| --- | --- | --- |
| The builder checkout must equal the contract's exact commit and bind the same source URL/digest. | `validate_builder`; "builder commit mismatch"; "builder definition does not bind the approved source and digest" | scripts/install-python-runtime.sh:107-123 |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): documented the validated staged builder flow — `validate_builder`/`require_reusable_builder`, full `--no-checkout` clone into a unique staging directory, atomic `mv -T --no-clobber` publication, concurrent-winner adoption, and self-only staging cleanup — replacing the previous inline blobless clone; refreshed line citations for the whole script. Verification metadata rebased from `60e429d1` to the bootstrap repair owning commit.

- 2026-08-29T16:10+02:00 — Created for the official checksum-verified CPython 3.13.15 source-build
  installer and project-owned prefix. Verification remains closeout-owned.

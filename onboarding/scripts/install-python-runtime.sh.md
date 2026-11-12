# scripts/install-python-runtime.sh

## Governing Overview

[repository overview](../overview.md)

## Purpose

Installs the official CPython 3.14.8 source release under a dedicated Agents Remember data prefix
using an exact pinned python-build revision and checksum-bound source archive. Since the root-owned
canonical bootstrap repair (commit eb05a8727801) it additionally does so through a staged,
atomically published, fully validated builder checkout so concurrent publishers converge on one
canonical winner and a poisoned or foreign builder cache can never be silently reused.

## Code Commentary

### Logic

The script validates absolute, version-suffixed installation and cache/tooling paths
(`install-python-runtime.sh:41-56`). The interpreter path it probes is built from the contract's
minor value (`python$AR_PYTHON_MINOR`, `install-python-runtime.sh:57`), so the reuse probe and the
installed-runtime probe follow a contract bump together. An existing runtime is reused only after
the full capability/provenance probe (`install-python-runtime.sh:58-71`); any other existing prefix
is refused. It downloads over HTTPS when needed, verifies the official archive digest both before and
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
- The pinned builder commit and the exact Python 3.14.8 source URL/digest are validated before
  publication; a symlink or non-git builder path is refused.
- The interpreter binary name comes from the contract's minor value, not a literal.
- Publication is atomic and no-clobber; a losing concurrent publisher adopts only a validated
  winner and never overwrites, deletes, or silently trusts a target.
- Interpreter, source cache, builder checkout, standard library, and compiled artifacts stay
  outside the Git repository.

### Todos

None recorded.

## Evidence

### Docs References

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

### Repo-Internal References

- Exact destination validation and full proof govern existing-runtime reuse. [1]
- The official archive is checksum-bound in the canonical contract, downloaded securely, and verified before and after caching. [2]
- The builder is validated against the pinned commit and the approved source URL/digest before publication. [3]
- Staged clone, atomic no-clobber publication, concurrent-winner adoption, and staging cleanup implement the deterministic bootstrap. [4]

### Cross-Repo References

The pinned python-build repository is a build tool input, not a runtime authority or code fallback.

- The builder checkout must equal the contract's exact commit and bind the same source URL/digest. [5]

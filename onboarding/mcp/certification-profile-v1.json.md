# mcp/certification-profile-v1.json

## Governing Overview

[overview](overview.md)

## Purpose

Declares Agents Remember's repository-owned certification selections, Gates 1–4 rails, selectors, Dagger adapter, result decoder and published-artifact inventory. The universal certification framework consumes these declarations; Gate 5 remains memory-domain authority.

## Code Commentary

### Logic

The generated-skills input declares only the packaged runtime skills tree and includes generated-copies.json beside the sync script and canonical skills source. The generated-runtime input declares the packaged benchmarks, providers and system trees with their canonical sources and scripts/sync-runtime.py; no generated-harness input is declared, while the generated-harness rail remains declared and runs scripts/sync-skills.py --check. These declarations are not certification or sync execution; the remaining rail/publication-artifact boundaries stay separate.

The profile declares no provider-runtime integration rail. `rails` declares each rail's `identity.railId` with its gate, class, artifacts, evidence contract and execution adapter, and that rail is absent from the declaration and from the gate selections. The mechanical binding table under the build-tooling directory follows this declaration and is follow-through, not a second account of it — it carries no card of its own.

`closeout-full` and `closeout-targeted` declare all four code gates. `local-targeted` declares Gate 4 not applicable. Each rail binds identity, prerequisites, observed evidence, required-on-pass artifacts, runtime and execution policy. Selector configuration and executor runtime digests are recomputed from their actual owners; the outer profile digest binds the canonical profile.

The publication inventory is finite: 45 declared paths, including 29 stable `rail-evidence/` capture paths. No ambient-role-chat or teardown-process-cleanliness rail or artifact is declared. Captures use `application/octet-stream` because an exact bounded byte tail may begin within a UTF-8 sequence. A rail's `requiredOnPass` artifact obligation remains distinct from an optional path's publication allowance. Exporting a result payload does not excuse absent evidence bytes.

Dashboard browser execution writes its configured Playwright JSON result with line and JSON reporters, and dashboard coverage keeps the stable `dashboard-coverage.json` export. No ambient summary, replication records, source-selection artifact or `teardown-proof.json` is declared.

The profile retains bounded dashboard dependency reconstruction, generated-input scopes and the remaining full/targeted/local selections. It declares no ambient-role source applicability or conditional teardown prerequisites.

The Dagger emission/export owners retain real files and exact output captures on a separate report branch. The profile declares those paths and their bounds; the host validates the full published snapshot and nested evidence before certificates can reference them.

### Conventions

Treat the JSON as canonical profile data. Refresh profile, runtime and selector digests from their actual owners after semantic source changes. Coverage and production CRAP observations are diagnostic under current repository policy; profile digests are not metric pass claims. Each rail's `lockDigest` is the content digest over both lock files (`dashboard/package-lock.json` and `mcp/uv.lock` together), each rail's `toolchainDigest` is an opaque declared identity that changes when the toolchain changes, and the outer `profileDigest` binds the canonical profile. No product code derives or checks `lockDigest` or `toolchainDigest`; a lock or toolchain change updates those two by hand from their owners. `profileDigest` is different: the canonical profile owner derives it with `repository_profile_digest` and admission refuses a declared value that differs from the canonical content.

### Invariants And Boundaries

- The profile chooses concrete repository rails, never gate order or Gate-5 ownership.
- Every required artifact needs actual producer bytes; declarations alone do not certify execution.
- Required capture bytes remain stable report-relative references, independently of physical generation identity.
- Local Gate-4 non-applicability is not terminal master Gate-4 certification.
- Declaration changes do not certify themselves; current lifecycle composition must be established from runtime owners and execution evidence.

### Todos

The profile declaration does not itself prove runtime composition or final-memory acceptance. Those facts require their canonical execution evidence.

## Evidence



- Generated inputs declare generated-projection-types, generated-runtime (packaged benchmarks, providers and system) and generated-skills (the packaged skills tree); no generated-harness input is declared. [7]

- The retained generated-harness rail checks skills through scripts/sync-skills.py --check. [8]
### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

- Bounded dependency reconstruction environments [1]


- Pinned Dagger execution adapter and actual runtime digest. [2]


- The declaration carries its own canonical profile digest. [3]


- 45 report paths include 29 rail-evidence captures; ambient and teardown publications are removed. [4]


- Full/targeted/local selections and explicit applicability. [5]

- Current source-owned selector configuration digest [6]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.

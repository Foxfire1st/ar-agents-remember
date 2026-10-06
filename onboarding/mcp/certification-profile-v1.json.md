# mcp/certification-profile-v1.json

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Declares Agents Remember's repository-owned certification selections, Gates 1–4 rails, selectors, Dagger adapter, result decoder and published-artifact inventory. The universal certification framework consumes these declarations; Gate 5 remains memory-domain authority.

## Code Commentary

### Logic

`closeout-full` and `closeout-targeted` declare all four code gates. `local-targeted` declares Gate 4 not applicable. Each rail binds identity, prerequisites, observed evidence, required-on-pass artifacts, runtime and execution policy. Selector configuration and executor runtime digests are recomputed from their actual owners; the outer profile digest binds the canonical profile.

The publication inventory is finite: 54 declared paths, including 32 stable `rail-evidence/` capture paths. Captures use `application/octet-stream` because an exact bounded byte tail may begin within a UTF-8 sequence. A rail's `requiredOnPass` artifact obligation remains distinct from an optional path's publication allowance. Exporting a result payload does not excuse absent evidence bytes.

Dashboard browser execution writes the Playwright JSON result at the explicitly configured report path with both line and JSON reporters. Provider integration writes the actual pytest phase report to `provider-integration-result.json`. For an applicable ambient scenario, the teardown verifier checks the existing clean-room summary and both successful `L5-C10` checkpoint records before writing `teardown-proof.json`. For an admitted not-applicable scenario, it requires summary absence and writes a zero-start proof with the exact source-decision digest and empty replications. Dashboard coverage retains its existing Vitest producer location and receives the stable exported name `dashboard-coverage.json`.

The profile also declares a bounded dashboard dependency census and reconstruction proof for resumed Gates 2–4, generated-input source/output scopes, and exact source applicability for the ambient-role rail. Its source-selection report remains required even when that rail is not applicable; teardown treats the ambient-role prerequisite conditionally. These declarations do not narrow the unconditional dashboard suite or turn full Python ownership into a focused population.

The Dagger emission/export owners retain real files and exact output captures on a separate report branch. The profile declares those paths and their bounds; the host validates the full published snapshot and nested evidence before certificates can reference them. These concrete producers close the earlier three Gate-4 mapping gaps.

### Conventions

Treat the JSON as canonical profile data. Refresh profile, runtime and selector digests from their actual owners after semantic source changes. The reduced test population changed selector configuration and the profile identity. Coverage and production CRAP observations are diagnostic under current repository policy; profile digests are not metric pass claims. Each rail's `lockDigest` is the content digest over both lock files (`dashboard/package-lock.json` and `mcp/uv.lock` together), each rail's `toolchainDigest` is an opaque declared identity that changes when the toolchain changes, and the outer `profileDigest` binds the canonical profile. No product code derives or checks `lockDigest` or `toolchainDigest`; a lock or toolchain change updates those two by hand from their owners. `profileDigest` is different: the canonical profile owner derives it with `repository_profile_digest` and admission refuses a declared value that differs from the canonical content.

### Invariants And Boundaries

- The profile chooses concrete repository rails, never gate order or Gate-5 ownership.
- Every required artifact needs actual producer bytes; declarations alone do not certify execution.
- Required capture bytes remain stable report-relative references, independently of physical generation identity.
- Local Gate-4 non-applicability is not terminal master Gate-4 certification.
- Declaration changes do not certify themselves; current lifecycle composition must be established from runtime owners and execution evidence.

### Todos

No remaining producer gap is recorded for the three L30 artifacts. The profile declaration does not itself prove runtime composition or final-memory acceptance. Those facts require their canonical execution evidence.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository. This card records repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured.

### Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

- Bounded dependency reconstruction environments [1]

- Pinned Dagger execution adapter and actual runtime digest [2]
- The declaration carries its own canonical profile digest. [3]
- 54 report paths including 32 rail-evidence captures [4]
- Full/targeted/local selections and explicit applicability [5]
- Current source-owned selector configuration digest [6]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository allowance is empty; no external source is relied upon here.

No cross-repository evidence is required for these file-local claims.

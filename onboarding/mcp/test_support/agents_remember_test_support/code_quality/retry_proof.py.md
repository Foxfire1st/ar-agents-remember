# mcp/test_support/agents_remember_test_support/code_quality/retry_proof.py

## Governing Overview

[Python quality verification overview](overview.md)

## Purpose

Owns fail-closed reuse of a passed pytest/branch-coverage proof inside the real nonce-attested
Dagger quality route after a later coverage-artifact/report operation fails. Proof lives in the locked
`ar-quality-retry-v3` Dagger cache volume, never in the source checkout. Ordinary CI execution does
not disable planning. L19 bound the immutable repository selector identity into the proof so a
changed selection can never reuse stale coverage.

## Code Commentary

### Logic

`prepare` requires a typed Dagger admission capability and an absolute cache root supplied by the
quality container. A compatibility key binds the complete tracked-file snapshot, resolved diff
base, product measurement scope and diagnostic report settings, Python/platform and coverage/pytest tool versions,
invocation-environment digest, selected population, exact evidence-lane digest/trigger/population,
and (L19) the exact immutable selection digest. The manifest and both coverage artifacts have
SHA-256 integrity checks. Tool-version capture records an unavailable distribution explicitly as
`absent`; package absence therefore participates in compatibility identity instead of being
conflated with an empty version.

The environment digest deliberately excludes only named runtime transport values. In particular,
Dagger creates new OpenTelemetry endpoint ports, trace parents, and log-span baggage for each
container exec; those values identify the observation channel rather than test semantics. They are
therefore explicit members of `EPHEMERAL_ENVIRONMENT`. An unclassified environment value remains
part of the digest and invalidates reuse when it changes.

An exact match restores coverage and skips pytest. L19 raises `SCHEMA_VERSION` to 5, adds
`selection_digest` to `RetryInputs`/`RetryPlan` and to the published manifest, and refuses an
`exact-selection-identity-changed` cache hit; a changed selection digest runs fresh. Otherwise
the canonical source-derived `DependencyOwnershipGraph` resolves changed product, test, support,
plugin, and governed fixture paths. Only a complete, non-global impact wholly inside the prior
population may run as a delta; incomplete ownership is now reported through every
`impact.unresolved_inputs` reason and runs the admitted current population fresh. The delta writes
unaffected prior contexts to a dedicated retained database and gives pytest-cov a clean active
database. Because the removed empty context cannot be attributed safely to an old test, the wrapper
re-collects the canonical population; `testing.retry_selection` then permits only the
graph-owned affected modules to execute. After pytest passes, `retry_coverage.py` explicitly
merges retained and fresh databases and regenerates the one JSON report scored by later rails. This
prevents pytest-cov/xdist worker combination from overwriting the retained proof. A read, merge, or
publication failure removes both public artifacts and fails the pytest proof; an inconclusive
aggregate still takes the explicit fresh-full-rerun path.

`RetryPlan.retained_data_available` records whether extraction actually produced unaffected arcs.
That explicit state permits an all-contexts-affected delta to merge its fresh database alone while
continuing to reject a retained database that was expected but disappeared.

Tracked symlinks are fingerprinted as Git stores them: tagged link-target text, not the bytes
reached by following the link. Global input, incomplete ownership, population or environment
drift, lane changes, missing contexts, corrupt artifacts, and unsupported selection all print a
stable cache-miss or disabled reason and run fresh inside the same admitted Dagger graph.

The compatibility key no longer includes a coverage-floor field; the CRAP review threshold and
report size remain explicit inputs. Metric findings alone are successful reports and do not
create a retry loop. Only a fresh full pytest pass followed by a later actual rail failure
publishes a new proof. A passing
wrapper removes it. A failed delta keeps the original full proof rather than chaining a filtered
aggregate.

### Invariants And Boundaries

- The Dagger graph owns one locked cache volume at
  `/var/cache/agents-remember-quality-retry`; the ordinary route receives that absolute root through
  `AR_QUALITY_RETRY_CACHE`.
- Evidence-only forcing routes use invocation-unique namespaces and remove only those namespaces.
- The manifest stores only an environment digest, never environment values or secrets.
- Dagger OpenTelemetry endpoint/trace transport is explicitly ephemeral; this is a closed named
  set, not a prefix or unknown-variable fallback. Every other environment variable stays in the
  compatibility identity.
- Context filtering requires branch arcs and at least one pytest runtime context.
- A delta proof never asks pytest-cov to append into the retained database. Retained and fresh
  evidence stay separate until the wrapper explicitly merges them after a passing delta run.
- Empty retained proof is represented by an explicit plan state, never by treating an unexpected
  missing file as empty.
- A delta proof removes affected runtime contexts and all old unattributed collection context; the
  current candidate must rebuild collection evidence before the explicit merge.
- `AR_QUALITY_NO_RETRY` is an explicit operator/forcing-route disable switch, not a CI default.
- Planning requires a capability minted only by `testing.dagger_admission`; host and diagnostic
  execution cannot read or publish certifying retry proof.
- A cache miss, disabled cache, corrupt proof, or inconclusive delta never silently changes
  authority. It names the reason and starts a fresh run in the already admitted route.
- The selection digest is a mandatory 64-hex immutable identity; a missing, malformed, or changed
  selection digest disables reuse or runs fresh (L19).

### Todos

None.

## Evidence

### Docs References

No external domain contract governs this repository-local verification cache.

### Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

- Admission and exact retry selection [1]
- Current snapshot/config/tool identity without diff floor [2]
- Complete dependency ownership required for delta [3]
- Manifest identity and artifact mismatch detection [4]
- Retained/fresh evidence and proof publication lifecycle [5]

### Cross-Repo References

The proof is Dagger-owned verification state and does not enter product or memory Git history.

## 260824-PDLS — Admission-Gated Persistent Retry

Retry preparation now stays enabled on the actual CI/Dagger route and consumes the same mounted
cache across attempts. A diagnostic runner cannot publish or restore this proof, and a matching
diagnostic candidate digest is not a certifying reuse key.

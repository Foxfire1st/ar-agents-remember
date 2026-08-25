# PDLS Onboarding Maintenance Input Ledger

| Field | Value |
| --- | --- |
| repository | agents-remember |
| mode | automated existing-memory-slice-maintenance |
| task | 260824-PDLS test evidence-system reform |
| capturedAt | 2026-08-25T15:44+02:00 |
| source registry | empty; discovery only |
| domain documentation | none configured |
| cross-repository sources | none allowed |
| operator decision | proceed; end-to-end master completion was explicitly authorized |

## Authoritative Inputs

The exact IAS working candidate, the approved 104-item PDLS requirement/rationale surface, the
PDLS reconciliation and Dagger reports, and existing onboarding are authoritative. Existing prose
supplies historical context but cannot override current source behavior.

## Source Inventory Delta

| Surface | Change | Existing coverage | Treatment |
| --- | ---: | ---: | --- |
| Production Python | 46 changed units | 11 sidecars | create 35; refresh 11 |
| Test/support Python | 60 changed units | 26 sidecars | create 34; refresh 26 |
| Dashboard contract guard | 1 changed unit | 1 sidecar | refresh 1; also refresh the unchanged snapshot sidecar whose documented consumer contract changed |
| Governing routes | application lifecycle, quality, closeout models, testing, integration closeout/legacy/lifecycle | partial | create seven route pillars; refresh parents |

The moved certifying plugin is preserved as a one-to-one onboarding move in meaning: the old
testing-package route had no sidecar to preserve, so the current root module receives the first
canonical sidecar and the testing overview records why no compatibility facade remains.

## Coverage Boundary

Resolved path rules include `mcp/**`. The standard vendor/build/cache/generated exclusions are
present. Documentation is excluded from file-level onboarding, and no cross-repository fact is
inferred. All 107 changed source units are in scope; none is deferred. The unchanged snapshot
fixture is not counted as changed source, but its sidecar is refreshed because the contract test no
longer requires the representative payload to instantiate every enum member.

## Operator Decision

Automated slice maintenance is authorized by the developer's approved master completion. This
ambient session performs the curation locally and does not start orchestration agents. Automated
bootstrap stops at the handoff; commit, closeout, push, and integration remain separate decisions.

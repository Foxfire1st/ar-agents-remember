# dashboard/src/cockpit/role-launcher/RoleCatalogStatus.test.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Exercise catalog-provenance presentation and the distinction between unknown data and a known empty offering.

## Code Commentary

### Logic

The cases check three-model preview bounds, remaining counts, host ID/label matching, per-part saved timestamps and unchecked notices. They preserve configured selection and replace older choices with the current answer even when it is empty. The unresolved-model case keeps a configured tier unchecked.

### Invariants And Boundaries

These supplied-data component and model cases do not measure a live catalog read or a native agent start.

## Repo-Internal References

- The cases cover saved provenance, unknown choices, known-empty replacement and host spelling. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.

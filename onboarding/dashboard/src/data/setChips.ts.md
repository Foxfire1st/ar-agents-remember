# dashboard/src/data/setChips.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pure shared presentation model for acceptance, pair, and route chips, queued composer hints, and
unacknowledged set attention.

## Code Commentary

### Logic

`deriveSetChips` orders pair state first, then per-kind pending and latest-unacknowledged ledger
evidence, then route errors. Route-terminated pairs use `routeErrorStep` to say effectiveness is
unknown; evidence-backed unsupported pairs keep the designed abort/refusal copy. The same models
feed the header, inspector-adjacent surfaces, and background toasts.

### Conventions

Every acceptance chip carries the acceptance word in `text`; tone never carries meaning alone.
Only 503 route errors are retryable.

### Invariants And Boundaries

Pending requested values never move effective markers. Clamp copy keeps both values; pair progress
spins only while an actual step remains active.

### Todos

- Reviewer sev-4 observation 4: a superseded `unknown` ledger entry can say a readback kept the
  prior value even though no readback resolved that superseded request.
- Reviewer sev-4 observation 7: an identical-value re-request temporarily hides the persistent
  clamp chip while the new in-flight chip is shown; attention remains held.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Chip ordering, copy selection, composer hint, and attention gate. [1]
- Full chip/pair/route/hint matrix. [2]
- Copy source consumed by every chip. [3]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.

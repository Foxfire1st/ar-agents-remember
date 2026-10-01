# dashboard/src/panels/review/recordsPageRefusal.captured.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured server body**: the exact bytes the real review route returned for a refused records
page, exported as `RECORDS_PAGE_REFUSAL_RESPONSE` for the mounted case that renders it. The file is
data with a provenance header, not a fixture anybody assembled — its own header says
**"do not hand-edit"** — and it exists because a hand-built body could not carry the property the case
is about.

That property is the **absence of the `page` key**. The route serializes with `exclude_none=True`, so a
refused page *omits* `page` rather than sending `page: null`; a hand-built body that sent the null made
the mounted refusal unreachable for every real response, because the component compared
`payload.page !== null` (undefined is not null). The capture is therefore the one artifact that cannot
drift from what the route actually sends, and the case asserts the key's absence **before** rendering
the body.

## Code Commentary

### Logic

**The header carries the provenance and the single normalisation.** The bytes were recorded by
`temp/icr/probe-l10-pagination.py` — a GET to `/api/review/intent` with `pageOf=records`, a stale
`continuation` and `pageSize=3`, over a real two-snapshot fixture whose candidate advanced after the
cursor was issued — and the header states the raw body's SHA-256 and byte count, the one substitution
(the per-run fixture repository uuid, written as `<repository_id>`), and the command that re-runs the
capture from the code worktree. Nothing else was changed.

**The export is typed `unknown` deliberately, and the header says why.** The route sends three fields
this client's review mirror does not declare — `evidence.channels` (`ICR-R14`), `knowledge.
revision_selection` (`ICR-R07`) and `source.attribution` (`ICR-R04`) — so annotating the body as
`ReviewResult` would need either a cast (which the dashboard's own fixture guard exists to refuse) or a
lossy projection of the very bytes under test. The mounted case feeds these bytes through the client's
own decode exactly as the browser does, so nothing is cast and nothing is dropped; the three missing
mirror fields are recorded as a finding for those leaves' client work rather than patched here.

**It is a page-refusal body, in the shape the surface publishes.** The captured payload carries no
`page` key, a `page_refusal` whose code is `comparison_page_reset`, the owner's `expected`/`observed`
identities, the offending cursor, and the matrix channels reported as `unavailable` rather than as a
measured zero — which is what "a refused read is not a zero" looks like on the wire.

### Conventions

- Captured bytes with a provenance header; never hand-assembled and never hand-edited.
- Provenance is stated in the file itself (source command, hash, byte count, the single normalisation),
  so a reader can re-derive it rather than trust it.
- Typed `unknown` on purpose: the fidelity of the bytes outranks the convenience of a declared type.

### Invariants And Boundaries

- **A body in this file is evidence, not a specification.** The contract it evidences is
  `ReviewCollectionPage` and the two page refusal codes in `models/knowledge/review.py`; the capture is
  how the mounted case proves the route's serialization is what the component actually receives.
- The missing mirror fields are a recorded finding for `ICR-R04`/`ICR-R07`/`ICR-R14` client work, not a
  gap this file fills.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The provenance header: the capture command, the raw body's hash and size, the one normalisation, and why the file is captured rather than assembled.** [1]
- **The captured body itself, exported as the one value the mounted case consumes.** [2]
- The mounted case that asserts the `page` key is absent and renders the refusal from these bytes. [3]
- The client decode these bytes travel through, exactly as the browser's do. [4]
- **The route's own serialization setting that makes the key absent rather than null.** [5]
- The published page and refusal shapes the captured body carries. [6]

### Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture.

No meaningful cross-repo references found.

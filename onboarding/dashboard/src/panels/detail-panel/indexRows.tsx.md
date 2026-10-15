# dashboard/src/panels/detail-panel/indexRows.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Own shared index-row identities, target resolution and status grouping independently of task-page composition.

## Code Commentary

A target prefers a resolvable master path, then a lifecycle link, then a matched authored slice slug. Unresolved rows remain inert with an explanatory title. Positions come from the full original row list, not a filtered group; matching projected task facts may supply row names and short IDs.

indexSlices builds one call-local Map keyed by the existing sliceSlug spelling, retaining the first document for duplicate slugs. Lookup requires a truthy ref.file and uses stripExt(ref.file) without new basename/path normalization; folder-qualified mismatches and empty files stay unresolved. indexedRows adds this matcher to a copied handler object. resolveRowTarget consumes a supplied matcher, otherwise keeps the legacy sliceForRef scan. taskRowFacts itself still uses the legacy scan; this optimization is not a new cross-call cache or a global dashboard complexity guarantee.

Sprint entries retain every row. A resolved commanded master contributes its projected status; seat/unprojected rows retain their authored status. Work, waiting, completed and abandoned groups derive from those facts without authoring state, fetching documents or deciding grants. This is the relocated index-row navigation/grouping seam, not a second identity authority.

## Evidence

- Master/lifecycle/slice target precedence, stable full-list positions and retained sprint rows belong to the extracted row seam. [1]

- The call-local slice index retains the first duplicate and exact legacy file spelling; target resolution optionally uses that matcher without changing precedence. [2]

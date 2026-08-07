# dashboard/src/topology/constel.test.ts

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `dashboard/src/topology/constel.test.ts`    |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-08-01T09:32+02:00                      |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                            |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Vitest coverage for the constellation's **colour grammar** — the one exported function in
`constel.ts` that does not need a canvas. It asserts that `constelColors` is total over the
`CONSTEL_STATUSES` vocabulary, that no status borrows another's hue, that a key outside the
vocabulary comes back `undefined` rather than falling through to the healthy fill, and that every
status asks for its own themed token with a concrete literal fallback.

It exists because the palette was the second half of this leaf's headline defect and nothing could
execute it. `model.ts` was made total over `State`; the step that turns a status into the pixels a
developer actually reads was left as `Record<string, string>` behind `COLORS[status] ?? COLORS.ok`,
and that map lived **inside `mountConstel`**, which jsdom cannot run. A totality claim nothing can
execute is a totality claim nothing can check.

## Code Commentary

### Logic

One `describe("constelColors")` over three `it`s, driven by a local `stub` `CssVarReader` that
returns a synthetic `var(<name>|<fallback>)` string, so the assertions never touch a stylesheet.

1. *gives every status in the vocabulary a colour of its own* — iterates `CONSTEL_STATUSES`,
   asserting each is a key of the returned record and that its value is truthy, then asserts
   `new Set(Object.values(colors)).size === CONSTEL_STATUSES.length`. The hue-uniqueness half is the
   load-bearing one: `ok` is the reading a developer skips past, so a status that silently shares it
   is the defect wearing a different name.
2. *declares no colour for a status the vocabulary does not contain* — reads the result through a
   `Partial<Record<string, string>>` view and asserts `colors["from-a-newer-build"]` is `undefined`.
   The map is **total, not defaulted**. The renderer only ever indexes it with a `ConstelStatus` that
   `buildTopology` produced, so a miss would mean the type lied — and a lie is better read as a blank
   than as "nothing needs you".
3. *asks for a themed token per status and offers a concrete fallback for each* — passes a recording
   reader and asserts the call count equals the vocabulary size, that the token names are all
   distinct, that each starts with `--`, and that each fallback matches `/^#[0-9a-f]{6}$/i`. The
   theme read itself belongs to `mountConstel`'s reader; what this pins is the half that lives in
   `constelColors`. An empty fallback would render a node with no fill, which reads as "nothing here"
   just as wrongly as the cyan did.

### Conventions

The vocabulary is **imported and iterated**, never restated: `CONSTEL_STATUSES` comes from
`./model`, so a sixth status is a failure here rather than an untested key. This mirrors
`model.test.ts` iterating `LIFECYCLE_STATES`, one layer down the same grammar. The reader is
injected per test, so no test depends on a stylesheet, a canvas, or `getComputedStyle`.

### Invariants And Boundaries

- No canvas, no DOM measurement, no `mountConstel`. This suite covers the pure palette only; the
  renderer's drawing behavior is out of scope by design.
- The vocabulary must stay imported. A local list of the five statuses re-creates exactly the gap
  this file closes.
- Test 2 must keep asserting `undefined`, not a specific colour. It is the assertion that fails if
  someone re-adds a `??` default to the palette.
- The stub reader must remain a pure function of `(name, fallback)`; a stub that returns a constant
  would make the uniqueness assertion in test 1 vacuous.

### Todos

No open file-local todos.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source and the module under test.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

The suite is the runtime half of a claim the type system already makes, so both halves are cited: the
`Record<ConstelStatus, string>` that fails `tsc -b`, and the vocabulary tuple both sides read.

| Finding | Anchor | Source |
| --- | --- | --- |
| The three `constelColors` cases cover vocabulary colors, undefined for unknown status, and themed tokens with concrete fallbacks. | "gives every status in the vocabulary a colour of its own"; "declares no colour for a status the vocabulary does not contain"; "asks for a themed token per status and offers a concrete fallback for each" | dashboard/src/topology/constel.test.ts:21-30; dashboard/src/topology/constel.test.ts:32-39; dashboard/src/topology/constel.test.ts:41-57 |
| `constelColors(cssVar): Record<ConstelStatus, string>` and the `CssVarReader` type are extracted from `mountConstel` for jsdom. | `constelColors`; `CssVarReader`; `mountConstel` | dashboard/src/topology/constel.ts:16-16; dashboard/src/topology/constel.ts:31-39; dashboard/src/topology/constel.ts:408-468 |
| `col` indexes the palette with no `??` fallback, which makes test 2's `undefined` expectation correct. | `col` | dashboard/src/panels/changeset/ChangeSetPane.tsx:18-18 |
| `CONSTEL_STATUSES` is the `as const` tuple from which `ConstelStatus` is derived. | `CONSTEL_STATUSES`; `ConstelStatus` | dashboard/src/topology/model.ts:16-16; dashboard/src/topology/model.ts:18-18 |
| The topology model maps `LIFECYCLE_STATES` into `CONSTEL_STATUS_BY_STATE` rather than restating the vocabulary. | `LIFECYCLE_STATES`; `CONSTEL_STATUS_BY_STATE` | dashboard/src/topology/model.ts:40-40; dashboard/src/topology/model.ts:48-59 |

## Cross-Repo References

No meaningful cross-repo references found. The palette and its vocabulary are entirely within the
`agents-remember` dashboard.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: rebound the three constel cases to their complete test bodies under the adversarial verdict, then the exact scoped fixer/check passed.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-01T09:32+02:00 — 260731-EFA-L4 curator: created. New suite covering `constelColors` —
  totality over `CONSTEL_STATUSES`, distinct hue per status, `undefined` (never a healthy default)
  for a key outside the vocabulary, and one `--token` plus a `#rrggbb` fallback per status. Written
  because the palette was the un-migrated twin of `model.ts`'s defect and, living inside
  `mountConstel`, was unreachable from jsdom. Verification metadata pinned to the leaf base
  (`abc7cbc`); the source file is still uncommitted and closeout stamps the code commit.

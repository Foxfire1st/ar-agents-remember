# dashboard/src/test/servedProjection.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/servedProjection.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:10+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The single sanctioned way to read `dashboard/src/fixtures/snapshot.json` as a `WorkspaceProjection`,
and the narrowest cast that does the job. Two exports, 43 lines: the type `AsJsonModule<T>` and the
function `asServedProjection`.

It exists because of a specific defect. `resolveJsonModule` widens every literal in an imported JSON
payload — `"blocked"` becomes `string`, `1` becomes `number` — so `snapshot.json` can never be
*assigned* to a mirror whose vocabularies are literal unions (`State`, `Phase`, `AttentionSeverity`, …).
Not because the payload is wrong, but because the import threw the literals away. The reflex fix was
`snapshot as unknown as WorkspaceProjection`, and a double cast turns off assignability, excess-property
checking and everything else at once. That is how a served field the mirror had never heard of
typechecked and passed, and how a payload missing a field the mirror requires did too. It is the
mechanical cause of this leaf's headline defect.

`AsJsonModule<T>` applies **exactly** the widening `resolveJsonModule` does — string→`string`,
number→`number`, boolean→`boolean`, recursing through arrays and objects — and nothing else. So the
fixture is bound by a real structural assignment: required fields, field types, array shapes and
nesting are all still checked. The single cast left inside the function body puts back only the literal
types the import erased.

## Code Commentary

### Logic

- `AsJsonModule<T>` (L22-L32): a conditional type distributed over `T`. Scalars widen to their base
  type; `readonly (infer Item)[]` maps to `AsJsonModule<Item>[]`; `object` maps homomorphically over
  its keys — which preserves optionality, so an optional mirror field stays optional. Anything else
  falls through unchanged.
- `asServedProjection(payload: AsJsonModule<WorkspaceProjection>): WorkspaceProjection` (L34-L43).
  **The PARAMETER type is the check.** A payload that does not satisfy `AsJsonModule<WorkspaceProjection>`
  fails `tsc -b` at the call site and names the field. The body is `return payload as WorkspaceProjection`
  — the only assertion, and it is narrow enough to describe in one sentence: it re-narrows the
  vocabularies, and only those.

### Conventions

Placement is deliberate and stated in the header (L16-L18): this lives beside the tests rather than in
`types/projection.ts` because it is scaffolding for *consuming* the fixture, not part of the contract.

The body cast is one of the sites registered in `wireFixtureGuard.test.ts::SANCTIONED_WIRE_SITES`
(`src/test/servedProjection.ts :: as WorkspaceProjection`, count 1) with the written reason "the
sanctioned narrowing: the PARAMETER type did the structural check, and this only puts back the literal
types `resolveJsonModule` erased". The registry counts occurrences, so a second cast added to this file
fails the guard rather than sheltering under the existing entry.

### Invariants And Boundaries

- **Every test that reads `snapshot.json` comes through here.** The header says why (L17-L18): a second
  `as unknown as` elsewhere silently re-opens the hole for that file. `contract.test.ts` and
  `test/fixtures/wire.ts` are the two current callers.
- `AsJsonModule<T>` must stay the *exact* widening the compiler performs — no more, no less. Widening
  more would let a wrong payload through; widening less would reject a correct one and push callers
  back to a double cast.
- The function does not validate at runtime. It is a compile-time narrowing only; nothing here inspects
  the payload's values.

### Todos

- The type does not model `null`. `resolveJsonModule` types a JSON `null` as `null`, which falls through
  the chain unchanged and therefore has to be assignable to the mirror field on its own. No fixture path
  exercises this today.
- Nothing here can see the direction that matters most: whether the mirror matches the *server*. This
  function binds the fixture to the mirror. `snapshot.json` is hand-maintained (no generator exists), so
  the mirror↔server link stays unheld — see `../fixtures/snapshot.json.md` and `contract.test.ts`'s
  header.

## Docs References

The behaviour this file compensates for is a TypeScript compiler behaviour: `resolveJsonModule` imports
a JSON file as a module whose type is inferred from its contents, with literals widened. No
project-external domain documentation governs the file beyond that language reference.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `resolveJsonModule` enables importing `.json` files as modules; the module's type is inferred from the file's contents, which is the widening this file re-applies deliberately. | `resolveJsonModule` | [TSConfig Reference — resolveJsonModule](https://www.typescriptlang.org/tsconfig/#resolveJsonModule) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The header stating the defect: `resolveJsonModule` widening, why the double cast was reached for, and what `AsJsonModule` restores. | L1-L18 | [servedProjection.ts](servedProjection.ts) |
| `AsJsonModule<T>` — the exact widening, and nothing else. | L22-L32 | [servedProjection.ts](servedProjection.ts) |
| `asServedProjection` — the parameter type is the check; the body cast only re-narrows vocabularies. | L34-L43 | [servedProjection.ts](servedProjection.ts) |
| The mirror whose literal unions the import erases (`State`, `Phase`, `AttentionSeverity`, `AttentionLane`, `ProcessFactState`, `ProcessHealth`). | L21-L30; L57-L70; L429-L442; L487-L519 | [../types/projection.ts](../types/projection.ts) |
| Caller 1: the contract guard reads the fixture through this function and then walks it in three directions. | L21-L22; L75 | [contract.test.ts](contract.test.ts) |
| Caller 2: the fixture builders take their bases from the payload read through this function. | L64; L69 | [fixtures/wire.ts](fixtures/wire.ts) |
| The registry entry that makes the body cast the only one allowed in this file, with its written reason. | L153-L157 | [wireFixtureGuard.test.ts](wireFixtureGuard.test.ts) |
| `tsconfig.app.json` sets `resolveJsonModule`, which is what makes the widening apply to the fixture import. | L11 | [../../tsconfig.app.json](../../tsconfig.app.json) |

## Cross-Repo References

The projection whose shape is being narrowed originates in the Python serving/observer layer, which is
the same repository. No sibling repository or external system is involved.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local; the payload's producer is `observer/projection.py` in this repo. | L1-L9 | [projection.py](../../../mcp/src/agents_remember/observer/projection.py) |

## Update History

- 2026-08-01T09:10+02:00 — 260731-EFA-L4 curator: created. Records `AsJsonModule<T>` as the exact
  `resolveJsonModule` widening, `asServedProjection`'s parameter type as the real check, the single
  registered body cast, and the two limits this file does NOT close — no runtime validation, and no
  binding of the mirror to the server (the fixture it narrows is hand-maintained). Verification metadata
  pinned to the leaf base `abc7cbcc74921cdcb57a61529445f61641e919e7` until closeout stamps the L4 code
  commit.

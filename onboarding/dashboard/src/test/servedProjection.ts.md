# dashboard/src/test/servedProjection.ts

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

- cit:([`AsJsonModule`], dashboard/src/test/servedProjection.ts:22-32): a conditional type distributed over `T`. Scalars widen to their base
  type; `readonly (infer Item)[]` maps to `AsJsonModule<Item>[]`; `object` maps homomorphically over
  its keys — which preserves optionality, so an optional mirror field stays optional. Anything else
  falls through unchanged.
- cit:([`asServedProjection`], dashboard/src/test/servedProjection.ts:41-43).
  **The PARAMETER type is the check.** A payload that does not satisfy `AsJsonModule<WorkspaceProjection>`
  fails `tsc -b` at the call site and names the field. The body is `return payload as WorkspaceProjection`
  — the only assertion, and it is narrow enough to describe in one sentence: it re-narrows the
  vocabularies, and only those.

### Conventions

The body cast is one of the sites registered in `wireFixtureGuard.test.ts::SANCTIONED_WIRE_SITES`
(`src/test/servedProjection.ts :: as WorkspaceProjection`, count 1) with the written reason "the
sanctioned narrowing: the PARAMETER type did the structural check, and this only puts back the literal
types `resolveJsonModule` erased". The registry counts occurrences, so a second cast added to this file
fails the guard rather than sheltering under the existing entry.

### Invariants And Boundaries

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

## Evidence

### Docs References

The behaviour this file compensates for is a TypeScript compiler behaviour: `resolveJsonModule` imports
a JSON file as a module whose type is inferred from its contents, with literals widened. The canonical
language reference is [TSConfig Reference — resolveJsonModule](https://www.typescriptlang.org/tsconfig/#resolveJsonModule).

### Repo-Internal References

- `AsJsonModule<T>` — the exact widening, and nothing else. [1]
- `asServedProjection` — the parameter type is the check; the body cast only re-narrows vocabularies. [2]
- The mirror whose literal unions the import erases (`State`, `Phase`, `AttentionSeverity`, `AttentionLane`, `ProcessFactState`, `ProcessHealth`). [3]
- Caller 1: the contract test imports `asServedProjection` for the sampled snapshot. [4]
- Caller 1: the contract test calls `asServedProjection` for the sampled snapshot. [5]
- The contract file documents the three type-level directions `mirror ⊇ served`, `served ⊇ mirror`, and `fixture ⊇ mirror`. [6]
- Caller 2: the fixture module exports `SERVED` from `asServedProjection(snapshot)`. [7]
- Caller 2: the fixture module reads the served projection's fields when constructing the `BASE_*` builders. [8]
- The registry entry that makes the body cast the only one allowed in this file, with its written reason. [9]
- `tsconfig.app.json` sets `resolveJsonModule`, which is what makes the widening apply to the fixture import. [10]

### Cross-Repo References

The projection whose shape is being narrowed originates in the Python serving/observer layer, which is
the same repository. No sibling repository or external system is involved.

- The reviewed behavior is wholly repository-local; the payload's producer is `observer/projection.py` in this repo. [11]

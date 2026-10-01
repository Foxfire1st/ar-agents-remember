# dashboard/src/test/fixtureOverrides.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The proof that `fixtures/overrides.ts` does what its header claims — and the companion to
`wireFixtureGuard.test.ts` for **the one impossible fixture no guard RULE can see**.

The header states the division precisely cit:([`exactOptionalPropertyTypes`], dashboard/src/test/fixtureOverrides.test.ts:16-16). `wireFixtureGuard.ts` measures property NAMES: it
catches a field the mirror never declared, an `any` with no shape at all, and every syntactic way of
opting out. It cannot catch a fixture whose names are all correct and whose VALUE is `undefined` on a
field the server always sends. `conversationPage({ capabilities: undefined })` names nothing wrong,
asserts nothing and suppresses nothing — yet it produces the exact page `conversationWire.ts`'s header
says it fixed: one whose REQUIRED `capabilities` is absent.

`exactOptionalPropertyTypes` is what would make that a compile error project-wide. It is not on here —
measured at 222 errors across 71 files, most of them in app code this leaf does not own — so the
builders carry the constraint themselves via `Overrides<O, T>`. This file is the proof that they do.

**And it runs over the guard's in-memory program precisely BECAUSE that program does not set the flag**
cit:([`GUARD_COMPILER_OPTIONS`], dashboard/src/test/wireFixtureGuard.ts:138-149). Whatever these assertions catch, they catch without it. That is the point of borrowing
`buildProgramWithVirtualFiles` rather than typechecking the real tree.

## Code Commentary

### Logic

- `ROOT` / cit:([`PROBE_DIR`], dashboard/src/test/fixtureOverrides.test.ts:23-23): probe sources are planted under `src/__override_probe__`, a directory
  that never exists on disk.
- cit:([`PROBE_FILES`], dashboard/src/test/fixtureOverrides.test.ts:25-78): three virtual modules, each importing the REAL builders and the REAL mirror.
  - `impossible.test.ts` cit:([`PROBE_FILES`], dashboard/src/test/fixtureOverrides.test.ts:25-78): the four calls that must fail — `conversationPage({ capabilities:
    undefined })`, `lifecycle({ state: undefined })`, `taskDoc({ steps: undefined })`,
    `projection({ enclosures: undefined })`. All four compiled before `Overrides` replaced the builders'
    bare `Partial<Node>`.
  - `excess.test.ts` cit:([`PROBE_FILES`], dashboard/src/test/fixtureOverrides.test.ts:25-78): the property `Overrides` must not cost — `lifecycle({ refusedPolarity:
    "amber" })` and `taskDoc({ createdAtButMisspelled: … })`. These are the two proven defects of this
    leaf restated as call sites; excess-property checking is where both would have died.
  - `honest.test.ts` cit:([`PROBE_FILES`], dashboard/src/test/fixtureOverrides.test.ts:25-78): eleven shapes the server DOES send, none of which may cost a diagnostic
    — no-argument calls, ordinary overrides, an OPTIONAL field written as `undefined` (the mirror marks
    it `?`, so absent is a real shape), builders whose override is required rather than defaulted, and
    the documented residue at entry `k`.
- cit:([`buildProgramWithVirtualFiles`], dashboard/src/test/fixtureOverrides.test.ts:80-80) builds one program; cit:([`diagnosticsFor`], dashboard/src/test/fixtureOverrides.test.ts:82-89)
  reads `getSemanticDiagnostics` for a named probe and flattens each message to a string. A probe file
  the program failed to load throws rather than returning `[]` — an empty diagnostic list must never be
  reachable by accident.
- The three assertions cit:(["a builder override cannot state that a required field is absent"], dashboard/src/test/fixtureOverrides.test.ts:91-117):
  1. **exactly four** diagnostics from `impossible.test.ts`, each containing
     `Type 'undefined' is not assignable to type 'never'` — one per call and no more, so the constraint
     bites exactly where it is aimed.
  2. **exactly two** from `excess.test.ts`, naming `refusedPolarity` and `createdAtButMisspelled`, each
     containing `Object literal may only specify known properties`. The comment states the stake: the
     constraint is laid OVER `O extends Partial<Node>`, not in place of it, and if generic inference had
     swallowed excess-property checking the builders would have lost the property they exist for.
  3. **zero** from `honest.test.ts`.

### Conventions

Counts, not "at least one". Every assertion is an exact length plus a message-content check, so a
diagnostic arriving for the wrong reason fails rather than passing as evidence.

### Invariants And Boundaries

- The probe program must keep NOT setting `exactOptionalPropertyTypes` — see
  `wireFixtureGuard.ts::GUARD_COMPILER_OPTIONS`. Turning it on there would make these assertions pass
  for a reason that does not hold in the real projects.
- The probe files must never exist on disk. They are sources whose whole purpose is to be impossible.
- `honest.test.ts` is as load-bearing as the failing probes: a constraint that also rejects the honest
  forms is one somebody deletes.

### Todos

**What this file does not cover.**

- It measures a VALUE-level hole for the four builders it names, at the CALL SITE, on a FRESH literal.
  Entry `k` of `honest.test.ts` cit:(["LC-2"], dashboard/src/test/fixtureOverrides.test.ts:74-74) asserts the documented residue as a **known pass**: an override
  pre-widened through a variable (`const widened: Partial<LifecycleProjection> = …`) infers
  `Partial<…>` for `O`, every slot admits `undefined` again, and it compiles. That is asserted so it is
  a known pass rather than a surprise — only `exactOptionalPropertyTypes` closes it.
- Nested overrides are out of reach: `conversationCapabilities({ controls: { interrupt: undefined } })`
  is one level deeper than `Overrides` binds and is not probed here.
- Nothing outside `fixtures/wire.ts` and `fixtures/conversationWire.ts` is covered. Any other
  `Partial<WireType>` parameter in the tree still admits an explicit `undefined`.
- These are **semantic diagnostics from an in-memory program**, not a run of the project's real
  `tsc -b`. They prove the constraint's shape; the typecheck gate is what proves the tree.

## Evidence

### Docs References

The assertions read TypeScript's own semantic diagnostics through the compiler API, and the behaviour
being pinned is the `exactOptionalPropertyTypes`-off rule described in the TSConfig reference.

- `ts.Program#getSemanticDiagnostics` and `ts.flattenDiagnosticMessageText` are the documented compiler-API surface these assertions read. [1]
- With `exactOptionalPropertyTypes` off, an optional property implicitly admits `undefined` — the rule that makes a bare `Partial<T>` override able to state that a required field is absent. [2]

### Repo-Internal References

- The header: what no guard rule can see, and why running over the guard's flag-free program is the point. [3]
- The four impossible calls, the two excess-property calls, and the eleven honest shapes. [4]
- The three exact-count assertions and their message checks. [5]
- The residue asserted as a known pass: a pre-widened `Partial<LifecycleProjection>` override still compiles. [6]
- The constraint under test, and the three limits it documents. [7]
- `buildProgramWithVirtualFiles` and `GUARD_COMPILER_OPTIONS` — the harness these probes borrow, whose option set is strict/bundler/`resolveJsonModule` and contains no `exactOptionalPropertyTypes` entry. [8]
- The guard's own statement of the same hole — item 5, "A VALUE" — which names this file as the answer. [9]
- The builders whose parameters are being pinned. [10]
- The conversation builders, including the `capabilities`-required page the first probe attacks. [11]
- The current fixture-override regression deliberately supplies undeclared `refusedPolarity` to `lifecycle` and `createdAtButMisspelled` to `taskDoc`, and asserts two unknown-property diagnostics. [12]
- The schema distinction is deliberate: the full `TaskDocNode` legitimately carries `createdAt`; a master's `TaskSubTaskRefNode` does not and instead may carry `linkedLifecycleId`; `SeriesSubTaskNode` may carry `createdAt`; the contract type assertions pin the master/series distinction. [13]

### Cross-Repo References

No cross-repository or external-system boundary is exercised. The probes import in-repo builders and
the in-repo mirror; the compiler is a devDependency, not a system boundary.

- Every probe import resolves inside this repository (`../test/fixtures/wire`, `../test/fixtures/conversationWire`, `../types/projection`). [14]

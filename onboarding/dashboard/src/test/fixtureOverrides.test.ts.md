# dashboard/src/test/fixtureOverrides.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtureOverrides.test.ts`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:20+02:00                           |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`       |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `../overview.md`                                 |

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

## Docs References

The assertions read TypeScript's own semantic diagnostics through the compiler API, and the behaviour
being pinned is the `exactOptionalPropertyTypes`-off rule described in the TSConfig reference.

| Finding | Anchor | Source |
| --- | --- | --- |
| `ts.Program#getSemanticDiagnostics` and `ts.flattenDiagnosticMessageText` are the documented compiler-API surface these assertions read. | `getSemanticDiagnostics`, `flattenDiagnosticMessageText` | dashboard/src/test/fixtureOverrides.test.ts:87-88 |
| With `exactOptionalPropertyTypes` off, an optional property implicitly admits `undefined` — the rule that makes a bare `Partial<T>` override able to state that a required field is absent. | `exactOptionalPropertyTypes` | dashboard/src/test/fixtureOverrides.test.ts:16-16 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The header: what no guard rule can see, and why running over the guard's flag-free program is the point. | `PROBE_FILES`, `GUARD_COMPILER_OPTIONS` | dashboard/src/test/fixtureOverrides.test.ts:25-78; dashboard/src/test/wireFixtureGuard.ts:138-149 |
| The four impossible calls, the two excess-property calls, and the eleven honest shapes. | `PROBE_FILES` | dashboard/src/test/fixtureOverrides.test.ts:25-78 |
| The three exact-count assertions and their message checks. | "a builder override cannot state that a required field is absent" | dashboard/src/test/fixtureOverrides.test.ts:91-117 |
| The residue asserted as a known pass: a pre-widened `Partial<LifecycleProjection>` override still compiles. | "LC-2" | dashboard/src/test/fixtureOverrides.test.ts:74-74 |
| The constraint under test, and the three limits it documents. | `Overrides` | dashboard/src/test/fixtures/overrides.ts:60-66 |
| `buildProgramWithVirtualFiles` and `GUARD_COMPILER_OPTIONS` — the harness these probes borrow, whose option set is strict/bundler/`resolveJsonModule` and contains no `exactOptionalPropertyTypes` entry. | `buildProgramWithVirtualFiles`, `GUARD_COMPILER_OPTIONS` | dashboard/src/test/wireFixtureGuard.ts:138-149; dashboard/src/test/wireFixtureGuard.ts:188-230 |
| The guard's own statement of the same hole — item 5, "A VALUE" — which names this file as the answer. | "A VALUE" | dashboard/src/test/wireFixtureGuard.ts:70-75 |
| The builders whose parameters are being pinned. | `lifecycle`, `taskDoc`, `projection` | dashboard/src/test/fixtures/wire.ts:241-246; dashboard/src/test/fixtures/wire.ts:282-287; dashboard/src/test/fixtures/wire.ts:329-345 |
| The conversation builders, including the `capabilities`-required page the first probe attacks. | `conversationPage`, `conversationItem` | dashboard/src/test/fixtures/conversationWire.ts:209-226; dashboard/src/test/fixtures/conversationWire.ts:228-243 |
| The current fixture-override regression deliberately supplies undeclared `refusedPolarity` to `lifecycle` and `createdAtButMisspelled` to `taskDoc`, and asserts two unknown-property diagnostics. | `refusedPolarity`; `createdAtButMisspelled`; "still rejects a field the mirror does not declare" | dashboard/src/test/fixtureOverrides.test.ts:45-46; dashboard/src/test/fixtureOverrides.test.ts:101-112 |
| The schema distinction is deliberate: the full `TaskDocNode` legitimately carries `createdAt`; a master's `TaskSubTaskRefNode` does not and instead may carry `linkedLifecycleId`; `SeriesSubTaskNode` may carry `createdAt`; the contract type assertions pin the master/series distinction. | "class TaskDocNode(BaseModel):"; "class TaskSubTaskRefNode(BaseModel):"; "class SeriesSubTaskNode(BaseModel):"; "keeps the master and series sub-task row models distinct" | dashboard/src/test/contract.test.ts:520-550; mcp/src/agents_remember/observer/projection.py:583-583; mcp/src/agents_remember/observer/projection.py:616-616; mcp/src/agents_remember/observer/projection.py:665-665 |

## Cross-Repo References

No cross-repository or external-system boundary is exercised. The probes import in-repo builders and
the in-repo mirror; the compiler is a devDependency, not a system boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Every probe import resolves inside this repository (`../test/fixtures/wire`, `../test/fixtures/conversationWire`, `../types/projection`). | `PROBE_FILES` | dashboard/src/test/fixtureOverrides.test.ts:25-78 |

## Update History

- 2026-08-02T23:29:31+02:00 — L6 W2-B02 curator: corrected the semantic citation ranges for the 2 supported repository-internal claims: the fixture regression now covers declarations 45-46 and its enclosing assertion test 101-112, while the schema claim covers Python model extents 561-578, 594-640, 643-658 and contract assertions 477-507; final scoped result 0 (checker-clean), with no Tier-3 residue.

- 2026-08-01T09:20+02:00 — 260731-EFA-L4 curator: created. Records the three exact-count assertions
  (four `undefined`-into-`never` rejections, two surviving excess-property errors, zero on the honest
  shapes), why the probe program's lack of `exactOptionalPropertyTypes` is the load-bearing detail, and
  — stated rather than flattened — the four limits: fresh-literal-only (with entry `k` asserting the
  widened case as a KNOWN PASS), no nested overrides, nothing outside the two fixture modules, and
  in-memory diagnostics rather than the project's real `tsc -b`. Verification metadata pinned to the
  leaf base `abc7cbcc74921cdcb57a61529445f61641e919e7` until closeout stamps the L4 code commit.

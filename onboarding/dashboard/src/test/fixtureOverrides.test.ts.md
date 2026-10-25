# dashboard/src/test/fixtureOverrides.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The proof that `fixtures/overrides.ts` does what its header claims — and the companion to
`wireFixtureGuard.test.ts` for **the one impossible fixture no guard RULE can see**.

The header states the division precisely cit:([`exactOptionalPropertyTypes`], dashboard/src/test/fixtureOverrides.test.ts:16-16). `wireFixtureGuard.ts` measures property NAMES: it
catches a field the mirror never declared, an `any` with no shape at all, and every syntactic way of
opting out. It cannot catch a fixture whose names are all correct and whose VALUE is `undefined` on a
field the server always sends. `enclosure({ repoName: undefined })` has correct field names and no cast/suppression, yet asks a required wire field to be absent. The retained probe uses this enclosure call; conversationPage/conversationWire are removed and supply no current fixture coverage.

Overrides constrain builder calls without enabling exactOptionalPropertyTypes in the virtual program. Historical project diagnostic counts are not a current typecheck measurement.

**And it runs over the guard's in-memory program precisely BECAUSE that program does not set the flag**
cit:([`GUARD_COMPILER_OPTIONS`], dashboard/src/test/wireFixtureGuard.ts:138-149). Whatever these assertions catch, they catch without it. That is the point of borrowing
`buildProgramWithVirtualFiles` rather than typechecking the real tree.

## Code Commentary

### Logic

- Virtual impossible calls supply undefined to enclosure.repoName, taskEntry.stage, taskSummary.steps and projection.enclosures: exactly four undefined-to-never diagnostics.
- Excess calls add refusedPolarity to taskEntry and createdAtButMisspelled to taskSummary: exactly two unknown-property diagnostics.
- Honest native calls, optional undefined and pre-widened Partial<TaskEntry> remain diagnostic-free. Missing probe modules throw before reading diagnostics.

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

Fresh flat call sites only: pre-widened Partial<TaskEntry> remains a known pass. Nested overrides/other Partial APIs are not established. Virtual semantic diagnostics are not the real tsc -b gate or execution in this preparation.

## Evidence

### Docs References

The assertions read TypeScript's own semantic diagnostics through the compiler API, and the behaviour
being pinned is the `exactOptionalPropertyTypes`-off rule described in the TSConfig reference.


- `ts.Program#getSemanticDiagnostics` and `ts.flattenDiagnosticMessageText` are the documented compiler-API surface these assertions read. [1]

- With `exactOptionalPropertyTypes` off, an optional property implicitly admits `undefined` — the rule that makes a bare `Partial<T>` override able to state that a required field is absent. [2]

### Repo-Internal References


- The header: what no guard rule can see, and why running over the guard's flag-free program is the point. [3]


- The four impossible calls, the two excess-property calls, and the nine honest shapes. [4]


- The three exact-count assertions and their message checks. [5]


- The residue asserted as a known pass: a pre-widened `Partial<TaskEntry>` override still compiles. [6]

- The constraint under test, and the three limits it documents. [7]
- `buildProgramWithVirtualFiles` and `GUARD_COMPILER_OPTIONS` — the harness these probes borrow, whose option set is strict/bundler/`resolveJsonModule` and contains no `exactOptionalPropertyTypes` entry. [8]

- The guard's own statement of the same hole — item 5, "A VALUE" — which names this file as the answer. [9]






- The builders whose parameters are being pinned: `projection`, `taskEntry`, `taskSummary`, `action` and `observerEvent`, each taking an `Overrides<O, Node>`.  Earlier card anchor caption (historical provenance): `lifecycle` `taskDoc` `projection` Source caption: `projection` `taskEntry` `taskSummary` `provider` `action` `observerEvent` [10]




- The excess-property probe supplies undeclared refusedPolarity to taskEntry and createdAtButMisspelled to taskSummary. Its regression expects exactly two diagnostics, checks each offending name and requires the unknown-property message for both; lifecycle/taskDoc are not the builders used in this probe. [12]


### Cross-Repo References

No cross-repository or external-system boundary is exercised. The probes import in-repo builders and
the in-repo mirror; the compiler is a devDependency, not a system boundary.


- Probe imports resolve to retained wire builders; the enclosure.repoName replacement preserves the required-undefined control. [14]

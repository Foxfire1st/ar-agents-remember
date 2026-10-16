# dashboard/src/test/wireFixtureGuard.test.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The policy half of the fixture guard. `wireFixtureGuard.ts` is the mechanism; this file supplies the
three things a mechanism cannot supply itself:

1. **The registry** — every site that still does what the rules forbid, with the sentence that earns it.
   Exact (counts, not files) and bidirectional (an entry that stops matching fails too), so a new
   consumer-authored fixture cannot appear silently and an old exemption cannot outlive its reason.
2. **The planted bypasses** — an AST guard written without them has holes; *this leaf proved that twice*.
   Every rule is shown FAILING against a source that must never exist on disk, over a virtual program
   laid on the real tree so planted files import the real wire types.
3. **The vacuity checks** — every rule is conditioned on "is this a wire type?", so a guard whose
   vocabulary came back empty would pass everything in silence.

Its framing sentence is R6: *a test whose fixture is authored by the consumer cannot detect producer
drift.* `contract.test.ts` makes the MIRROR honest; this file makes the FIXTURES honest. Neither is
worth much alone — a perfect mirror nobody is checked against, or fixtures checked against a mirror that
lies.

## Code Commentary

### Logic

SANCTIONED_WIRE_SITES retains exact reasoned file/site occurrence exemptions, not file-wide permission.

- Decode sites: store TaskEntry/TaskCounts/enclosure/provider/metrics/analytics/events and taskDocuments TaskSummary.
- Fixture exemption: servedProjection narrowing only.
- contract.test.ts retains one @ts-expect-error allowance.
- Removed count-grammar/topology widenings are not exemptions; counts/reasons reconcile bidirectionally.

**The sweep over the real tree** builds the program once and derives `findings` and
`vocabulary` from it.

**`the guard has something to police`** — the vacuity suite:

- Vocabulary floor is >50, not >100; it is not a pinned total.
- Required names include EngineProcessEdge, TaskEntry and ObserverEvent.
- Exact mirror modules are types/event.ts and types/projection.ts; src/types markers and fixture-surface true/false probes remain guarded.

**`no dashboard test asserts against a payload the server cannot produce`** — the
reconciliation: `unregistered` must be empty (with a failure message telling the author to build the
fixture with retained `fixtures/wire.ts`, annotate it, or `satisfies` it — *do not cast
it*), `spent` and `miscounted` must be empty, and every entry must carry a written reason.

**`PLANTED_FILES`** — seven virtual modules under `src/__wire_guard_planted__`, numbered
1-15 in their own comments:

| Probe | What it plants |
| --- | --- |
| casts.test.ts | Native TaskEntry/TaskSummary aliases, casts/wrappers, context-supplied never/any/unknown, typeof and unresolved names |
| freshness.test.ts | Spread/Object.assign extras and JSON.parse any reaching TaskEntry |
| suppression.test.ts | A suppressed impossible property on a TaskEntry literal |
| union.test.ts | Fresh/nonfresh blends and impossible extras for TaskDecisionNode or TaskHeaderNoteNode, not retired SubTaskRow |
| helper.ts + twoModule.test.ts | Cross-module TaskEntry smuggling, with the harness required to resolve the planted import |
| honest.test.ts | Checked native literals/builders, DOM mocks and each declared union member alone |

**`the guard is shown able to fail`** asserts each rule biting, and two of the assertions are
harness assertions as much as rule ones. The `twoModule` case exists because a planted file
importing another planted file used to resolve to nothing, degrade to `any`, and trip rule 3 — *the test
passed for the wrong reason*, which is the same as a harness that cannot express the case at all. The
unresolved-name case asserts `wire-cast: asserts <unresolved>`, because "the guard did not
understand this" must read as a failure.

**`the guard leaves the honest forms alone`** asserts ZERO findings on `honest.test.ts`. The
comment states the stake: a guard that also flags the fix is a guard that gets deleted — and `satisfies`
and a type annotation both do FULL checking, which is what the whole file exists to force fixtures back
onto.

**`the registry cannot be quietly outgrown`** unit-tests `reconcileWithRegistry` on
synthetic findings: a site no entry covers, an entry matching nothing, a second occurrence hiding behind
a one-site exemption, and an entry with a blank reason.

### Conventions

- A registry entry is a sentence, not a flag. `unreasoned` fails on a blank one, so "why" is structurally
  required.
- The planted sources are string arrays joined with `\n`, and the suppression probe writes `${"@"}ts-…`
  so the directive exists in the planted TEXT without existing in this file — which is also why the
  guard reads suppressions from comment trivia rather than from raw lines.
- Both directions of the module-set assertion are one `toEqual`, deliberately: a module that LOSES its
  marker silently narrows every rule, and a NEW mirror module fails here too — "which is the moment to
  decide what its fixtures are allowed to do".

### Invariants And Boundaries

- The registry is the only escape hatch, and it escapes by SITE, never by file. Adding an entry is a
  decision with a written justification; growing a count is a new hole.
- The vacuity assertions must stay. Every other assertion in this file is conditioned on a non-empty
  vocabulary.
- `honest.test.ts` must keep returning zero findings. New rules are added against a planted bypass AND
  against the honest set.
- This file asserts; it holds no matching logic. Rule behaviour belongs in `wireFixtureGuard.ts`.

### Todos

**What these assertions do not establish.**

Inline changeset/files/notes response models remain outside marker vocabulary. Planted counterexamples show selected rules can bite, not completeness. A >50 floor alone can miss partial vocabulary loss; exact module/required-name guards are separate.

## Evidence

### Docs References

The registry, the planted bypasses and the honest set are all statements about TypeScript's own
checking: an assertion suppresses excess-property checking, a double assertion suppresses assignability
too, excess-property checking applies only to fresh literals, and an unused `@ts-expect-error` is itself
an error.

No external documentation is used for this bounded card.

### Repo-Internal References

- The framing and three responsibilities the mechanism cannot supply itself. [1]
- The sanctioned-site registry and its four groups. [2]
- The real-tree sweep derives its discovered vocabulary with `wireTypeNames(program, ROOT)`. [3]
- The vacuity suite's fixture-surface checks. [4]
- The reconciliation over the real tree. [5]
- The virtual planted modules and honest forms. [6]
- Each rule shown biting, including cross-module and unresolved-name cases. [7]
- Zero findings on the honest forms. [8]
- The registry reconciliation unit cases. [9]
- The five-rule mechanism and discovered vocabulary. [10]
- The guard's documented uncovered-evasions section names `ElementAccessExpression`. [11]



- The sanctioned narrowing the registry names. [15]


- The contract test suppresses the carried `refusedPolarity` property. [21]


### Cross-Repo References

No cross-repository boundary. Every scanned root, every registry key and every planted module is inside
`dashboard/` in this repository.

- The sweep is built from the in-repo dashboard root and scanned source files; nothing outside this repository is read. [25]

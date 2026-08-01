# dashboard/src/dev/cockpitScenarios.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/dev/cockpitScenarios.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T10:20+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate |  2026-08-01T11:01:51+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pins dev-scenario isolation across stores and unresolved asynchronous authority boundaries, and —
since 260731-EFA-L4 — that the dev injector answers only shapes the daemon could produce.

## Code Commentary

### The Daemon-Answerability Describe

260731-EFA-L4 added `describe("the scenario server answers only what the daemon could answer")`, two
`it`s covering the two routes whose response types live in **unmarked** modules
(`data/harnessCatalog.ts`, `data/submissionLifecycleClient.ts`) and are therefore outside
`wireFixtureGuard.ts`'s discovered wire vocabulary. Both had carried a field the server cannot send.

1. *serves harness catalog rows with exactly `DetectedHarness`'s three fields* — installs the
   scenario fetch, calls `/api/harnesses`, and asserts every row's sorted key set is
   `["detected", "id", "name"]`. The removed field was `control: "ready"`.
2. *withdraws with exactly the fields `WithdrawalResultWire` declares* — calls the local
   `authorityTransport(...).withdraw(...)` and asserts the sorted key set is
   `["detail", "outcome", "requestId", "state", "withdrawnAt"]`. The removed field was `bridgeEpoch`.

The `satisfies`/return-type pins beside each fixture catch a field added to a *fresh* literal; these
two assertions catch the rest.

**The withdraw transport now declares its return type.** `withdraw` was an async arrow with a concise
body, and an object literal in that position **loses excess-property checking** — the literal is
compared against the arrow's own inferred `Promise<…>` rather than checked fresh against the
contextual one — so it carried a `bridgeEpoch` that neither `WithdrawalResultWire` nor the server's
`extra="forbid"` model declares. It had been copied from the `/submit` receipt, which does carry one.
Writing `: Promise<WithdrawalResultWire>` on the arrow makes a re-added field fail `tsc -b` at the
literal.

### FEUI MX-FIX-2 Real-Client Open Proof

The new scenario test calls the real shared opener through the dev injector for one raw and one
harness request. It asserts both accepted identities, retained harness model/effort facts, and the
catalog projection. The raw response and catalog row must have no harness/control authority,
preventing a fixture-only fail-open from masking production behavior.

The suite proves a reset clears transient cockpit/catalog/capability/announcement/lifecycle/PTY and
connection state while preserving allowed preferences. Deferred tests reuse ids across generations
and prove old authority reads, withdrawals, pollers, and catalog hydrates neither overwrite the new
owner nor delete its in-flight registration or poll-health truth.

### Logic

The suite installs one named scenario injector, issues real raw and Codex open requests through the
production client, and asserts the returned accepted row matches each request's kind, harness,
lifecycle, leaf, and control boundary.

### Conventions

Tests use real `Response` objects and reset scenario state between cases so parser behavior, not a
partial fetch double, determines acceptance. A helper transport that returns a wire type writes that
return type out explicitly rather than relying on inference, so its literal keeps excess-property
checking.

### Invariants And Boundaries

These are race tests, not fixture snapshots: assertions must release the retired promise after the
successor authority exists.

- The daemon-answerability assertions compare **exact sorted key sets**, not `toMatchObject`. A subset
  match is what would have let `control` and `bridgeEpoch` survive.
- They exist specifically for routes `tsc` and `wireFixtureGuard.ts` cannot cover. A route whose
  response type is a marked mirror or lives under `src/types/` does not need one here.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Cross-Repo References

The race suite exercises repository-local generation guards and stores; no cross-repository source applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

This table is two columns; line ranges are carried inside the `Finding` cell so every row keeps the
same arity.

| Finding | Source Path |
| --- | --- |
| L110-L142 — the daemon-answerability `describe` and its two exact-key-set assertions. | [cockpitScenarios.test.ts](cockpitScenarios.test.ts) |
| L63-L75 — `authorityTransport`'s `withdraw`, now annotated `: Promise<WithdrawalResultWire>`, with the comment recording why the concise async body lost excess-property checking. | [cockpitScenarios.test.ts](cockpitScenarios.test.ts) |
| L40-L46 — `WithdrawalResultWire`'s five declared fields; `bridgeEpoch` is not among them. | [submissionLifecycleClient.ts](../data/submissionLifecycleClient.ts) |
| L4-L9 — `HarnessInfo`'s three fields, declared inline in a module with no mirror marker. | [harnessCatalog.ts](../data/harnessCatalog.ts) |
| L355-L366 — the server's `DetectedHarness` / `DetectedHarnessesResponse`, `extra="forbid"` over exactly three fields. | [response_contract.py](../../../mcp/src/agents_remember/serving/response_contract.py) |
| L456-L468 — the `/api/harnesses` fixture these assertions read, pinned by `satisfies HarnessInfo[]`. | [cockpitScenarios.ts](cockpitScenarios.ts) |
| L55-L64 — the guard's record of the unmarked-mirror blind spot both removed fixtures lived in. | [wireFixtureGuard.ts](../test/wireFixtureGuard.ts) |
| Unit under test. | [cockpitScenarios.ts](cockpitScenarios.ts) |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-01T10:20+02:00 — 260731-EFA-L4 curator: documented the new
  `describe("the scenario server answers only what the daemon could answer")` — two exact-sorted-key-set
  assertions covering the two routes whose response types live in unmarked modules and are therefore
  outside `wireFixtureGuard.ts`'s vocabulary: `/api/harnesses` rows must be exactly
  `detected`/`id`/`name` (a `control` field was live), and the withdrawal result exactly the five
  fields `WithdrawalResultWire` declares (a `bridgeEpoch` was live). Recorded why the second one
  compiled: `withdraw` was an async arrow with a concise body, which loses excess-property checking
  because the literal is compared against the inferred `Promise<…>` rather than the contextual one —
  it now carries an explicit `: Promise<WithdrawalResultWire>`. Added the exact-key-set and
  scope invariants, and six two-cell Repo-Internal rows with line ranges inside the `Finding` cell,
  matching this table's existing two-column arity rather than widening the header. Verification
  metadata left pinned; closeout stamps the code commit.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: added real-client scenario coverage for accepted raw
  and harness opens and verified raw catalog rows remain free of fabricated harness authority.
  Verification metadata remains pinned until closeout.

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 same-id cross-generation regressions; verification
  metadata remains blank until commit.

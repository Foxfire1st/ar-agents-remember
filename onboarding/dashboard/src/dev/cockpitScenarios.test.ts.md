# dashboard/src/dev/cockpitScenarios.test.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

No configured Domain Documentation source exists for this file.

### Cross-Repo References

The race suite exercises repository-local generation guards and stores; no cross-repository source applies.

No applicable cross-repository source was found.

### Repo-Internal References

This table keeps exact findings, anchors, and source ranges in three columns.

- L110-L142 — the daemon-answerability `describe` and its two exact-key-set assertions. [1]
- L63-L75 — `authorityTransport`'s `withdraw`, now annotated `: Promise<WithdrawalResultWire>`, with the comment recording why the concise async body lost excess-property checking. [2]
- L40-L46 — `WithdrawalResultWire`'s five declared fields; `bridgeEpoch` is not among them. [3]
- L4-L9 — `HarnessInfo`'s three fields, declared inline in a module with no mirror marker. [4]
- L366-L377 — the server's `DetectedHarness` / `DetectedHarnessesResponse` declares exactly three fields, inheriting strict `WireResponse` whose `model_config` sets `extra="forbid"`. [5]
- The `/api/harnesses` GET branch returns its `harnesses` fixture, type-pinned with `satisfies HarnessInfo[]`. [6]
- L55-L64 — the guard documents the unmarked-mirror blind spot and names the removed `control` and `bridgeEpoch` fixtures. [7]

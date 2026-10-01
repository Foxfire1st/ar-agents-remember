# dashboard/e2e-production/cockpit.production.spec.ts

## Governing Overview

[agents-remember root overview](../../overview.md)

There is no route-local overview for `dashboard/e2e-production/`, and none for `dashboard/` itself,
so the repository root overview is this file's nearest governing ancestor. The sibling suite
[dashboard/e2e-chats overview](../e2e-chats/overview.md) resolves the same way and describes the
contrast between the two: `e2e-chats/` drives the real composed app against real installed harnesses;
this suite route-mocks the whole backend to exercise the **shipped bundle** in isolation.

## Purpose

The production smoke suite for the Chats cockpit: it loads the **built** dashboard and drives the
chooser, the raw-terminal and harness launch paths, the responsive chooser layout, and every session
open failure mode — with no MCP daemon anywhere in the picture. `playwright.production.config.ts`
boots `npm run preview` (Vite's preview server) on `http://127.0.0.1:4173` with `reuseExistingServer:
false`, and the spec fulfils **every** endpoint itself through `page.route`.

That makes it a fixture author, which is the point of its 260731-EFA-L4 change: if this file serves a
payload the server could never produce, a client bug behind that shape cannot be caught here.

## Code Commentary

### Logic

`routeProductionApis(page)` installs the whole fake backend and returns handles the tests drive it
with (`readCount`, `failNext`, `setNextOpen`, `openRequests`, `lastSessionId`). Routes:

- `**/api/stream` — one SSE `snapshot` event carrying `src/fixtures/snapshot.json` spread with a
  `servingBuild` whose `dashboardBuild` is read from disk (see below), so the client's
  build-currency badge resolves to `data-client-build-current="true"`.
- `**/api/events` — a single `ready` event.
- `**/api/terminal/*` (POST) — the open endpoint, dispatched by a module-level `OpenDisposition`
  that the next call consumes and resets: `accept` | `network` | `http` | `harness` | `missing` |
  `malformed` | `contradictory`.
- `**/api/terminal/sessions` — the catalog, replaying rows the accept path pushed.
- `**/api/harnesses` and `**/api/harnesses/claude/capabilities**` — the launch registry (with a
  one-shot `failNext` abort) and a `capabilityEnvelope("claude", "hit")` from the shared typed
  fixture.

Seven tests: the fresh-bundle chooser + client identity, in-place recovery from a failed catalog
read (asserting exactly two extra reads), a `400`/`480`px viewport loop, the raw-terminal open, the
canonical harness launch (model + effort → one opener call), a five-way failure loop asserting the
error text and **zero ghost rows**, and the rejected-harness case that stays in the chooser.

### The Three Answers To "Could The Server Send This?"

The header states them, and they are deliberately different:

1. **The projection is REUSED, which is not the same as being produced by the server — and the
   header now says so.** `snapshot.json` is the largest payload in the file and is read whole from
   `src/fixtures/snapshot.json` rather than written here. The header spells out what that does and
   does not buy: reuse is **not provenance**. `snapshot.json` is hand-maintained and **no generator
   exists** — verified by search, every reference to it in the repository is a read
   (`contract.test.ts`, `test/fixtures/wire.ts`, `data/store.test.ts`, `dev/fixtures.ts`, and this
   spec); nothing derives it from `observer/projection.py`'s pydantic models. It is type-checked
   against `types/projection.ts` by `src/test/contract.test.ts`, and **that mirror is itself
   hand-maintained**, so the chain terminates at a human and not at the server. The biggest payload
   in this file is therefore exactly as unverified as a hand-written one — it is merely unverified
   in ONE place instead of many, which is a real benefit and a smaller one than "generated".

   The capability envelopes are the genuinely stronger claim in this file:
   `capabilityEnvelope("claude", "hit")` comes from `src/test/fixtures/capabilityEnvelopes.ts`,
   which is annotated with the wire types from `types/harnessCapabilities` (`CapabilityEnvelope`,
   `CapabilitySnapshotWire`, `ModelCapabilityWire`, …), so a mirror field it fails to supply does
   not compile.
2. **The happy-path terminal payloads now carry `satisfies`.** The catalog row is
   `satisfies TerminalCatalogRow` and the open response `satisfies TerminalOpenSuccessBody`. This
   found real drift: the open response **omitted `controlEndpoint` and `controlProtocol`**, which
   `TerminalOpenSuccessBody` declares required and `serving/app.py::api_terminal_open` always sends
   (null until the control plane reports an endpoint); and it spread `harness`/`controlState`
   conditionally where the server always sends the key with a `null` value. A client bug behind any
   of those keys could not have been caught here. Both are now unconditional expressions.
   The catalog row keeps its conditional spreads on purpose — `TerminalCatalogRow` declares
   `harness`, `lifecycleId`, `leafKey` and `seatRole` **optional**, so omitting them is a shape the
   server can produce.
3. **The fault-injection payloads are untyped ON PURPOSE.** `missing` (a 200 with an empty body),
   `malformed` (a 200 with `not-json`), `contradictory` (a 200 with a plausible-looking but wrong
   object), and the `503`/`400` bodies must stay untyped. Their entire job is to be shapes the server
   should never send; a `satisfies` there would delete the test. Being unable to type them is not a
   gap in the guard — it is the distinction the guard has to respect.

### Conventions

Payload typing is decided per payload by intent, never applied uniformly: a fixture standing in for
the server is pinned to the wire mirror, a fixture standing in for a *broken* server is not. When a
`satisfies` forces a previously-absent key, the key is written with a comment naming the server
function that always sends it, rather than being spread conditionally to make the type check pass.

### Invariants And Boundaries

- No MCP daemon and no real harness. Every endpoint is `page.route`-fulfilled; the only server is
  Vite's preview of the built bundle.
- The fault-injection dispositions must remain untyped and must remain reachable through
  `setNextOpen`. A future guard rule that demands a wire type at every fulfilled route has to
  exempt them explicitly.
- Failure tests assert **zero** `rail-row-*` elements. A ghost row surviving a failed open is the
  defect class this loop exists for.
- The disposition is one-shot: each open consumes `nextOpen` and resets it to `accept`, so a test
  that opens twice must set it twice.

### Todos

**This spec cannot run in this worktree at all.** At module import it reads
`mcp/src/agents_remember/package_data/dashboard.fingerprint` with `readFileSync`, and that file is
gitignored (`.gitignore` line 24) and written by the release/sync path
(`scripts/sync-dashboard.py::source_fingerprint`, the algorithm `vite.config.ts` compiles into the
bundle). It is absent here, so importing the spec throws before any test runs. This is by design for
a suite that verifies a *built* artefact, but it means the file gets no local signal.

**The projection payload's chain ends at a human, not at the server** — this is a standing property
of the suite, not an open action. `snapshot.json` is hand-maintained, `types/projection.ts` is
hand-maintained, and `contract.test.ts` binds one to the other; nothing in that chain reaches
`observer/projection.py` mechanically. So a green production run claims "the **mirror** could
produce this shape", never "the server sent it". Codegen from the pydantic models is what would
change that, and it is deferred repo-wide (`types/projection.ts` header;
`contract.test.ts` "LEFT FOR CODEGEN (R3)") — it is not a debt owed by this file.

(The header's earlier assertion that `snapshot.json` "is GENERATED from the pydantic models" was
**fixed in the source during this leaf** and is no longer an open item. The header now states the
chain above explicitly. Do not re-open it.)

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source, the Playwright config that runs
it, and the server/mirror types its payloads are pinned to.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

The spec's payloads sit between two contracts it does not own — the dashboard wire mirrors and the
server routes those mirror — so both are cited, along with the config that decides how the suite runs.

- The header's three-answer rule (L8-L29), the `snapshot.json` read (L32-L34), and the module-level `dashboard.fingerprint` read that makes import fail without a release-generated file (L35-L38). [1]
- The fault-injection dispositions — the `OpenDisposition` union declaring `missing`/`malformed`/`contradictory` (L47-L54) and the arms that fulfil them alongside the `503`/`400` bodies (L93-L122), all deliberately untyped. [2]
- The catalog row `satisfies TerminalCatalogRow` (L141) and the open response `satisfies TerminalOpenSuccessBody` (L163), with `harness` (L149), `controlState` (L156), `controlEndpoint` (L159) and `controlProtocol` (L160) written unconditionally. [3]
- The five-way failure loop asserting the error text and zero `rail-row-*` elements (the count assertion at L297). [4]
- The shared typed capability fixture the envelopes come from — annotated with the `types/harnessCapabilities` wire mirrors, which is why it is a stronger claim than the reused projection. [5]
- Nothing generates `snapshot.json`: every reference in the repository reads it. [6]
- `TerminalOpenSuccessBody` — every field required, including the two that were absent before the `satisfies` pin. [7]
- `TerminalCatalogRow` — `harness`, `lifecycleId`, `leafKey` and `seatRole` are optional, which is why the row's conditional spreads stay valid. [8]
- `testDir: "./e2e-production"` and the `npm run preview` web server on `127.0.0.1:4173` — the built bundle, no daemon. [9]
- `dashboard.fingerprint` is gitignored, so the file this spec reads at import does not exist in a working tree. [10]
- `source_fingerprint` — the release-path writer of that file, byte-for-byte the algorithm the bundle carries. [11]

### Cross-Repo References

No meaningful cross-repo references found. The mocked endpoints correspond to routes served by the
`mcp/` package in this same repository; nothing here crosses a repository boundary.

No meaningful cross-repo references found.

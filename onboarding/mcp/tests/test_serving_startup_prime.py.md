# mcp/tests/test_serving_startup_prime.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_startup_prime.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T15:02+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be` |
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

Reviewed at 2026-09-15T15:02+02:00 against the leaf base `d868486c`; the module itself is an
uncommitted candidate at that base, so it does not exist at the commit above and normal closeout owns
the final verification-metadata stamping. The hash records only the base this card was read against.

## Purpose

Falsifiable proof of one startup-ordering boundary: every serving lifespan takes **exactly one**
terminal-catalog observation prime, positioned after control-plane migration and workspace-river
compaction and strictly before `runtime.projector.prime()`, before any recurring loop exists, and
before the lifespan yields — and a prime that raises is contained so serving still starts. It is the
executable half of the `LOCR-R18@v1` contract that
[_app_lifespan.py](../src/agents_remember/serving/_app_lifespan.py.md) implements.

The module does not build a second harness. It imports `_entry`, `_LiveHost`, `_observer_tasks`,
`_RefreshProbe`, `_ServingFixture`, `_VirtualClock` and `_wait_until` from
[test_serving_observation_loop.py](test_serving_observation_loop.py.md) and drives the real
`_serving_lifespan` under the real virtual clock, so a case fails if production stops taking the
prime and also if a hand-aligned harness stops agreeing with production.

## Code Commentary

### Logic

`_seeded_catalog` builds one durable catalog holding a single alive-but-unobserved row;
`_canonical_sweeper` composes the one real `TerminalCatalogLivenessSweeper` over a real
`TerminalCatalog`, the fixture's live fake tmux host, the shared clock, and a real pane capturer; and
`_add_collaborators` gives the fixture's `SimpleNamespace` runtime the extra collaborators the real
agent-notifier loop reads without turning that fake into an untyped bag. `_startup_steps` projects the
fixture's ordered `startup` record down to its step names.

The six cases read the fixture's `startup` record, whose entries are `(step, sweeps_completed)`.
Because the prime is the only sweep that may have completed before the projection is built, that
count is the ordering witness:

- The prime is taken exactly once and before everything else: `probe.calls == 1` at the yield
  boundary, the first startup entry dispatches the prime's own worker task while zero sweeps have
  completed, `startup[1] == ("projection-prime", 1)`, every later step carries that same count, and
  the last step is `("lifespan-yield", 1)` — so the prime is neither skipped, doubled, nor moved.
- The prime runs off the event loop through the drained helper: a spy records the callable handed to
  `_to_thread_drained_on_cancel`, the recorded thread is never the main thread, and a loop timer
  keeps firing while the pass is parked — a bare call on the loop thread would freeze those timers.
- A failed prime still serves: entering the lifespan body at all is the containment assertion, the
  projection is still primed, the recurring owner is still registered, and the owner then retries at
  `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` on its own cadence while staying alive.
- The prime publishes truth the projection and the first notifier sweep read: over a real catalog the
  seeded `ready` row is committed as `unsupported`, and both the captured initial projection and the
  captured first notifier sweep contain that exact committed entry.
- No GET, dashboard, or model message is needed: the app really exposes a
  `GET /api/terminal/sessions` route, the notifier loop really is started, and the prime still
  commits before the yield with the route never dispatched and the notifier never sweeping.
- The prime commits through the same canonical sweeper: the helper was handed the sweeper's own
  `refresh`, the row carries the canonical pane classifier's verdict for the captured pane text, and
  one reference pass over an identical seed at the same clock instant commits an equal entry.

### Conventions

`unittest.IsolatedAsyncioTestCase` with one temporary directory per case, the shared serving fixture,
and no HTTP dispatch, no browser, no real second, no process and no container. Ordinary
version-controlled test source, registered in the repository's `unit-regression` evidence lane; host
results are development evidence and grant no certification authority.

### Invariants And Boundaries

The prime is an attempt, not an availability gate: containment is the contract, so a case that
required startup to abort on a raised prime would be asserting forbidden overreach, and a case that
accepted zero primes or two primes would be asserting a different defect. `probe.calls == 1` at the
yield boundary is the multiplicity invariant; a mutation that removes the prime, doubles it, moves it
after the projection prime or after the recurring tasks, runs it on the loop thread, or replaces it
with a startup-only catalog write each fails named cases.

**Recorded instrument limits — honest boundaries, not resolved claims.** Both were measured by this
leaf's independent review and both remain open for a later hardening leaf:

1. **Cancellation at the prime is reasoned but unfalsified.** The production docstring states
   cancellation is not contained and the surrounding drain still owns thread teardown, and the code
   supports it because the boundary catches `Exception` while `CancelledError` is a `BaseException`
   — but no case here cancels the lifespan while the prime is parked. Replacing the boundary with
   `except BaseException` leaves all eighteen cases in this module and its sibling green
   (`L18-RV-2`). Do not read this module as evidence for the prime's cancellation property.
2. **The ordering witness does not constrain prime-versus-migration/compaction.** `running()` patches
   `migrate_control_plane_identity_logs` and `compact_workspace_river` with plain un-recording mocks,
   so no startup entry is ever recorded for those two steps. Moving the whole prime **before** the
   compaction step also leaves all eighteen cases green (`L18-RV-3`). The witness does genuinely
   constrain prime-versus-projection, prime-versus-recurring-tasks, prime-versus-yield, and
   multiplicity. Migration/compaction precedence rests on the production straight-line order in
   `_serving_lifespan`, not on this proof.

The module claims nothing about the recurring owner's steady cadence or its own per-pass failure
boundary (that is the sibling module's contract), nothing about a health or readiness payload (R18
defines none), and nothing about shutdown draining.

### Todos

None. The two instrument limits above are recorded so the next reader inherits them; hardening them
belongs to a leaf that owns the instrumentation, not to this card.

## Docs References

No Domain Documentation entries are configured in the resolved memory root. The module tests
repository-owned serving behavior, so no external domain claim is needed.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

The cases are grounded in the production startup seam and in the shared serving fixture; these
references describe the behavior under test and do not claim a certification result.

| Finding | Anchor | Source |
| --- | --- | --- |
| One contained pre-serve terminal-catalog observation attempt through the drained helper. | `_prime_terminal_observation` | mcp/src/agents_remember/serving/_app_lifespan.py:129-149 |
| The lifespan runs migration, then compaction, then the prime, then the projection prime, then creates the recurring tasks. | `_serving_lifespan` | mcp/src/agents_remember/serving/_app_lifespan.py:255-310 |
| The steady-state owner the prime shares its canonical entry point with. | `_terminal_observation_loop` | mcp/src/agents_remember/serving/_app_lifespan.py:109-126 |
| The off-loop drain-on-cancel boundary the prime and every later pass both go through. | `_to_thread_drained_on_cancel` | mcp/src/agents_remember/serving/_app_lifespan.py:60-73 |
| The one canonical observation entry point both the prime and later passes call. | `refresh` | mcp/src/agents_remember/serving/terminal_liveness.py:174-221 |
| The six startup-order cases and their `(step, sweeps_completed)` witness. | `ServingStartupPrimeTests` | mcp/tests/test_serving_startup_prime.py:93-352 |
| The shared fixture whose `startup` record and `_Gate` this module reads and reuses. | `_ServingFixture`; `_Gate` | mcp/tests/test_serving_observation_loop.py:246-354; mcp/tests/test_serving_observation_loop.py:223-243 |
| The candidate registers this module once, in the explicit unit-regression lane, one row below its sibling. | "mcp/tests/test_serving_startup_prime.py" | mcp/tests/test-evidence-lanes.toml:128-128 |

## Cross-Repo References

No meaningful cross-repository implementation boundary is established by this repository-owned
unit-regression module.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-18T06:06:32+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:128-128. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T05:29:42+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:126-126. No content impact: mechanical anchor-range projection bound to citation source snapshot 06573647d943a17f74a593342fb552db93e49e5db447dd1a77e4b0a61b2cdf2a; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:35+02:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_serving_startup_prime.py"` → `mcp/tests/test-evidence-lanes.toml:125-125`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.
- 2026-09-18T02:37:44+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:123-123. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:121-121. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_serving_startup_prime.py" repointed to mcp/tests/test-evidence-lanes.toml:117-117. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-15T15:02+02:00 — 260831-LOCR-L18 curator (uncommitted change set on `ar/260831-locr-l18`,
  base `d868486c`): created this card for the leaf's new startup-prime proof module (352 lines, six
  cases, one class, sha256 `fdc8becb…`). It is the executable half of `LOCR-R18@v1` and imports the
  shared fixture from its sibling rather than declaring a second harness, so the card records what
  the module actually pins — one prime, dispatched off-loop through the drained helper, before the
  projection prime and before any recurring task exists; containment of a raised prime with the owner
  retrying on its first cadence; committed truth visible to the initial projection and the first
  notifier sweep; no GET/dashboard/model-message dependency; and the same canonical sweeper entry
  point as every later pass. Two instrument limits are recorded as honest boundaries rather than
  resolved claims, both measured by this leaf's independent review: the boundary's cancellation
  property has no falsifying case here (`except BaseException` leaves all eighteen green —
  `L18-RV-2`), and the `startup` witness records no migration/compaction step, so moving the prime
  before compaction also leaves all eighteen green (`L18-RV-3`). The module is ordinary
  version-controlled test source in the `unit-regression` lane, not a governed evidence artifact.
  Verification metadata is pinned to the leaf base only; the source is an uncommitted candidate, so
  normal closeout owns the final stamping.

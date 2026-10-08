# mcp/tests/test_conversation_library_open.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Deep tests for the 260718-CHATS-L2 `ConversationOpenService` with doubled launch/proof/retire
boundaries: idempotence, exact-identity proof, honest retirement, ledger bounds, the codex
resume channel, and the review-driven race/ownership regressions.

## Code Commentary

### Logic

Twenty async tests cover: the pre-launch poll race (status/reconcile stay pending, released
mismatch retires for real — review F1); absent-row retirement reporting `retire-pending` with
reconcile completing it; the codex `resume_thread_id` channel pass-through, its invalid-target
and non-codex-kind guards; identical replay after ledger-record eviction absorbing through the
live row; evicted changed-conversation replay never retiring the foreign session (review F5);
exact-identity proof with idempotent replay; changed-fingerprint conflict without launch;
unsupported resume never launching; stale expected digest and stale native resolve mapping;
launch-failure 503 shape with no identity; identity-mismatch retirement and reporting;
timeout-unknown staying reconcilable and opening later; ledger-full-of-live refusal; LRU
terminal eviction; ready-without-vendor-identity staying reconciliable; and pre-existing catalog
rows never being touched.

Two further classes carry the history gate's own routing contract, over a **live**
`LibraryGateRegistry` whose only substituted surface is `which` (1173, `_gate_registry`):

- **`UnservedHarnessRefusalTests` (1191)** — a harness the locked helper host does not serve is
  refused **by name**, not crashed on. This experiment extended `HarnessId` to include `"eve"` and
  registered an `eve` row while `HelperHarness`/`HELPER_ENTRY_BY_HARNESS` still name only
  `claude`/`pi`, so a gate that sent every non-codex harness to the helper path indexed that table
  directly — a `KeyError` out of a capability query whose whole job is to fail closed and visibly. The
  shipped `eve` row's argv is not a PATH program, so a default install returns
  `harness not installed: 'eve'` before the helper is consulted and the crash path is **latent**; it
  becomes live as soon as an `eve`-id harness resolves to an executable, which the registry's own
  header permits. The case is therefore the resolvable one, and it asserts the refusal's named reason
  and that no helper process is spawned; the unresolvable sibling keeps its distinct
  not-installed reason.
- **`HelperRouteAuthorityTests` (1235)** — the route follows the **helper host's own entry table**.
  `_NeverCalledHelperHost` (1148) fails loudly if it is reached, so a case can prove the helper route
  was *not* taken; emptying the derived ids is what a hardcoded pair cannot survive, because a table
  member must then be refused by name instead of routed.

Both classes exist because the gate's refusal is a claim about *which* harness reached *which* owner,
and neither half is observable from the outcome alone.

### Conventions

The opener, readiness, and retirement boundaries are doubled with event-parked drives and
flaky-catalog constructions so interleavings are deterministic; the installed suite covers the
same arms live.

### Invariants And Boundaries

- A poll must never settle a pre-launch record, and a tombstone claim must never precede a real
  retirement.
- An absorbed pre-existing session is never retired, whatever it proves.
- Every terminal outcome leaves the ledger evictable; no zombie pending slot survives a drive
  fault.

### Todos

None.

The launch/resume doubles now live in [conversation_open_test_support.py](conversation_open_test_support.py.md). The pre-launch race waits for `_BlockingPort`'s resolve-entry signal before asserting the service stays pending and has not launched; it releases the same gate to test the mismatch and actual retirement.

## Evidence

### Docs References

No Domain Documentation source is configured. The repository sources are direct evidence.

No configured domain documentation was available.

### Repo-Internal References

- The open service, bounded ledger, and record model under test. [1]
- The ASGI open/status/reconcile surface mapping the same outcomes to HTTP. [2]
- The helper host's own entry table, which the gate consults instead of a hardcoded harness pair. [3]
- The gate registry whose routing these cases pin, and the probes they substitute. [4]
- The two classes this leaf added: the named refusal for an unserved harness, and the authority of the derived table over a hardcoded pair. [5]

### Cross-Repo References

No neighboring repository participates in this open suite.

No meaningful cross-repo references found.

- The pre-launch pending assertion follows actual resolve entry. [6]

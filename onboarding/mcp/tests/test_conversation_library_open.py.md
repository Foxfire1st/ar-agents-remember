# mcp/tests/test_conversation_library_open.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_library_open.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| lastVerifiedCommitDate | 2026-09-16T22:28:15+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured. The repository sources are direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The open service, bounded ledger, and record model under test. | "class ConversationOpenService" | mcp/src/agents_remember/serving/conversation/library/open_service.py:242-242 |
| The ASGI open/status/reconcile surface mapping the same outcomes to HTTP. | "class LibraryApiTests(unittest.IsolatedAsyncioTestCase):" | mcp/tests/test_conversation_library_api.py:310-503 |
| The helper host's own entry table, which the gate consults instead of a hardcoded harness pair. | `HELPER_ENTRY_BY_HARNESS`; `HelperHarness`; `ConversationLibraryHelperHost` | mcp/src/agents_remember/serving/conversation/library/helper_host.py |
| The gate registry whose routing these cases pin, and the probes they substitute. | `LibraryGateRegistry`; `GateProbes`; `history_capabilities` | mcp/src/agents_remember/serving/conversation/library/gates.py |
| The two classes this leaf added: the named refusal for an unserved harness, and the authority of the derived table over a hardcoded pair. | `UnservedHarnessRefusalTests`; `HelperRouteAuthorityTests`; `_NeverCalledHelperHost` | mcp/tests/test_conversation_library_open.py:1191-1234; mcp/tests/test_conversation_library_open.py:1235-1297; mcp/tests/test_conversation_library_open.py:1148-1161 |

## Cross-Repo References

No neighboring repository participates in this open suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: recorded the two classes this leaf added to the
  history gate's own routing contract, which extends this module's subject beyond the open service.
  `UnservedHarnessRefusalTests` pins that a harness the locked helper host does not serve is refused
  **by name** rather than crashing on the entry table — the latent `KeyError` path this experiment's
  `HarnessId` extension to `"eve"` created, reachable as soon as an `eve`-id harness resolves to an
  executable — and keeps the distinct `harness not installed` reason for the unresolvable case.
  `HelperRouteAuthorityTests` pins that the route follows the helper host's own derived entry table,
  which a hardcoded `("claude", "pi")` pair cannot survive. Both drive a **live** `LibraryGateRegistry`
  with only `which` substituted, and `_NeverCalledHelperHost` proves the helper route was not taken.
  The cases cost no catalog row and no lane row because they went into an existing module; the D15
  production repair they cover was verified by the independent reviewer, not closed by this pass.
  Verification metadata moves to this leaf's synced base `8997e184`; the candidate is deliberately
  uncommitted, so the governed closeout stamps the real code commit and no hash or fingerprint was
  invented here.

- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `LibraryApiTests` repointed to mcp/tests/test_conversation_library_api.py:310-503. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_conversation_library_open.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B19 curator: replaced the `n/a` table rows with
  exact anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation into
  `test_conversation_library_installed.py`. The two real-open E2E classes are now `PiOpenEndToEndTests`
  L284-L413 and `CodexOpenEndToEndTests` L416-L551 (was the single range L360-L539, which straddled the
  two). Verified by reading both class bodies.
- 2026-07-31T16:50+02:00 — No content impact: 260731-EFA-L2 curator checked this file against the
  leaf diff. Every `ConversationOpenService` construction now takes
  `LibraryBinding(runtime=…, shared=…, authorization=…)`, every `service.open(...)` call passes an
  `OpenRequest(request_id=…, expected_identity_digest=…, cwd=…, launch_context=…)`, and the
  `_Opener` double now receives a `TerminalLaunchRequest`/`SpawnProvenance` pair — so the launch
  assertions read `launch.harness`, `launch.control.resume_thread_id`, `launch.knobs.launch_args`
  and `launch.workspace_root` where they previously read the same values out of a kwargs dict. The
  `retire_entry` patches also absorb positional arguments. All twenty async tests keep their names
  and their asserted outcomes (`opened`, `unsupported`, `stale-identity`, `launch-failed`,
  `identity-mismatch`, `timeout-unknown`, `retire-pending`, ledger-full refusal and LRU eviction),
  and this sidecar cites no line range into this file, so the Logic enumeration and the three
  invariants stand.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the open service deep-test sidecar.
  Verification is blank until closeout commits and stamps the new source.

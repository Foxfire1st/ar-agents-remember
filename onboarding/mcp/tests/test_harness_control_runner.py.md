# test_harness_control_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585` |
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[tests overview](overview.md)

## Purpose
Verifies runner payload decoding, adapter factory composition, Codex app-server argv translation,
session-command correlation, transcript rendering, and shutdown behavior.

## Code Commentary

### Logic

ACPUI-L2 expands this file into the end-to-end hosted launch regression suite. Runner config
round-trips a typed `ResolvedLaunch`; native discovery sees the unmodified base argv; pure
adapter-owned selector preflight runs before discovery; catalog validation selects an exact model
and model-local effort; and a fresh runtime adapter receives the resulting native argv or Codex
session configuration. Pi and Codex echo verification, Claude model mismatch propagation, and the
persistent bridge failure snapshot are covered without submitting a prompt.

The roleless Codex case pins the L2/L4 temporal boundary: ambient spawn spend is ignored, dynamic
advertise supplies the single visible default model and its model-local default effort, and the
session still starts while serving request authority remains a later leaf. Duplicate native
selectors and dynamic refusal stop before the configured runtime adapter or discovery side effect,
while unrelated launch arguments pass.

### Conventions

Use small fake discovery/runtime adapters and an in-process bridge to assert ordering and exact
failure evidence. Native launch channels are asserted at the factory seam; vendor protocol detail
remains in each adapter's own test module.

### Invariants And Boundaries

- Discovery and launch preparation are token-free and submit no turn.
- Adapter-owned model/effort selectors refuse before discovery or vendor startup.
- A failed launch remains queryable as `failed`/`rejected` with exact `raw.bridgeError`.
- Roleless defaults do not read ambient `AR_SPAWN_MODEL` or `AR_SPAWN_EFFORT` as authority.

### Todos

No file-local todos; mid-session switching and serving request fields belong to later ACPUI leaves.
The tests preserve ordinary terminal passthrough and ensure hosted runner behavior remains bridge-owned.

## Docs References
No relevant external/domain documentation was configured.

## Repo-Internal References
- [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py)

## Cross-Repo References
No meaningful cross-repo references.

## Update History
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: expanded the runner card for typed launch
  round-trip, pre-discovery conflict refusal, token-free discovery/validation ordering, native
  launch application, roleless Codex defaults, exact echo checks, and persistent failed-state
  evidence. Verification metadata remains pinned until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added runner and factory conformance coverage.

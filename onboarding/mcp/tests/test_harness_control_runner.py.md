# test_harness_control_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[tests overview](overview.md)

## Purpose
Verifies runner payload decoding, adapter factory composition, the shared public adapter-argv
translation used by runtime launch and pre-session discovery, session input, transcript rendering,
startup failure evidence, and shutdown behavior.

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

ACPUI-L4 moves argv normalization to the public `adapter_argv(harness_id, argv)` seam so the daemon
capability catalog can enumerate with the same effective executable form as a controlled session.
The runner tests continue to require Codex's `app-server` insertion with every caller argument
preserved and unchanged Claude argv. This is a composition refactor only: the existing input-loop
case still submits each complete nonempty terminal line once and reports rejection without paste or
retry behavior.

### Conventions

Use small fake discovery/runtime adapters and an in-process bridge to assert ordering and exact
failure evidence. Native launch channels are asserted at the factory seam; vendor protocol detail
remains in each adapter's own test module.

### Invariants And Boundaries

- Discovery and launch preparation are token-free and submit no turn.
- Adapter-owned model/effort selectors refuse before discovery or vendor startup.
- A failed launch remains queryable as `failed`/`rejected` with exact `raw.bridgeError`.
- Roleless defaults do not read ambient `AR_SPAWN_MODEL` or `AR_SPAWN_EFFORT` as authority.
- Capability discovery and session startup must share `adapter_argv`; Codex gains exactly one
  `app-server` segment while other native harness argv remains unchanged.
- The line-oriented runner input loop owns interactive terminal lines only. The daemon whole-message
  endpoint is covered by the serving API and exact-session IPC suites.

### Todos

No file-local todos. Mid-session switching and serving request fields are covered by their focused
L3/L4 suites; this file preserves runner preparation and interactive loop ownership.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test file proves runner composition and startup behavior; daemon advertise and reliable-submit
contracts remain in their dedicated suites.

| Finding | Anchor | Source |
| --- | --- | --- |
| Runner payload round-trip and `adapter_argv` preserve Codex arguments while inserting `app-server` and leave Claude argv unchanged. | "adapter_argv(config.harness_id" | mcp/tests/test_harness_control_runner.py:98-100 |
| Native factory and launch-preparation cases retain token-free discovery, model-gated validation, and adapter-owned selector refusal. | `test_factory_maps_all_builtins_and_keeps_custom_unsupported`; `LaunchPreparationTests` | mcp/tests/test_harness_control_runner.py:115-127; mcp/tests/test_harness_control_runner.py:167-316 |
| Preparation/start failures remain queryable as failed/rejected evidence with exact bridge detail. | `RunnerStartupFailureTests` | mcp/tests/test_harness_control_runner.py:354-450 |
| Interactive input submits complete nonempty lines once and renders acceptance or rejection; state rendering preserves structured terminal results. | `RunnerLoopTests` | mcp/tests/test_harness_control_runner.py:506-544 |
| Session preparation calls the public argv normalizer; its implementation inserts Codex `app-server` while preserving all caller arguments and leaves other harness argv unchanged. | `adapter_argv` | mcp/src/agents_remember/serving/harness_control_runner.py:311-319 |

## Cross-Repo References

No sibling repository is needed to prove runner composition.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:50+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the four malformed rows with
  class/method anchors and exact extents (`LaunchPreparationTests` 115-318 incl. the factory
  cases, `RunnerStartupFailureTests` 354-452, `RunnerLoopTests` 506-546, and the `adapter_argv`
  call site plus implementation in harness_control_runner.py), and widened the first row's range
  54-108 → 59-114 so the "leave Claude argv unchanged" assertion (110-113) is actually inside it.
  Claim wording unchanged.
- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the public `adapter_argv` seam shared
  by controlled launch and daemon discovery, preserved Codex/Claude argv authority, and clarified
  the interactive line-loop boundary from daemon whole-message submit. Body verified against the
  uncommitted L4 candidate; verification metadata remains pinned to the latest committed source
  revision until closeout.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: expanded the runner card for typed launch
  round-trip, pre-discovery conflict refusal, token-free discovery/validation ordering, native
  launch application, roleless Codex defaults, exact echo checks, and persistent failed-state
  evidence. Verification metadata remains pinned until closeout stamps the L2 code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added runner and factory conformance coverage.

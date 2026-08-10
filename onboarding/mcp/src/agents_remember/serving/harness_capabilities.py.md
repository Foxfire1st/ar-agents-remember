# harness_capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the normalized own-adapter capability vocabulary shared by Claude stream-json, Codex
app-server, and Pi RPC. It carries live model catalogs with model-local effort choices, projects the
ACP Sense 1 category-keyed select shape without ACP transport, and establishes launch/set result
types for later leaves.

## Code Commentary

### Logic

`ModelCapability` nests `EffortOption` rows under one model and retains optional resolved identity,
description, default, visibility, selectability, and provider facts. `CapabilitySnapshot` carries the
catalog and current selection. Its config projection emits a `model` select only when the current
model is known and a `thought_level` select only when current effort is known. The selected model is
always retained in model options—even if hidden or no longer selectable—so `currentValue` remains
honest and belongs to the option set. `LaunchKnobs` carries additive native argv/env/session config
plus the argv options and config keys exclusively owned by that adapter. The launch boundary uses
those ownership declarations to reject a competing free-form selector instead of silently choosing
one. `SetResult` carries explicit mutation acceptance evidence. `SET_ACCEPTANCE_VALUES` is the
runtime authority for the same five tokens expressed by the static literal, and serialization
rejects any out-of-vocabulary value before exposing a serving shape. Serializer helpers expose
stable camel-case objects without inferring effective values. L4's strict inverse parsers rebuild
snapshots and `SetResult` values from exact-session IPC. They validate required text and boolean
fields, the five acceptance tokens, nested model-local effort lists, and any supplied
`configOptions`; that projection must exactly equal what the catalog itself derives.

### Conventions

Normalized keys preserve vendor tokens rather than inventing aliases. ACP-inspired config ids and
categories use `model` and `thought_level`; this is shape adoption only. Config `currentValue` is
always a string when a select is emitted.

### Invariants And Boundaries

- Effort is model-gated; there is no global effort list or hardcoded default catalog path.
- The only set acceptance values are `echo-verified`, `immediate`, `queued`, `unknown`, and
  `unsupported`; runtime validation and serialization fail closed outside that set.
- `echo-verified` is the only result category that may carry a proven effective value; the queue
  additionally enforces the `ok`/effective-value relationships for every category.
- Unknown current model/effort values are omitted from the ACP-style projection rather than guessed.
- IPC parsing rejects a config projection that disagrees with the model-gated catalog instead of
  trusting two competing representations of the same state.
- Adapter-owned launch selectors are explicit data; callers must conflict-check them before native
  discovery or startup rather than relying on argument order.
- This module has no vendor subprocess, session lifecycle, ACP transport, composer-paste, daemon, or
  settings ownership.

### Todos

None known for the normalized L4 serialization/parsing boundary.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The adapter boundary consumes these data types, and each native adapter exposes cached advertise
plus transient discovery through that boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The protocol, discovery, and launchable adapter ports consume `CapabilitySnapshot`, `LaunchKnobs`, and `SetResult`. | `HarnessProtocolAdapter`; `HarnessCapabilityDiscoverer`; `LaunchableHarnessProtocolAdapter` | mcp/src/agents_remember/serving/harness_control_adapter.py:32-59; mcp/src/agents_remember/serving/harness_control_adapter.py:62-65; mcp/src/agents_remember/serving/harness_control_adapter.py:78-88 |
| The submission authority validates the exact `SET_ACCEPTANCE_VALUES` vocabulary and the ok/effective-value relationship before releasing a setter result to its waiter. | `_apply_set_result_locked`; `_validate_set_result` | mcp/src/agents_remember/serving/harness_submission_authority.py:856-882; mcp/src/agents_remember/serving/harness_submission_authority.py:1010-1023 |
| The launch boundary consumes owned selectors before token-free discovery and runtime construction. | `validate_launch_selection`; `apply_launch_knobs` | mcp/src/agents_remember/serving/harness_launch.py:78-119; mcp/src/agents_remember/serving/harness_launch.py:173-206 |
| The exact-session client uses the strict inverse parsers for live advertise and set responses. | `read_control_capabilities`; `_set_control_value` | mcp/src/agents_remember/serving/harness_control_client.py:149-156; mcp/src/agents_remember/serving/harness_control_client.py:584-610 |
| The normalized capability and setter payloads have strict inverse parsers. | `capability_snapshot_from_json`; `set_result_from_json` | mcp/src/agents_remember/serving/harness_capabilities.py:228-246; mcp/src/agents_remember/serving/harness_capabilities.py:249-265 |
| The daemon emits this unchanged normalized shape for both pre-session and live capability reads. | `api_harness_capabilities`; `api_terminal_capabilities` | mcp/src/agents_remember/serving/harness_control_api.py:231-253; mcp/src/agents_remember/serving/harness_control_api.py:255-265 |
| Claude produces native model/effort flags. | `claude_launch_knobs` | mcp/src/agents_remember/serving/harness_control_claude.py:128-142 |
| Codex declares session config plus owned CLI/config selectors. | `codex_launch_knobs` | mcp/src/agents_remember/serving/codex_app_server_session.py:35-54 |
| Pi declares provider-qualified model and thinking flags. | `pi_launch_knobs` | mcp/src/agents_remember/serving/pi_rpc_protocol.py:118-132 |

## Cross-Repo References

No external repository or ACP transport dependency is implemented by the normalized type layer.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 15 citation findings, converting 7 malformed/unanchored adapter rows and 1 legacy prose reference to exact capability, launch, parser, and native-adapter anchors.

- 2026-08-02T01:42+02:00 — 260731-EFA-L6 debt this leaf created, now cleared: three L6 workers split six oversized `serving/` classes while this memory tree was being edited, and every line range in this document that pointed into them went out of bounds the instant the sources shrank (`citation_range_out_of_bounds`). Ranges were re-derived by READING the cited construct at its current location, never by scaling or subtracting a delta — the splits moved code between files rather than shifting it uniformly. Where a construct left the file the row names, the Source Path moved with the range into its own row rather than being silently re-pointed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 cross-file line citations. The setter
  row pointed at `harness_control_queue.py` L476-L508, but that module is now a 227-line facade
  whose `set_model`/`set_effort` cit:([`set_model`, `set_effort`], mcp/src/agents_remember/serving/harness_submission_authority.py:296-297; mcp/src/agents_remember/serving/harness_submission_authority.py:299-300) only delegate — the validation moved with the rest of
  the ordering truth into `harness_submission_authority.py`. Repointed the link and the range to
  `_apply_set_result_locked` cit:([`_apply_set_result_locked`, `_validate_set_result`], mcp/src/agents_remember/serving/harness_submission_authority.py:856-882; mcp/src/agents_remember/serving/harness_submission_authority.py:1010-1023), which is where `SET_ACCEPTANCE_VALUES` membership and the
  `ok`/`effective_value` coherence per acceptance tier are actually enforced, and renamed the row's
  subject accordingly. Both adapter `launch_knobs` rows had also drifted: Claude's native
  `--model`/`--effort` argv is L271-L285 (was `L188-L202`) and Codex's `session_config` plus
  `owned_argv_options`/`owned_config_keys` is L225-L243 (was `L128-L146`). Read all four ranges
  back.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/harness_capabilities.py` since the L2 base commit is the whole-
  tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds. Noted while checking: the references table also
  cites line ranges inside `codex_app_server_adapter.py`, `harness_control_claude.py`,
  `harness_control_client.py` and 1 other file(s); those ranges shifted because this task edited
  those files, so treat the cited numbers as approximate and the linked cards as authoritative.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented strict exact-session inverse
  parsing, model-gated config-projection validation, and unchanged normalized daemon serialization.
- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented the executable five-value
  acceptance authority, fail-closed serialization, and the queue-enforced relationship between
  acceptance, success, and effective values.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented adapter-owned argv/config selectors
  on `LaunchKnobs` and the fail-loud duplicate-authority contract they enable.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: created the normalized capability sidecar for
  model-local effort, ACP Sense 1 select projection, selected-hidden-model honesty, additive launch
  knobs, and the exact mutation-acceptance vocabulary. Verification remains empty until closeout
  stamps the new source.

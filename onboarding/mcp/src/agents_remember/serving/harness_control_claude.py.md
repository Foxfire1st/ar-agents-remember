# harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides the Claude Code long-lived native stream-json adapter, including capability-negotiated
startup, native initial model/effort flags, honest startup verification, cached running
advertisement, MCP-isolated transient token-free discovery, correlated mid-session model/effort
mutation, normalized state/events, interactions, reconciliation, and shutdown.

## Code Commentary

### Logic

`launch_knobs` produces native `--model <key> --effort <level>` argv and declares both flags as
adapter-owned. `start` applies the stream-json protocol flags to the caller launch unchanged,
negotiates structured initialization, and retains the live catalog before constructing the
steady-state reader; it also passes the expected launch's requested model key
(`expected_launch.model_key`) into `negotiate_claude_catalog` so that when the running harness echoes
a resolved id shared by several catalog rows, current-model selection resolves to the requested alias
and the effective-launch echo compares like-for-like (the claude `opus[1m]` refused-pair fix).

A floor-gated sub-agent text launch (fix-round review finding 8) runs through
cit:([`_negotiate`, `start`], mcp/src/agents_remember/serving/harness_control_claude.py:176-223; mcp/src/agents_remember/serving/harness_control_claude.py:283-318): the FIRST launch deliberately omits
`--forward-subagent-text` because no
version seam exists at argv-build time — the installed version is provable only from the captured
`system/init`. When `forward_subagent_text_supported(system_init.version)` confirms the probed
floor (`FORWARD_SUBAGENT_TEXT_FLOOR = (2, 1, 220)`), the adapter stops the transport, re-launches
WITH the flag, and re-negotiates startup; a proven install that then rejected the flag would fail
loudly at launch, never silently degrade. Below the floor (or with an unparseable/absent version)
the adapter simply runs on without the flag. The verdict crosses on the snapshot metadata as
cit:(["subagentTextForwarding"], mcp/src/agents_remember/serving/harness_control_claude.py:225-258): an explicit "enabled: … meets the probed floor …" note
or the exact fail-closed "unverified: … flag was omitted …" reason — never a silent omission.

That re-launch reuses the SAME transport object, so it depends on the transport releasing process
ownership at a completed stop; a transport that retained its terminated process would refuse the
second `start` as already started, and the `HarnessControlError` handler would convert the whole
handshake into an `unsupported` snapshot — the exact shape of the 260727-CHATS-IM-L4 defect, where
every install at or above the floor lost control readiness and therefore model/effort selection.
The probe runs before cit:([`start_reader`], mcp/src/agents_remember/serving/harness_control_claude.py:294-306) exists, so no state reader
competes with that stop.

`discover` copies the `LaunchSpec`, replaces only that transient copy's argv
through `build_claude_discovery_argv`, invokes the same startup/catalog negotiation, returns the
advertisement, and forces the transient adapter down in `finally`. It does not mutate the original
launch or create a second startup implementation.

The discovery-only transform prevents a token-free catalog query from starting unrelated
user-configured MCP children. It removes Claude 2.1.210-supported MCP selectors before the first
`--`, supplies one native strict empty set, and preserves the entire positional suffix. Normal
sessions deliberately retain the installed MCP configuration; cheap discovery resource figures
must not be projected onto real session capacity.

`set_model` and
`set_effort` validate the requested value against the selected dynamic catalog row, submit an
ordinary structured `/model` or `/effort` user frame, then require replay acceptance plus a terminal
result. Model echo matching uses a finite set of exact terminal strings derived from that dynamic
row, resolved identity, catalog-equivalent aliases, and exact default variants; effort requires its
exact session-only result prefix. Only an exact echo updates the cached selection. A completed but
non-matching result is `immediate` without an invented effective value, native failure is
`unsupported`, and missing/disconnected evidence is `unknown`.

### Conventions

The installed/current CLI is launched directly. Initial selection uses native flags and live
switching uses native structured session commands—never composer/session-command paste. No model
key, prefix, alias, or provider name (including Fable) has an AR-side launch-only heuristic: every
selectable row follows the same evidence path, and a generic vendor refusal is mapped only from its
terminal result. The CLI version remains opaque handshake evidence. A running advertise call
performs no RPC, and cold discovery sends no model prompt or user turn. MCP isolation is scoped to
`discover`; `start` preserves configured MCP selectors byte-for-byte before adding only transport
flags.

### Invariants And Boundaries

- Initialization and `list_models` must both succeed before the adapter becomes ready.
- Discovery must remove inherited accepted MCP selectors before adding the strict empty set;
  append-only isolation is invalid because Claude accumulates repeated configs.
- Discovery isolation ends at the first `--`, and a normal session must preserve the caller's MCP
  argv. The adapter wiring must continue to use a copied transient launch, not rewrite `start`.
- The cached catalog is tied to the same native process/session whose `system/init` supplied the
  current model; it is not a hardcoded or cross-session cache.
- Unsupported or stopped state cannot advertise stale capabilities.
- A successful expected launch must echo the selected model; a mismatch is launch failure with exact
  runner evidence, EXCEPT that a requested alias and the echoed key resolving to the same underlying
  model now validate (resolved via the threaded requested key + `verify_effective_launch`'s
  `_resolves_to_same_model`); genuine startup/protocol incompatibility remains `unsupported`.
- Claude effort acceptance is not fabricated: stream-json has no effective-effort echo.
- Mid-session selection changes only after exact terminal echo; replay alone and near-match model
  labels cannot promote the capability snapshot.
- Cancellation and timeout abandon the exact retained submission so a late result cannot satisfy a
  later setter.
- Pane/log fallback, ACP transport, Toad hosting, composer-paste model changes, and blind resend are
  outside this adapter.
- Acceptance remains distinct from completion.
- `--forward-subagent-text` emission is fail-closed: the first launch never
  carries the flag; it is added only on a re-launch after `system/init` proves the version meets
  the probed floor 2.1.220. An unproven or below-floor install runs without the flag and the
  snapshot says so verbatim (`subagentTextForwarding` = "unverified: …") — sub-agent text blocks
  then simply do not cross the live stream instead of being partially guessed.
- The floor gate is the ONLY version heuristic in this adapter (justified because the contract is
  argv-only and cannot be probed without launching the flag); the "no launch-only heuristic"
  convention above otherwise stands unchanged.
- The floor re-launch requires a restartable transport, not a retry or a downgrade: the adapter stops
  and starts the same object exactly once and has no fallback for a refused second start, so the
  transport's ownership-release contract is load-bearing for control readiness.

### Todos

None known for the discovery-isolation and native setter seams.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Startup controls the stdout ownership boundary and the dedicated parser controls live catalog
normalization.

| Finding | Anchor | Source |
| --- | --- | --- |
| State requires the same vendor session, retained UUID, exact canonical replay body, and ordered terminal result. | `ClaudeStreamState`, `_require_faithful_replay`, `_handle_result` | mcp/src/agents_remember/serving/claude_stream_state.py:112-1030; mcp/src/agents_remember/serving/claude_stream_state.py:720-738; mcp/src/agents_remember/serving/claude_stream_state.py:790-849 |
| Protocol keeps normal stream argv construction separate from discovery-only MCP selector replacement and pins the first-`--` boundary. | `build_claude_stream_argv`, `build_claude_discovery_argv` | mcp/src/agents_remember/serving/claude_stream_protocol.py:88-113; mcp/src/agents_remember/serving/claude_stream_protocol.py:116-145 |
| The sub-agent-text forwarding floor gate: `FORWARD_SUBAGENT_TEXT_FLAG`, the probed floor `(2, 1, 220)`, and `forward_subagent_text_supported` — fail-closed so unproven/unparseable versions never get the flag. | `FORWARD_SUBAGENT_TEXT_FLAG`, `FORWARD_SUBAGENT_TEXT_FLOOR`, `forward_subagent_text_supported` | mcp/src/agents_remember/serving/claude_stream_protocol.py:56-56; mcp/src/agents_remember/serving/claude_stream_protocol.py:65-65; mcp/src/agents_remember/serving/claude_stream_protocol.py:77-85 |
| Protocol command gating admits native model/effort categories without model-name heuristics while keeping identity changes blocked. | `_IDENTITY_CHANGING_COMMANDS`, `_NATIVE_CAPABILITY_COMMANDS`, `command_unsupported_detail` | mcp/src/agents_remember/serving/claude_stream_protocol.py:21-24; mcp/src/agents_remember/serving/claude_stream_protocol.py:352-360 |
| Claude catalog parsing validates unique models, selectability, resolved current identity, and model-local effort. | `parse_list_models_response`, `_parse_model`, `_require_unique_model_keys`, `_select_current_model` | mcp/src/agents_remember/serving/claude_stream_capabilities.py:15-32; mcp/src/agents_remember/serving/claude_stream_capabilities.py:50-75; mcp/src/agents_remember/serving/claude_stream_capabilities.py:78-83; mcp/src/agents_remember/serving/claude_stream_capabilities.py:86-110 |
| The shared submission authority admits setters onto the same ordinary-operation timeline as prompt/interaction/reconciliation commands and validates honest `SetResult` evidence. `HarnessControlQueue` no longer exists — it was deleted in 260731-EFA-L6 as a pure forwarding facade, so the authority is now the only owner rather than the thing behind a facade. | `_validate_set_result` | mcp/src/agents_remember/serving/harness_submission_authority.py:1010-1023 |
| Adapter regressions prove token-free discovery, complete selector replacement, end-of-options preservation, forced transient stop, and byte-for-byte normal-start preservation. | `test_discover_uses_only_token_free_bootstrap_and_list_models`, `test_discover_replaces_all_installed_mcp_selector_spellings`, `test_normal_start_preserves_existing_mcp_selectors_byte_for_byte` | mcp/tests/test_harness_control_claude.py:256-276; mcp/tests/test_harness_control_claude.py:278-390; mcp/tests/test_harness_control_claude.py:392-412 |

## Submission Authority Delta

The Claude hosted adapter passes full operation refs through prompt, response, model, and effort
methods and delegates sole-operation preflight to stream state. An unknown setter remains the common
authority barrier until exact resolution; it is not released merely because a caller timed out.

## Native Interrupt Acceptance Delta

The Claude control adapter now sends native interrupts through the shared control channel and returns a typed acceptance outcome. It does not infer terminal delivery from the write acknowledgement; stream settlement remains the authority.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Floor-Gated Sub-Agent Text Forwarding Delta

`start` now performs the floor-gated `--forward-subagent-text` launch (fix-round review finding 8): first launch omits the flag (no version seam exists at argv-build time), the captured `system/init` version decides, a proven install re-launches with the flag and re-negotiates, and the snapshot metadata carries the explicit `subagentTextForwarding` verdict — "enabled" with the floor citation or "unverified" with the exact fail-closed reason. This is the claude half of the sub-agent conversation story (the `subagents/*.jsonl` native-library side joins by `parent_tool_use_id` in the projector).

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

**`ExpectedEcho`** (`expected_result`, `prefix_match`, `allowed_results`) names what counts as the
harness having **ACCEPTED** one set command, in its own words. A Claude set is proven only by the
echo it writes back, so the exact expected line, whether a prefix is enough, and which other lines
also settle it are one acceptance rule — splitting them is how a command gets matched against
another command's echo. The accepted echoes themselves are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-03T02:59:16+02:00 — Curator W3-B02 repaired 6 Repo-Internal citation rows, resolving 12 manifest findings with exact current state, protocol, capability, and regression-test anchors; converted 3 current prose line references to exact `cit:` citations; removed 2 unsupported external-evidence claims rather than preserving them as empty-state rows. Verification metadata was preserved.
- 2026-08-02T01:42+02:00 — 260731-EFA-L6 debt this leaf created, now cleared: three L6 workers split six oversized `serving/` classes while this memory tree was being edited, and every line range in this document that pointed into them went out of bounds the instant the sources shrank (`citation_range_out_of_bounds`). Ranges were re-derived by READING the cited construct at its current location, never by scaling or subtracting a delta — the splits moved code between files rather than shifting it uniformly. Where a construct left the file the row names, the Source Path moved with the range into its own row rather than being silently re-pointed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 2 stale self-citations. The
  floor-gated launch is now cited as `start` L115-L237 with the gate block at L120-L144 (the old
  L116-L145 clipped the `def` line and both ends of the gate). The "`_state` does not exist yet"
  claim cited L201-L211, which the added `requestedLaunchModel`/`requestedLaunchEffort`/
  `launchEffortEvidence` snapshot-`raw` entries turned into part of that dict; `self._state` is
  assigned at L213-L224 and its reader started at L225, so the ordering claim holds and now points
  there. The neighbouring `subagentTextForwarding` citations (L173-L182, L199) were re-read and are
  still exact.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that moved when the command queue became a facade. `harness_control_queue.py` is now 227 lines of pure delegation, so the setter-serialization/`SetResult`-validation row was repointed to `harness_submission_authority.py` (`set_model`/`set_effort` L335-L339, `_admit_setter` enqueueing onto the single timeline L725-L760, `_apply_set_result_locked` L1021-L1049, `_validate_set_result` L1323-L1336) and the claim reworded to name the authority.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `ExpectedEcho` as the one acceptance rule per set command.
- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: recorded that the floor re-launch reuses one transport
  object and therefore depends on the transport's ownership-release contract, that the probe runs
  before the state reader exists, and that a refused second start degrades the whole handshake to
  `unsupported` rather than retrying.
- 2026-07-26T15:34 — 260718-CHATS-L7 curator: documented the floor-gated `--forward-subagent-text`
  launch in `start` (fail-closed first launch, `system/init`-proven re-launch, snapshot
  `subagentTextForwarding` verdict), added the fail-closed invariants, refreshed the protocol argv
  citation ranges for the L7-shifted source, and added the floor-gate protocol citation row.
  Verification metadata stays pinned to the pre-commit source history until closeout (the L7 change
  is uncommitted).
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R2 — `start` now passes the expected launch's
  requested model key into `negotiate_claude_catalog`, so a resolved-model collision (e.g. `opus[1m]`
  and `default` sharing `claude-opus-4-8[1m]`) resolves the current model to the requested alias and
  `verify_effective_launch` validates the natively-succeeding launch instead of refusing it. Verification
  metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented op-aware Claude control and the exact unknown-
  setter barrier.

- 2026-07-16T07:25+02:00 — 260714-ACPUI-L5 curator: documented adapter wiring through a copied
  discovery launch, native MCP selector normalization, forced transient teardown, token/resource
  rationale, and the hard boundary that normal startup preserves user configuration. Preserved the
  blocked append-only attempt and the final two-marker plus independent-marker closure. Verification
  metadata remains pinned to the latest committed L3 source until the reviewed L5 candidate lands.
- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented structured native setters,
  model-gated validation, exact dynamic terminal-label evidence, honest immediate/unsupported/unknown
  outcomes, tombstone-safe cancellation, and the live-reviewed absence of a Fable heuristic or
  launch-only policy.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented native model/effort launch flags,
  Fable-compatible launch selection, honest no-effort-echo evidence, and failed/rejected treatment
  for an effective-model mismatch after successful negotiation.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented live catalog negotiation,
  same-process cached advertise, transient prompt-free discovery, and the later-leaf launch/mutation
  boundary; removed stale account-field requirements.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: historicized the obsolete
  exact-2.1.207 normative contract and made consumed structured capability evidence authoritative.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented direct launch and structured Claude capability
  negotiation replacing the production version preflight.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.

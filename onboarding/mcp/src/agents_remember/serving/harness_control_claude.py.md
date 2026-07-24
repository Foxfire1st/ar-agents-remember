# harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
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
steady-state reader; since 260718-CHATS-L5F R2 it passes the expected launch's requested model key
(`expected_launch.model_key`) into `negotiate_claude_catalog` so that when the running harness echoes
a resolved id shared by several catalog rows, current-model selection resolves to the requested alias
and the effective-launch echo compares like-for-like (the claude `opus[1m]` refused-pair fix). `discover` copies the `LaunchSpec`, replaces only that transient copy's argv
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
  model now validate (R2, resolved via the threaded requested key + `verify_effective_launch`'s
  `_resolves_to_same_model`); genuine startup/protocol incompatibility remains `unsupported`.
- Claude effort acceptance is not fabricated: stream-json has no effective-effort echo.
- Mid-session selection changes only after exact terminal echo; replay alone and near-match model
  labels cannot promote the capability snapshot.
- Cancellation and timeout abandon the exact retained submission so a late result cannot satisfy a
  later setter.
- Pane/log fallback, ACP transport, Toad hosting, composer-paste model changes, and blind resend are
  outside this adapter.
- Acceptance remains distinct from completion.

### Todos

None known for the L5 discovery-isolation and native setter seams.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Startup controls the stdout ownership boundary and the dedicated parser controls live catalog
normalization.

| Finding | Citations | Source Path |
| --- | --- | --- |
| State requires the same vendor session, retained UUID, exact canonical replay body, and ordered terminal result. | L102-L169; L412-L471; L529-L565 | [claude_stream_state.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_state.py) |
| Protocol keeps normal stream argv construction separate from discovery-only MCP selector replacement and pins the first-`--` boundary. | L41-L87 | [claude_stream_protocol.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_protocol.py) |
| Protocol command gating admits native model/effort categories without model-name heuristics while keeping identity changes blocked. | L223-L261 | [claude_stream_protocol.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_protocol.py) |
| Claude catalog parsing validates unique models, selectability, resolved current identity, and model-local effort. | L15-L97 | [claude_stream_capabilities.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_capabilities.py) |
| The shared queue serializes setters with prompt/interaction/reconciliation commands and validates honest `SetResult` evidence. | L73-L180; L476-L508 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |
| Adapter regressions prove token-free discovery, complete selector replacement, end-of-options preservation, forced transient stop, and byte-for-byte normal-start preservation. | L195-L351 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |

## Cross-Repo References

No runtime cross-repository boundary is implemented by this adapter. The coordination evidence is
retained because the resource measurement triggered the discovery-only change and independent
review found the selector-collision class that the first implementation missed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Resource proof distinguishes cheap strict-empty discovery from materially heavier normal sessions and records the corrected live two-marker closure. | L65-L109 | [260716-ACPUI-L5-worker-closeout-report.md](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-worker-closeout-report.md) |
| Independent review confirms the copied discovery path, normal-start preservation, absent marker, complete live catalog, and final repository gates. | L70-L88 | [260716-ACPUI-L5-reviewer-verdict.md](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-reviewer-verdict.md) |

## 260715-FEUI-L5 Submission Authority Delta

The Claude hosted adapter passes full operation refs through prompt, response, model, and effort
methods and delegates sole-operation preflight to stream state. An unknown setter remains the common
authority barrier until exact resolution; it is not released merely because a caller timed out.

## 260718-CHATS-L5I Current Delta

The Claude control adapter now sends native interrupts through the shared control channel and returns a typed acceptance outcome. It does not infer terminal delivery from the write acknowledgement; stream settlement remains the authority.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

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

# harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:19+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides the Claude Code long-lived native stream-json adapter, including capability-negotiated
startup, native initial model/effort flags, honest startup verification, cached running
advertisement, transient token-free discovery, correlated mid-session model/effort mutation,
normalized state/events, interactions, reconciliation, and shutdown.

## Code Commentary

### Logic

`launch_knobs` produces native `--model <key> --effort <level>` argv and declares both flags as
adapter-owned. `start` applies the stream-json protocol flags, negotiates structured initialization,
and retains the live catalog before constructing the steady-state reader. `set_model` and
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
performs no RPC, and cold discovery sends no model prompt or user turn.

### Invariants And Boundaries

- Initialization and `list_models` must both succeed before the adapter becomes ready.
- The cached catalog is tied to the same native process/session whose `system/init` supplied the
  current model; it is not a hardcoded or cross-session cache.
- Unsupported or stopped state cannot advertise stale capabilities.
- A successful expected launch must echo the selected model; mismatch is launch failure with exact
  runner evidence, while genuine startup/protocol incompatibility remains `unsupported`.
- Claude effort acceptance is not fabricated: stream-json has no effective-effort echo.
- Mid-session selection changes only after exact terminal echo; replay alone and near-match model
  labels cannot promote the capability snapshot.
- Cancellation and timeout abandon the exact retained submission so a late result cannot satisfy a
  later setter.
- Pane/log fallback, ACP transport, Toad hosting, composer-paste model changes, and blind resend are
  outside this adapter.
- Acceptance remains distinct from completion.

### Todos

None known for the L3 native setter seam.

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
| Protocol command gating admits native model/effort categories without model-name heuristics while keeping identity changes blocked. | L190-L227 | [claude_stream_protocol.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_protocol.py) |
| Claude catalog parsing validates unique models, selectability, resolved current identity, and model-local effort. | L15-L97 | [claude_stream_capabilities.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_capabilities.py) |
| The shared queue serializes setters with prompt/interaction/reconciliation commands and validates honest `SetResult` evidence. | L73-L180; L476-L508 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |

## Cross-Repo References

No external repository boundary is implemented by this adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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

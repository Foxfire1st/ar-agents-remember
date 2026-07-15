# harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585` |
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides the Claude Code long-lived native stream-json adapter, including capability-negotiated
startup, native initial model/effort flags, honest startup verification, cached running
advertisement, transient token-free discovery, normalized state/events, interactions,
reconciliation, and shutdown.

## Code Commentary

### Logic

`launch_knobs` produces native `--model <key> --effort <level>` argv and declares both flags as
adapter-owned. `start` applies the stream-json protocol flags around that configured argv, completes
structured initialization, and fetches the live model catalog before constructing the steady-state
reader. When an expected launch is present, it validates the selected model against `system/init`
and the catalog. Claude exposes no effort echo, so successful evidence is honestly limited to
model-gated catalog validation plus native-flag startup and is recorded as such. A post-negotiation
model mismatch force-closes transport and propagates as a failed/rejected runner launch rather than
being reclassified as unsupported. `discover` uses the native start/catalog path then forces
shutdown; ordinary unsupported negotiation remains distinct.

### Conventions

The installed/current CLI is launched directly. Fable-5 and initial effort use native flags, never
composer/session-command paste. The CLI version remains opaque handshake evidence. A running
advertise call performs no RPC, and cold discovery sends no model prompt or user turn.

### Invariants And Boundaries

- Initialization and `list_models` must both succeed before the adapter becomes ready.
- The cached catalog is tied to the same native process/session whose `system/init` supplied the
  current model; it is not a hardcoded or cross-session cache.
- Unsupported or stopped state cannot advertise stale capabilities.
- A successful expected launch must echo the selected model; mismatch is launch failure with exact
  runner evidence, while genuine startup/protocol incompatibility remains `unsupported`.
- Claude effort acceptance is not fabricated: stream-json has no effective-effort echo.
- Pane/log fallback, ACP transport, Toad hosting, composer-paste model changes, and blind resend are
  outside this adapter.
- Acceptance remains distinct from completion.

### Todos

L3 adds honest mid-session model/effort mutation.

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
| Startup completes initialization and correlated catalog enumeration before returning capabilities. | L59-L109 | [claude_stream_startup.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_startup.py) |
| Claude catalog parsing validates unique models, selectability, resolved current identity, and model-local effort. | L15-L97 | [claude_stream_capabilities.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_capabilities.py) |
| Shared effective-launch verification permits the documented no-effort-echo asymmetry but requires the model echo. | L122-L146 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| The hosted runner persists propagated startup mismatch as failed/rejected with exact bridge error. | L103-L140 | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |

## Cross-Repo References

No external repository boundary is implemented by this adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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

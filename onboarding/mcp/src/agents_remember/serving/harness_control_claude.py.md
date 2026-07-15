# harness_control_claude.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_claude.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Provides the Claude Code long-lived native stream-json adapter, including capability-negotiated
startup, cached running advertisement, transient token-free discovery, normalized state/events,
interactions, reconciliation, and shutdown.

## Code Commentary

### Logic

`start` validates Claude launch identity, applies stream-json flags, starts the subprocess, completes
structured initialization, and immediately fetches the live model catalog before constructing the
steady-state reader. The normalized catalog is retained in `_capabilities`; `advertise` returns it
only while adapter state is ready. `discover` uses the same native start/catalog path and then forces
shutdown. Existing submission, response, reconciliation, and unsupported-handshake behavior remains
delegated to the bounded state/transport components.

### Conventions

The installed/current CLI is launched directly. The CLI version remains opaque handshake evidence.
A running advertise call performs no RPC, and cold discovery sends no model prompt or user turn.

### Invariants And Boundaries

- Initialization and `list_models` must both succeed before the adapter becomes ready.
- The cached catalog is tied to the same native process/session whose `system/init` supplied the
  current model; it is not a hardcoded or cross-session cache.
- Unsupported or stopped state cannot advertise stale capabilities.
- Pane/log fallback, ACP transport, Toad hosting, composer-paste model changes, and blind resend are
  outside this adapter.
- Acceptance remains distinct from completion.

### Todos

L2 adds settings-owned launch flags and L3 adds honest mid-session model/effort mutation.

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
| Startup completes initialization and correlated catalog enumeration before returning capabilities. | L59-L109 | [claude_stream_startup.py](claude_stream_startup.py) |
| Claude catalog parsing validates unique models, selectability, resolved current identity, and model-local effort. | L15-L97 | [claude_stream_capabilities.py](claude_stream_capabilities.py) |

## Cross-Repo References

No external repository boundary is implemented by this adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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

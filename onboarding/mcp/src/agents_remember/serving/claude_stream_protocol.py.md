# claude_stream_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines strict Claude Code stream-json framing and the protocol parsers used by the long-lived
native adapter. It owns launch transport flags, initialization and bootstrap frames, the correlated
`list_models` request shape, session commands, interactions, and safe terminal-result extraction.

## Code Commentary

### Logic

`build_claude_stream_argv` preserves caller arguments while requiring stream-json input/output,
stdio permission prompts, print mode, verbosity, and replayed user messages. Initialization combines
a correlated control request with a synthetic, non-query user frame so `system/init` can establish
the session without a model turn. `list_models_request` adds the token-free catalog control request;
catalog payload parsing is deliberately separated into `claude_stream_capabilities.py`. The rest of
the module validates command use, maps permission and question interactions, clips transcript text,
and retains only safe terminal metadata.

### Conventions

Control responses are matched by exact request id and subtype. The CLI-reported version is opaque
evidence rather than an allowlist. Slash-command names are normalized without their leading slash,
and the synthetic bootstrap keeps `shouldQuery` false.

### Invariants And Boundaries

- Structured control/system frames are authoritative; pane, log, prompt-text, and timing fallbacks
  cannot establish readiness or capabilities.
- Initialization requires session, cwd, model, permission mode, tools, and slash commands, but model
  catalog and effort menus come only from the later `list_models` control response.
- Identity-changing commands remain blocked inside one long-lived adapter. Other session commands,
  including model/effort commands when advertised, are not blocked by a fabricated local denylist.
- A nominal success frame with error evidence remains failed, and credentials are not retained.

### Todos

None known for the L1 advertise contract.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Startup owns the request ordering, while the dedicated catalog parser owns the dynamic model and
model-gated effort projection.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Startup sends initialization/bootstrap before the correlated catalog request and rejects unexpected catalog frames. | L59-L109 | [claude_stream_startup.py](claude_stream_startup.py) |
| Catalog parsing validates model identities, disabled state, and each model's own effort menu. | L15-L97 | [claude_stream_capabilities.py](claude_stream_capabilities.py) |

## Cross-Repo References

No external repository boundary is implemented by this protocol module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented the correlated token-free
  `list_models` request, modern initialization fields, command-gate boundary, and split catalog
  parser; refreshed all required onboarding sections and internal citations.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: replaced the stale exact-version description with the
  structured Claude capability contract; fixture versions remain non-production evidence.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.

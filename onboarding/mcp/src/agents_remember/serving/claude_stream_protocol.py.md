# claude_stream_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:19+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines strict Claude Code stream-json framing and the protocol parsers used by the long-lived
native adapter. It owns launch transport flags, initialization and bootstrap frames, the correlated
`list_models` request shape, native session commands, their canonical replay bodies, interactions,
and safe terminal-result extraction.

## Code Commentary

### Logic

`build_claude_stream_argv` preserves caller arguments while requiring stream-json input/output,
stdio permission prompts, print mode, verbosity, and replayed user messages. Initialization combines
a correlated control request with a synthetic, non-query user frame so `system/init` can establish
the session without a model turn. `list_models_request` adds the token-free catalog control request;
catalog payload parsing is deliberately separated into `claude_stream_capabilities.py`.
`session_command_replay_text` derives Claude's canonical
`<command-name>/<command-message>/<command-args>` replay for an ordinary slash-command frame, so
state correlation can compare the vendor replay exactly without pretending it is byte-identical to
the submitted text. The command gate keeps identity-changing commands local-blocked while allowing
the native model/effort capability commands to be decided by structured vendor evidence. The rest
of the module maps interactions, clips transcript text, and retains only safe terminal metadata.

### Conventions

Control responses are matched by exact request id and subtype. The CLI-reported version is opaque
evidence rather than an allowlist. Slash-command names are normalized without their leading slash;
model and effort are capability-command categories, not model-name special cases. The synthetic
bootstrap keeps `shouldQuery` false.

### Invariants And Boundaries

- Structured control/system frames are authoritative; pane, log, prompt-text, and timing fallbacks
  cannot establish readiness or capabilities.
- Initialization requires session, cwd, model, permission mode, tools, and slash commands, but model
  catalog and effort menus come only from the later `list_models` control response.
- Identity-changing commands remain blocked inside one long-lived adapter. Model/effort commands
  are admitted to the native evidence path without a Fable key/prefix heuristic or launch-only
  policy; any native refusal is classified later from the correlated terminal result.
- A command replay is authoritative only when its retained UUID, vendor session, and exact canonical
  body agree; this module supplies the canonical body but does not promote acceptance itself.
- A nominal success frame with error evidence remains failed, and credentials are not retained.

### Todos

None known for the L3 native-command framing contract.

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
| Startup sends initialization/bootstrap before the correlated catalog request and rejects unexpected catalog frames. | L59-L109 | [claude_stream_startup.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_startup.py) |
| State requires the same session, retained UUID, and exact canonical replay body before accepting a command. | L412-L471 | [claude_stream_state.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_state.py) |
| Catalog parsing validates model identities, disabled state, and each model's own effort menu. | L15-L97 | [claude_stream_capabilities.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_capabilities.py) |

## Cross-Repo References

No external repository boundary is implemented by this protocol module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented native model/effort command
  admission, canonical replay-body derivation, exact downstream correlation, and the absence of
  any Fable name heuristic or launch-only classification.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented the correlated token-free
  `list_models` request, modern initialization fields, command-gate boundary, and split catalog
  parser; refreshed all required onboarding sections and internal citations.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: replaced the stale exact-version description with the
  structured Claude capability contract; fixture versions remain non-production evidence.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.

# claude_stream_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T07:25+02:00 |
| lastVerifiedCommitHash | `d99a1a7f3ac251957ae155ea9beb878b9ba1ab25` |
| lastVerifiedCommitDate | 2026-07-16T07:36:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines strict Claude Code stream-json framing and the protocol parsers used by the long-lived
native adapter. It owns normal stream transport flags, a discovery-only MCP-selector normalizer,
initialization and bootstrap frames, the correlated `list_models` request shape, native session
commands, their canonical replay bodies, interactions, and safe terminal-result extraction.

## Code Commentary

### Logic

`build_claude_stream_argv` preserves caller arguments while requiring stream-json input/output,
stdio permission prompts, print mode, verbosity, and replayed user messages.
`build_claude_discovery_argv` is a separate, discovery-only transform for Claude Code 2.1.210's
accumulating MCP grammar. Before the first `--`, it removes separate variadic/repeated
`--mcp-config <configs...>`, equals-attached `--mcp-config=<config>`, and the exact
`--strict-mcp-config` flag. It preserves unrelated arguments and order, treats an attached config
as one token only, preserves the complete post-`--` positional suffix byte-for-byte, then inserts
exactly one strict empty MCP config immediately before `--` or at argv end.

Initialization combines a correlated control request with a synthetic, non-query user frame so
`system/init` can establish the session without a model turn. `list_models_request` adds the
token-free catalog control request; catalog payload parsing is deliberately separated into
`claude_stream_capabilities.py`.
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
bootstrap keeps `shouldQuery` false. Discovery normalization recognizes only selector spellings
accepted by the live 2.1.210 grammar; it does not guess unsupported boolean or negated strict forms.

### Invariants And Boundaries

- Structured control/system frames are authoritative; pane, log, prompt-text, and timing fallbacks
  cannot establish readiness or capabilities.
- Initialization requires session, cwd, model, permission mode, tools, and slash commands, but model
  catalog and effort menus come only from the later `list_models` control response.
- Normal `start()` argv remains caller-owned and is processed only by `build_claude_stream_argv`;
  discovery isolation must never strip configured MCP selectors from a real user session.
- Discovery removes all recognized MCP selectors only before the first `--`, preserves the entire
  positional suffix, and installs one native strict empty set. Appending without removal is not
  isolation because Claude accumulates repeated MCP configs.
- Identity-changing commands remain blocked inside one long-lived adapter. Model/effort commands
  are admitted to the native evidence path without a Fable key/prefix heuristic or launch-only
  policy; any native refusal is classified later from the correlated terminal result.
- A command replay is authoritative only when its retained UUID, vendor session, and exact canonical
  body agree; this module supplies the canonical body but does not promote acceptance itself.
- A nominal success frame with error evidence remains failed, and credentials are not retained.

### Todos

None known for the L5 discovery-normalization and native-command framing contract.

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
| The adapter applies discovery normalization only to a copied transient launch, then uses the ordinary startup/advertise/forced-stop sequence. | L192-L206 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| Regression cases cover separate, repeated/variadic, equals-attached, end-of-options, exactly-one-empty-selector, and normal-start preservation behavior. | L195-L351 | [test_harness_control_claude.py](agents-remember/mcp/tests/test_harness_control_claude.py) |
| Startup sends initialization/bootstrap before the correlated catalog request and rejects unexpected catalog frames. | L59-L109 | [claude_stream_startup.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_startup.py) |
| State requires the same session, retained UUID, and exact canonical replay body before accepting a command. | L412-L471 | [claude_stream_state.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_state.py) |
| Catalog parsing validates model identities, disabled state, and each model's own effort menu. | L15-L97 | [claude_stream_capabilities.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_capabilities.py) |

## Cross-Repo References

No runtime cross-repository boundary is implemented by this protocol module. Task-local live and
review evidence records why the strict-empty discovery grammar exists and preserves the failed
append-only attempt as review history.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The final worker report records the blocked append-only selector attempt, the corrected pre-`--` grammar, and two-marker zero-turn closure. | L72-L96 | [260716-ACPUI-L5-worker-closeout-report.md](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-worker-closeout-report.md) |
| Independent review confirms normal-start preservation, the absent synthetic MCP marker, all five live rows, and the closed high-severity collision. | L70-L88; L165-L168 | [260716-ACPUI-L5-reviewer-verdict.md](ar-coordination/tasks/agents-remember/260714_dependency-owned-acp-session-interface/notes/reports/260716-ACPUI-L5-reviewer-verdict.md) |

## Update History

- 2026-07-16T07:25+02:00 — 260714-ACPUI-L5 curator: documented the discovery-only native MCP
  selector grammar, first-`--` boundary, exactly-one strict empty replacement, and normal-start
  preservation. Retained the adversarial review history: append-only isolation was blocked, then
  fake grammar cases plus two independent live marker probes closed the collision. Verification
  metadata remains pinned to the latest committed L3 source until the reviewed L5 candidate lands.
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

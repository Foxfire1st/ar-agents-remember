# claude_stream_protocol.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_protocol.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:34 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines strict Claude Code stream-json framing and the protocol parsers used by the long-lived
native adapter. It owns normal stream transport flags, a discovery-only MCP-selector normalizer,
initialization and bootstrap frames, the correlated `list_models` request shape, native session
commands, their canonical replay bodies, interactions, and safe terminal-result extraction. It
also owns the fail-closed
`--forward-subagent-text` capability: the flag constant, its probed version floor, and the
parse/verdict helpers `build_claude_stream_argv` consults before emitting the flag — the only
version gate in the module, justified because an argv-only contract cannot be probed without
launching the flag itself.

## Code Commentary

### Logic

cit:([`build_claude_stream_argv`], mcp/src/agents_remember/serving/claude_stream_protocol.py:88-113) preserves caller arguments while requiring stream-json
input/output, stdio permission prompts, print mode, verbosity, and replayed user messages. It
takes a keyword-only `forward_subagent_text` flag: the
`--forward-subagent-text` transport flag cit:([`FORWARD_SUBAGENT_TEXT_FLAG`], mcp/src/agents_remember/serving/claude_stream_protocol.py:56-56) is appended only when
the caller proved the installed CLI meets `FORWARD_SUBAGENT_TEXT_FLOOR` (2.1.220, L65) — never by
default. The verdict helpers are `claude_version_tuple` (L68-L74 — parses `major.minor.patch`;
anything unparseable is `None`, never guessed) and `forward_subagent_text_supported` (L77-L85 —
fail-closed: `None`/unproven versions never get the flag). A caller-supplied flag inside `argv` is
preserved verbatim exactly like every other caller argument.
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
evidence rather than an allowlist — with ONE justified exception: the
`--forward-subagent-text` floor, because an argv-only contract cannot be probed without launching
the flag itself, and even there an unparseable version parses to `None` (unproven), never a
guess. Slash-command names are normalized without their leading slash;
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
- `--forward-subagent-text` emission is fail-closed (fix-round review finding
  8): the flag is appended only when the caller proved the installed CLI meets
  `FORWARD_SUBAGENT_TEXT_FLOOR` (2.1.220, the only version it was ever probed against); unproven
  or unparseable versions never get it, and a caller-supplied flag inside `argv` is preserved
  verbatim like every other caller argument.
- No version seam exists at argv-build time — the installed version is captured only by
  `system/init` AFTER launch — so the floor verdict is consumed downstream of that capture: the
  adapter launches WITHOUT the flag (the fail-closed default) and re-launches WITH it only on a
  proven install; below the floor the capability is marked unverified with the exact reason,
  never silently omitted.

### Todos

None known for the discovery-normalization and native-command framing contract.

## Repo-Internal References

Startup owns the request ordering, while the dedicated catalog parser owns the dynamic model and
model-gated effort projection. The adapter also owns the flag's consumption:
it launches WITHOUT `--forward-subagent-text`, consults this module's floor verdict against the
`system/init`-captured version, and re-launches WITH the flag only on a proven install.

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter applies discovery normalization only to a copied transient launch, then uses the ordinary startup/advertise/forced-stop sequence. | `ClaudeStreamJsonAdapter` | mcp/src/agents_remember/serving/harness_control_claude.py:145-571 |
| The adapter launches without the flag, re-launches with it when `system/init` proves the floor, and records the exact enabled/unverified reason in the snapshot. | `ClaudeStreamJsonAdapter` | mcp/src/agents_remember/serving/harness_control_claude.py:145-571 |
| Regression cases cover separate, repeated/variadic, equals-attached, end-of-options, exactly-one-empty-selector, and normal-start preservation behavior. | `test_discover_uses_only_token_free_bootstrap_and_list_models` | mcp/tests/test_harness_control_claude_stream_1.py:33-53 |
| Floor-gate regressions: at/above the floor the adapter re-launches with the flag; an unparseable version stays fail-closed with no flag. | `test_forward_subagent_text_stays_fail_closed_on_an_unparseable_version` | mcp/tests/test_harness_control_claude_stream_1.py:275-290 |
| Startup sends initialization/bootstrap before the correlated catalog request and rejects unexpected catalog frames. | `negotiate_claude_startup` | mcp/src/agents_remember/serving/claude_stream_startup.py:59-81 |
| State requires the same session, retained UUID, and exact canonical replay body before accepting a command. | `ClaudeStreamState` | mcp/src/agents_remember/serving/claude_stream_state.py:112-1030 |
| Catalog parsing validates model identities, disabled state, and each model's own effort menu. | `parse_list_models_response` | mcp/src/agents_remember/serving/claude_stream_capabilities.py:15-32 |

## Structured Interaction And Interrupt Grammar Delta

Claude protocol parsing now normalizes structured multi-question interactions and the native interrupt request/response grammar. Terminal classification treats an interrupt as `interrupted` only when accepted-interrupt correlation and the supported abort shape prove it; unrelated errors remain failures.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: deleted 2 unanchorable task-report claims and repaired the remaining 16 citation findings; scoped check passed.

- 2026-07-26T15:34 — 260718-CHATS-L7 curator: documented R4 — the fail-closed
  `--forward-subagent-text` capability (`FORWARD_SUBAGENT_TEXT_FLAG`, `FORWARD_SUBAGENT_TEXT_FLOOR`
  = 2.1.220, `claude_version_tuple`, `forward_subagent_text_supported`, and the keyword-only
  `forward_subagent_text` parameter on `build_claude_stream_argv`); emission stays behind the
  `system/init` version capture (launch without, re-launch with), with unproven/unparseable
  versions never receiving the flag. Updated Purpose/Logic/Conventions/Invariants, re-pointed
  drifted reference rows (discovery launch now L233-L242 in harness_control_claude.py,
  command-replay acceptance now L598-L648 in claude_stream_state.py, discovery tests now
  L260-L445), and added rows for the adapter's launch/re-launch consumption and the floor-gate
  regression tests. Verification metadata stays pinned — the L7 change is uncommitted, so no
  commit hash can attest it.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

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

# mcp/src/agents_remember/mcp/tools/base.py

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Owns the one shared response-finalization adapter, and **re-exports** the advertised MCP tool-name
tuple from its single definition in `models`.

## Code Commentary

The module is 24 lines. It declares `TRANSPORT`, an empty `RESERVED_TOOLS`, `__all__`, and
`_tool_payload` — and defines nothing else. `PUBLIC_TOOLS` is imported at L14 and declared as an
export by `__all__` at L19.

### Logic

**`PUBLIC_TOOLS` is no longer defined here (260831-LOCR-L32).** The exact ordered tuple now
lives at `mcp/src/agents_remember/models/tools/public_roster.py` — 62 names at L32, **63** since
260831-LOCR-L37 added `worktree_pause`, extent `L22-L86`; L14 imports it and L19's
`__all__` declares the re-export, because this is not an `__init__.py` (where ruff exempts the `X as
X` idiom) and a bare import would otherwise read as unused. The object is identical — same tuple,
same order, and 62 unique names at the time of the move — so
`agents_remember.mcp.tools.base.PUBLIC_TOOLS` still resolves the same object and every existing
consumer is unchanged. The later membership change (63 names) was made in the roster leaf and the
worktree registrar together.

The relocation is what made the roster readable from `models`: a `models → mcp` import is a
`layers.toml` violation (models = 2, mcp = 22; the `mcp` charter forbids any import from below), a
function-local import trips `ruff PLC0415` with suppressions forbidden in this repository, and
module-level imports in either direction are circular. `models/worktree.py` now reads the roster to
enforce the worktree surface's next-move vocabulary; the roster's own card records why.

Structural agent operations are
`dispatch_agent`, `retire_child`, `rename_child`, `rename_self`, `message_parent`, and
`message_child`; structural gate names remain `lifecycle_gate`, `gate_decide`, and `gate_list`.
Removed exact-id/leaf-address agent tools are absent. `_tool_payload`
cit:([`_tool_payload`], mcp/src/agents_remember/mcp/tools/base.py:22-24) passes every
application result through `application/tool_response.py::complete_tool_response`.

### Conventions

Live registration and the public response-model registry must match the advertised tuple exactly.
Order is part of the advertisement contract; set-only parity is insufficient. A change to the roster
is a change to `models/tools/public_roster.py`, never a second tuple here.

### Invariants And Boundaries

- **This module re-exports the roster; it does not own it.** Do not re-declare `PUBLIC_TOOLS` here,
  and do not add a derived copy — the single definition is what keeps `mcp.tools.base.PUBLIC_TOOLS`
  and the model-layer reader the same object.
- Public tool names cannot restore session/lifecycle/inbox/gate-id cognition.
- Structural operations use document+role vocabulary.
- Every public result passes the common response finalizer.
- Reserved tools are empty.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- The advertised tuple names the structural public surface, and is now defined in the `models` leaf. [1]
- The adapter re-exports the roster through `__all__` instead of declaring its own copy. [2]
- The live registration is compared to this tuple, in order, by the inventory suite. [3]
- The shared adapter finalizes one application result. [4]
- Registrars are the only published declaration family. [5]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260815-DAG-L3 Public Tool Census

`closeout_queue` is now part of `PUBLIC_TOOLS`, so registry parity, response conformance, and common
envelope/next-step behavior treat it as a real public MCP surface rather than an internal helper.

## 260821-CLIVE-L2 Current Contract

The current source seams include the module-level vocabulary. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

- The shared protocol vocabulary declares stdio transport. [6]
- The public tool-name tuple's one definition, moved out of this adapter by 260831-LOCR-L32. [7]
- The reserved-tool tuple is explicitly empty. [8]
- The protocol adapter delegates response completion to the application boundary. [9]

## 260821-CLIVE Public Tool Census

`closeout_door` joins the canonical public tool-name set used by response-envelope validation.
This is an additive public surface with its own strict response model; it is not an internal
compatibility name and does not change token/envelope finalization for existing tools.

## MCAR-L02 Public Tool Inventory

`PUBLIC_TOOLS` includes exactly one `curator_coherence` name. Status, preparation, publication, and
validation remain actions of that tool rather than four overlapping public tools.

## 260831-CCR-L15 Status-Wait Public Tool

The public tool census `PUBLIC_TOOLS` adds `worktree_status_wait`, so the
read-only lifecycle status-change wait is part of the public tool inventory enforced by the
conformance suite.

## 260831-LOCR-L29 Public-Inventory Repair — The Self-Referential Test

`PUBLIC_TOOLS` gained `worktree_record_landing` immediately after `worktree_integrate`, so the tuple
again named every tool the server advertises and held 61 entries at that leaf (62 since
260831-LOCR-L30 added the checkpoint landing route).

The gap was not cosmetic. `mcp/registration/closeout.py` registered the tool and FastMCP published
it, while this tuple and `models/tools/tool_registry.py` both omitted it — and
`finalize_tool_response` indexes that registry by tool name, so the advertised tool raised instead
of returning a payload. Nothing exercised the invariant this card states. `mcp/public_surface.py`
compares a live `list_tools()` result against this tuple, and `mcp/registration/__init__.py`
documents that FastMCP publishes in registration order, but the only test comparing them built its
list FROM `PUBLIC_TOOLS`: `server_info` reports `list(PUBLIC_TOOLS)` (`mcp/tools/core.py`), so the
comparison was self-referential and a registered-but-unlisted tool was invisible to a fully green
suite.

`PublicSurfaceInventoryTests` (`mcp/tests/test_tools.py`) closes the hole. It registers every entry
in `TOOL_REGISTRARS` against a probe `FastMCP` and asserts the live `list_tools()` names equal this
tuple in order, then asserts the advertised names have validating response models. Order is part of
the comparison because publication follows registration order, so a misplaced row is a reordering
bug rather than a missing one. Do not replace this with an assertion against `server_info`: that
payload is this tuple, and comparing a tuple to itself is the failure mode the repair removed.

## 260831-LOCR-L30 Checkpoint Landing Joins The Census

`PUBLIC_TOOLS` gained `worktree_checkpoint_landing` immediately after `worktree_integrate`, so the
tuple again names every tool the server advertises and holds **62** entries. The same change register
the name in `mcp/registration/closeout.py`, in `models/tools/tool_registry.py::TOOL_RESPONSE_MODELS`,
and in `models/worktree.py::WorktreeCheckpointLandingResponse`.

This is the three-registry rule the L29 repair established, exercised a second time by construction
rather than by repair: a public tool needs the advertised tuple, the by-name response-model registry,
**and** its envelope model, and missing any one of them leaves the tool published but unable to
answer. `mcp/tests/test_tools.py::PublicSurfaceInventoryTests` now drives a validating
`finalize_tool_response` call for the checkpoint name as well, because the set comparison alone
cannot tell the two landing tools apart — they sit next to each other in the registry and their
payloads differ only in the operation literal, so a swap would still pass a set check.

## 260831-LOCR-L32 The Roster Moves To `models` — This Card Is Now A Re-Export

`PUBLIC_TOOLS` left this module. The 62-name tuple's one definition is now
`mcp/src/agents_remember/models/tools/public_roster.py:22-85`, a zero-import `models` leaf; this
module imports it at L14 and declares the re-export through `__all__` at L19, so
`mcp.tools.base.PUBLIC_TOOLS` resolves the same object and every consumer, the `public_surface` pin,
and `PUBLIC_TOOL_RESPONSE_MODELS` are unchanged. This file shrank from 79 lines to **24**:
`TRANSPORT` moved L9 → L16, `RESERVED_TOOLS` L74 → L17, and `_tool_payload` L77-L79 → L22-L24.

**Why it moved — this is the point of the change, not a tidy-up.** The roster living in `mcp` is
precisely why the worktree next-move vocabulary could not be enforced at the model boundary.
`application/worktree_status.py::_project_terminal_contract_status` writes `nextAction` / `nextTool` /
`nextArgs` into the payload validated once against `WorktreeStatusResponse`, whose envelope declared
none of them under `extra="allow"`, so the values crossed the wire verbatim and unchecked. Enforcing
that vocabulary requires `models/worktree.py` to read `PUBLIC_TOOLS`, and from `mcp` that read is
unwritable: `models → mcp` is a `layers.toml` violation (models = 2, mcp = 22; the `mcp` charter
forbids any import from below), a function-local import trips `ruff PLC0415` and suppressions are
forbidden here, and module-level imports in either direction are circular. Moving the tuple to a
zero-import `models` leaf makes the check *expressible* instead of special-cased, and matches
`layers.toml`'s own doctrine that wire vocabulary is defined in `models` and imported by the decider.
The layering checker returned to its exact baseline of 16 violations, with no `models → mcp` edge and
no new cycle.

**The dated entries below describe the tuple at their own leaf.** They remain accurate history — the
names, counts and registry rules they record still hold — but the roster's *location* in each of them
is `mcp/tools/base.py`. Read them as history; read the roster's current home from
`models/tools/public_roster.py`. Where one of them says the `base.py` tuple "is the authority on the
advertised name set", that now means the re-exported object, which is the same object.

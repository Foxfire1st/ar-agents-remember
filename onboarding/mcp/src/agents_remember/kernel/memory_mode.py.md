# mcp/src/agents_remember/kernel/memory_mode.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/memory_mode.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T14:25+02:00 |
| lastVerifiedCommitHash | `b281bcd68261866be306cc80a48241921b6dd0d2` |
| lastVerifiedCommitDate | 2026-09-16T14:24:58+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l12`; code candidate landed as `b281bcd68261866be306cc80a48241921b6dd0d2` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

The single home of the supported memory-mode and memory-topology vocabulary, and of the one typed
refusal for the mode this product **removed**. `internal` memory is no longer produced, accepted,
typed, branched on or documented anywhere; `external` and `disabled` are the whole supported set. The
module also owns the legacy directory-name constants used *only* to detect and report an existing
repo-sidecar layout, and the documented route out of it.

## Code Commentary

### Logic

The module declares two literals because they are one fact seen from two altitudes. `Topology` says
where a repository's durable memory root lives and has the single member `external`;
`MemoryMode` says what a started worktree task does with that root and has `external` and `disabled`.
Both lost their `internal` member together, so both are declared together rather than re-declared per
consumer. `SUPPORTED_TOPOLOGIES` and `SUPPORTED_MEMORY_MODES` are derived from those literals with
`get_args`, so the tuple a refusal prints cannot drift from the type a caller is narrowed onto.

`REMOVED_MEMORY_MODES` is the explicit removal declaration: a tuple containing the one member the
product no longer supports. It is a positive statement of what was removed, not an absence, which is
what lets detection and refusal be by name.

The refusal path is deliberately one construction. `memory_mode_refusal_message` builds the one
operator-legible text; `memory_mode_refusal` wraps it in the typed error; `memory_mode_refusal_fields`
returns the same facts as a publishable mapping; and `refuse_removed_memory_mode` raises it. A surface
that returns a typed result instead of raising therefore publishes the *same* facts as a surface that
raises, and the removal cannot acquire two spellings. `MEMORY_MODE_REMEDIES` states the route out once
for every surface: re-point to an external memory root and set the contract's `memory_mode` to
`external`, or re-initialize with the `c-00-initialize-memory-repo` skill — with the explicit statement
that nothing is migrated automatically and no existing memory root, contract or settings file is
rewritten in place.

The two narrowing functions are the only place the vocabulary is narrowed. `require_supported_memory_mode`
and `require_supported_topology` each test the *removed* set first and refuse it by name through the
typed error, then test the supported set and raise a plain `ValueError` for anything else. That ordering
is the whole point: a caller that compared strings inline (`if value != "external"`) would answer the
removed token and a typo with the same message, which is how a removed mode quietly degrades into "just
invalid input". The distinction is asserted by its own case.

`legacy_internal_memory_root` and `legacy_internal_coordination_root` compose the legacy directory names
onto a code-repository root and return resolved paths. They exist so an existing repo-sidecar layout can
be **named at an exact path** in a report; nothing calls them to create, read or migrate such a root.

### Conventions

Both literals are declared here rather than beside their consumers, and both are exported by name rather
than as bare strings, so a consumer that needs the supported set imports it instead of retyping it. The
supported tuples are derived rather than hand-written for the same reason.

Module-level constants carry docstrings stating what each is for, including the two legacy directory
names, whose docstrings say plainly that they are kept *only* to detect and report the old layout. That
wording is load-bearing: it is what stops a later reader from treating them as residue and deleting the
detection along with the mode.

### Invariants And Boundaries

**`internal` is not a member of either literal.** It cannot be constructed by a typed caller, and no
branch in the product selects behaviour on it. Every surviving occurrence of the token in the
production tree is one of exactly three classes: this single declaration, a loud refusal call site that
carries the artifact, or a docstring stating that the mode is refused.

**Existing state is reported, never rewritten.** The module names and detects a removed layout; it
never migrates one. No code path here writes to a contract, a settings file or a memory root.

**Deliberate survivors, not residue.** `LEGACY_INTERNAL_MEMORY_DIRNAME` (`ar-memory`) and
`LEGACY_INTERNAL_COORDINATION_DIRNAME` (`ar-coordination`) are intentional and must not be "corrected"
away: they are the detection vocabulary for a layout that still exists on disk in the wild. They are
distinct from the `ar-memory-*` versioned schema identifiers (`ar-memory-ledger/v1`,
`ar-memory-candidate-pair/v1`, `ar-memory-census/v1`), which are wire contracts and unrelated to memory
mode, and from `INTERNAL_COMPAT_TOOL_NAMES` in `models/tools/tool_registry.py`, which is MCP
response-compatibility naming.

**`repo-sidecar` is a placement, not a topology.** The removed `internal` mode used a repo-sidecar
layout; `repo-sidecar` itself survives as a per-artifact storage placement
(`is_sidecar_storage`) and is not a memory mode.

**No onboarding prose in code.** The module docstring explains *why* the mode was removed and what the
refusal does — the developer's stated boundary forbids setup instructions in code, and none are here;
the setup route lives in this vocabulary's remedy text and in the instruction corpus.

## Docs References

No Domain Documentation entries are configured in this memory root. The behaviour above is a
repository-owned product decision, not an external library contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `Topology` has the single supported member `external`. | `Topology` | mcp/src/agents_remember/kernel/memory_mode.py:30-30 |
| `MemoryMode` has exactly `external` and `disabled`. | `MemoryMode` | mcp/src/agents_remember/kernel/memory_mode.py:35-35 |
| The supported tuples are derived from the literals, not hand-written. | `SUPPORTED_MEMORY_MODES` | mcp/src/agents_remember/kernel/memory_mode.py:33-38 |
| The removal is declared positively, not left as an absence. | `REMOVED_MEMORY_MODES` | mcp/src/agents_remember/kernel/memory_mode.py:40-40 |
| The old repo-sidecar directory names survive only to detect and report that layout. | `LEGACY_INTERNAL_MEMORY_DIRNAME` | mcp/src/agents_remember/kernel/memory_mode.py:43-47 |
| The documented route out is stated once for every refusal surface, with no automatic migration. | `MEMORY_MODE_REMEDIES` | mcp/src/agents_remember/kernel/memory_mode.py:49-56 |
| Legacy roots are computed as resolved paths so a report can name the exact artifact. | `legacy_internal_memory_root` | mcp/src/agents_remember/kernel/memory_mode.py:60-62 |
| One refusal text is shared by every surface, naming the value, the removal and the supported set. | `memory_mode_refusal_message` | mcp/src/agents_remember/kernel/memory_mode.py:78-86 |
| The same facts are constructible as a typed error and as a publishable mapping. | `memory_mode_refusal_fields` | mcp/src/agents_remember/kernel/memory_mode.py:100-107 |
| A removed member is refused by name, never substituted by a supported one. | `refuse_removed_memory_mode` | mcp/src/agents_remember/kernel/memory_mode.py:110-112 |
| A removed token is refused by name while an unknown token is an invalid-argument error. | `require_supported_memory_mode` | mcp/src/agents_remember/kernel/memory_mode.py:115-130 |
| The topology narrower applies the same removal-versus-typo distinction. | `require_supported_topology` | mcp/src/agents_remember/kernel/memory_mode.py:133-142 |
| The typed refusal carries a stable status plus requested, supported, artifact and remedies. | `MemoryModeUnsupportedError` | mcp/src/agents_remember/errors.py:566-614 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local vocabulary and refusal claims.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History


- 2026-09-16T14:25+02:00 — 260915-CAPS-L12 curator (closeout-gate follow-up): the two verification fields above, which this card's creation entry left un-advanced, were populated on the closeout gate's refusal — `external-memory closeout requires onboarding verification metadata before memory commit`. They follow the canonical file-level model (`file-level-onboarding-workflow.md` § Metadata Rules: "use the latest commit that touched the source file once the content has been verified") and now read hash `b281bcd68261866be306cc80a48241921b6dd0d2`, date `2026-09-16T14:24:58+02:00` — the `[260915-CAPS-L12]` code commit that actually contains this source file, matching the value closeout's own `refresh_onboarding_metadata_for_context` writes for every required card. An earlier revision of this entry named the pre-commit base `c1dbebf8`, which does not contain this file; that value was replaced rather than retained, and no earlier history entry was rewritten. The creation entry's sentence that no stamp was advanced is superseded here, added rather than edited because `Update History` is append-only. Closeout re-stamps both fields authoritatively at the real commit.
- 2026-09-16T14:05+02:00 — 260915-CAPS-L12 curator: **created the missing sidecar** for the module
  `CAPS-R12@v1` added. It is the single home of the post-removal vocabulary (`Topology` = `external`;
  `MemoryMode` = `external`/`disabled`), the removal declaration, the legacy-layout detection constants
  and the one typed refusal. Recorded that `internal` is not a member of either literal, that existing
  state is reported rather than rewritten, and that `LEGACY_INTERNAL_*` and `repo-sidecar` are
  deliberate survivors rather than residue. Verification metadata remains closeout-owned: the source is
  uncommitted, so no stamp was advanced and no commit hash was invented.

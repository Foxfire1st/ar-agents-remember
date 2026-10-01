# mcp/src/agents_remember/kernel/memory_mode.py

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

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. The behaviour above is a
repository-owned product decision, not an external library contract.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

- `Topology` has the single supported member `external`. [1]
- `MemoryMode` has exactly `external` and `disabled`. [2]
- The supported tuples are derived from the literals, not hand-written. [3]
- The removal is declared positively, not left as an absence. [4]
- The old repo-sidecar directory names survive only to detect and report that layout. [5]
- The documented route out is stated once for every refusal surface, with no automatic migration. [6]
- Legacy roots are computed as resolved paths so a report can name the exact artifact. [7]
- One refusal text is shared by every surface, naming the value, the removal and the supported set. [8]
- The same facts are constructible as a typed error and as a publishable mapping. [9]
- A removed member is refused by name, never substituted by a supported one. [10]
- A removed token is refused by name while an unknown token is an invalid-argument error. [11]
- The topology narrower applies the same removal-versus-typo distinction. [12]
- The typed refusal carries a stable status plus requested, supported, artifact and remedies. [13]

### Cross-Repo References

No cross-repository implementation evidence is required for these local vocabulary and refusal claims.

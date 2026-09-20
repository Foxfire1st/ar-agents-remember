# mcp/tests/test_tool_entry_point_sweep.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_tool_entry_point_sweep.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T19:52+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a`|
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l6-ar` uncommitted source (**1353 lines / 15 cases**, sha256 `c748a345b32b68ee…`, edited by `260918-TSIP-L6`); base `a1351504`. L5's own candidate (**1274 lines / 14 cases**, sha256 `4223c626…`) is recorded in the Update History below. |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Every registered public tool, driven through the production entry point, in one hermetic world.
This module is the durable form of `260918-TSIP-L5`'s happy-path trace: a real in-memory MCP
client session against a server built by `create_server`, so each answer is the answer a
consumer's call actually receives. The assertion is about vocabulary, not about counts — a tool
must answer in a validated payload, a typed refusal carrying a machine-readable identity, or one
of two **pinned** defect families, and a pin is the only place an exception is tolerated.

## Code Commentary

### Logic

**One world, built once, for all 67 tools.** `EntryPointWorld` (`:325-866`) lays out a scratch
coordination root under `/tmp` with a code repository, an external memory repository, an authored
master/leaf pair, and one real leaf enclosure opened through `worktree_start`; the lifecycle that
start opened is then ended, so the sweep's own `lifecycle_start` case begins from `none`. Its
`benign` argument table is asserted equal to `PUBLIC_TOOLS` in **both** directions — a new tool
cannot arrive unswept and a table entry for no tool fails — and the roster is also asserted equal
to the live server's own advertisement, so the sweep covers what is advertised rather than what
the module believes is advertised.

**The arms are the product's vocabulary, named.** `classify` (`:286-298`) is the one classifier
the sweep and its controls share, so a control proves the sweep rather than a second
implementation of it. Seven arms: `payload`, `refusal`, `bare-not-ok`, `unvalidatable`,
`boundary-validation`, `argument-validation`, `error`. A raise is split by **which model
refused**: `REFUSED_MODEL` (`:208`) extracts `1 validation error for <Model>` and `_raised_arm` (`:245-263`) compares that name with the tool's own registered model, so a `T7`-class break — a
tool's own response model refusing the payload its producer built — is diagnosed apart from the
caller's invalid arguments, which are the generated `<tool>Arguments` input model. Both arms are
asserted **empty by name**, so such a break is diagnosed instead of arriving as an anonymous
raiser.

**Two pins, one update rule.** `ENVELOPE_LOSING_RAISERS` (`:98`) **was** `T34`'s nine tools that raise where they should
refuse, so the caller loses `ok`/`status`/`nextAction`; every entry named an ordinary precondition
(an absent provider, an unrecorded default-branch authority), and `provider_status` and
`memory_baseline_status` meet the same conditions with a typed payload, which is why it was a
defect rather than a contract. **Superseded by `260918-TSIP-L6`, below: the nine are repaired and
this constant is now `frozenset()`** — emptied in the change that repaired them, which is this
module's own update rule. `STATE_DEPENDENT_RAISERS` (`:128-134`) is
the same defect on the lifecycle family's *state* precondition: five tools, each with the states
in which it loses the envelope, measured as a four-state matrix (`AMBIENT_STATES`, `:136`) over
`LIFECYCLE_STATE_POPULATION` (`:144-152`), which is **derived by rule from the roster** and
asserted equal to the written-out `EXPECTED_LIFECYCLE_STATE_POPULATION` (`:154-169`) — the rule
alone cannot be checked by a subset assertion, so weakening it takes a second visible edit.
`UNMARKED_NOT_OK` (`:189`) **was** the same shape for the third defect (`T64`): a validated
payload reporting `ok:false` while carrying neither a refusal identity (`REFUSAL_IDENTITY_KEYS`,
`:191`) nor a next action (`NAVIGATION_KEYS`, `:192`). One entry, `citation_migrate`, whose preview
answered `ok:false` where its sibling `citation_fix` answers `ok:true` for the equivalent shape.
**Superseded by `260918-TSIP-L6`, below: `citation_migrate` answers the envelope and this constant
is now `{}`.**

**The rule for all three pins: a repaired tool leaves the pin in the same change.** Delete that
one entry in the change that lands the repair — never delete a constant, never widen one to make
a new failure pass; a new raiser is a failure until it is pinned deliberately. Each pin is
asserted *equal* to what was observed, in both directions, and `refusal_marks` (`:229-244`) reads
a refusal's marks from the **payload**, never from the arm the classifier assigned, so a case
that asserts on marks cannot be satisfied by a classifier that labels everything a refusal.

**The positive control is a case, not a comment.** `ChokePointControlTests` (`:1182-1280`) drives
`finalize_tool_response` with a payload its model forbids and requires it to refuse *and*
requires the sweep's classifier to mark that payload unvalidatable: if the choke point stops
validating, this case goes red rather than the sweep quietly passing on payloads nothing checked.
It also executes both `T7`-class break shapes through the entry point, patching the handler where
the registrar looks it up — a producer key emitted *through* `_tool_payload` arrives as
`boundary-validation`, a raw dict returned *past* it arrives as `unvalidatable` — and drives a
real invalid argument (`citation_fix` without its `contract_path`) to its own arm.

### Conventions

`unittest.TestCase` throughout; no `pytest` marks and no `-m` override, so the cases are in the
default selection and their lane is **`unit-regression`**
(`mcp/tests/test-evidence-lanes.toml:154`). Four classes, 15 cases: coverage 1
(`EntryPointCoverageTests`, `:867-886`), the sweep 7 (`EntryPointProbeTests`, `:887-1181`), the
choke-point controls 5 (`ChokePointControlTests`, `:1182-1280`), the census controls 2
(`EntryPointCensusControlTests`, `:1281-1353`). Every number it needs is derived at run time —
the roster, the response-model registry and the live advertisement are all read, never written as
literals.

### Invariants And Boundaries

- **Hermeticity is a measured boundary, not a claim.** Per repository the case asserts `HEAD`,
  the Git status, and every file outside `.git` by digest. The memory repository may gain exactly
  `KNOWN_MEMORY_SCAFFOLD_ADDITIONS` (`:171`) — the two scaffold files the product's own
  `memory_init` repair writes — and every tracked status line must be identical. Across the
  coordination root: nothing removed, nothing added or rewritten outside
  `COORDINATION_WRITE_ZONES` (`:215-226`), which are measured rather than guessed (a full sweep of
  all 67 tools adds 18 files and rewrites 2, every one inside these zones, and removes none).
  `.git` is excluded deliberately: opening a linked worktree rewrites its administrative files,
  which is Git doing its job.
- **The census controls exercise the boundary where it is blind.** `EntryPointCensusControlTests`
  performs a write into the memory repository, a rewrite and a delete in the code repository, and
  — at the coordination root — an undeclared add, a rewrite and a delete outside every zone. The
  predicate the case asserts is the predicate the controls mutate.
- **The pins are a repair backlog, not a safety net.** While these raisers are pinned the sweep is
  green over them; the equality assertions are what make each repair's pin removal mandatory.
- **The matrix cannot collapse onto the pin.** The state case asserts the pin is a *strict* subset
  of the derived population, so the population cannot silently become the pin and stop measuring
  the three members that never raise.
- **Scope boundary.** The sweep invokes the tool surface; it does not certify the tools. A pinned
  raiser means the envelope is lost at the entry point, and the repair belongs to the tool's owner
  (`L6`), not to this module.

## Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned contract and assertion facts; no external library behaviour is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and
they make no acceptance claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| The world: one scratch coordination root, two repositories, one real leaf enclosure, then the opened lifecycle ended. | `EntryPointWorld` | mcp/tests/test_tool_entry_point_sweep.py:325-866 |
| The classifier both the sweep and the controls use, so a control proves the sweep. | `classify` | mcp/tests/test_tool_entry_point_sweep.py:286-298 |
| The refused model's identity, which separates a response-model break from the caller's invalid arguments. | `REFUSED_MODEL` | mcp/tests/test_tool_entry_point_sweep.py:208-208 |
| `T34`'s nine tools that lose the whole envelope, each with the ordinary precondition that loses it. **Now empty** — repaired by `260918-TSIP-L6`. | `ENVELOPE_LOSING_RAISERS` | mcp/tests/test_tool_entry_point_sweep.py:98-98 |
| The same defect on the lifecycle family's state precondition, five tools with their losing states. | `STATE_DEPENDENT_RAISERS` | mcp/tests/test_tool_entry_point_sweep.py:128-134 |
| The matrix's four ambient states. | `AMBIENT_STATES` | mcp/tests/test_tool_entry_point_sweep.py:136-136 |
| The population derived by rule from the roster, so the pin cannot be measured over itself. | `LIFECYCLE_STATE_POPULATION` | mcp/tests/test_tool_entry_point_sweep.py:144-146 |
| The population written out, so weakening the derivation rule is a second visible edit. | `EXPECTED_LIFECYCLE_STATE_POPULATION` | mcp/tests/test_tool_entry_point_sweep.py:154-165 |
| The two scaffold files the sweep's own world may gain, and nothing else. | `KNOWN_MEMORY_SCAFFOLD_ADDITIONS` | mcp/tests/test_tool_entry_point_sweep.py:171-171 |
| The third pin: an envelope reporting `ok:false` that a caller cannot act on. **Now empty** — `citation_migrate` answers the envelope, repaired by `260918-TSIP-L6`. | `UNMARKED_NOT_OK` | mcp/tests/test_tool_entry_point_sweep.py:189-189 |
| A refusal's own marks, read from the payload rather than from the arm. | `refusal_marks` | mcp/tests/test_tool_entry_point_sweep.py:229-244 |
| The coordination-root zones inside which the product may legitimately write. | `COORDINATION_WRITE_ZONES` | mcp/tests/test_tool_entry_point_sweep.py:215-226 |
| The swept population is derived and equals the live server's advertisement. | `EntryPointCoverageTests` | mcp/tests/test_tool_entry_point_sweep.py:934-951 |
| The sweep itself: one world, one run, and the equality assertions that bind every pin. | `EntryPointProbeTests` | mcp/tests/test_tool_entry_point_sweep.py:887-1181 |
| The executed positive control over the choke point, and both break shapes at the entry point. | `ChokePointControlTests` | mcp/tests/test_tool_entry_point_sweep.py:1182-1280 |
| The census controls: write, rewrite and delete in both repositories and outside every zone. | `EntryPointCensusControlTests` | mcp/tests/test_tool_entry_point_sweep.py:1281-1353 |
| The lane row that keeps this module in the default selection. | "mcp/tests/test_tool_entry_point_sweep.py" | mcp/tests/test-evidence-lanes.toml:188-188 |
| The advertised roster the swept population is derived from and asserted equal to. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-91 |
| The registry whose models classify a payload that does not validate. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:156-241 |
| The choke point a bypassing handler skips, and the validation this module's control executes. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| The validation the positive control drives directly. | `finalize_tool_response` | mcp/src/agents_remember/models/tools/tool_response.py:15-26 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No repository or external-system boundary is proved by this module. | N/A | N/A |

## 260918-TSIP-L6 Both Pins Emptied In The Change That Repaired Them

This module is L5's, and this leaf **edited it in the same change that repaired what it pinned**,
which is the update rule the card itself states. `ENVELOPE_LOSING_RAISERS` is now
`frozenset()` and `UNMARKED_NOT_OK` is now `{}`: `T34`'s nine tools answer the envelope at the
entry point (`memory_baseline_adopt`, `grepai_search`, `grepai_trace`, the six `cgc_*`), and
`citation_migrate`'s preview no longer answers `ok: false` where its sibling answers `ok: true`.
Both constants remain declared and asserted **equal** to what the sweep observed in both
directions, so a tool that starts raising again fails the case rather than silently re-entering a
pin nobody widened.

`T34_REPAIRED_TOOLS` (`:103-117`) is new here, beside the pin it belongs to, and is the **single
source of truth** for the repaired nine: `mcp/tests/test_tool_refusal_conformance.py` imports it
rather than keeping a second inline copy that could drift. A new case,
`test_the_t34_family_answers_with_a_named_refusal_instead_of_raising` (`:963-1008`, with its
`assert_named_refusal` helper at `:977-1008`), asserts the repair where it is observable — through
the real entry point — and this module grew **1274 → 1353 lines** in the change.
`STATE_DEPENDENT_RAISERS` is untouched: its five members cannot refuse without a contract change
(`T66`, deferred), so the pin stays and names itself as an open, measured defect.

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: `EntryPointCoverageTests` repointed to mcp/tests/test_tool_entry_point_sweep.py:934-951. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: "mcp/tests/test_tool_entry_point_sweep.py" repointed to mcp/tests/test-evidence-lanes.toml:188-188. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T19:52+02:00 — 260918-TSIP-L6 curator (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): **both pins emptied in the change that repaired them** — `ENVELOPE_LOSING_RAISERS` → `frozenset()`, `UNMARKED_NOT_OK` → `{}` — with `T34_REPAIRED_TOOLS` added as the single source of truth for the repaired nine and a new entry-point case asserting the repair. `STATE_DEPENDENT_RAISERS` untouched (`T66`, deferred). The module grew 1274 → 1353 lines; every citation range re-derived against the candidate. Closeout owns the real commit stamp.
- 2026-09-18T19:48+02:00 — 260918-TSIP-L5 curator (uncommitted change set on `ar/260918-tsip-l5-ar`, base `f05ba167`): **created**. The module is new in this leaf (**1274 lines / 14 cases**, sha256 `4223c626…`), and it is the durable form of this leaf's happy-path trace: every registered public tool driven through a real in-memory MCP client session against `create_server`, in one hermetic scratch world. Recorded the two pinned raiser constants and their update rule, the third pin (`T64`), the executed choke-point control and the two break shapes it drives, the measured hermeticity boundary (`KNOWN_MEMORY_SCAFFOLD_ADDITIONS`, `COORDINATION_WRITE_ZONES`) and its census controls. Its lane row was added by the same change set at `mcp/tests/test-evidence-lanes.toml:153` in `unit-regression`. Verification metadata is the recorded base commit; the candidate is uncommitted and the governed closeout stamps the real code commit.

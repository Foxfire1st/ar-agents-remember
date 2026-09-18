# mcp/tests/test_tool_entry_point_sweep.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_tool_entry_point_sweep.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T19:48+02:00 |
| lastVerifiedCommitHash | `a135150459f8499ba309faf0373cc3b4bf7ff852`|
| lastVerifiedCommitDate | 2026-09-18T19:58:12+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l5-ar` uncommitted source (new file, **1274 lines / 14 cases**, sha256 `4223c626d24500368f5927ad0572274a44a0443e55b3b62590ce5415c2e88049`); base `f05ba167cd6dfb56b48a775f3da5d45528c09c82` |
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

**One world, built once, for all 67 tools.** `EntryPointWorld` (`:306-845`) lays out a scratch
coordination root under `/tmp` with a code repository, an external memory repository, an authored
master/leaf pair, and one real leaf enclosure opened through `worktree_start`; the lifecycle that
start opened is then ended, so the sweep's own `lifecycle_start` case begins from `none`. Its
`benign` argument table is asserted equal to `PUBLIC_TOOLS` in **both** directions — a new tool
cannot arrive unswept and a table entry for no tool fails — and the roster is also asserted equal
to the live server's own advertisement, so the sweep covers what is advertised rather than what
the module believes is advertised.

**The arms are the product's vocabulary, named.** `classify` (`:267-277`) is the one classifier
the sweep and its controls share, so a control proves the sweep rather than a second
implementation of it. Seven arms: `payload`, `refusal`, `bare-not-ok`, `unvalidatable`,
`boundary-validation`, `argument-validation`, `error`. A raise is split by **which model
refused**: `REFUSED_MODEL` (`:189`) extracts `1 validation error for <Model>` and `_raised_arm`
(`:226-242`) compares that name with the tool's own registered model, so a `T7`-class break — a
tool's own response model refusing the payload its producer built — is diagnosed apart from the
caller's invalid arguments, which are the generated `<tool>Arguments` input model. Both arms are
asserted **empty by name**, so such a break is diagnosed instead of arriving as an anonymous
raiser.

**Two pins, one update rule.** `ENVELOPE_LOSING_RAISERS` (`:90-100`) is `T34`'s nine tools that
raise where they should refuse, so the caller loses `ok`/`status`/`nextAction`; every entry names
an ordinary precondition (an absent provider, an unrecorded default-branch authority), and
`provider_status` and `memory_baseline_status` meet the same conditions with a typed payload,
which is why this is a defect rather than a contract. `STATE_DEPENDENT_RAISERS` (`:113-119`) is
the same defect on the lifecycle family's *state* precondition: five tools, each with the states
in which it loses the envelope, measured as a four-state matrix (`AMBIENT_STATES`, `:121`) over
`LIFECYCLE_STATE_POPULATION` (`:129-131`), which is **derived by rule from the roster** and
asserted equal to the written-out `EXPECTED_LIFECYCLE_STATE_POPULATION` (`:139-150`) — the rule
alone cannot be checked by a subset assertion, so weakening it takes a second visible edit.
`UNMARKED_NOT_OK` (`:165-170`) is the same shape for the third defect (`T64`): a validated payload
reporting `ok:false` while carrying neither a refusal identity (`REFUSAL_IDENTITY_KEYS`, `:172`)
nor a next action (`NAVIGATION_KEYS`, `:173`). One entry, `citation_migrate`, whose preview
answers `ok:false` where its sibling `citation_fix` answers `ok:true` for the equivalent shape.

**The rule for all three pins: a repaired tool leaves the pin in the same change.** Delete that
one entry in the change that lands the repair — never delete a constant, never widen one to make
a new failure pass; a new raiser is a failure until it is pinned deliberately. Each pin is
asserted *equal* to what was observed, in both directions, and `refusal_marks` (`:210-223`) reads
a refusal's marks from the **payload**, never from the arm the classifier assigned, so a case
that asserts on marks cannot be satisfied by a classifier that labels everything a refusal.

**The positive control is a case, not a comment.** `ChokePointControlTests` (`:1103-1199`) drives
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
(`mcp/tests/test-evidence-lanes.toml:153`). Four classes, 14 cases: coverage 1
(`EntryPointCoverageTests`, `:848-865`), the sweep 6 (`EntryPointProbeTests`, `:868-1100`), the
choke-point controls 5 (`ChokePointControlTests`), the census controls 2
(`EntryPointCensusControlTests`, `:1202-1274`). Every number it needs is derived at run time —
the roster, the response-model registry and the live advertisement are all read, never written as
literals.

### Invariants And Boundaries

- **Hermeticity is a measured boundary, not a claim.** Per repository the case asserts `HEAD`,
  the Git status, and every file outside `.git` by digest. The memory repository may gain exactly
  `KNOWN_MEMORY_SCAFFOLD_ADDITIONS` (`:156`) — the two scaffold files the product's own
  `memory_init` repair writes — and every tracked status line must be identical. Across the
  coordination root: nothing removed, nothing added or rewritten outside
  `COORDINATION_WRITE_ZONES` (`:196-207`), which are measured rather than guessed (a full sweep of
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
| The world: one scratch coordination root, two repositories, one real leaf enclosure, then the opened lifecycle ended. | `EntryPointWorld` | mcp/tests/test_tool_entry_point_sweep.py:306-845 |
| The classifier both the sweep and the controls use, so a control proves the sweep. | `classify` | mcp/tests/test_tool_entry_point_sweep.py:267-277 |
| The refused model's identity, which separates a response-model break from the caller's invalid arguments. | `REFUSED_MODEL` | mcp/tests/test_tool_entry_point_sweep.py:189-189 |
| `T34`'s nine tools that lose the whole envelope, each with the ordinary precondition that loses it. | `ENVELOPE_LOSING_RAISERS` | mcp/tests/test_tool_entry_point_sweep.py:90-100 |
| The same defect on the lifecycle family's state precondition, five tools with their losing states. | `STATE_DEPENDENT_RAISERS` | mcp/tests/test_tool_entry_point_sweep.py:113-119 |
| The matrix's four ambient states. | `AMBIENT_STATES` | mcp/tests/test_tool_entry_point_sweep.py:121-121 |
| The population derived by rule from the roster, so the pin cannot be measured over itself. | `LIFECYCLE_STATE_POPULATION` | mcp/tests/test_tool_entry_point_sweep.py:129-131 |
| The population written out, so weakening the derivation rule is a second visible edit. | `EXPECTED_LIFECYCLE_STATE_POPULATION` | mcp/tests/test_tool_entry_point_sweep.py:139-150 |
| The two scaffold files the sweep's own world may gain, and nothing else. | `KNOWN_MEMORY_SCAFFOLD_ADDITIONS` | mcp/tests/test_tool_entry_point_sweep.py:156-156 |
| The third pin: an envelope reporting `ok:false` that a caller cannot act on. | `UNMARKED_NOT_OK` | mcp/tests/test_tool_entry_point_sweep.py:165-170 |
| A refusal's own marks, read from the payload rather than from the arm. | `refusal_marks` | mcp/tests/test_tool_entry_point_sweep.py:210-223 |
| The coordination-root zones inside which the product may legitimately write. | `COORDINATION_WRITE_ZONES` | mcp/tests/test_tool_entry_point_sweep.py:196-207 |
| The swept population is derived and equals the live server's advertisement. | `EntryPointCoverageTests` | mcp/tests/test_tool_entry_point_sweep.py:848-865 |
| The sweep itself: one world, one run, and the equality assertions that bind every pin. | `EntryPointProbeTests` | mcp/tests/test_tool_entry_point_sweep.py:868-1100 |
| The executed positive control over the choke point, and both break shapes at the entry point. | `ChokePointControlTests` | mcp/tests/test_tool_entry_point_sweep.py:1103-1199 |
| The census controls: write, rewrite and delete in both repositories and outside every zone. | `EntryPointCensusControlTests` | mcp/tests/test_tool_entry_point_sweep.py:1202-1274 |
| The lane row that keeps this module in the default selection. | "mcp/tests/test_tool_entry_point_sweep.py" | mcp/tests/test-evidence-lanes.toml:153-153 |
| The advertised roster the swept population is derived from and asserted equal to. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-91 |
| The registry whose models classify a payload that does not validate. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:156-241 |
| The choke point a bypassing handler skips, and the validation this module's control executes. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| The validation the positive control drives directly. | `finalize_tool_response` | mcp/src/agents_remember/models/tools/tool_response.py:15-26 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No repository or external-system boundary is proved by this module. | N/A | N/A |

## Update History
- 2026-09-18T19:48+02:00 — 260918-TSIP-L5 curator (uncommitted change set on `ar/260918-tsip-l5-ar`, base `f05ba167`): **created**. The module is new in this leaf (**1274 lines / 14 cases**, sha256 `4223c626…`), and it is the durable form of this leaf's happy-path trace: every registered public tool driven through a real in-memory MCP client session against `create_server`, in one hermetic scratch world. Recorded the two pinned raiser constants and their update rule, the third pin (`T64`), the executed choke-point control and the two break shapes it drives, the measured hermeticity boundary (`KNOWN_MEMORY_SCAFFOLD_ADDITIONS`, `COORDINATION_WRITE_ZONES`) and its census controls. Its lane row was added by the same change set at `mcp/tests/test-evidence-lanes.toml:153` in `unit-regression`. Verification metadata is the recorded base commit; the candidate is uncommitted and the governed closeout stamps the real code commit.

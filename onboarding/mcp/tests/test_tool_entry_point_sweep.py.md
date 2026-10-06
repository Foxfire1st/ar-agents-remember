# mcp/tests/test_tool_entry_point_sweep.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Every registered public tool, driven through the production entry point, in one hermetic world.
This module is the durable form of `260918-TSIP-L5`'s happy-path trace: a real in-memory MCP
client session against a server built by `create_server`, so each answer is the answer a
consumer's call actually receives. The assertion is about vocabulary, not about counts — a tool
must answer in a validated payload, a typed refusal carrying a machine-readable identity, or one
of two **pinned** defect families, and a pin is the only place an exception is tolerated.

## Current source account

The benign invocation census adds role_start and role_message. Because the scratch server was started by no role launch, both exercise caller-has-no-binding refusal before any read/start/send. These rows expand the advertised population without weakening pinned envelope/error assertions or proving bound-agent success.

## Code Commentary

### Logic

**One world, built once, for every advertised tool.** `EntryPointWorld` (`:325-866`) lays out a scratch
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
refused**: `REFUSED_MODEL` extracts `1 validation error for <Model>` and `_raised_arm` compares that name with the tool's own registered model, so a `T7`-class break — a
tool's own response model refusing the payload its producer built — is diagnosed apart from the
caller's invalid arguments, which are the generated `<tool>Arguments` input model. Both arms are
asserted **empty by name**, so such a break is diagnosed instead of arriving as an anonymous
raiser.

**Every sweep call is bounded, and the sweep's own deadline is not a product raiser.**
`EntryPointWorld._call` runs under three 60-second phase limits — session initialization, the tool
response and session cleanup — and a passed limit raises `_ToolCallTimeout` naming the tool and the
phase. `call` lets that exception through instead of counting it as a product raiser, so the sweep
stops at the first tool that does not answer rather than recording the hang as an envelope loss.
`ChokePointControlTests.test_a_tool_that_never_answers_fails_by_name_and_closes_its_handler` holds a
tool answer back, patches the response limit to three seconds, and requires the named failure, the
closed handler and a working next call. The world's cleanup is registered with `addClassCleanup`
before `build()` can fail, so a class setup that fails still closes the world. The fixture's own
`_git` calls (setup and the census) pass no timeout and are outside the bounded protocol
operations.

**Two pins, one update rule.** `ENVELOPE_LOSING_RAISERS` **was** `T34`'s nine tools that raise where they should
refuse, so the caller loses `ok`/`status`/`nextAction`; every entry named an ordinary precondition
(an absent provider, an unrecorded default-branch authority), and `provider_status` and
`memory_baseline_status` meet the same conditions with a typed payload, which is why it was a
defect rather than a contract. **Superseded by `260918-TSIP-L6`, below: the nine are repaired and
this constant is now `frozenset()`** — emptied in the change that repaired them, which is this
module's own update rule. `STATE_DEPENDENT_RAISERS` is
the same defect on the lifecycle family's *state* precondition: five tools, each with the states
in which it loses the envelope, measured as a four-state matrix (`AMBIENT_STATES`) over
`LIFECYCLE_STATE_POPULATION`, which is **derived by rule from the roster** and
asserted equal to the written-out `EXPECTED_LIFECYCLE_STATE_POPULATION` — the rule
alone cannot be checked by a subset assertion, so weakening it takes a second visible edit.
`UNMARKED_NOT_OK` **was** the same shape for the third defect (`T64`): a validated
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
default selection and their lane is **`unit-regression`**. Four classes: coverage (`EntryPointCoverageTests`), the
sweep (`EntryPointProbeTests`), the choke-point controls (`ChokePointControlTests`), the census
controls (`EntryPointCensusControlTests`). Every number it needs is derived at run time —
the roster, the response-model registry and the live advertisement are all read, never written as
literals.

### Invariants And Boundaries

- **Hermeticity is a measured boundary, not a claim.** Per repository the case asserts `HEAD`,
  the Git status, and every file outside `.git` by digest. The memory repository may gain exactly
  `KNOWN_MEMORY_SCAFFOLD_ADDITIONS` — the two scaffold files the product's own
  `memory_init` repair writes — and every tracked status line must be identical. Across the
  coordination root: nothing removed, nothing added or rewritten outside
  `COORDINATION_WRITE_ZONES` (`:215-226`), which are measured rather than guessed (the historical 67-tool measurement added 18 files and rewrote 2 inside these zones;
  current calls are measured against the same declared write boundary).
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

## Evidence

### Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned contract and assertion facts; no external library behaviour is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and
they make no acceptance claim.

- The world: one scratch coordination root, two repositories, one real leaf enclosure, then the opened lifecycle ended. [1]

- The classifier both the sweep and the controls use, so a control proves the sweep. [2]
- The refused model's identity, which separates a response-model break from the caller's invalid arguments. [3]
- `T34`'s nine tools that lose the whole envelope, each with the ordinary precondition that loses it. **Now empty** — repaired by `260918-TSIP-L6`. [4]
- The same defect on the lifecycle family's state precondition, five tools with their losing states. [5]
- The matrix's four ambient states. [6]
- The population derived by rule from the roster, so the pin cannot be measured over itself. [7]
- The population written out, so weakening the derivation rule is a second visible edit. [8]
- The two scaffold files the sweep's own world may gain, and nothing else. [9]
- The third pin: an envelope reporting `ok:false` that a caller cannot act on. **Now empty** — `citation_migrate` answers the envelope, repaired by `260918-TSIP-L6`. [10]
- A refusal's own marks, read from the payload rather than from the arm. [11]
- The coordination-root zones inside which the product may legitimately write. [12]
- The swept population is derived and equals the live server's advertisement. [13]
- The sweep itself: one world, one run, and the equality assertions that bind every pin. [14]

- The executed positive control over the choke point, and both break shapes at the entry point. [15]

- The census controls: write, rewrite and delete in both repositories and outside every zone. [16]
- The lane row that keeps this module in the default selection. [22]
- The advertised roster the swept population is derived from and asserted equal to. [18]
- The registry whose models classify a payload that does not validate. [19]
- The choke point a bypassing handler skips, and the validation this module's control executes. [20]
- The validation the positive control drives directly. [21]

- The three 60-second phase limits and the named timeout that the classifier does not count as a product raiser. [23]
- The control that holds an answer back and requires the named failure, the closed handler and a working next call. [24]

### Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

No repository or external-system boundary is proved by this module.

## 260918-TSIP-L6 Both Pins Emptied In The Change That Repaired Them

This module is L5's, and this leaf **edited it in the same change that repaired what it pinned**,
which is the update rule the card itself states. `ENVELOPE_LOSING_RAISERS` is now
`frozenset()` and `UNMARKED_NOT_OK` is now `{}`: `T34`'s nine tools answer the envelope at the
entry point (`memory_baseline_adopt`, `grepai_search`, `grepai_trace`, the six `cgc_*`), and
`citation_migrate`'s preview no longer answers `ok: false` where its sibling answers `ok: true`.
Both constants remain declared and asserted **equal** to what the sweep observed in both
directions, so a tool that starts raising again fails the case rather than silently re-entering a
pin nobody widened.

`T34_REPAIRED_TOOLS` is new here, beside the pin it belongs to, and is the **single
source of truth** for the repaired nine: `mcp/tests/test_tool_refusal_conformance.py` imports it
rather than keeping a second inline copy that could drift. A new case,
`test_the_t34_family_answers_with_a_named_refusal_instead_of_raising` (`:963-1008`, with its
`assert_named_refusal` helper at `:977-1008`), asserts the repair where it is observable — through
the real entry point — and this module grew **1274 → 1353 lines** in the change.
`STATE_DEPENDENT_RAISERS` is untouched: its five members cannot refuse without a contract change
(`T66`, deferred), so the pin stays and names itself as an open, measured defect.

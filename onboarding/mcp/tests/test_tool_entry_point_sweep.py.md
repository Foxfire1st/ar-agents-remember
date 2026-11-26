# mcp/tests/test_tool_entry_point_sweep.py

## Current operative account — MIK-R112

The self-contained world now builds without an ambient lifecycle. Its prepared_state/state_after strings are fixed fixture labels, not observations. The ambient matrix, arrange helper and STATE_DEPENDENT_RAISERS/AMBIENT_STATES/population declarations are removed. Retained roster equality, exact envelope pins, three-axis refusal marks, choke/census controls and read-only annotation/file oracles remain separate guarantees. No test invocation or historical census is renewed. The current main module imports its world, classifier and population pins from `tool_entry_point_sweep_support.py`; negative controls live in `test_tool_entry_point_sweep_controls.py` and read-only oracles in `test_tool_entry_point_read_only.py`. The support declares an empty `ENVELOPE_LOSING_RAISERS`, `T34_REPAIRED_TOOLS={memory_baseline_adopt}` and empty `UNMARKED_NOT_OK`. Current equality assertions remain in the main probe. Older inline line positions and explicitly superseded captions below retain their source epoch; they are not current owner locations.

The self-contained world seeds user settings through the protected-settings guard under pytest’s isolated XDG home; its code repository is a workspace sibling. The benign census includes `direct_execution_grant` and explicit canonical leaf identity for direct landing. The invalid-input control omits required `repo_id`. The census includes `role_start_set` and native `retire_child`; caller/no-target refusals do not prove a bound Manager set or successful retirement.

### MIK-R109 read-only annotation assertions

`test_tool_entry_point_read_only.ReadOnlyMarkTests` asserts every public roster name lies in exactly one of READ_ONLY_TOOLS or MUTATING_TOOLS and that advertised readOnlyHint matches the list. It invokes each marked-read default case plus declared refusal variants, comparing code/memory repository state and the coordination file census. The coordination-file comparison filters its logs prefix, nested log paths and the runtime/knowledge-index prefix. Other runtime files stay in the comparison. context_packet is marked false because include_freshness can fetch, and knowledge_diff is marked false because an omitted after revision can write Git objects.

The ordinary-file, Git-metadata and non-index-runtime controls write probe files directly and assert that the comparison oracle notices them; they do not inject a writing registered read handler. The requested context-packet fetch case asserts a false mark and FETCH_HEAD creation. These are source assertions, not executions performed here or a universal no-write theorem.

### Source and authority bounds

- Source comparison: `mcp/tests/test_tool_entry_point_sweep.py:135-303` (current population and probe tests).
- Source comparison: `mcp/tests/tool_entry_point_sweep_support.py` (the extracted world, classifier and pins) and `mcp/tests/test_tool_entry_point_sweep_controls.py` (negative controls).
- Source comparison: `mcp/tests/test_tool_entry_point_read_only.py:61-90` (the current read-only-mark class and list assertions).

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Current source contract evidence

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Runs the public tool-entry probes declared by the census, using the extracted world and pin owners.

Every registered public tool, driven through the production entry point, in one hermetic world.
This module is the durable form of `260918-TSIP-L5`'s happy-path trace: a real in-memory MCP
client session against a server built by `create_server`, so each answer is the answer a
consumer's call actually receives. The assertion is about vocabulary, not about counts — a tool
is classified as a payload, refusal, unmarked refusal or one of the error arms. The main probe keeps exact error and unmarked populations and forbids unvalidatable and boundary-validation results. A separate invalid-input control covers argument validation.

## Current source account

The benign invocation table includes role_start, role_message, role_start_set and retire_child in a server fixture with no launched role binding. The sweep classifies their delivered outcomes. Bound-role success requires a separate fixture.

## Code Commentary

### Current Contract

ENVELOPE_LOSING_RAISERS is empty on the current source; exact bidirectional equality still pins the declared population. The formerly carried four L111 raisers are historical, not today's backlog. The current sweep uses one benign invocation per public tool; `prepare` performs no arrangement and its two state fields are fixed to `none`. No sweep execution, broader acceptance or relaxed pin is implied by this current declaration.

EntryPointProbeTests drives the registered entry points through the shared world and declared input pins. After the sweep completes, each tool gets its own unvalidatable and boundary-validation subtests. The raiser, unmarked and census checks have separate global subtests. Pins are compared with observed populations in both directions. The classifier, census controls and phase-budget machinery are extracted owners. A probe records the tool’s route outcome; its existence proves neither every environment nor every unsupported consumer. Test definitions are not execution results.

The sweep imports its world, classifier and population pins from `tool_entry_point_sweep_support.py`. Negative controls live in `test_tool_entry_point_sweep_controls.py`; read-only oracles live in `test_tool_entry_point_read_only.py`.

### Logic

**One world, built once, for every advertised tool.** `EntryPointWorld` builds a temporary coordination root, code and memory repositories, an authored master/leaf pair and a real leaf enclosure. Its benign argument table must equal `PUBLIC_TOOLS` in both directions; the server advertisement must equal the same set.

**The arms are the product's vocabulary, named.** `classify` (`tool_entry_point_sweep_support.py:244-254`) is the one classifier
shared by this sweep and its extracted controls. Seven arms: `payload`, `refusal`, `bare-not-ok`, `unvalidatable`,
`boundary-validation`, `argument-validation`, `error`. A raise is split by **which model
refused**: `REFUSED_MODEL` extracts `1 validation error for <Model>` and `_raised_arm` compares that name with the tool's own registered model, so a `T7`-class break — a
tool's own response model refusing the payload its producer built — is diagnosed apart from the
caller's invalid arguments, which are the generated `<tool>Arguments` input model. The probe asserts `boundary-validation` and `unvalidatable` empty by name. The invalid-input control separately requires `argument-validation`; the benign sweep does not assert that arm empty.

The mounted support classifier validates a readable dictionary from the response log under the registered model. It uses the delivered dictionary when the log is absent, unreadable or yields a non-dictionary, and checks extra keys at the top level. PRF-D58CPV covers that fixture behavior. The ordinary sibling has its own readable-whole-result requirement and checks the delivered response recursively. PRF-KZVVQJ covers its missing and unreadable log controls.

**Every sweep call is bounded, and the sweep's own deadline is not a product raiser.**
`EntryPointWorld._call` runs under three 60-second phase limits — session initialization, the tool
response and session cleanup — and a passed limit raises `_ToolCallTimeout` naming the tool and the
phase. `call` lets that exception through instead of counting it as a product raiser. A timeout propagates out of the call and aborts the sweep; it is not recorded as an `unvalidatable` result.
`ChokePointControlTests.test_a_tool_that_never_answers_fails_by_name_and_closes_its_handler` holds a
tool answer back, patches the response limit to three seconds, and requires the named failure, the
closed handler and a working next call. The world's cleanup is registered with `addClassCleanup`
before `build()` can fail, so a class setup that fails still closes the world. The fixture's own
`_git` calls (setup and the census) pass no timeout and are outside the bounded protocol
operations.

**Pins and their update rule.** `ENVELOPE_LOSING_RAISERS` is empty, `UNMARKED_NOT_OK` is empty, and `T34_REPAIRED_TOOLS` contains `memory_baseline_adopt`. The main probe compares observed raisers and bare-not-ok answers with their corresponding pins by equality.

**The pins have distinct checks.** Observed `error` and `bare-not-ok` populations must equal `ENVELOPE_LOSING_RAISERS` and `UNMARKED_NOT_OK`; their messages require repairs or deliberate population changes to update the corresponding declaration in the same change. `T34_REPAIRED_TOOLS` selects previously repaired advertised tools: it must have no intersection with observed errors, and each selected tool must return the required refusal axes. `refusal_marks` (`tool_entry_point_sweep_support.py:160-173`) reads marks from the payload independently of the classifier arm.

**The positive control is a case, not a comment.** `ChokePointControlTests` (`test_tool_entry_point_sweep_controls.py:23-153`) drives
`finalize_tool_response` with a payload its model forbids and requires it to refuse *and*
requires the sweep's classifier to mark that payload unvalidatable: if the choke point stops
validating, this case goes red rather than the sweep quietly passing on payloads nothing checked.
It also executes both `T7`-class break shapes through the entry point, patching the handler where
the registrar looks it up — a producer key emitted *through* `_tool_payload` arrives as
`boundary-validation`, a raw dict returned *past* it arrives as `unvalidatable` — and drives a
real invalid argument (`citation_fix` without its required `repo_id`) to its own arm.

### Conventions

The cases use `unittest.TestCase` without `pytest` marks or an `-m` override.
The coverage case reads the literal public roster, the response-model registry and the live advertisement. It requires exact roster equality with both the invocation table and the advertisement, and requires a response model for every public tool.

### Invariants And Boundaries

- **Hermeticity is a measured boundary, not a claim.** Per repository the case asserts `HEAD`,
  the Git status, and every file outside `.git` by digest. The memory repository may gain exactly
  `KNOWN_MEMORY_SCAFFOLD_ADDITIONS` — the two scaffold files the product's own
  `memory_init` repair writes — and every tracked status line must be identical. Across the
  coordination root: nothing removed, nothing added or rewritten outside
  `COORDINATION_WRITE_ZONES` (`tool_entry_point_sweep_support.py:146-157`), which the case applies to its before and after census.
  `.git` is excluded deliberately: opening a linked worktree rewrites its administrative files,
  which is Git doing its job.
- **The census controls exercise the boundary where it is blind.** `EntryPointCensusControlTests`
  performs a write into the memory repository, a rewrite and a delete in the code repository, and
  — at the coordination root — an undeclared add, a rewrite and a delete outside every zone. The
  predicate the case asserts is the predicate the controls mutate.
- **The pins are a repair backlog, not a safety net.** While these raisers are pinned the sweep is
  green over them; the equality assertions are what make each repair's pin removal mandatory.

- **Scope boundary.** The sweep invokes the tool surface; it does not certify the tools. A pinned
  raiser means the envelope is lost at the entry point. Current source declares empty raiser and
  bare-not-ok pins.

Both ordinary and support worlds are exercised with RuntimeWarning messages that are nonempty or empty. The cases require the captured detail string, actual exception type and innermost traceback file:line. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Retained Source-Epoch Context

These attributed excerpts preserve earlier module history, rationale, deliberate omissions and evidence limits recorded in the memory base. Source coordinates, populations, outcomes and ownership describe their recorded epochs. They do not renew execution results or replace the current source account. This pass did not rerun the historical checks.

### Earlier fixture and ambient-state account

Summary based on the account in memory base `81cfe4a8`, 9–14:

> > **Retained historical source account — superseded by the current contract:**
> > - The self-contained world seeds user settings through the protected-settings guard under pytest’s isolated XDG home; its code repository is a workspace sibling, not a coordination-root child. The benign census includes `direct_execution_grant` and explicit canonical leaf identity for direct landing. The invalid-input control omits required `repo_id`, not the now-optional citation contract.
> > - EntryPointWorld, classifier/constants and control classes are now defined in this file, not only extracted owners.
> > - STATE_DEPENDENT_RAISERS is empty and the derived matrix population retains lifecycle_finalize_task only.
> > - UNMARKED_NOT_OK is empty; the surviving T34 advertised family is memory_baseline_adopt only.
> > - The benign invocation census includes role_start_set and native retire_child under the same roster-equality and envelope checks. Fixture caller/no-target refusals do not prove a bound Manager set or successful retirement.

### Earlier pin ownership

Summary based on the account in memory base `81cfe4a8`, 65–65:

> EntryPointProbeTests drives the registered entry points through the shared world and declared input pins. Every tool and every aspect is judged on its own subTest, so one tool's failure never keeps the aspects behind it unrun. The pins record the measured surface — the four lifecycle raisers owned by L111 and the bare `memory_quality_check` answer owned by L110 — with bidirectional exactness: a new raiser or a vanished pin fails. The classifier, census controls and phase-budget machinery are extracted owners, not declarations in this module. A probe records the tool's actual route outcome; its existence alone proves neither every environment nor every unsupported consumer. Removed local classifier helpers, pin constants and control class names must not be attributed to this file. Test definitions are not an execution result.

### Extraction lineage

Summary based on the account in memory base `81cfe4a8`, 67–67:

> The inline line positions in the following original account refer to the unsplit source. MIK-R26 moved the world/classifier/constants to `tool_entry_point_world.py` and the three control classes to `test_tool_entry_point_controls.py`; the sweep imports those owners. Definitions and historical run observations below are not a new execution result.

### Earlier lifecycle fixture arrangement

Summary based on the account in memory base `81cfe4a8`, 71–78:

> **One world, built once, for every advertised tool.** `EntryPointWorld` (`:325-866`) lays out a scratch
> coordination root under `/tmp` with a code repository, an external memory repository, an authored
> master/leaf pair, and one real leaf enclosure opened through `worktree_start`; the lifecycle that
> start opened is then ended, so the sweep's own `lifecycle_start` case begins from `none`. Its
> `benign` argument table is asserted equal to `PUBLIC_TOOLS` in **both** directions — a new tool
> cannot arrive unswept and a table entry for no tool fails — and the roster is also asserted equal
> to the live server's own advertisement, so the sweep covers what is advertised rather than what
> the module believes is advertised.

### L130 deadline-repair history

Summary based on the account in memory base `81cfe4a8`, 90–99:

> Before L130 the sweep stopped at the first tool that did not answer; since L130 it records one tool's deadline as that tool's unvalidatable finding and goes on (MIK-R130 rule 6), so every tool is judged.

### Pin rationale and repair lineage

Summary based on the account in memory base `81cfe4a8`, 101–119:

> **Two pins, one update rule.** `ENVELOPE_LOSING_RAISERS` **was** `T34`'s nine tools that raise where they should
> refuse, so the caller loses `ok`/`status`/`nextAction`; every entry named an ordinary precondition
> (an absent provider, an unrecorded default-branch authority), and `provider_status` and
> `memory_baseline_status` meet the same conditions with a typed payload, which is why it was a
> defect rather than a contract. **At the `260918-TSIP-L6` landing, below: the nine were repaired and
> this constant became `frozenset()`** — emptied in the change that repaired them. Since L130 the
> constant records the four lifecycle preconditions that raise (owner L111); T34's nine remain
> repaired, guarded by the pin test below. `STATE_DEPENDENT_RAISERS` is
> the same defect on the lifecycle family's *state* precondition: five tools, each with the states
> in which it loses the envelope, measured as a four-state matrix (`AMBIENT_STATES`) over
> `LIFECYCLE_STATE_POPULATION`, which is **derived by rule from the roster** and
> asserted equal to the written-out `EXPECTED_LIFECYCLE_STATE_POPULATION` — the rule
> alone cannot be checked by a subset assertion, so weakening it takes a second visible edit.
> `UNMARKED_NOT_OK` **was** the same shape for the third defect (`T64`): a validated
> payload reporting `ok:false` while carrying neither a refusal identity (`REFUSAL_IDENTITY_KEYS`,
> `:191`) nor a next action (`NAVIGATION_KEYS`, `:192`). One entry, `citation_migrate`, whose preview
> answered `ok:false` where its sibling `citation_fix` answers `ok:true` for the equivalent shape.
> **At the L6 landing: `citation_migrate` answered the envelope and this constant became `{}`.**
> Since L130 it records the bare `memory_quality_check` answer (owner L110).

### Earlier census and matrix boundary

Summary based on the account in memory base `81cfe4a8`, 147–168:

> - **Hermeticity is a measured boundary, not a claim.** Per repository the case asserts `HEAD`,
>   the Git status, and every file outside `.git` by digest. The memory repository may gain exactly
>   `KNOWN_MEMORY_SCAFFOLD_ADDITIONS` — the two scaffold files the product's own
>   `memory_init` repair writes — and every tracked status line must be identical. Across the
>   coordination root: nothing removed, nothing added or rewritten outside
>   `COORDINATION_WRITE_ZONES` (`:215-226`), which are measured rather than guessed (the historical 67-tool measurement added 18 files and rewrote 2 inside these zones;
>   current calls are measured against the same declared write boundary).
>   `.git` is excluded deliberately: opening a linked worktree rewrites its administrative files,
>   which is Git doing its job.
> - **The census controls exercise the boundary where it is blind.** `EntryPointCensusControlTests`
>   performs a write into the memory repository, a rewrite and a delete in the code repository, and
>   — at the coordination root — an undeclared add, a rewrite and a delete outside every zone. The
>   predicate the case asserts is the predicate the controls mutate.
> - **The pins are a repair backlog, not a safety net.** While these raisers are pinned the sweep is
>   green over them; the equality assertions are what make each repair's pin removal mandatory.
> - **The matrix cannot collapse onto the pin.** The state case asserts the pin is a *strict* subset
>   of the derived population, so the population cannot silently become the pin and stop measuring
>   the three members that never raise.
> - **Scope boundary.** The sweep invokes the tool surface; it does not certify the tools. A pinned
>   raiser means the envelope is lost at the entry point, and the repair belongs to the owning leaf —
>   `L111` for the four lifecycle raisers, `L110` for the bare `memory_quality_check` surface — not to
>   this module. The pins were first measured under `L6`; the owners above are current.

### Earlier raiser-pin citation custody

Summary based on the account in memory base `81cfe4a8`, 191–191:

> - `T34`'s surviving repaired tool stays repaired, and the envelope-losing raiser pin is empty because the four lifecycle preconditions were repaired. [Past-epoch source caption, detached from live reference 26. Recorded citation custody: mcp/tests/test_tool_entry_point_sweep.py blob 1fe4dc4416c2727815fcab3f9558e152bb422ee4 (available); historical event commit not identified. No historical event or intent inferred.]

### Earlier bare-answer-pin citation custody

Summary based on the account in memory base `81cfe4a8`, 207–207:

> - The bare-answer pin is empty since L110 repaired the `memory_quality_check` coherence refusal; T64's citation-preview repair remains. [Past-epoch source caption, detached from live reference 30. Recorded citation custody: mcp/tests/tool_entry_point_world.py blob fd07730a1a1bd23acfdd526b3ac57a628c498940 (available); historical event commit not identified. No historical event or intent inferred.]

### Earlier fixture citation custody

Summary based on the account in memory base `81cfe4a8`, 217–217:

> - The world: one scratch coordination root, two repositories, one real leaf enclosure, then the opened lifecycle ended. [Past-epoch source caption, detached from live reference 31. Recorded citation custody: mcp/tests/tool_entry_point_world.py blob fd07730a1a1bd23acfdd526b3ac57a628c498940 (available); historical event commit not identified. No historical event or intent inferred.]

### Earlier repaired-family citation custody

Summary based on the account in memory base `81cfe4a8`, 286–286:

> - The lifecycle pin is exact in both directions; T34's original nine must remain repaired. [Past-epoch source caption, detached from live reference 49. Recorded citation custody: mcp/tests/test_tool_entry_point_sweep.py blob 1fe4dc4416c2727815fcab3f9558e152bb422ee4 (available); historical event commit not identified. No historical event or intent inferred.]

### Earlier L111 citation custody

Summary based on the account in memory base `81cfe4a8`, 295–295:

> - The four lifecycle raisers are pinned empty after L111 repaired them, and the equality is still asserted in both directions. [Past-epoch source caption, detached from live reference 50. Recorded citation custody: mcp/tests/test_tool_entry_point_sweep.py blob 1fe4dc4416c2727815fcab3f9558e152bb422ee4 (available); historical event commit not identified. No historical event or intent inferred.]

### L6 same-change repair account

Summary based on the account in memory base `81cfe4a8`, 314–321:

> This module is L5's, and this leaf **edited it in the same change that repaired what it pinned**,
> which is the update rule the card itself states. `ENVELOPE_LOSING_RAISERS` is now
> `frozenset()` and `UNMARKED_NOT_OK` is now `{}`: `T34`'s nine tools answer the envelope at the
> entry point (`memory_baseline_adopt`, `grepai_search`, `grepai_trace`, the six `cgc_*`), and
> `citation_migrate`'s preview no longer answers `ok: false` where its sibling answers `ok: true`.
> Both constants remain declared and asserted **equal** to what the sweep observed in both
> directions, so a tool that starts raising again fails the case rather than silently re-entering a
> pin nobody widened.

### Repaired-family ownership and deferred state contract

Summary based on the account in memory base `81cfe4a8`, 323–330:

> `T34_REPAIRED_TOOLS` is new here, beside the pin it belongs to, and is the **single
> source of truth** for the repaired nine: `mcp/tests/test_tool_refusal_conformance.py` imports it
> rather than keeping a second inline copy that could drift. A new case,
> `test_the_t34_family_answers_with_a_named_refusal_instead_of_raising` (`:963-1008`, with its
> `assert_named_refusal` helper at `:977-1008`), asserts the repair where it is observable — through
> the real entry point — and this module grew **1274 → 1353 lines** in the change.
> `STATE_DEPENDENT_RAISERS` is untouched: its five members cannot refuse without a contract change
> (`T66`, deferred), so the pin stays and names itself as an open, measured defect.

### L130 source-epoch pins

Summary based on the account in memory base `81cfe4a8`, 332–332:

> Current pins (L130): `ENVELOPE_LOSING_RAISERS` holds `worktree_checkpoint_landing`, `worktree_cleanup`, `worktree_integrate` and `worktree_record_landing` (owner L111, repaired under MIK-R111 rule 7); `UNMARKED_NOT_OK` holds `memory_quality_check` (owner L110, repaired under MIK-R110 rule 4). A repair removes its entry in the same change; each pin stays asserted equal to what the sweep observes, in both directions.

### Prior lane-anchor retirement

Summary based on the account in memory base `81cfe4a8`, 360–360:

> Retired at the fifth freeze d59c3493: mcp/tests/test-evidence-lanes.toml:364-365 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 3104b78bb309a8e1a912503557adb08599b52ef0. Retired means the anchor no longer stands, not that the cited subject was deleted [Past-epoch source caption, detached from live reference 40. Recorded citation custody: mcp/tests/test-evidence-lanes.toml blob 9a4619c222e8fb25a05e0f7b7254ff2f9ce3d51c (available); mcp/tests/test_tool_entry_point_sweep.py blob 1fe4dc4416c2727815fcab3f9558e152bb422ee4 (available); recorded commits code d59c3493ec682c2ab58fd9d1ed127d08038e90c4, code 3104b78bb309a8e1a912503557adb08599b52ef0. No historical event or intent inferred.]

Current-source qualifications for the retained account: `EntryPointWorld.call` propagates `_ToolCallTimeout` and the current `sweep` does not catch it, so a timeout aborts that sweep. The probe separately asserts `unvalidatable` and `boundary-validation` empty; it does not assert the benign `argument-validation` population empty. Error and bare-not-ok pins use equality, while the selected repaired T34 population is checked for no error intersection and complete refusal axes. The current support performs no ambient-state arrangement and stores `none` in its two state fields. Earlier quoted descriptions of different machinery are retained as recorded accounts, not current implementation claims.

## Retained Full-Card Audit Context

These distinct accounts are retained from memory base `81cfe4a8`. Dates, source coordinates, counts, outcomes and ownership describe their recorded epochs; this pass adds no execution, mutation result or acceptance. Historical reference labels are custody text and do not select live anchors.

### Earlier positive-control caption

Summary of the earlier card account:

> - The executed positive control over the choke point, and both break shapes at the entry point. (earlier reference label 38; custody only)

The duplicate [51] caption in the earlier card states the same predicate as [38]. “Executed” belongs to that earlier caption; current refs describe source-defined controls and this audit adds no execution receipt.

### Earlier final-bytes subTest caption

Summary of the earlier card account:

> - Every tool and every aspect is judged on its own subTest on the final bytes. (earlier reference label 48; custody only)

Current source separates per-tool unvalidatable/boundary-validation subTests from global raiser, unmarked and census subTests. The earlier every-aspect/final-bytes caption is retained as the prior wording, not renewed as an exact claim about this current loop or a fresh run.

## Evidence
### Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned contract and assertion facts; no external library behaviour is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and
they make no acceptance claim.

- `EntryPointProbeTests` owns the current boundary described above.

Anchor: `ENVELOPE_LOSING_RAISERS`

Current source: The current support source declares ENVELOPE_LOSING_RAISERS as an empty frozenset and T34_REPAIRED_TOOLS as the one-member memory_baseline_adopt set. The sweep source asserts equality with observed error-arm tools in both directions and a named refusal for that surviving T34 member. These are source declarations/assertions, not a fresh run or current four-tool backlog.

- The sweep itself: one world, one run, and the equality assertions that bind every pin.

- The support classifier derives refusal marks from nonempty strings in the delivered payload. [29]

Anchor: `UNMARKED_NOT_OK`

Current source: The support world used by the main sweep declares UNMARKED_NOT_OK as an empty dictionary. The main probe compares that pin with the observed bare-not-ok population by equality. This is a source assertion, not a new sweep result; the L110/T64 repair account remains historical source commentary.

Anchor: `EntryPointWorld`

Current source: The ordinary EntryPointWorld source constructs one temporary coordination root, code and memory repositories and a real leaf enclosure through the public tools. Its close method cleans the temporary world; the retained opened-lifecycle/ended caption is historical and does not describe a current lifecycle API call.

- The support classifier extracts the model name from validation detail and compares it with the registered response model. [32]

- The ordinary sibling classifier also compares the validation error model name with the tool’s registered response model. [52]

- The extracted invalid-argument control calls citation_fix without repo_id and requires the citation_fixArguments arm. [53]

- The main probe requires exactly the two declared scaffold additions in the memory census and untracked status. [35]

- The main coverage case compares this sweep’s invocation table and live server advertisement with the public roster. [37]

- The extracted controls check one memory-file add, code-file rewrite and delete, and three changes outside the coordination write zones. [39]

- The advertised roster the swept population is derived from and asserted equal to. [41]

- The ordinary sibling coverage case checks its own invocation table and live advertisement against PUBLIC_TOOLS. [54]


- The registry whose models classify a payload that does not validate. [42]


- The extracted bypass control returns a raw dictionary past `_tool_payload` and checks that the support classifier sees an unvalidatable result. [43]

- The extracted control calls the response validator with an undeclared key and checks the support classifier’s unvalidatable arm. [44]

- The three 60-second phase limits and the named timeout that the classifier does not count as a product raiser.

- The extracted control patches a server handler to withhold its answer and requires a named three-second timeout, handler closure and a successful next call. [46]

Anchor: `test_the_pinned_raisers_are_exactly_the_ones_that_lose_the_envelope`

Current source: The current sweep asserts exact equality between observed error-arm tools and ENVELOPE_LOSING_RAISERS in both directions, then asserts none of the current T34_REPAIRED_TOOLS population raises. That population now contains only memory_baseline_adopt; the original nine-tool caption is historical. No source assertion is an executed result.

Anchor: `ENVELOPE_LOSING_RAISERS`

Current source: The current support source declares ENVELOPE_LOSING_RAISERS as an empty frozenset and T34_REPAIRED_TOOLS as the one-member memory_baseline_adopt set. The sweep source asserts equality with observed error-arm tools in both directions and a named refusal for that surviving T34 member. These are source declarations/assertions, not a fresh run or current four-tool backlog.

### Cross-Repo References

No cross-repository implementation evidence is required for these local contract claims.

No repository or external-system boundary is proved by this module.

### Repo-Internal References (continued)

- The self-contained world obtains its protected-settings write path and uses a workspace-sibling code repository. [55]

- The benign support table names the canonical leaf reference for direct landing and the isolated grant input. [56]

- ENVELOPE_LOSING_RAISERS is empty on the current source, and exact bidirectional equality still pins it; the four L111 raisers it once carried are historical, not today's backlog. No sweep execution, broader acceptance or relaxed pin is implied by this declaration.

## Current source evidence

- Envelope loss is pinned empty; the positive T34 population retains only memory_baseline_adopt.

- The main probe retains exact equality between observed raisers and the current pin.



- The current support source declares ENVELOPE_LOSING_RAISERS as an empty frozenset and T34_REPAIRED_TOOLS as the one-member memory_baseline_adopt set. The sweep source asserts equality with observed error-arm tools in both directions and a named refusal for that surviving T34 member. These are source declarations/assertions, not a fresh run or current four-tool backlog. [26]




- The support world declares an empty unmarked-refusal map. The main test compares it with both the classified and directly counted populations. [30]



- The ordinary EntryPointWorld source constructs one temporary coordination root, code and memory repositories and a real leaf enclosure through the public tools. Its close method cleans the temporary world; the retained opened-lifecycle/ended caption is historical and does not describe a current lifecycle API call. [31]



- The support call uses 60-second limits for session initialization, tool response and session cleanup. A named timeout leaves call without entering the product outcome classifier. [45]

- `EntryPointProbeTests` owns the current boundary described above. Anchor: `EntryPointProbeTests` [47]



- The current sweep asserts exact equality between observed error-arm tools and ENVELOPE_LOSING_RAISERS in both directions, then asserts none of the current T34_REPAIRED_TOOLS population raises. That population now contains only memory_baseline_adopt; the original nine-tool caption is historical. No source assertion is an executed result. [49]





- The current support source declares ENVELOPE_LOSING_RAISERS as an empty frozenset and T34_REPAIRED_TOOLS as the one-member memory_baseline_adopt set. The sweep source asserts equality with observed error-arm tools in both directions and a named refusal for that surviving T34 member. These are source declarations/assertions, not a fresh run or current four-tool backlog. [50]





- ENVELOPE_LOSING_RAISERS is empty on the current source, and exact bidirectional equality still pins it; the four L111 raisers it once carried are historical, not today's backlog. No sweep execution, broader acceptance or relaxed pin is implied by this declaration. [57]





- Envelope loss is pinned empty; the positive T34 population retains only memory_baseline_adopt. [58]





- The main probe retains exact equality between observed raisers and the current pin. [59]




- Both ordinary and support worlds are exercised with RuntimeWarning messages that are nonempty or empty. The cases require the captured detail string, actual exception type and innermost traceback file:line. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [60]

- The source-defined positive control over the choke point and both break shapes at the entry point. [38]

- The source-defined positive control over the choke point and both break shapes at the entry point. [51]

- The probe asserts observed error and bare-not-ok populations equal their declarations, checks no selected repaired T34 tool raises, and requires complete refusal axes for each selected tool. Anchor: `EntryPointProbeTests` [28]

- Completed sweep results receive per-tool subTests for unvalidatable and boundary-validation arms, followed by separate global raiser, unmarked and census subTests. [48]

- The `unit-regression` lane selects `mcp/tests/test_tool_entry_point_sweep.py` in the default test population. [40]

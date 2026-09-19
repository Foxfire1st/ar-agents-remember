# mcp/tests/test_tool_refusal_conformance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_tool_refusal_conformance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T19:50+02:00 |
| lastVerifiedCommitHash | `a30509587c0456038d616b0ccd1a69ef969eff93`|
| lastVerifiedCommitDate | 2026-09-20T01:12:38+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l6-ar` uncommitted source (new file, **349 lines / 7 cases**, sha256 `a7980fae537b799a…`); base `a1351504` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Every public tool's **failure** path, driven through its production entry point. L5's
`test_tool_entry_point_sweep.py` sweeps the same surface with a *benign* argument set and can
therefore only see half of it; this module drives the other half — the one where a seat actually
needs the envelope — and asks, for each advertised tool, whether the answer is a **typed
refusal**, a recorded always-answer, or a recorded bare raiser.

It is the durable form of `260918-TSIP-L6`'s delivery-shape rule. The census it asserts is the
one the leaf measured on the live adapter: **67 tools = 32 refusals + 18 pinned bare raisers +
17 always-answer**. The nine tools `T34` recorded (`memory_baseline_adopt`, `grepai_search`,
`grepai_trace`, the six `cgc_*`) are no longer bare raisers, and the case that says so reads the
repair where it is observable — at the entry point, through the real MCP adapter.

## Code Commentary

### Logic

**Three shapes, each named, and the partition is asserted.** A *typed refusal* is `ok: false`
with three independently asserted axes — a refusal identity (`REFUSAL_IDENTITY_KEYS`, `:45`), a
non-empty reason (`REASON_KEYS`, `:49`), and machine-readable navigation
(`NAVIGATION_KEYS`, `:50`). The two remaining shapes are pins: `ALWAYS_ANSWERS` (`:64-122`), the
seventeen invocations that legitimately answer `ok: true` here, each with its reason written
beside it; and `BARE_RAISERS` (`:153-174`), the eighteen tools that still lose the whole envelope
to an exception. Both are asserted **equal** to what the census observed, in both directions, so
a new raiser fails, a stale entry fails, and neither can be made to pass by widening a constant.
`test_every_failure_path_answers_in_one_of_the_three_named_shapes` (`:215-234`) asserts the three
sets partition the population — there is no fourth shape.

**The population is derived at run time, never written as a count.**
`test_the_censused_population_is_the_advertised_one` (`:204-214`) asserts the live server's
`list_tools` equals `PUBLIC_TOOLS` and that the census drove exactly that set. The census's own
table lives in `tool_refusal_census_support.py::failure_invocations`, and `drive_census` refuses
a table that is not the roster before it drives anything.

**The three axes are asserted separately, by name.**
`test_every_refusal_names_what_refused_why_and_the_next_action` (`:235-255`) collects the tools
missing each axis and reports them by axis, so a refusal that stops naming *why* fails on that
axis rather than as a generic "refusal shape changed". `refusal_axes` (`:177-190`) reads the axes
from the payload itself; `ok` is deliberately not one of the three, because a payload that is not
a refusal at all should fail as *answered*, not as *refused without a reason*.

**The positive control for the repair, and the control for the predicate.** The `T34` case
(`:256-282`) takes the repaired nine from `test_tool_entry_point_sweep.py::T34_REPAIRED_TOOLS` —
**one source of truth**, so a second inline copy cannot drift from the pin it belongs to — and
requires each to answer `RETURNED` with all three axes complete; it cannot pass by removing the
tools from the roster, because the roster equality in the first case fails first.
`FailurePathControlTests` (`:283-324`) takes a real refusal and strips its identity, its reason
and its navigation one axis at a time, requiring the predicate to reject each — the case proves
the predicate can see a refusal that stopped naming something rather than describing one.

### Conventions

Plain pytest classes, no `unittest`, no `-m` override: the module is in the default selection and
its lane is **`unit-regression`** (`mcp/tests/test-evidence-lanes.toml:155`). Seven cases: the
census class 4 (`FailurePathCensusTests`, `:191-282`), the controls 2
(`FailurePathControlTests`), and one module-level hermeticity case (`:325-349`). The world is
built once per class (`setup_class`, `:195-200`) and closed in `teardown_class` (`:201-203`).

### Invariants And Boundaries

- **Hermeticity is asserted as a property of the fixture, not promised in prose.**
  `test_the_module_runs_in_seconds_and_touches_no_real_state` (`:325-349`) reads the fixture's own
  settings file and requires every repository path and memory root to sit inside the disposable
  root, the coordination root to be the fixture's, and `providers` to be empty — a configured
  provider would make the census live.
- **The pins are the same repair backlog as L5's.** The rule is identical and is stated in the
  module: **repaired ⇒ remove that entry in the same change; never delete the constant, never
  widen it.** `T34` is the worked example — its nine left `ENVELOPE_LOSING_RAISERS` in the sweep
  and are asserted here as refusals.
- **What the census does not claim.** A refusal that answers in the envelope is not a claim that
  the tool did the right thing: the census is about delivery shape. The eighteen remaining bare
  raisers are grouped in the source by the mechanism that raises (`require_repo`, the worktree
  contract address, the lifecycle state precondition, and four single tools), each already on the
  master register with its owner.
- **Two of the eighteen are blocked on a product decision, not on effort.** `lifecycle_start` and
  `lifecycle_resume` are also pinned by the sweep's `STATE_DEPENDENT_RAISERS`; their repair needs
  a refusal shape the strict `LifecycleResponse` family does not have (`T66`, deferred).

## Docs References

No external Domain Documentation source is configured in this memory root. These are
repository-owned delivery-shape facts; no external library behaviour is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The anchors below identify current behaviour of this module; they are not execution evidence and
they make no acceptance claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| The three axes of a typed refusal, read from the payload itself. | `refusal_axes` | mcp/tests/test_tool_refusal_conformance.py:177-190 |
| The seventeen invocations that legitimately answer `ok: true`, each with its reason. | `ALWAYS_ANSWERS` | mcp/tests/test_tool_refusal_conformance.py:64-122 |
| The eighteen tools that still lose the envelope, grouped in the source by the mechanism that raises. | `BARE_RAISERS` | mcp/tests/test_tool_refusal_conformance.py:153-174 |
| The census: one world, one run, and the assertions that bind both pins in both directions. | `FailurePathCensusTests` | mcp/tests/test_tool_refusal_conformance.py:191-282 |
| The population is derived from the live advertisement and the roster, never a literal count. | `test_the_censused_population_is_the_advertised_one` | mcp/tests/test_tool_refusal_conformance.py:204-214 |
| The three shapes partition the population: there is no fourth answer. | `test_every_failure_path_answers_in_one_of_the_three_named_shapes` | mcp/tests/test_tool_refusal_conformance.py:215-234 |
| Each refusal axis asserted by name, so a regression says which one it broke. | `test_every_refusal_names_what_refused_why_and_the_next_action` | mcp/tests/test_tool_refusal_conformance.py:235-255 |
| `T34`'s nine answer in the envelope at the entry point, read from the sweep's single source of truth. | `test_the_t34_family_is_no_longer_a_bare_raiser` | mcp/tests/test_tool_refusal_conformance.py:256-282 |
| The executed control: each axis stripped from a real refusal, and the predicate required to reject it. | `FailurePathControlTests` | mcp/tests/test_tool_refusal_conformance.py:283-324 |
| The hermeticity statement the module is held to: every fixture root inside the disposable world, no provider configured. | `test_the_module_runs_in_seconds_and_touches_no_real_state` | mcp/tests/test_tool_refusal_conformance.py:325-349 |
| The measured population and the production invocation per tool, kept in a support module so a probe can drive the same census. | `failure_invocations` | mcp/tests/tool_refusal_census_support.py:54-228 |
| The driver that refuses a table which is not the roster before it drives anything. | `drive_census` | mcp/tests/tool_refusal_census_support.py:229-253 |
| The nine tools `T34` repaired, owned by the sweep module beside the pin they left. | `T34_REPAIRED_TOOLS` | mcp/tests/test_tool_entry_point_sweep.py:103-117 |
| The sweep whose benign half this module completes, and the world both share. | `EntryPointWorld` | mcp/tests/test_tool_entry_point_sweep.py:325-866 |
| The advertised roster the population is derived from and asserted equal to. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-91 |
| The lane row that keeps this module in the default selection. | "mcp/tests/test_tool_refusal_conformance.py" | mcp/tests/test-evidence-lanes.toml:188-188 |

## Cross-Repo References

Each invocation goes through the real MCP adapter against a server built by `create_server` over
the fixture's own disposable coordination root. No production cross-repository authority is
claimed by this census.

| Finding | Anchor | Source |
| --- | --- | --- |
| No repository or external-system boundary is proved by this module. | N/A | N/A |

## Update History

- 2026-09-19T19:50+02:00 — 260918-TSIP-L6 curator (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): **created**. The module is new in this leaf (**349 lines / 7 cases**, sha256 `a7980fae537b799a…`) and is the durable form of the leaf's delivery-shape rule: every advertised tool driven down a path that cannot succeed, through the production entry point, and required to answer as a typed refusal, a recorded always-answer, or a recorded bare raiser. Recorded the measured census (**67 = 32 + 18 + 17**), the three refusal axes, both pins with their update rule, the executed axis-stripping control, the `T34` repair read at the entry point from the sweep's single source of truth, and the hermeticity property the module asserts of its own fixture. Its lane row was added by the same change set at `mcp/tests/test-evidence-lanes.toml:155` in `unit-regression`. Verification metadata is the recorded base commit; the candidate is uncommitted and the governed closeout stamps the real code commit.

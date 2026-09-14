# mcp/tests/test_memory_attribution_producers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_attribution_producers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Makes the memory-content producer surface **total** rather than mostly converted, and holds the census
that says so. A memory commit with no `Code-Commit:` trailer contributes no ledger row, and a projected
ledger cannot tell that apart from a producer that kept the old shape — the pairing is simply gone. So
the two things this module owns are the census of producers and the one renderer they all reach, plus the
two producers outside the closeout routes driven end to end through their real public tools.

The module was created by 260913-LCA-L4, whose corrected census is the master's 2026-09-13T23:50
decision.

## The Corrected Census: 5 Producers, 0 Untrailered

Measured at base `5bb124d4` from source, by grepping each producer's commit site and renderer call. The
master's 2026-09-13T22:05 census was wrong in two places, and this module's docstring carries the
correction:

| Producer | Commit site | How it reaches the renderer | Code commit it names |
| --- | --- | --- | --- |
| `worktrees/modules/closeout_external.py` | `:165` | `effective_input.memory_content_message(code_commit)` (`:167`) | the accepted code commit of the same closeout |
| `worktrees/integration/direct_landing/direct_landing_execution.py` | `:270` | `direct_landing_input(...).effectiveInput.memory_content_message(code_commit)` (`:272`) | `operation_input.codeCommit` |
| `worktrees/integration/closeout/preparation/memory_output.py` | `:92` (memory-content leg only) | `render_memory_content_message(effective.message_for("memory"), result.candidate.codeView.codeCommit)` (`:92-94`) | the candidate's certified code commit |
| `memory/carryover.py` | `:846` | `render_memory_content_message(options.memory_commit_message, official_head)` (`:848`) | `official_head` |
| `memory/baseline.py` | `:210` | `render_memory_content_message(<adopt subject>, code_source_commit)` (`:212-215`) | the code source-branch commit |

**The two corrections.** `worktrees/queue/closeout_recovery.py` is **not** a producer, so the
22:05 census's third "remaining producer" does not exist: the recovery route's commit sites are its CODE
leg (`:209`, `commit_verified_staged(contract.code_worktree, effective_input.message_for("code"))`) and
its ledger legs (`:278`, `:357`), and `resume_external_commits` only *proves* an already-journaled
memory commit. When a resumed closeout still owes that memory commit, it is created by
`closeout_external.py:165` — the same producer the first attempt uses, which is why the recovery route is
attributed transitively rather than by its own copy. The producer the census **missed** is
`preparation/memory_output.py:92`, the preparation/certification closeout route: its prepared
memory-content intent is hashed into the private commit that `finalization.py` publishes to the live
memory ref.

### Trailerless By Rule, each with its reason

| Site | Reason it carries no trailer |
| --- | --- |
| `closeout_external.py:241` | ledger leg — the `memory.md`-only commit names no code commit |
| `direct_landing_execution.py:323` | ledger leg |
| `closeout_recovery.py:278`, `:357` | ledger legs |
| `closeout_recovery.py:209` | a **code** commit; the memory attribution names a code commit and must not ride on one |
| `carryover.py:748`, `:852` | the ledger-mapped-head branch's ledger-only commit, and the ordinary ledger leg |
| `baseline.py:224` | ledger leg |
| `worktrees/sync_transaction_git.py:304`, `:333` | memory **merge** commits: two memory parents and no single code commit to name |
| carryover's `nothing-to-carryover` branch | creates no memory commit at all |

## Code Commentary

### Logic

The five cases split into a source census and a behavioural half.

`test_the_attribution_key_is_named_and_rendered_in_exactly_one_module` (`:86-117`) is the one-definition
guard, and it reads source as text rather than through imports — a test that read
`CODE_COMMIT_TRAILER_KEY` to check it would follow a wrong constant instead of catching it. It derives
`_production_source()` (`:68-70`) from `__file__`, then asserts three things about
`mcp/src/agents_remember`: the key identifier and its interpolation appear in exactly one production
module (`kernel/memory_attribution.py`, `_ONE_MODULE`), and no module anywhere in that tree starts
the trailer as a **quoted literal** — a declared trailer always begins with the key it interpolates, so
`"Code-Commit"` written out anywhere in production is the failure.

`test_every_census_producer_reaches_the_shared_renderer` (`:119-137`) is the census itself: it reads each
of the five `_PRODUCERS` entries (`:55-63`) and asserts its expected renderer entry string is present, so
a producer that stopped calling the shared renderer fails by name. It is a source census rather than a
behavioural case for exactly one of the five — the prepared memory-content leg has no reachable public
entry point (`certification/execution.execute_selected_closeout` is bound in
`build_default_worktree_services` but has no production caller) — and that residual gap is stated on the
kernel card rather than hidden. The other four are covered end to end elsewhere: worktree closeout and
recovery in `test_transaction_only_worktree_delivery.py`, direct landing in `test_direct_landing.py`,
carryover and baseline in this module.

`test_the_one_renderer_keeps_the_callers_body_verbatim_and_its_trailer_final` (`:140-163`) is the dialect
case, and it uses a hostile body on purpose: several paragraphs whose own last paragraph is itself
`Key: value` lines, including a `Code-Commit:` lookalike. It asserts the caller's bytes survive
unchanged, that the trailer is its own final block after a blank line, and that the package's reader
takes ours rather than the caller's lookalike. This is the case that would fail if a producer wove the
attribution into the body instead of appending it — the failure mode that matters because carryover and
baseline take that body as a public argument of another tool.

The module drives a real disposable world for the two non-closeout producers. `_carryover_world`
(`:165-236`) composes the `QueueFixture` from `test_closeout_queue` with a real worktree contract, and
`test_carryover_attributes_its_memory_content_commit_to_the_official_head` (`:237-287`) calls the public
`memory_carryover_apply_tool` with `CarryoverCommitMessages`/`CarryoverSelection`/`MemoryBranches` and
the hostile body, then asserts the trailer equals `official_head` (read with
`git log --format='%(trailers:key=Code-Commit)'` and with `git interpret-trailers --parse`), that the
ledger row agrees, and that the ledger commit carries none.
`test_baseline_attributes_its_memory_content_commit_to_the_code_source_branch` (`:289-345`) drives the
public `memory_baseline_adopt_tool` over a real code repository and asserts the trailer equals the code
source-branch commit while `load_ledger(...).rows[0]` maps that same commit and the ledger commit
carries none.

### Conventions

Real Git object names, not labels: `CODE_ONE`/`CODE_TWO` are forty hex characters, because the census
and the readers only mean something against real objects. The expected renderer entry per producer lives
in one `_PRODUCERS` mapping beside the one-module and key-name constants, so adding a producer means
adding a row rather than editing an assertion. Assertions are derived from source text and from real
commits; nothing restates the trailer's spelling in production terms, and the only literal `Code-Commit`
text in the module is the oracle the census forbids in production.

The module is a consumer of `mcp/tests/closeout_fixture_test_support.py` and
`mcp/tests/closeout_input_test_support.py` in `mcp/tests/evidence-lifecycle.toml`, both reached
transitively through `QueueFixture`. Consumer declarations are ownership accounting only; they are not
execution or acceptance evidence. **The module has no evidence-lane row**, which is a pending open item
recorded on the `test-evidence-lanes.toml` card: `load_lane_manifest` derives every `test_*.py` module and
refuses a manifest that omits one, so the gap is a fail-closed load error until the builder registers the
row. Which lane it belongs in is the builder's call and is not asserted here.

### Invariants And Boundaries

- The census is a **source** fact measured at a base commit; it is not a runtime guarantee. A future
  producer that built the trailer string some third way would evade all three census assertions, and only
  its own route's behavioural case would catch it.
- The prepared memory-content leg has no behavioural case, because its route has no reachable caller
  today. The census case is its only protection, which is what makes that case load-bearing rather than
  decorative.
- The producer count is 5 and the untrailered count is 0 **because every trailerless commit site has a
  recorded reason**; "no trailer" is never tolerated as an unexplained state.
- This module asserts source shape and commit-object content. It makes no claim that a route ran in
  production, and the tests are focused development evidence, not certification.

### Todos

None recorded. The dead-route findings that shaped this module — `WorktreeArgs.recovery_commits` is never
assigned for closeout anywhere in `mcp/src` except `direct_landing_execution.py:90`, and
`execute_selected_closeout` has no production caller — are recorded as the master's
2026-09-13T23:50 decision, not as work this module owns.

## Docs References

No Domain Documentation source is configured for this repository; the proving evidence is git's own
trailer rendering plus this repository's source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for this repository-owned producer census. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one-definition guard: the key identifier and its interpolation in exactly one production module, and no module spelling the trailer as a quoted literal. | `test_the_attribution_key_is_named_and_rendered_in_exactly_one_module`; `_ONE_MODULE`; `_KEY_NAME`; `_production_source` | mcp/tests/test_memory_attribution_producers.py:64-65; mcp/tests/test_memory_attribution_producers.py:68-69; mcp/tests/test_memory_attribution_producers.py:86-116 |
| The census: five producers, each asserted to reach the named shared renderer entry. | `test_every_census_producer_reaches_the_shared_renderer`; `_PRODUCERS` | mcp/tests/test_memory_attribution_producers.py:55-63; mcp/tests/test_memory_attribution_producers.py:119-137 |
| The dialect: a hostile multi-paragraph caller body survives byte for byte, the trailer is its own final block, and the reader takes ours not the caller's lookalike. | `test_the_one_renderer_keeps_the_callers_body_verbatim_and_its_trailer_final` | mcp/tests/test_memory_attribution_producers.py:140-162 |
| Carryover end to end through the public tool, with the ledger row agreeing and the ledger commit unattributed. | `test_carryover_attributes_its_memory_content_commit_to_the_official_head`; `_carryover_world` | mcp/tests/test_memory_attribution_producers.py:165-234; mcp/tests/test_memory_attribution_producers.py:237-286 |
| Baseline adoption end to end through the public tool, attributed to the code source-branch commit its initial ledger row maps. | `test_baseline_attributes_its_memory_content_commit_to_the_code_source_branch` | mcp/tests/test_memory_attribution_producers.py:289-345 |
| The one renderer and the one key the census defends. | `render_memory_content_message`; `CODE_COMMIT_TRAILER_KEY` | mcp/src/agents_remember/kernel/memory_attribution.py:56-56; mcp/src/agents_remember/kernel/memory_attribution.py:72-97 |
| The closeout-shaped way in to the renderer, which two of the five producers call. | `memory_content_message` | mcp/src/agents_remember/models/closeout/input.py:148-166 |
| The recovery route's own commit sites, which the census deliberately leaves untrailered or attributes through `closeout_external.py`. | `commit_verified_staged`; `resume_external_commits` | mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:209-211; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:236-303; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:278-281; mcp/src/agents_remember/worktrees/queue/closeout_recovery.py:357-360 |
| The sync memory merge commits, whose two memory parents are why they are trailerless by rule. | `_finish_staged_memory_merge`; `continue_side_merge` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:304-326; mcp/src/agents_remember/worktrees/sync_transaction_git.py:329-350 |
| The end-to-end closeout-recovery case in the sibling module, which is the behavioural half for the route that has no commit site of its own. | `test_closeout_recovery_attributes_the_memory_commit_it_still_owed`; `_assert_memory_attribution` | mcp/tests/test_transaction_only_worktree_delivery.py:328-452; mcp/tests/test_transaction_only_worktree_delivery.py:183-227 |
| The artifact rows that now declare this module as an exact consumer, both through `QueueFixture`. | "path = \"mcp/tests/closeout_fixture_test_support.py\""; "path = \"mcp/tests/closeout_input_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:265-265; mcp/tests/evidence-lifecycle.toml:283-283 |

## Cross-Repo References

The carryover and baseline cases build both repositories they span — a code repository and an external
memory repository — as real temporary Git repositories, which is why the attribution can be read back
with git's own readers rather than asserted from a returned string. No production cross-repository
authority is claimed by this focused module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The external-memory side of each case is a real second repository created by the fixture, not a mock. | `init_repo`; "class QueueFixture:" | mcp/tests/test_closeout_queue.py:52-52; mcp/tests/test_closeout_queue.py:186-727; mcp/tests/test_worktree_support.py:97-117 |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 8 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): created this one-to-one sidecar for the leaf's new test module, which is the census
  the leaf is really about. Recorded the corrected census (5 producers, 0 untrailered, with the
  producer→commit-site→renderer→code-commit table), both corrections to the master's 2026-09-13T22:05
  decision (`closeout_recovery.py` is the recovery route's CODE leg, not a producer; the missed producer
  is `preparation/memory_output.py:92`), and the trailerless-by-rule table with a reason per site. Stated
  the durable rule the module enforces — the key is declared once and never spelled as a quoted literal
  in a second production module, and the trailer is appended as its own final block rather than woven
  into the caller's body, because carryover and baseline take that body as a public argument that may be
  multi-paragraph — together with the residual gap the census cannot close (a third-way producer, and the
  prepared leg having no behavioural case). Verification metadata is intentionally blank: the candidate
  is uncommitted and no commit contains this file yet, so closeout owns the stamp.

# mcp/tests/test_next_step_address_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_next_step_address_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T19:07+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a`|
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The lane that pins **a next-step hint describing the task the response addressed, never a process
cursor**. `D-13` recorded the failure: two `worktree_status` calls addressing *different* contracts
answered with the same `nextStep.nextArgs.enclosure_path`, taken from the globally most recently
published record under `controlplane/lifecycle-enclosures/`. `nextStep` is the field that says *call
this next*, so a caller that trusted it was walked into another master's live enclosure.

Two independent fixes are in the candidate and this module is their only case, because neither had
one before it:

- `application.next_step.compute_next_step` (`mcp/src/agents_remember/application/next_step.py:110-131`)
  is a pure function of the resolved contract — the hint follows the task the caller addressed, and
  the global enclosure cursor is gone from the hint path (its only remaining reader is the locator
  plane);
- `application.tool_response.bound_next_step`
  (`mcp/src/agents_remember/application/tool_response.py:30-50`) **omits** a hint whose `nextArgs`
  path fields contradict the response's own `contractPath`/`enclosurePath`, so a contradicting hint
  cannot reach a caller of an address-carrying envelope at all.

The reachable surface is **stated rather than assumed.** The binder can only compare a carrier that
declares an address, and `TaskDocResponse`
(`mcp/src/agents_remember/models/task_doc.py:138`) declares neither field, so the fourth case pins
what that carrier does instead of implying a guarantee it does not have — a future address field
there becomes a deliberate change with a red case rather than a silent one.

## Code Commentary

### Logic

**The module drives the two shipped functions directly and asserts on their answers**, without
standing up a coordination tree. `_contract` (`:48-73`) builds a real `WorktreeContract` in
`tmp_path`, with one keyword of difference between its two instances (`closeout_status="completed"`
on the second) so the two hints genuinely differ; `_live_state` (`:36-45`) supplies one running
lifecycle so the *linear* half of the guidance is the branch under test rather than the
"no lifecycle" branch. `_status_response` (`:76-86`) builds an address-carrying
`WorktreeStatusResponse` — the carrier D-13 was measured on — whose `contractPath` and
`enclosurePath` both name the addressed contract.

The four cases are one property each:

- **`test_a_hint_naming_another_contract_is_omitted_not_forwarded`** (`:89-105`) — the binder's whole
  purpose. The hint's `nextArgs.contract_path` names `/tmp/coordination/enclosures/leaf-b/series-contract.md`
  while the response addresses `leaf-a`, and the assertion is `bound_next_step(...) is None`.
  Forwarding it would tell the caller to call a tool against a task this response was not about, and
  keeping it would be indistinguishable at the wire from the correct hint.
- **`test_a_hint_naming_the_addressed_contract_is_kept_unchanged`** (`:108-119`) — the omission is a
  **contradiction check, not a blanket suppression of guidance**; the hint is returned by identity
  (`is own`), so a binder that started dropping every hint fails here.
- **`test_two_addressed_contracts_in_sequence_yield_two_different_hints`** (`:122-164`) — the plan's
  case, driven as a **sequence** rather than as one asserted value. L14's original measurement
  asserted a single wrong string, which is why a same-day re-measurement could not reproduce it: the
  defect was state-dependent, left behind by another session's attach. The case therefore asserts
  that each hint follows the contract it was passed *and* that neither serialized response body
  contains the other contract's path anywhere (`model_dump_json`, `:161-164`), which is what makes
  the property testable instead of momentary.
- **`test_an_envelope_with_no_address_passes_the_hint_through_unchanged`** (`:167-198`) — the
  boundary. It asserts `"contractPath" not in TaskDocResponse.model_fields` and
  `"enclosurePath" not in TaskDocResponse.model_fields` first, then that the hint passes through
  unchanged. The hint's source is `compute_next_step` over the caller's *own* session contract, so
  this is not the D-13 leak — it is the honest statement of where the binder's reach ends.

### Conventions

The module imports the shipped seams rather than re-deriving them: `compute_next_step` from
`application/next_step.py`, `bound_next_step` from `application/tool_response.py`, `NextStep` from
`models/base.py`, the two response envelopes from `models/task_doc.py` and `models/worktree.py`,
`LifecycleState` from `observer/lifecycle_state.py`, `lifecycle_guidance` from
`worktrees/modules/guidance.py` and `WorktreeContract` from `worktrees/worktree_contract.py`. Every
helper takes `tmp_path` so no case observes another's contract, and each helper carries a docstring
that states what it supplies rather than what it is.

**The lane registration is the manifest row**, not a module-level mark: this module carries **no
`pytestmark`**, and its single lane row was **appended** to the end of `unit-regression` in
`mcp/tests/test-evidence-lanes.toml:191` (item 16's half (a) — a mid-list insertion would shift every
row below it and stale every citation into that file). The lane manifest is what registers a module
here; only 42 of the tree's 297 test modules carry a category mark, so an unmarked module is the
house pattern rather than an omission.

### Invariants And Boundaries

- **The binder never invents an address.** It compares the hint's declared path arguments against the
  response's own; with no address on the carrier there is nothing to compare and the hint is returned
  unchanged (`tool_response.py:35-41`).
- **More than one address on one envelope is a refusal, not a guess.** `bound_next_step` returns
  `None` when the response's address fields disagree with each other (`:42-43`), so an ambiguous
  carrier cannot forward a hint at all.
- **Only the declared argument fields are compared** — `_ARGUMENT_PATH_FIELDS`
  (`tool_response.py:22`) — so a hint whose arguments carry no path is never suppressed.
- **A wrong hint must fail loudly, not silently.** Every case asserts the exact returned object
  (`is None`, `is foreign`, `is own`) rather than truthiness.
- **Boundary.** This is a test module. It owns no production contract, declares no fixture consumed
  by a sibling, and adds no support module.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the candidate: the two functions the module drives, the
carrier D-13 was measured on, the carrier that declares no address, and each case with the property
it pins.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of D-13 and of the two fixes it pins. | "A next-step hint must describe the task the response addressed, never a process cursor." | mcp/tests/test_next_step_address_binding.py:1-20 |
| **The binder's one rule: a hint whose arguments contradict the response's own address is omitted; an ambiguous address is a refusal.** | `bound_next_step` | mcp/src/agents_remember/application/tool_response.py:30-58 |
| The two field tuples the comparison reads. | `_RESPONSE_PATH_FIELDS`; `_ARGUMENT_PATH_FIELDS` | mcp/src/agents_remember/application/tool_response.py:22-28 |
| **The contract-derived hint, which is why no global cursor can reach a caller.** | `compute_next_step` | mcp/src/agents_remember/application/next_step.py:110-131 |
| One running lifecycle, so the linear half is the branch under test. | `_live_state` | mcp/tests/test_next_step_address_binding.py:50-59 |
| One addressed contract, with the closeout state its hint is derived from. | `_contract` | mcp/tests/test_next_step_address_binding.py:48-73 |
| The address-carrying envelope of the carrier D-13 was measured on. | `_status_response` | mcp/tests/test_next_step_address_binding.py:90-100 |
| **The contradicting-address case: the hint is omitted, not forwarded.** | `test_a_hint_naming_another_contract_is_omitted_not_forwarded` | mcp/tests/test_next_step_address_binding.py:89-105 |
| The positive control: the omission is a contradiction check, not blanket suppression. | `test_a_hint_naming_the_addressed_contract_is_kept_unchanged` | mcp/tests/test_next_step_address_binding.py:122-133 |
| **The plan's case, driven as a sequence: two addressed contracts yield two different hints and neither body carries the other's path.** | `test_two_addressed_contracts_in_sequence_yield_two_different_hints` | mcp/tests/test_next_step_address_binding.py:122-164 |
| **The stated reach: the one carrier that declares no address — `TaskDocResponse` — has its hint WITHHELD, asserted against the model's own fields. `260918-TSIP-L10` renamed this case because it asserted the opposite until that leaf; the row is corrected with it.** | `test_an_envelope_with_no_address_has_its_hint_withheld`; `TaskDocResponse` | mcp/tests/test_next_step_address_binding.py:182-219; mcp/src/agents_remember/models/task_doc.py:138-138 |
| The lane row this module was appended to. | "mcp/tests/test_next_step_address_binding.py" | mcp/tests/test-evidence-lanes.toml:196-196 |

## Cross-Repo References

No cross-repository behavior is implemented or measured in this file. Every case builds its
contracts under `tmp_path` and asserts one repository's own address binder.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: `_RESPONSE_PATH_FIELDS`; `_ARGUMENT_PATH_FIELDS` repointed to mcp/src/agents_remember/application/tool_response.py:22-22; mcp/src/agents_remember/application/tool_response.py:23-28. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `_live_state` repointed to mcp/tests/test_next_step_address_binding.py:50-59. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `_status_response` repointed to mcp/tests/test_next_step_address_binding.py:90-100. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `test_a_hint_naming_the_addressed_contract_is_kept_unchanged` repointed to mcp/tests/test_next_step_address_binding.py:122-133. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: "mcp/tests/test_next_step_address_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T01:20+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `test_next_step_address_binding.py.md:143` (test_an_envelope_with_no_address_has_its_hint_withheld) — re-read the claim against the successor case's own docstring, which records the rename (and, where it says so, the reversal of the behaviour the row described).
- 2026-09-18T19:07+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): created this one-to-one card for the case lane that pins the addressed-hint binder. It records that the module has **two** subjects (the contract-derived `compute_next_step` and the omitting `bound_next_step`), that the sequence case exists because L14's single-value assertion could not be reproduced, and that the binder's reach stops at a carrier declaring no address — which is why `TaskDocResponse`'s absent fields are asserted rather than implied. It also records that this module carries **no `pytestmark`** and is registered by its appended `unit-regression` lane row. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.

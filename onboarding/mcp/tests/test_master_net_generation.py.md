# mcp/tests/test_master_net_generation.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **production-composition evidence for `ICR-R13@v1`**: the master NET comparison is
endpoint-correct and bound to a generation, measured through the operations the dashboard
really calls. The NET/generation cases build a real series contract on disk, real leaf enclosure contracts,
real code and memory repositories with real branches, and drive `master_changeset`,
`master_file_diff` and their HTTP routes. The address-preservation cases exercise inventory
functions and the task changeset route on real Git repositories. Nothing here injects a
preconstructed payload or a hand-built comparison — which is what the packet's own evidence
class requires, since "tests that merely mirror implementation or assert returned prebuilt
payloads are insufficient for production-composition claims".

## Code Commentary

### Logic

The NET/generation cases assert these properties:

- `test_two_leaves_that_add_then_remove_a_file_net_to_exactly_zero` — the packet's
  conforming example and the falsifier for its non-conforming one: two leaves add then
  remove one file, the net is exactly `[]` with zero counters while both leaf counters stay
  nonzero. cit:([`test_two_leaves_that_add_then_remove_a_file_net_to_exactly_zero`], mcp/tests/test_master_net_generation.py:258-285)
- `test_a_net_zero_source_result_still_reports_memory_effects` — the packet's boundary:
  net-zero source with a one-line `memory.md` effect reports `code: []` + `memory:
  [memory.md]`. cit:([`test_a_net_zero_source_result_still_reports_memory_effects`], mcp/tests/test_master_net_generation.py:288-303)
- `test_a_pinned_generation_reopens_after_the_branch_advances` — the completed master's
  recorded result: a pinned generation reopens byte-identically after the branch advances
  (`superseded`) while the live view moves on (`current`, new digest). cit:([`test_a_pinned_generation_reopens_after_the_branch_advances`], mcp/tests/test_master_net_generation.py:306-329)
- `test_an_opened_file_stays_bound_to_the_listed_generation` — a pinned file expansion
  returns the recorded bytes while the live expansion returns `after: None`.
  cit:([`test_an_opened_file_stays_bound_to_the_listed_generation`], mcp/tests/test_master_net_generation.py:332-363)
- `test_an_unreadable_child_never_invalidates_the_net` — a garbage leaf contract plus an
  unresolvable leaf commit leave the net matching the live integrated result.
  cit:([`test_an_unreadable_child_never_invalidates_the_net`], mcp/tests/test_master_net_generation.py:366-383)
- `test_a_missing_code_endpoint_is_refused_never_substituted` — a missing endpoint is
  refused by name (`not-recorded` / `unresolvable`), never substituted with a later tip;
  an unknown master keeps degrading to empty. cit:([`test_a_missing_code_endpoint_is_refused_never_substituted`], mcp/tests/test_master_net_generation.py:386-417)
- `test_a_live_leaf_is_labelled_working_and_its_draft_stays_out_of_the_net` — a live leaf
  row reads `working` beside the integrated net and its uncommitted delta never leaks in.
  cit:([`test_a_live_leaf_is_labelled_working_and_its_draft_stays_out_of_the_net`], mcp/tests/test_master_net_generation.py:420-473)
- `test_the_master_routes_carry_the_generation_and_its_named_refusal` — the served routes:
  the list publishes `generation` + `currentness` + `scope`, and the shared 400/404 mapping
  carries the named refusal. cit:([`test_the_master_routes_carry_the_generation_and_its_named_refusal`], mcp/tests/test_master_net_generation.py:476-502)
- `test_a_diff_failure_after_validation_is_refused_never_reported_as_zero` — the F1 fix:
  a diff that fails *after* endpoint validation (monkeypatched
  `changed_files_with_counts` raising) is refused with `kind == "unresolvable"`, never
  reported as an empty net. cit:([`test_a_diff_failure_after_validation_is_refused_never_reported_as_zero`], mcp/tests/test_master_net_generation.py:505-523)

Two cases hold the master net's endpoint-keyed reuse.
`test_a_master_net_is_served_again_from_its_endpoint_commits` reads the real
`/api/changeset/master` route twice on one registered app and requires the second read to
add no net diff and no sidecar decision while both bodies match.
cit:([`test_a_master_net_is_served_again_from_its_endpoint_commits`], mcp/tests/test_master_net_generation.py:743-790)
`test_a_master_nets_sidecar_flags_follow_the_onboarding_index` requires a created or
rewritten onboarding route index to move the `hasSidecar` flag on the next read, so the
flags are observed rather than frozen.
cit:([`test_a_master_nets_sidecar_flags_follow_the_onboarding_index`], mcp/tests/test_master_net_generation.py:793-844)

Additional address-preservation cases exercise quoted names, leading spaces and literal backslashes
through inventory, closeout worklists, rename destinations and the changeset route. Their literal
addresses must survive routing unchanged; this source account is not a new execution receipt.

The shared world is `MasterFixture` with its `master_fixture(tmp_path)` builder — a
master-shaped fixture (series contract + two leaf contracts + real code/memory repos) that
leaf one adds `src/feature.py` into and leaf two removes. cit:([`MasterFixture`], mcp/tests/test_master_net_generation.py:124-133) cit:([`master_fixture`], mcp/tests/test_master_net_generation.py:252-255)
`pytestmark = pytest.mark.evidence_unit` declares the evidence lane; the catalog selects this module at
`mcp/tests/test-evidence-lanes.toml:323`. The registration states membership, not an invocation.

### Conventions

Real-Git fixture module in the `test_knowledge_review_source_endpoints.py` idiom: real
contracts on disk, real branches, the real resolution plus the real HTTP routes. Case names
state the property as a sentence. The F1 case pins the exact refusal kind and the
refused-not-empty wording.

### Invariants And Boundaries

- The NET cases compute their comparison through production owners rather than injecting a comparison payload. The sidecar-flag case writes a fixture route index and delegates its status observations to the real reader.
- R24 navigation is explicitly not claimed here; mounted-browser observation of the
  generation caption belongs to R24/R25 assembly (jsdom proves URLs + caption render).
- The module owns no contract or artifact row in `mcp/tests/evidence-lifecycle.toml`. The catalog
  declares it as a consumer of `mcp/tests/_user_settings_guard.py` and
  `mcp/tests/fixtures/repository_profiles/node/package-lock.json` in the current lifecycle catalog. These declarations state membership, not invocation.

## Retained Full-Card Audit Context

The following distinct accounts are retained from memory base `81cfe4a8`. Dates, source coordinates, counts, outcomes and ownership describe that recorded epoch. They add no fresh execution, mutation result or acceptance. Historical numeric reference labels are custody text and do not select live sidecar anchors.

### Original nine-case cohort

> The original NET/generation cohort had nine cases, one property each (the original docstring listed
> seven; route and diff-failure cases completed that cohort). The addresses below describe that historical
> cohort, not a fresh collection result or current source-line census:

### Endpoint-reuse leaf-step attribution

> Two further cases hold the master net's endpoint-keyed reuse (L174 S7).

### Earlier named-tree artifact addresses

> - The module owns no contract or artifact row in `mcp/tests/evidence-lifecycle.toml`. The catalog
>   declares it as a consumer of `mcp/tests/_user_settings_guard.py` and
>   `mcp/tests/fixtures/repository_profiles/node/package-lock.json` (lines 448 and 2800
>   in code tree `cb321e2ad3b69d960c4ca1ddf9442663278f429c`). These declarations state membership, not invocation.

The named cb321e2a tree and its old coordinates identify the earlier catalog reading; they are not proposed current source selectors.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References


- The shared master-shaped world (series + two leaf contracts, real code/memory repos) and its builder. [2]
- The conforming add-then-remove case and the F1 diff-failure refusal case. [3]

### Cross-Repo References

This card maps a repository-local agents-remember test module. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

### Repo-Internal References (continued)

- The selection under test (endpoint binding, digest, currentness, refusal) and the thin entry that publishes it. Anchor: `select_master_net` [5]


- The module declares the evidence_unit marker. [1]


- The lane manifest registers mcp/tests/test_master_net_generation.py in unit-regression. Membership selects evidence and does not establish execution. [4]

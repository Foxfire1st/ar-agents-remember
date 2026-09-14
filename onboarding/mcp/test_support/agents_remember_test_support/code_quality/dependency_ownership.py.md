# mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the source-derived test-consumer graph shared by targeted selection, retry proof and causal localization. It preserves reason provenance and distinguishes proved global invalidation from unresolved ownership.

## Code Commentary

### Logic

DependencyOwnershipGraph builds repository dependency facts, observed imports/literal consumers and independently checked evidence-catalog declarations. resolve retains every unresolved input and returns complete=false instead of silently expanding an incomplete graph. Parse failures, ambiguous modules and invalid lifecycle catalogs produce explicit unresolved reasons.

Changed tests own themselves; deleted tests leave the population. Repository-owned non-Python
inputs declare exact consumers only when the independently observed set matches. The reduced
suite's declarations enumerate retained consumers rather than old suite counts. An explicitly
declared empty set is distinct from an absent declaration: only observed-empty equality emits
`verified-repository-input-no-consumers`. Unknown inputs still retain unresolved ownership;
empty declarations cannot hide an actual consumer.

`REPOSITORY_TEST_INPUT_CONSUMERS` gained twelve exact declarations in the same change set — the
260913-LCA-L8 module and eleven sibling suites that the extracted shared fixtures now reach — so
`mcp/tests/test_terminal_blocker_reasons.py`, `mcp/tests/test_checkpoint_landing_end_to_end.py`,
`mcp/tests/test_cross_master_concurrency.py`, `mcp/tests/test_lifecycle_playthrough_end_to_end.py`,
`mcp/tests/test_memory_attribution_producers.py`, `mcp/tests/test_pause_stop_only_end_to_end.py`,
`mcp/tests/test_leaf_doc_master_link_binding.py`,
`mcp/tests/test_closeout_projection_source_classification.py`,
`mcp/tests/test_automatic_post_integration_cleanup.py`,
`mcp/tests/test_retired_door_publication_fields.py`,
`mcp/tests/test_terminal_enclosure_archive_sync_journal.py` and
`mcp/tests/test_worktree_status_terminal_next_tool.py` are all declared consumers of the ambient-role
runner `scripts/e2e_harness/run.py`. The declarations are the manifest-side half of those modules' routes
registration; it records ownership for targeted selection and claims nothing about execution.

Global inputs and conftest roots deliberately invalidate the full population and are separately recorded. Otherwise observed import/literal relationships are preferred; filename matching remains a labeled heuristic. ownership_configuration_digest binds the versioned global inputs, declarations, irrelevant roots/suffixes and dashboard test patterns, so selection authority changes are visible.

### Conventions

Keep test-consumer ownership separate from product-package/coverage ownership. Use deterministic sorted paths and typed SelectionReasonKind values when reporting why a test was selected or an input remains unresolved.

### Invariants And Boundaries

- Unknown ownership does not become a safe-full success at this layer.
- Catalog declarations must agree with independently observed consumers.
- Intentional pytest-global invalidation is distinct from incomplete ownership.
- Necessary import fan-out remains attributable rather than being pruned for speed.
- The selector configuration digest changes when classification authority changes.

### Todos

The previous card incorrectly described unresolved ownership as a full-population fallback. Current source retains incomplete/unresolved results and the targeted caller refuses them.

## Docs References

No external Domain Documentation source is configured. These are repository-owned implementation and verification contracts; no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or certification pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| Observed and declared ownership, exact-empty distinction and refusals | `DependencyOwnershipGraph` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:225-519 |
| Transitive importer closure | `transitive_importers` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:522-542 |
| Digest binds declarations and classification authority | `ownership_configuration_digest` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:593-614 |
| The repository-owned declaration table; the L8 module is declared as an exact consumer of the ambient-role runner. | `REPOSITORY_TEST_INPUT_CONSUMERS`; `AMBIENT_ROLE_RUNNER_PATH` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:56-175; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. In-tree fixture languages and Dagger SDK doubles remain same-repository evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |


## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the frozen source added
  twelve consumer rows to `REPOSITORY_TEST_INPUT_CONSUMERS`, which now ends at `:175`. Re-read the
  card and corrected both: the table range (56-163 → 56-175) and the sentence that still said one
  declaration was gained, which now names the twelve modules the extracted shared fixtures reach.
  Verification metadata remains closeout-owned.
- 2026-09-14T15:05+02:00 — 260913-LCA-L8 curator: recorded the one exact declaration this change set
  adds to `REPOSITORY_TEST_INPUT_CONSUMERS` — `mcp/tests/test_terminal_blocker_reasons.py` as a
  consumer of `AMBIENT_ROLE_RUNNER_PATH` (`scripts/e2e_harness/run.py`), the manifest-side half of
  that module's route registration and an ownership record only. Re-derived the three reference
  anchors this card keeps: `DependencyOwnershipGraph` `223-517` → `225-519`, `transitive_importers`
  `520-540` → `522-542`, `ownership_configuration_digest` `591-612` → `593-614`; the previous values
  were one line short of the symbols at both ends before this change as well. Added the declaration
  and runner rows. Verification metadata remains closeout-owned.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=28e3e565cb0fe0868771a37ec2e5daf640a6857c25c560df15d983534d6c0124; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-06T21:35:26+00:00 — Reconciled the d3610903 test-policy reduction against the current source, preserved integrity/ownership boundaries, and replaced stale forcing-suite citations with current owner evidence. Existing verification hash/date retained; source comparison is not final acceptance.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Reconciled exact ambient-runner consumer closure and added publication/evidence consumers; preserved incomplete-ownership refusal and explicit global invalidation.

- 2026-09-05T06:14:14+00:00 — Corrected obsolete safe-full wording to the implemented explicit unresolved-ownership contract and incorporated new profile consumers.

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: rewrote the
  Docs References task-artifact rows as prose (absolute ar-coordination paths are not
  repo-relative citations and carry no verifiable provenance).

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for eb05a872780112640359232063168639d20fa87b (root bootstrap repair): documented the added exact literal consumer `mcp/tests/test_gate_certificate_authority.py` for the certification profile; verification metadata rebased from `0506b57a` to the bootstrap repair owning commit.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 added exact, source-verified ownership for
  `layers.toml`: five declared consumers, no full-population launch, and no scanner fallback.
  Verification remains closeout-owned.

- 2026-08-30T21:25+02:00 — 260821-ARSPAWN-L5 added source-verified exact consumer ownership for `.codex/config.toml`, avoiding both global invalidation and an unproved narrow selection. Verification remains closeout-owned.

- 2026-08-27T14:04+02:00 — Removed the misleading graph-local `product_*` projection. Consumer
  ownership remains cross-package; explicit configured package authority now exclusively owns the
  distinct product-versus-verification measurement decision.

- 2026-08-27T11:14+02:00 — Reconciled source-first ownership: recursive plugin/import/reference
  facts are authoritative, catalog consumers are a cross-check, and incomplete truth names a fresh
  rerun instead of silently selecting a narrower population.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.

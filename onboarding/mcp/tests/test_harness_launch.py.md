# mcp/tests/test_harness_launch.py

| Field                  | Value                              |
| ---------------------- | ---------------------------------- |
| repository             | agents-remember                    |
| path                   | `mcp/tests/test_harness_launch.py` |
| doc_type               | `file-level-onboarding`            |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Harness-specific launch vocabulary and exact model identity.

## Code Commentary

### Logic

Pi accepts only the full provider-qualified catalog key. Effective launch refuses a different model. Applying native knobs preserves fixed argv/environment and rejects duplicate selector authority; a parameterized harness population carries the selected model and effort through each native vocabulary.

`_knob_values` is the extraction helper that defines what "carried into its own launch vocabulary"
means, and 260915-CAPS-L6 extended it to collect **`knobs.env`** beside `knobs.argv` and
`knobs.session_config.values()`. The reason is eve: its model and reasoning effort are compiled
application values with no argv vocabulary, so its selection rides the launch environment the adapter
composes (`eve_launch_knobs` returns `argv=()` with the model/effort in `env`). Without the env
carrier the parametrized case failed for `eve`; extending the helper was preferred over weakening the
assertion or excluding `eve` from the parametrization. The parametrization is over
`sorted(BUILTIN_PROTOCOL_HARNESSES)` — the registry `create_harness_protocol_adapter` itself consults
— so it now covers four harnesses.

### Conventions

This card describes the retained source at the leaf's uncommitted candidate over IAS `d3610903`.
Historical entries below record earlier test populations; they do not require restoring removed cases.
Source inspection is memory preparation and does not claim a test run or acceptance.

A carrier added to `LaunchKnobs` must be reflected in `_knob_values`, or the contract silently stops
covering that carrier for every harness at once.

### Invariants And Boundaries

Catalog identity owns selection; an ambiguous model suffix is not a substitute. These cases do not start vendor processes or prove every historical catalog-validation edge.

The population is a registry parametrization, not a list: adding a fifth harness to
`BUILTIN_PROTOCOL_HARNESSES` holds it to the contract without an edit here, and excluding one would
defeat the contract this file exists to assert. The test asserts the shared contract rather than any
harness's own flag spelling.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pi requires the exact provider qualified catalog key. | `test_pi_requires_the_exact_provider_qualified_catalog_key` | mcp/tests/test_harness_launch.py:40-71 |
| Effective launch still refuses a genuinely different model. | `test_effective_launch_still_refuses_a_genuinely_different_model` | mcp/tests/test_harness_launch.py:108-116 |
| Apply launch knobs preserves fixed argv and refuses duplicate authority. | `test_apply_launch_knobs_preserves_fixed_argv_and_refuses_duplicate_authority` | mcp/tests/test_harness_launch.py:119-154 |
| Every harness carries a clean selection into its own launch vocabulary. | `test_every_harness_carries_a_clean_selection_into_its_own_launch_vocabulary` | mcp/tests/test_harness_launch.py:188-196 |
| The extraction helper enumerates every carrier, including the launch environment added for eve. | `_knob_values` | mcp/tests/test_harness_launch.py:173-186 |
| eve is the environment-only harness whose addition forced the carrier extension. | `eve_launch_knobs` | mcp/src/agents_remember/serving/eve_runtime_launch.py:392-407 |
| The two environment names eve's selection rides on are module constants rather than inline strings, which is what makes the carrier assertable. | `MODEL_ENV`; `EFFORT_ENV` | mcp/src/agents_remember/serving/eve_runtime_launch.py:86-87 |
| The registry the parametrization drives is the one the adapter factory consults. | `BUILTIN_PROTOCOL_HARNESSES`; `harness_launch_knobs` | mcp/src/agents_remember/serving/harness_control_factories.py:33-54 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `eve_launch_knobs` repointed to mcp/src/agents_remember/serving/eve_runtime_launch.py:392-407. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `MODEL_ENV`; `EFFORT_ENV` repointed to mcp/src/agents_remember/serving/eve_runtime_launch.py:86-86; mcp/src/agents_remember/serving/eve_runtime_launch.py:87-87. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): the body is retained (this file is
  byte-identical between the A1 and A2 candidates), and three citation findings were **repaired**
  rather than restamped. The parametrized case's range was corrected to the lines it occupies now
  (`:188-196`; the file ends at 196), the helper's range was tightened to `:173-186`, and the eve row
  was split so every anchor names its own declaring source: `eve_launch_knobs` at
  `eve_runtime_launch.py:310-327`, and the `MODEL_ENV` / `EFFORT_ENV` constants at `:70-71` — the
  previous single row cited `:301-317`, which holds neither constant, and the claim could not be
  compared with its provenance because those identifiers resolve in more than one file. Verification
  metadata moves to the leaf's current base `e9300687`; the candidate is uncommitted, so the governed
  closeout re-stamps the real code commit and no hash was invented here.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: body updated for the env-carrier extension. `_knob_values` now collects `knobs.env` beside argv and session config, because eve's selection is environment-only; the parametrized contract case therefore covers four harnesses instead of failing for the fourth. Recorded the deliberate choice to extend the helper rather than weaken the assertion or exclude eve, and the standing rule that a new `LaunchKnobs` carrier must be reflected here. Verification metadata is pinned to the leaf's base commit `67b21aeb` because the candidate is deliberately uncommitted — the governed closeout stamps the real code commit, and no hash or fingerprint was invented here.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 3 repository-internal launch-policy and runner-contract references for effective echo/knob checks, Codex config parsing, and discovery/failure ordering; final scoped result 0 (checker-clean).

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_harness_launch.py`
  since the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3
  line(s) with no token change whatsoever. Checked by parsing both revisions and comparing the
  abstract syntax trees (identical) and the comment tokens (identical), so no symbol, signature,
  default, decorator, control-flow branch, docstring, or assertion this card describes has moved,and every claim this card makes about its own source still holds.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: added the R2 resolved-identity acceptance
  coverage — the opus[1m] regression pin (alias collapsed onto the default's `resolved_model` now
  validates via `_resolves_to_same_model`), the still-refuses-a-genuinely-different-model direction,
  and `_select_current_model` preferring the requested alias over the default collapse. Verification
  metadata stays pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-15T23:16+02:00 — Created for 260714-ACPUI-L2 with complete selection, dynamic
  model-gated validation, Pi identity, echo verification, duplicate-selector census, and
  unrelated-argument preservation coverage; final-audited the no-configured-domain-source evidence.
  Verification metadata is blank until closeout stamps the new source file's first commit.

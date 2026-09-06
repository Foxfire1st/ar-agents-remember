# test_agentic_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_agentic_settings.py`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Two-layer agentic settings merge and authority-boundary tests.

## Code Commentary

### Logic

Local leaf overrides preserve global siblings; arrays replace and absent files expose defaults. Retained refusals name malformed settings paths, reject local gate delegation, human-pinned delegation and executor authority in agentic settings. Role overrides inherit flat defaults; harness references resolve against the effective merged registry.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Executor selection is not an agentic-settings option. The remaining tests do not establish the removed unknown-key, free-form knob or effort-policy matrices.

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
| Local leaf overrides global leaf and siblings survive. | `test_local_leaf_overrides_global_leaf_and_siblings_survive` | mcp/tests/test_agentic_settings.py:51-86 |
| Arrays replace never concatenate. | `test_arrays_replace_never_concatenate` | mcp/tests/test_agentic_settings.py:88-94 |
| Absent files mean documented defaults. | `test_absent_files_mean_documented_defaults` | mcp/tests/test_agentic_settings.py:96-116 |
| Local gate delegation is refused global layer only. | `test_local_gate_delegation_is_refused_global_layer_only` | mcp/tests/test_agentic_settings.py:131-146 |
| Malformed json fails loud with path. | `test_malformed_json_fails_loud_with_path` | mcp/tests/test_agentic_settings.py:148-157 |
| Human pinned gate kind cannot be delegated. | `test_human_pinned_gate_kind_cannot_be_delegated` | mcp/tests/test_agentic_settings.py:173-175 |
| Level override deep merges over the flat default. | `test_level_override_deep_merges_over_the_flat_default` | mcp/tests/test_agentic_settings.py:205-221 |
| New id adds a harness with defaults derived. | `test_new_id_adds_a_harness_with_defaults_derived` | mcp/tests/test_agentic_settings.py:248-256 |
| Cross layer reference and partial override merge. | `test_cross_layer_reference_and_partial_override_merge` | mcp/tests/test_agentic_settings.py:258-271 |
| Reference to an id known nowhere fails naming the manual. | `test_reference_to_an_id_known_nowhere_fails_naming_the_manual` | mcp/tests/test_agentic_settings.py:273-275 |
| Executor authority is not accepted in agentic settings. | `test_executor_authority_is_not_accepted_in_agentic_settings` | mcp/tests/test_agentic_settings.py:290-298 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the executor-field removal assertions in agentic settings tests.


- 2026-08-14T11:27+02:00 — R39 curator: aligned settings assertions with container-only
  acceptance. Verification remains closeout-owned.
- 2026-08-14T06:38+02:00 — L23 final candidate review: settings regressions pin Dagger as the only
  accepted executor and reject stale local/fallback quality policy. Verification stays
  closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: replaced the
  obsolete 2 GiB default assertions with absent/empty host-managed assertions
  while retaining explicit positive-cap and fail-loud schema coverage.
  Verification metadata remains pinned until closeout stamps L24.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the `orchestration.escalation`
  fail-loud retirement tests (family and `respawnAfterRung` refused; no `settings.escalation`
  attribute). Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: recorded
  `QualityGateSettingsTests` and the quality-gate default assertions in the
  merge/seed classes. Verification metadata stays pinned until closeout stamps
  the 260731-EFA-L17 commit.
- 2026-08-04T18:49+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the four malformed rows
  (settings-json.md `## Agentic Settings` section, `load_agentic_settings`, `find_harness`, and the
  supervisor test spans) and rewrote the parenthesized L16 series-tag spellings as cit forms. Renamed construct
  resolved deterministically: `SupervisorFamilyTests` no longer exists — the supervisor cases were
  folded into `TypedModelTests` (defaults/parse at 416-446, floor refusal at 463-466) — so the two
  body mentions now say so; the pinned behavior is unchanged. NOT a Tier-3 deletion.
- 2026-07-31T16:40+02:00 — 260731-EFA-L2: the whole-tree `ruff format` pass (`00e8379`) reflowed
  `mcp/tests/test_agentic_settings.py` and moved the lines this card cites, so the Citations
  column no longer pointed at the code its rows name. Corrected the ranges (L443-L488 →
  L419-L464). The behaviour described is unchanged — the file's AST is identical to the base
  revision — this is a citation repair only. Verification metadata pinned until closeout stamps
  the L2 commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented the partial-override regressions
  that prevent built-in static effort policy from reappearing and corrected the nearest governing
  overview link. Verification metadata remains pinned until closeout stamps the L2 code commit.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: documented declared-menu versus
  builtin-Codex dynamic effort regression coverage from the final candidate.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: covered the one-row supervisor default and safe Codex
  effort-flag template override. Verification metadata remains pinned until closeout stamps the
  eventual L15 code commit.

- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: updated `SupervisorFamilyTests` for
  `signalCooldownSeconds`, the 900-second default/floor, and fail-loud sub-floor refusals for both
  redelivery and signal cooldown settings. Verification metadata pinned until closeout stamps the
  260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm, R4): updated supervisor settings
  regressions for the conservative `redeliver_budget` default and `redeliverBudget` positive-int
  parsing/refusal. Verification metadata pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (escalation ladder, R1): added `EscalationSettingsTests` —
  absent-block defaults, full-block parsing of `slaSeconds`/`rungSeconds`/
  `nudgeRateLimitSeconds`/`respawnAfterRung` (with per-kind fallback for an unconfigured
  `message_kind`), and fail-loud coverage for an unknown SLA kind, a non-positive SLA value, an
  out-of-range rung key, an out-of-range `respawnAfterRung`, and an unknown top-level escalation
  key. Verification metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep, R1/R5): added `SupervisorFamilyTests` —
  absent-block defaults, full-block parsing of all four knobs, `enabled`-must-be-boolean,
  `intervalSeconds`-must-be-positive, and unknown-key fail-loud (`sweepSeconds`). Verification
  metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 route impact (small): `TypedModelTests` role-knob
  fixture gained a flat `system-specialist` entry asserting `RoleKnobs(harness="claude",
  model="fable")`, pinning the ninth `KNOWN_ROLES` member's flat role-knob parsing. Verification
  metadata pinned until closeout stamps the HFX-L7 commit.
- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: role-knob parsing tests
  now include a flat `curator` entry, and `RolesPerLevelTests` adds
  `test_curator_is_allowed_inside_a_level` to pin per-level curator overrides while preserving
  unknown-role refusals. Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: role-knob
  parsing tests now include an `architect` flat role entry, and `RolesPerLevelTests` adds
  `test_architect_is_allowed_inside_a_level` to pin per-level architect overrides while
  preserving unknown-role refusals. Verification metadata pinned until closeout stamps the
  HFX-L6 commit.
- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, findings 4 + 6): `FailLoudTests` gained the
  null-family refusal tests (repo-local walk across the six families + a global-layer case, proving no
  silent wipe); `HarnessesFamilyTests` gained the `effortSessionCommand` template-validation tests
  (three bad shapes, the builtin-override path, and a valid `{value}`-only template). Verification
  metadata pinned until closeout stamps the L18 commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): added `FreeFormRoleKnobTests`
  (additive escape-hatch parsing, free-string effort at load, shape fail-loud),
  `RolesPerLevelTests` (per-level deep-merge over flat defaults, the reviewer-economics walk,
  level/role fail-loud, list-replace), and `HarnessesFamilyTests` (registry openness: add/override
  semantics, vehicle-pair rules, effective-id references, cross-layer partial overrides, the
  manual-naming refusal). Existing loader tests unmodified. Verification metadata pinned until
  closeout stamps the L16 commit.

- 2026-07-07T06:10+02:00 — PR #100 review fix (Codex P2, merge `e358c4a`): `FreeFormRoleKnobTests`
  gained `test_empty_free_form_list_is_refused` and `test_empty_per_level_list_override_is_refused`
  (an empty free-form list refuses with omit-to-inherit guidance, flat and per-level). Post-merge
  onboarding refresh (developer-approved) verified against main @ e358c4a.

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up: local-gateDelegation refusal test added (L13R-2). Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T22:15+02:00 — 260703-L13 (settings unification): created the loader suite —
  merge precedence (global-only / local-only / override / array-replace), fail-loud
  unknown-key refusal naming the offending file with the top-level-family tolerance
  reservation, absent-file defaults, malformed-JSON refusal, typed loop/role/concurrency/
  spawn/gateDelegation models, and the install-seed round-trip. Verification metadata
  pinned until closeout stamps the L13 commit.

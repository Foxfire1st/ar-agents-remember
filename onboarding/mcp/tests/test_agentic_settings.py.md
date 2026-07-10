# test_agentic_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_agentic_settings.py`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T13:03+02:00 |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009` |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_agentic_settings.py` covers the two-layer agentic settings loader
(`kernel/agentic_settings.py`, 260703-L13): merge precedence, the fail-loud
unknown-key discipline, absent-file defaults, and the typed models — plus, since
260703-L16, the free-form role knobs (`FreeFormRoleKnobTests`), the per-level
overrides (`RolesPerLevelTests`), the harness-definition family
(`HarnessesFamilyTests`), the supervisor sweep's own knob family (since 260707-HFX2-L2,
`SupervisorFamilyTests`), and — since 260707-HFX2-L4 — the escalation ladder's own knob family
(`EscalationSettingsTests`).

## Code Commentary

### Logic

**260707-HFX2-L15 coverage.** The harness-family tests pin the redelivery default of one and prove
that replacing the Codex builtin's effort flag clears its builtin `--config` value template,
preserving the normal two-argument custom-flag contract.

L13 review follow-up adds `test_local_gate_delegation_is_refused_global_layer_only` (L13R-2): a repo-local gateDelegation raises AgenticSettingsError naming the local file.

Seven test classes, each writing real settings files into a temp coordination
root / repo root (no mocking — the loader's file I/O is the unit under test):

- `MergePrecedenceTests` — global-only, local-only, local-leaf-overrides-global
  (proving leaf-key granularity: the overridden sibling and untouched family
  survive), arrays REPLACE never concatenate (direct `merge_settings` check),
  absent-files → the full documented default posture (all-human gates, L12 loop
  defaults, empty roles, uncapped concurrency, no spawn preference, empty
  `sources`), and the optional `repo_root` argument.
- `FailLoudTests` — an unknown `orchestration.*` key raises
  `AgenticSettingsError` NAMING the offending file (asserted for both the
  global and the local layer), unknown TOP-LEVEL families are
  tolerated-not-parsed (the gate-amendment reservation: a `contextProviders`
  top-level key coexists while a typo'd `orchestration.*` key still fails),
  malformed JSON and non-object roots fail loud with the path, and per-family
  unknown-key refusals (gateDelegation, loop defaults, role names,
  concurrency caps). **260703-L18 (finding 6):** a JSON `null` at a known family
  key refuses loudly — one test walks concurrency/roles/loops/spawn/rolesPerLevel/
  harnesses in the repo-local layer (proving no silent global wipe), a second
  proves the global layer refuses too.
- `TypedModelTests` — the full L12 loop schema round-trips (defaults,
  perLevel, perMaster), partial perLevel keeps the other level defaults,
  maxRounds/concurrency positive-integer validation (bools rejected),
  complexity scale validation, role knobs with empty-knob defaults via
  `role_knobs()`, harness values validated against the registry ids (the
  documented-but-wrong `claude-code` id is the regression case), and
  gateDelegation parsing in its new home (named policy, at-seams binding,
  human-pinned and unsupported-kind refusals as `AgenticSettingsError`).
  **260707-HFX-L7** adds a flat `system-specialist` role-knob entry
  (`{"harness": "claude", "model": "fable"}`) to the settings fixture and asserts
  `settings.roles["system-specialist"] == RoleKnobs(harness="claude", model="fable")`, pinning
  the ninth `KNOWN_ROLES` member's flat role-knob parsing.
- `FreeFormRoleKnobTests` (L16) — launchArgs/promptKeywords/sessionCommands
  parse ADDITIVELY into `RoleKnobs` tuples (old files unchanged, empty-tuple
  defaults), effort stays a FREE string at load (the developer's `ultracode`
  file boots; per-harness vocabulary is dispatch-time), and shape violations
  (non-list, empty member, non-string member) fail loud naming the knob. **PR #100 review
  (Codex P2):** an EMPTY list refuses with omit-to-inherit guidance — covered flat
  (`launchArgs: []`) and as a per-level override (`sessionCommands: []`, which would silently
  inherit the flat default through the field-wise `or` merge).
- `RolesPerLevelTests` (L16, the developer's reviewer-economics fixture) —
  a level override deep-merges over the flat default (harness inherited,
  model/effort replaced per level: sonnet/high leaf → opus/xhigh master →
  fable/ultracode portfolio), the default level is leaf, an absent family
  changes nothing, unknown level keys and unknown roles inside a level fail
  loud, `architect` and `curator` are accepted and deep-merged inside a level
  (HFX-L6/L6R3), and free-form lists REPLACE (never concatenate) per level.
- `HarnessesFamilyTests` (L16 registry openness) — an absent family means the
  builtin registry; a new id ADDS a harness (command⇄argv derivation, name
  defaulting, `defined_in="settings"`, builtin order preserved + new ids
  appended); a builtin override replaces declared fields and keeps the rest
  (claude keeps its knob mapping and `defined_in="registry"`); a new id with
  neither command nor argv, unknown entry keys, and unpaired delivery-vehicle
  fields (effortFlag without values, session values without their command)
  all fail loud; roles/spawn references accept settings-defined ids; a LOCAL
  layer may reference/partially override a GLOBAL entry (per-file validation
  is shape-only, cross-references bind on the merged block); and a reference
  to an id known nowhere fails naming the harnesses.md manual. **260703-L18
  (finding 4):** the `effortSessionCommand` template is validated post-merge —
  the three bad shapes (`/set {mode}={value}`, `{}`, an unmatched brace) refuse
  naming the harness, the builtin-override-supplying-only-the-command path is
  validated, and a `{value}`-only template is accepted.
- `SupervisorFamilyTests` (260707-HFX2-L2, R1/R5) — an absent `orchestration.supervisor` block
  yields the documented defaults (`enabled=True`, `interval_seconds=10.0`,
  `stale_cutoff_seconds=60.0`, `redeliver_rate_limit_seconds=None`,
  `signal_cooldown_seconds=900.0`, `redeliver_budget=250`);
  a full block parses every knob (`enabled=False`, `intervalSeconds=5`, `staleCutoffSeconds=30`,
  `redeliverRateLimitSeconds=900`, `signalCooldownSeconds=1200`, `redeliverBudget=75`);
  `enabled` rejects a non-boolean (`"yes"`) naming `supervisor.enabled`; `intervalSeconds` rejects a
  non-positive value naming `intervalSeconds`; `redeliverRateLimitSeconds` and
  `signalCooldownSeconds` both reject `899` as below the 900-second floor; and an unknown key
  (`sweepSeconds`) fails loud naming itself against `KNOWN_SUPERVISOR_FIELDS`.
- `EscalationSettingsTests` (260707-HFX2-L4, R1) — an absent `orchestration.escalation` block
  yields the documented defaults (`sla_for("nudge") == 300.0`, `rung_dwell(1) == 300.0`,
  `rung_dwell(2) == 900.0`, `nudge_rate_limit_seconds == 900`, `respawn_after_rung == 2`); a full
  block parses `slaSeconds`/`rungSeconds`/`nudgeRateLimitSeconds`/`respawnAfterRung`, with an
  unconfigured `message_kind` still falling back to its own documented default alongside the
  configured ones; an unknown `slaSeconds` key, a non-positive `slaSeconds` value, an out-of-range
  `rungSeconds` key, an out-of-range `respawnAfterRung`, and an unknown top-level `escalation` key
  all fail loud naming the offending path.
- `SeedTests` — `default_agentic_settings_seed()` round-trips through the
  loader to the SAME posture an absent file yields, except
  `gate_delegation_configured` is True (the seed explicitly claims the key's
  home for the boot-snapshot consumer).

### Conventions

Standard suite conventions: `MCP_SRC` path bootstrap, `unittest`, tempfile
roots per test class. The file-writing helper `write_settings` goes through
`agentic_settings_path` so the layout under test is the real one.

### Invariants And Boundaries

- No test touches the real coordination root; everything is temp-rooted.
- Boot-flow integration (gateDelegation legacy fallback + warnings) lives in
  `test_config.py`; spawn resolution lives in `test_spawn_agent_session.py` —
  this file owns the loader only.

### Todos

No known follow-up in this file.

## Docs References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The documented merge/fail-loud/default semantics these tests pin. | Agentic Settings section | [../../docs/reference/settings-json.md](../../docs/reference/settings-json.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The loader under test. | whole module | [../src/agents_remember/kernel/agentic_settings.py](../src/agents_remember/kernel/agentic_settings.py) |
| The harness registry bounding harness-id validation. | L41-L48 | [../src/agents_remember/serving/harnesses.py](../src/agents_remember/serving/harnesses.py) |
| Supervisor-family tests pin the `signalCooldownSeconds` default/full-block parse and sub-900 floor refusals. | L443-L488 | [test_agentic_settings.py](agents-remember/mcp/tests/test_agentic_settings.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Loader-local behavior only. | - | - |

## Update History

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

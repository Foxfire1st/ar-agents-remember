# test_agentic_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_agentic_settings.py`       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T23:45+02:00 |
| lastVerifiedCommitHash | `9d58058e3ce4815b0356794fc21973ebe9c71345` |
| lastVerifiedCommitDate | 2026-07-06T11:47:10+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_agentic_settings.py` covers the two-layer agentic settings loader
(`kernel/agentic_settings.py`, 260703-L13): merge precedence, the fail-loud
unknown-key discipline, absent-file defaults, and the typed models.

## Code Commentary

### Logic

L13 review follow-up adds `test_local_gate_delegation_is_refused_global_layer_only` (L13R-2): a repo-local gateDelegation raises AgenticSettingsError naming the local file.

Four test classes, each writing real settings files into a temp coordination
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
  concurrency caps).
- `TypedModelTests` — the full L12 loop schema round-trips (defaults,
  perLevel, perMaster), partial perLevel keeps the other level defaults,
  maxRounds/concurrency positive-integer validation (bools rejected),
  complexity scale validation, role knobs with empty-knob defaults via
  `role_knobs()`, harness values validated against the registry ids (the
  documented-but-wrong `claude-code` id is the regression case), and
  gateDelegation parsing in its new home (named policy, at-seams binding,
  human-pinned and unsupported-kind refusals as `AgenticSettingsError`).
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

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Loader-local behavior only. | - | - |

## Update History

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up: local-gateDelegation refusal test added (L13R-2). Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T22:15+02:00 — 260703-L13 (settings unification): created the loader suite —
  merge precedence (global-only / local-only / override / array-replace), fail-loud
  unknown-key refusal naming the offending file with the top-level-family tolerance
  reservation, absent-file defaults, malformed-JSON refusal, typed loop/role/concurrency/
  spawn/gateDelegation models, and the install-seed round-trip. Verification metadata
  pinned until closeout stamps the L13 commit.

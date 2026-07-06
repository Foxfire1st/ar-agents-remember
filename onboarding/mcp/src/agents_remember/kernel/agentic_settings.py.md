# mcp/src/agents_remember/kernel/agentic_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/agentic_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-06T23:45+02:00 |
| lastVerifiedCommitHash | `9d58058e3ce4815b0356794fc21973ebe9c71345` |
| lastVerifiedCommitDate | 2026-07-06T11:47:10+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`agentic_settings.py` is the two-layer AGENTIC settings loader (260703-L13): it reads the
GLOBAL `<coordination_root>/system/settings.json` plus an optional repo-local
`<code_repo>/system/settings.json`, merges them, and parses the top-level `orchestration`
family — gate delegation, the three-party-loop knobs, per-role knob overrides, concurrency
caps, and the spawn harness preference — into frozen typed models. It is the single parser
for the agentic family; the MCP authority file, memory-topology settings, and provider
lifecycle settings are separate families with separate parsers.

## Code Commentary

### Logic

L13 review follow-up (L13R-2): the loader REFUSES `gateDelegation` in the repo-local layer — a local value would validate and then silently do nothing (the boot snapshot reads the global file only), a fail-open shape; the refusal names the local file and states "global-layer only".

`load_agentic_settings(coordination_root, repo_root=None)` is the PER-USE entry point: each
call re-reads both files (no caching), so an edit takes effect on the next use without a
server restart. Each present file's `orchestration` block is first validated INDIVIDUALLY
(`_validated_orchestration_block` runs the full parse per file) so key/type/semantic errors
name the offending file; the blocks are then merged (`merge_settings` — deep merge at
leaf-key granularity, object leaves recurse, scalars AND arrays are REPLACED by the
override, local over global) and the merged block is parsed into `AgenticSettings`.

The fail-loud rule is scoped to `orchestration.*`: every nesting level has a frozen
known-key set (`KNOWN_ORCHESTRATION_FIELDS` = gateDelegation/loops/roles/concurrency/spawn,
plus per-family sets for gateDelegation kinds, loop defaults/complexity/levels, the six
l-01 role names, concurrency caps, and spawn) and `_refuse_unknown` raises
`AgenticSettingsError` naming the unknown keys, the allowed set, and the offending file.
Unknown TOP-LEVEL keys are deliberately tolerated-not-parsed: the same coordinator file is
the c-08 memory-settings fallback and the earmarked future home of further families
(`contextProviders` first in line — gate amendment 2026-07-06), so the fail-loud scope must
not foreclose them. Absent files (or an absent `orchestration` key) yield the documented
defaults: all-human gate policy, the L12 loop defaults (`maxRounds` 3, `delta-verify`
reviewer reuse, complexity high/medium, perLevel scored/seam-required/strategist), no role
overrides, uncapped concurrency, no spawn preference. Malformed JSON and non-object roots
fail loud with the path.

`parse_gate_delegation(raw, source=...)` is the gateDelegation parser MOVED here from
`mcp/config.py` (its logic is unchanged: named policy via `named_gate_policy`, per-kind
rule overrides via `_parse_gate_policy_rule`, `requireReviewerVerdictAtSeams` binding via
`apply_seam_verdict_requirement`); it now raises `AgenticSettingsError` with the source
appended and is shared by this loader (the key's new home) and `mcp/config.py`'s one-cycle
legacy authority-file fallback. `AgenticSettings.gate_delegation_configured` records
whether a FILE set the key (vs. the default) — the boot-snapshot consumer branches on it.

Harness preferences (`orchestration.spawn.harness`, `orchestration.roles.<role>.harness`)
are validated against `HARNESS_IDS` — the registry ids from `serving/harnesses.py`
(claude/codex/pi) — so a settings value can never inject argv (the fixed-argv posture).
Loop POSTURE names (`perLevel.<level>.loop`, `perMaster.<master>.<level>.loop`) are
model-interpreted doctrine, validated as non-empty strings, deliberately not a closed set;
complexity thresholds ARE scale-validated against `COMPLEXITY_SCALE` (low/medium/high).
`default_agentic_settings_seed()` / `default_agentic_settings_seed_text()` produce the
seeded global-file content (`$comment` header naming the schema doc, all-human
gateDelegation, the L12 loop defaults, no spawn preference) shared by `install/runtime.py`'s
copy-if-missing seeding and the c-13 interview's starting point.

### Conventions

Kernel-level module: consumers are `mcp/config.py` (boot-snapshot gateDelegation),
`mcp/tools/terminal.py` (per-use spawn harness resolution), and `install/runtime.py`
(seed). Frozen dataclasses (`AgenticSettings`, `LoopSettings`, `LoopDefaults`,
`LoopComplexity`, `RoleKnobs`, `ConcurrencySettings`) follow the `McpRuntimeConfig` style;
`AgenticSettingsError` joins the typed `AgentsRememberError` family (a `ValueError`
subclass). The kernel→serving import is a constant-table import only (`HARNESSES`).

### Invariants And Boundaries

- Read PER-USE, never boot-cached — the ONE boot-snapshot consumer is
  `mcp/config.py`'s gateDelegation (documented restart-required semantics).
- Fail-loud is `orchestration.*`-scoped; top-level families are tolerated
  (reserved: contextProviders returns here in a follow-up).
- Doctrine floors are not knobs: no key touches the master-exit seam gate or the
  strategist's mandatory pre-run (L12 ruling, restated in the module docstring).
- Arrays REPLACE on merge, never concatenate; sibling leaves survive an override.
- `sources` records the files actually read (global first) for error/refusal messages.

### Todos

No known follow-up in this file. (The contextProviders family migration and a
dashboard settings write path are tracked outside as follow-ups.)

## Docs References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The schema reference for the agentic family (two-layer model, merge semantics, fail-loud rule, loop schema, reserved families). | Agentic Settings section | [../../../../../docs/reference/settings-json.md](../../../../../docs/reference/settings-json.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The gate policy primitives the gateDelegation parse builds on (named policies, rule construction, seam verdict binding). | L1-L120 | [../controlplane/gate_policy.py](../controlplane/gate_policy.py) |
| The harness registry whose ids bound every harness preference value. | L41-L48 | [../serving/harnesses.py](../serving/harnesses.py) |
| The boot-snapshot consumer: gateDelegation sourced from the global file at boot with the legacy authority fallback. | parse_orchestration_settings | [../mcp/config.py](../mcp/config.py) |
| The per-use spawn consumer: explicit arg > repo-local > global > detection-gated default. | _resolve_spawn_harness | [../mcp/tools/terminal.py](../mcp/tools/terminal.py) |
| The install seeding consumer (copy-if-missing global file). | seed_agentic_settings | [../install/runtime.py](../install/runtime.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The loader operates on coordinator/repo-local files only. | - | - |

## Update History

- 2026-07-06T23:45+02:00 — L13 adversarial-review follow-up (L13R-2): repo-local gateDelegation refused loudly (global-layer only); regression test added. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-07-06T22:10+02:00 — 260703-L13 (settings unification): created the two-layer agentic
  settings loader — per-use global+local read, leaf-key deep merge with array-replace,
  `orchestration.*`-scoped fail-loud unknown-key refusal naming the offending file, typed
  models for gateDelegation (moved here from `mcp/config.py`), the L12 loop schema, role
  knobs, concurrency caps, and the registry-validated spawn harness preference, plus the
  shared install seed. Verification metadata pinned until closeout stamps the L13 commit.

# mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:42+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[kernel primitives overview](overview.md) — the module moved here from `mcp/` by 260731-EFA-L9;
and `kernel/`.

## Purpose

`provider_degradation_settings.py` is the dedicated parser for the optional
`providerDegradation` MCP settings block (260707-HFX-L7): it validates and produces the frozen
`ProviderDegradationSettings` thresholds the degradation detector (`providers/degradation.py`)
reads every evaluation. It follows the same fail-loud-allowlist discipline as
`timeoutCaps`/`dashboard` in `mcp/config.py` — unsupported keys and wrong shapes/types raise at
settings load, never silently ignored.

## Code Commentary

### Logic

`KNOWN_PROVIDER_DEGRADATION_FIELDS` is the closed 15-key allowlist (`enabled`,
`failSafeEnabled`, `memoryDegradedRatio`, `memoryCriticalRatio`, `degradedSamples`,
`criticalSamples`, `healthySamples`, `watcherLagDegradedCommits`, `watcherLagCriticalCommits`,
`watcherLagDegradedMinutes`, `watcherLagCriticalMinutes`, `probeDegradedMs`, `probeCriticalMs`,
`setupFailureDegradedStreak`, `setupFailureCriticalStreak`, `recentSampleLimit`).
`parse_provider_degradation_settings(raw)` returns the all-defaults `ProviderDegradationSettings()`
when the key is absent (`raw is None`); a non-dict raw value raises
`ProviderDegradationSettingsError` naming "must be an object"; unknown keys raise naming the
unsupported keys and the full allowed set. Each field then parses through one of three typed
helpers: `_bool_setting` (must be an actual `bool`, not an int), `_positive_setting` (must be a
non-bool `int >= 1` — every threshold/sample-count/limit field), and `_ratio_setting` (must be a
non-bool numeric in `(0, 1]` — the two memory-pressure ratios). Every rejection names the offending
`providerDegradation.<key>` and its expected shape.

`ProviderDegradationSettings` is a frozen dataclass with conservative production defaults:
`enabled=True`, `fail_safe_enabled=True`, `memory_degraded_ratio=0.80`,
`memory_critical_ratio=0.92`, `degraded_samples=3`, `critical_samples=2`, `healthy_samples=3`,
watcher-lag commit/minute pairs (5/20 commits, 10/30 minutes), probe-latency pair (2000/10000 ms),
setup-failure-streak pair (2/3), and `recent_sample_limit=120` — the detector's default posture
runs enabled with the failsafe armed at these bounds, per the task's "default ON at a
conservative bound" requirement.

`ProviderDegradationSettingsError` subclasses `AgentsRememberError` (the typed `ValueError`
family shared by `ConfigError` and the other settings-parser errors), so `mcp/config.py` wraps it
into `ConfigError` at the call site without changing the boot fail-loud contract.

### Conventions

Mirrors the `timeoutCaps`/`dashboard` settings-parser pattern in `mcp/config.py`: a frozen
dataclass of typed defaults, a `KNOWN_*_FIELDS` frozenset gate, and small per-type validator
helpers (`_bool_setting`/`_positive_setting`/`_ratio_setting`) rather than a general schema
library.

### Invariants And Boundaries

- Absent `providerDegradation` key ⇒ all-defaults, detector enabled with failsafe armed.
- Unknown keys, wrong container shape, and wrong per-field types all fail loud at settings load
  (never silently dropped or coerced).
- Ratios are bounded `(0, 1]`; sample/threshold counts are bounded `>= 1`; booleans must be actual
  bools (an int like `1` is rejected, matching the `dashboard`/`timeoutCaps` convention).
- This module owns validation and the typed shape only; it does not read the metrics log or post
  alerts — that is `providers/degradation.py`.

### Todos

No known follow-up in this file.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `providerDegradation` settings block is documented with its full key list, defaults, and behavior in the settings reference. | `# settings.json Reference` | docs/reference/settings-json.md:1-526 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `mcp/config.py` imports this module's `ProviderDegradationSettings`/`ProviderDegradationSettingsError`/`parse_provider_degradation_settings`, wraps parse errors into `ConfigError`, and stores the result on `McpRuntimeConfig.provider_degradation`. | "class McpRuntimeConfig" | mcp/src/agents_remember/kernel/primitives/runtime_config.py:123-123 |
| The degradation detector consumes every field of `ProviderDegradationSettings` as its threshold/behavior surface. | "class ProviderDegradationStore" | mcp/src/agents_remember/providers/degradation.py:171-171 |
| The public settings example ships a representative `providerDegradation` block. | `coordinationRoot` | examples/mcp/settings.example.json:3-3 |
| Settings-parsing tests cover defaults, explicit thresholds, unknown-key rejection, and per-field type rejection. | `ProviderDegradationSettingsTests` | mcp/tests/test_config.py:480-556 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Settings parsing is a repository-local MCP boundary; no external system or sibling repo involved. | n/a | n/a |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-08-02T01:42+02:00 — No content impact: corrected Source Path link depth. The link(s) in this document carried one `../` too many and had never resolved from this card's directory — not code moving out from under a citation, the path as written. Enumerating every depth in both trees leaves exactly one that resolves and it is exactly one level shallower, so there was nothing to judge (`memory_quality/style/citations`, `citation_link_depth_wrong`). No claim, range or target document changed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds. Noted while checking: the references table also
  cites line ranges inside `config.py`; those ranges shifted because this task edited those files,
  so treat the cited numbers as approximate and the linked cards as authoritative.

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: **mechanical only, attested unchanged.** The
  file's diff against `c1dc505` is a single `ruff format` line rewrap of the
  `recent_sample_limit=_positive_setting(...)` argument in
  `parse_provider_degradation_settings`. No setting, default, threshold or validation rule changed.
  Every claim in this sidecar was re-checked against the current source and still holds; the prose
  was deliberately not rewritten. (The whole-tree reformat is commit `00e8379`.)
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 curator memory pass: created for the new
  `providerDegradation` settings parser landed alongside the degradation detector. Verification
  metadata pinned until closeout stamps the HFX-L7 commit.

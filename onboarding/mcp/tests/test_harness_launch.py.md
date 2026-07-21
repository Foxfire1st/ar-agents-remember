# mcp/tests/test_harness_launch.py

| Field                  | Value                              |
| ---------------------- | ---------------------------------- |
| repository             | agents-remember                    |
| path                   | `mcp/tests/test_harness_launch.py` |
| doc_type               | `file-level-onboarding`            |
| lastUpdated            | 2026-07-21T11:30+02:00             |
| lastVerifiedCommitHash |                                    `38c3fd81bdf851dce96e9b2b14e2bff741e7b383`|
| lastVerifiedCommitDate |                                    2026-07-21T11:31:07+02:00|
| governingOverview      | `overview.md`                      |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

This file is the focused contract suite for ACPUI-L2's settings-resolved native launch layer. It
proves complete selection resolution, token-free dynamic model/effort validation, Pi's exact
provider-qualified identity rule, honest effective-launch echo checks, native launch-knob
application, and refusal of duplicate adapter-owned selectors before a vendor process can start.

## Code Commentary

### Logic

`_selection` and `_snapshot` build one small normalized selection/catalog fixture. The first group
round-trips `ResolvedLaunch`, refuses missing model or effort, accepts a unique resolved Claude
model, rejects unknown/model-gated values, requires Pi's exact `provider/model` catalog key, and
checks model/effort echoes with the harness-specific effort-echo requirement.

The second group applies `LaunchKnobs` to a base `LaunchSpec`. It proves adapter arguments are
inserted without losing fixed argv or environment, then enumerates every installed Codex model and
`-c`/`--config` spelling owned by the adapter. Those spellings refuse as duplicate authority while
unrelated config and sandbox arguments pass unchanged.

The 260718-CHATS-L5F group (R2) pins effective-launch acceptance on resolved-model identity, not the
catalog key. `test_effective_launch_accepts_alias_collapsed_onto_default_resolved_model` is the
opus[1m] regression pin: when the requested alias and the harness-reported key resolve to the SAME
underlying model, `verify_effective_launch` accepts (via `_resolves_to_same_model`) instead of
refusing a natively-succeeding launch; `test_effective_launch_still_refuses_a_genuinely_different_model`
holds the strict direction (a genuinely different or absent resolved model still fails); and
`test_select_current_model_prefers_requested_alias_over_default_collapse` proves
`_select_current_model(requested_key=…)` returns the requested alias rather than collapsing onto the
is-default row when several rows share one `resolved_model`. The codex exact-key and pi exact-key
guards are unchanged.

### Conventions

Keep this suite protocol-neutral and synchronous. Vendor discovery framing belongs in each adapter
test; this file tests the normalized launch policy with immutable capability and launch objects.
Parameterized CLI grammar tables are intentional executable documentation of the accepted Codex
parser forms.

### Invariants And Boundaries

- Settings-resolved native launches require both model and effort.
- Effort is validated under the selected model; there is no global effort list.
- Pi accepts only the exact provider-qualified dynamic catalog key.
- Effective-launch acceptance is by resolved-model identity: an alias whose `resolved_model` matches
  the reported key's is accepted, a genuinely different/absent resolved model still refuses, and the
  requested alias wins over a default collapse when rows share one `resolved_model` (260718-CHATS-L5F R2).
- Duplicate adapter-owned argv or config authority refuses before launch preparation proceeds.
- Echo verification never invents evidence when a protocol cannot report effort.
- No test in this file submits a prompt, starts a turn, or uses composer paste.

### Todos

No file-local todos. Mid-session set acceptance belongs to ACPUI-L3, and serving request exposure
belongs to ACPUI-L4.

## Docs References

The resolved source registry has no Domain Documentation entries, so no live documentation source
was available for this repository-owned launch contract. The code and tests below provide the
direct evidence.

| Finding                                                        | Citations | Source Path |
| -------------------------------------------------------------- | --------- | ----------- |
| No Domain Documentation source is configured for this repository.       | n/a       | n/a         |

## Repo-Internal References

The production module defines the exact policy exercised here, while the hosted runner establishes
the ordering and persistence boundary covered by its sibling tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `ResolvedLaunch` is complete and JSON-safe; dynamic validation is model-gated and Pi requires an exact provider-qualified key. | L17-L119 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| Effective echo verification is honest, and launch-knob application refuses duplicate adapter-owned argv/config keys. | L122-L182 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| Codex config parsing covers separated, equals-attached, and short-attached forms. | L185-L226 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| The sibling runner suite verifies discovery/application ordering and persistent failed launch evidence. | L110-L474 | [test_harness_control_runner.py](agents-remember/mcp/tests/test_harness_control_runner.py) |

## Cross-Repo References

No sibling repository participates in this own-adapter policy test; installed vendor CLIs are
covered through adapter and live-matrix evidence rather than a cross-repository code dependency.

| Finding                                      | Citations | Source Path |
| -------------------------------------------- | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: added the R2 resolved-identity acceptance
  coverage — the opus[1m] regression pin (alias collapsed onto the default's `resolved_model` now
  validates via `_resolves_to_same_model`), the still-refuses-a-genuinely-different-model direction,
  and `_select_current_model` preferring the requested alias over the default collapse. Verification
  metadata stays pinned (uncommitted); closeout re-stamps the candidate commit.
- 2026-07-15T23:16+02:00 — Created for 260714-ACPUI-L2 with complete selection, dynamic
  model-gated validation, Pi identity, echo verification, duplicate-selector census, and
  unrelated-argument preservation coverage; final-audited the no-configured-domain-source evidence.
  Verification metadata is blank until closeout stamps the new source file's first commit.

# mcp/src/agents_remember/serving/harness_launch.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_launch.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `3eafc555c848ac45a07a07720641f1735f8df0eb`|
| lastVerifiedCommitDate |  2026-08-21T05:15:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Defines the single typed settings-resolved native launch selection and the fail-loud boundary that
validates it against dynamic own-adapter capabilities, verifies effective startup where possible,
and applies adapter-produced launch material without duplicate authority.

## Code Commentary

### Logic

`ResolvedLaunch` binds one harness id, model key, effort, and workspace and provides a strict JSON
round trip for the runner process boundary. `resolve_settings_launch` requires a complete model and
effort instead of defaulting a role-configured spawn. `validate_launch_selection` looks up the
model in the live `CapabilitySnapshot`, requires it to be selectable, and checks effort only against
that model's launch-settable options. Pi requires an exact provider-qualified catalog key; Claude
and Codex may use one unambiguous resolved vendor identity.

`verify_effective_launch` reuses catalog validation and compares running model/effort echoes. Its
explicit `require_effort_echo` parameter preserves real protocol asymmetry: Pi requires both echoes,
while Claude can truthfully accept model echo plus catalog-validated native effort because
stream-json exposes no effort echo. Since 260718-CHATS-L5F R2 a strict catalog-KEY equality is no
longer the only acceptance path: the `_resolves_to_same_model` secondary guard accepts when the
running-reported key and the requested selection resolve to the SAME underlying model — the fix for
the claude `opus[1m]` refused-pair, where request `opus[1m]` and `default` share
`resolved_model=claude-opus-4-8[1m]` and the harness echoes the resolved id. A genuinely different
or absent resolved model still fails loudly (both directions test-pinned); codex exact-key and pi
exact-provider-qualified-key acceptance are unchanged. `apply_launch_knobs` inserts adapter argv immediately after the
executable, merges adapter env, and refuses conflicts with owned argv options or config keys. The
Codex grammar scan covers separated, equals-attached, and short-attached selector/config forms.

### Conventions

This module is vendor-neutral policy and pure data transformation; vendor adapters produce
`LaunchKnobs`, and the hosted runner owns ordering and subprocess lifecycle. Errors name the exact
requested value and advertised alternatives so daemon/readiness clients can surface useful launch
evidence.

### Invariants And Boundaries

- The dynamic per-install/auth catalog is the native validation authority; no default path uses a
  package-owned model or global effort enum.
- Effort is always validated under the selected model.
- Pi model identity is exact `provider/id`; a bare id is refused with matching alternatives.
- Adapter-owned argv/config/environment cannot coexist with a second free-form declaration.
- Duplicate-selector preflight must happen before token-free discovery starts a transient process.
- Effective launch mismatch fails loudly, EXCEPT when the reported key and the requested selection
  resolve to the same underlying model (`_resolves_to_same_model`, R2) — an alias/default collision
  on one `resolved_model` validates; a different or absent resolved model still refuses. Acceptance
  evidence is never invented where a protocol lacks an echo.
- The module performs no subprocess, settings write, ACP transport, Toad hosting, composer paste,
  or mid-session mutation.

### Todos

L4 supplies typed selections from daemon requests/defaults; L3's setters may reuse the same model
lookup and model-gating semantics without conflating launch and mid-session acceptance.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this new file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The launch policy is carried by the shared opener/runner and consumed by each own adapter.

| Finding | Anchor | Source |
| --- | --- | --- |
| The normalized capability types nest effort under each model and declare owned launch selectors. | `LaunchKnobs` | mcp/src/agents_remember/serving/harness_capabilities.py:136-148 |
| The runner performs pure conflict preflight, transient discovery, dynamic validation, then fresh runtime construction. | `launch_knobs` | mcp/src/agents_remember/serving/harness_control_runner.py:239-239 |
| Claude produces native model/effort flags and verifies the model echo without fabricating effort echo. | `claude_launch_knobs` | mcp/src/agents_remember/serving/harness_control_claude.py:128-142 |
| Codex produces thread config plus owned model/config selectors. | `codex_launch_knobs` | mcp/src/agents_remember/serving/codex_app_server_session.py:35-54 |
| Pi produces native provider-qualified model/thinking flags and requires both effective echoes. | `pi_launch_knobs` | mcp/src/agents_remember/serving/pi_rpc_protocol.py:118-132 |
| The opener serializes this typed object into the runner and persists its selected values as catalog provenance. | "The durable row for the process this open just spawned" | mcp/src/agents_remember/serving/terminal_opener.py:526-526 |

## Cross-Repo References

No external repository boundary is implemented; installed native harnesses are reached only through
their in-repository own adapters.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 curator: repaired the terminal_opener.py citation range (525→526, the durable-row docstring) surfaced by the leaf-scoped quality check; no content impact. Verification metadata remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:30:45+02:00 — 260731-EFA-L6 curator W2-B10: repaired 12 citation findings (6 reference rows); scoped recheck clean.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations. Claude's row now
  cites the three places the claim actually lives in `harness_control_claude.py`: the
  `verify_effective_launch(..., require_effort_echo=False)` guard at L160-L172, the honest
  `launchEffortEvidence` note ("catalog-validated native `--effort`; stream-json init has no effort
  echo") at L200-L210, and `launch_knobs`, which emits `("--model", model_key, "--effort", effort)`,
  at L271-L285 (was L77-L140; L188-L202). Codex's `launch_knobs`, which returns the `session_config`
  model/`model_reasoning_effort` pair plus `owned_argv_options`/`owned_config_keys`, is now L225-L243
  in `codex_app_server_adapter.py` (was L128-L146).
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R2 model-acceptance — `verify_effective_launch`
  gains the `_resolves_to_same_model` secondary guard so an alias/default catalog-key collision that
  resolves to one underlying model VALIDATES (the claude `opus[1m]`·medium refused-pair defect, where
  request `opus[1m]` and `default` share `resolved_model=claude-opus-4-8[1m]` and the harness echoes
  the resolved id); a genuinely different or absent resolved model still fails loudly, and codex/pi
  exact-key acceptance is unchanged (both directions test-pinned). Verification metadata stays pinned
  until closeout stamps the candidate commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: created onboarding for the complete typed
  launch selection, dynamic model-gated validation, exact Pi identity, honest effective-echo
  verification, and pre-discovery duplicate-authority refusal. Verification metadata remains empty
  until closeout stamps the new source commit.

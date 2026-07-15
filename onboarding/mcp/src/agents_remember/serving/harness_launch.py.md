# mcp/src/agents_remember/serving/harness_launch.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_launch.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash |  `5fa7026c644edfb4eb884173b64d31c9a14a6585`|
| lastVerifiedCommitDate |  2026-07-15T23:33:30+02:00|
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
stream-json exposes no effort echo. `apply_launch_knobs` inserts adapter argv immediately after the
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
- Effective launch mismatch fails loudly; acceptance evidence is never invented where a protocol
  lacks an echo.
- The module performs no subprocess, settings write, ACP transport, Toad hosting, composer paste,
  or mid-session mutation.

### Todos

L4 supplies typed selections from daemon requests/defaults; L3's setters may reuse the same model
lookup and model-gating semantics without conflating launch and mid-session acceptance.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this new file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The launch policy is carried by the shared opener/runner and consumed by each own adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The normalized capability types nest effort under each model and declare owned launch selectors. | L73-L156 | [harness_capabilities.py](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) |
| The runner performs pure conflict preflight, transient discovery, dynamic validation, then fresh runtime construction. | L152-L191 | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |
| Claude produces native model/effort flags and verifies the model echo without fabricating effort echo. | L77-L140; L188-L202 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |
| Codex produces thread config plus owned model/config selectors. | L128-L146 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| Pi produces native provider-qualified model/thinking flags and requires both effective echoes. | L94-L153; L181-L191 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |
| The opener serializes this typed object into the runner and persists its selected values as catalog provenance. | L170-L216; L311-L460 | [terminal_opener.py](agents-remember/mcp/src/agents_remember/serving/terminal_opener.py) |

## Cross-Repo References

No external repository boundary is implemented; installed native harnesses are reached only through
their in-repository own adapters.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: created onboarding for the complete typed
  launch selection, dynamic model-gated validation, exact Pi identity, honest effective-echo
  verification, and pre-discovery duplicate-authority refusal. Verification metadata remains empty
  until closeout stamps the new source commit.

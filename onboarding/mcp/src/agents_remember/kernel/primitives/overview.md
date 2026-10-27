# kernel/primitives/ — Kernel Primitive Vocabulary Overview

## What This Area Is

This directory owns the shared runtime configuration, checkout coordination isolation, gate policy and vocabulary, provider identity, optional memory-cap planning, drift snapshot and observer paths, command capture, tool reports, provider-degradation settings, version identity, and host authority primitives. Higher layers consume these definitions without making the primitive owners depend on MCP, controlplane, providers, or worktrees.

## Hot Path Summary

Legacy gateDelegation migration warnings are deduplicated per authority-file-path/shadowed-state pair in the process, rather than on every re-resolution. The downstream direct-leaf authority, ignored directExecutionEnabled input, configured policy precedence and host/readiness boundaries are unchanged. The provider-degradation parser's actual source owner is provider_degradation_settings.py; retained primitives do not restore removed provider tools.

`runtime_config.py` supplies the trusted runtime configuration record and parser. Its Paseo authority property reads the shared host settings on each use; a folder does not establish runtime readiness or model availability. `checkout_coordination.py` selects the loaded checkout's write boundary before runtime configuration reads. Gate policy defaults to human decisions, and memory-cap planning remains an explicit opt-in.

Repository configuration carries an optional certification-profile reference. This parser validates its path spelling; profile loading and execution belong to downstream certification owners. Native role launch and replay likewise belong downstream: the CLI launch owner carries task/workspace identity and the stored launch call, while its catalog owner validates model, effort and service-tier selections.

## Construction

directExecutionEnabled is ignored for every value and warned when trusted settings contain it; it creates no runtime field. Current direct-leaf grant authority belongs to the external addressed store and product mutation owners, not primitives settings or harness restarts. Other configured authority/provider/host semantics are unchanged.

> **Retained historical source account — superseded by the current route account:**
> The runtime record and parser live in kernel so consumers can share configuration without importing the MCP package. The record separates repository and provider scopes, gate policy, dashboard settings, degradation settings, retirement settings and tool-log settings. The Paseo runtime is read through the shared authority reader rather than stored as a boot snapshot.

The host primitives comprise the packaged host/Node contract, release-owned Node paths, the active MCP authority-file reader, the session-environment filter, and the strict Paseo settings parser. Node path selection requires Linux x86_64 with `/proc`. A configured Paseo block requires `installPrefix`, `home`, `listen`, `providers` and `embed`; `version` is optional and does not select a build. The authority reader uses the `paseoRuntime` block of the server's own `--config` settings file and reads it per use, with no user-settings or per-harness fallback. The environment filter removes named session variables plus the `PASEO_` and `AR_SPAWN_` prefixes, while retaining unrelated login/configuration variables.

Model, effort and service tier are separate role settings. The agentic settings records and parsers preserve those fields and their settings precedence; the native CLI catalog owner resolves their provider/model scope and refuses selections the host does not offer. Effort remains model-bound and requires a selected model. These primitives do not themselves perform launch or establish host readiness.

Checkout classification derives from the loaded package path, independently of the working directory. An undeclared linked-checkout process gets a synthetic runtime configuration and disposable coordination root; the central durable-write guard permits that root and the enclosure's exact `reports/` root. Declared MCP, dashboard, lifecycle-operation and test modes bypass checkout CLI isolation. The lifecycle-operation declaration does not yield a daemon writer role.

Other modules provide command-module output capture, drift snapshot path/removal helpers, observer store paths, provider instance naming, degradation-settings parsing, and tool-report retention/redaction. Version identity resolves installed distribution metadata through a function seam, falling back to the committed source-checkout release identity when distribution metadata is unavailable.

## The fresh host block

`fresh_host.py` spells the `paseoRuntime` block a cold host needs — the packaged install prefix, the daemon home, the dedicated listen address, an empty provider map and one embed entry per dashboard origin — so the settings writer asks for a block instead of spelling an address of its own. The serving host modules read that block from the MCP authority settings file: `paseo_install.install_host` and `paseo_start._settings` both resolve the file the tool server was started with, and neither writes settings.

## What Belongs Here

| Path | Role |
| --- | --- |
| `checkout_coordination.py` | Loaded-checkout classification, execution-mode declaration, and leaf-local durable-write containment. |
| `runtime_config.py` | Runtime configuration record + parsing (from `mcp/config.py`). |
| `command_capture.py` | Package-local command-module adapter helpers. |
| `drift_snapshot.py` | Drift-snapshot path/removal primitives. |
| `gate_policy.py` | Gate delegation policy. |
| `gate_vocab.py` | Gate-kind vocabulary. |
| `identity.py` | Provider instance identity/naming. |
| `inbox_backoff.py` (historical, removed) | Former inbox redelivery/backoff helper; no current module or scheduler. |
| `memory_cap.py` | Optional explicit full-gate hard-cap planning; default host memory/swap remains untouched. |
| `observer_paths.py` | Observer store-root path conventions. |
| `provider_degradation_settings.py` | Provider degradation settings parsing. |
| `tool_reports.py` | Bulk tool-report retention/redaction. |
| `version.py` | Installed package identity with an explicit metadata-or-source fallback resolver. |
| `fresh_host.py` | The five-key `paseoRuntime` host block a cold settings file receives. |

The host modules described above and `user_settings_location.py` also belong to this directory; the preserved inventory table predates those entries.

## Structures Found Here

- Settings records with fail-loud `ConfigError` and typed error families.
- Policy/vocabulary literals with single-declaration ownership.
- Path, checkout-containment, cap-planning and identity helpers, alongside explicit settings reads, report writes and snapshot removal.

## Operating Model

Kernel owns primitive vocabulary. Structural gate models re-export the gate names from kernel, and controlplane records consume them through models. Higher owners compose the primitives rather than moving lifecycle machinery into this directory.

The layering contract declares a strict total order between top-level packages. Its checker records an import violation when the imported package's rank is greater than or equal to the importing package's rank; imports within the same package are skipped. This establishes the intended boundary, not evidence that the current checkout passes the rail.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `checkout_coordination.py` | checkout write policy | Prevents unpublished worktree code from selecting or writing the deployed coordinator through supported paths. | covered |
| `runtime_config.py` | config authority | Every layer reads the same runtime record. | covered |
| `gate_policy.py` | policy | Human-first gate decisions. | covered |
| `memory_cap.py` | gate economics | Plans explicit opt-in full-wrapper caps; uncapped runs remain host-managed. | covered |

## Local Invariants And Traps

- Kernel must not import upward; if a primitive needs a producer above it, the producer supplies a port/implementation instead. There is a current discrepancy in the retained settings evidence: `_agentic_settings_core.py` imports `models.role_identity`. The architectural intent remains, but this overview does not claim that the current source satisfies it throughout kernel.
- Declare primitive vocabulary once; wire layers re-export it rather than retyping it. Structural gate models follow this rule for the kernel gate vocabulary.
- Checkout execution mode is declared in kernel. Undeclared linked worktrees own only `<worktree-group>/provider-runtime/dev-ar-coordination` for coordination rows and the enclosure's exact `reports/` root for operational artifacts. Undeclared primary-checkout access is refused. Test mode is explicit. This is a boundary for supported application paths, not a filesystem sandbox.
- The intended `lifecycle-operation` mode belongs to the detached task worker and grants no MCP/dashboard daemon writer role. The declaration helper exists, but no current source caller of that helper was found; activation by the worker remains an unresolved wiring question.
- Gate delegation preserves the human decision path. Human-pinned gate kinds reject non-human delegation.
- A certification-profile reference must be a canonical, traversal-free repository-relative POSIX path. Absolute paths, backslashes, drive prefixes and normalization-changing spellings refuse. Profile loading and execution remain downstream.
- Runtime configuration participates in protected-ref authority. The configured-contract owner checks code and memory repository identities, memory mode, coordination root and canonical task/enclosure paths against the durable contract at its mutation boundary; these checks are not performed by the primitive parser itself.
- An absent Paseo block selects no runtime. Requiring a runtime produces an explicit refusal; malformed configured settings refuse during parsing. Host capability refusals belong to the native catalog consumer.
- Memory caps are explicit opt-ins. Uncapped full gates remain under their executor runtime's host-managed RAM and swap policy.

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Policy/record stores or lifecycle machinery | `controlplane/`, `worktrees/`, `application/` |
| Wire/response models | `models/` |
| Provider runtime/teardown | `application/provider_runtime.py` |

## How To Use This Area

When adding a primitive:

1. Read this overview and the closest sibling sidecar.
2. Keep it import-free of higher packages; declare the vocabulary once.
3. Run the layering check and structural-coverage suite.

These are standing contributor instructions, not a report of checks executed for this proposal.

## Preserved Metadata

The following route and onboarding tables are retained metadata. Their `covered` values do not establish lifecycle completion, source conformance or acceptance; lifecycle authority was not supplied for this read-only assignment.

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/kernel/primitives/` |
| onboardingRoute | `mcp/src/agents_remember/kernel/primitives/overview.md` |
| parentOverview | [`mcp/overview.md`](../../../../overview.md) |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `checkout_coordination.py` | [`checkout_coordination.py.md`](checkout_coordination.py.md) | covered | Checkout execution and durable-write isolation policy. |
| `runtime_config.py` | [`runtime_config.py.md`](runtime_config.py.md) | covered | Config authority. |
| `command_capture.py` | [`command_capture.py.md`](command_capture.py.md) | covered | Command adapter. |
| `drift_snapshot.py` | [`drift_snapshot.py.md`](drift_snapshot.py.md) | covered | Snapshot primitives. |
| `gate_policy.py` | [`gate_policy.py.md`](gate_policy.py.md) | covered | Gate policy. |
| `gate_vocab.py` | [`gate_vocab.py.md`](gate_vocab.py.md) | covered | Gate vocabulary. |
| `identity.py` | [`identity.py.md`](identity.py.md) | covered | Provider identity. |
| `memory_cap.py` | [`memory_cap.py.md`](memory_cap.py.md) | covered | Memory cap. |
| `observer_paths.py` | [`observer_paths.py.md`](observer_paths.py.md) | covered | Observer paths. |
| `provider_degradation_settings.py` | [`provider_degradation_settings.py.md`](provider_degradation_settings.py.md) | covered | Degradation settings. |
| `tool_reports.py` | [`tool_reports.py.md`](tool_reports.py.md) | covered | Tool reports. |
| `version.py` | [`version.py.md`](version.py.md) | covered | Version identity. |

## Child Overviews

None.

**L184.** The host contract's pin moves to 0.12.0, and the runtime settings read the extra harness arguments a harness entry or a role entry carries.

`control_vocabulary.py` defines the shared execution-receipt directory/schema, report-log name, held-message schema, provider-limit reason and bridge timeout/refusal/unknown-outcome spellings. It imports no internal tier: writers and readers use the same constants, while permission, delivery and recovery decisions remain with their operation owners.

## Evidence

- Checkout policy derives from the loaded package path, separates coordination rows from enclosure reports, and centrally refuses targets outside both exact leaf-local roots.
- The layering contract loader establishes package ranks; the checker enforces their order on imports between distinct packages.
- Structural gate models import the producer-owned gate vocabulary from kernel.
- Paseo settings own strict nested runtime fields and the explicit unconfigured-runtime refusal.
- Runtime configuration owns repository/profile parsing and reads shared host authority per use.
- Agentic settings keep model, effort and service tier separate and resolve role settings precedence; this file also contains the disclosed upward model import.
- Role settings parsers shape-check independent fields; quality-gate caps remain optional.
- The authority reader reads the block of the MCP settings file on each use.
- The session environment filter delegates to named-variable and prefix predicates.
- The five-fact settings parse accepts an optional non-selecting version key.
- Checkout modes, leaf-local roots and daemon-role narrowing define the execution boundary.
- Gate policy is human-first and rejects non-human delegation of pinned kinds; gate vocabulary is kernel-owned.
- Command capture, snapshot removal, observer paths and provider naming are shared primitive operations.

- Remaining opt-in memory-cap planning, provider-degradation settings parsing, report retention/redaction and package/source version resolution keep their primitive owners; removed inbox backoff supplies no current scheduler.
- Packaged host pins, Linux x86_64 Node selection and the user-settings location supply shared host primitives.
- Configured-contract authority checks repository identities, memory mode and canonical task/enclosure paths at its mutation boundary.
- Native launch construction and replay belong to the CLI launch owner; catalog selection refuses unsupported model, effort and feature selections.

- The kernel validates the optional certification-profile path; requested certification loads that profile, freezes exact admission and executes the selected quality plan through its own owner, independently of ordinary closeout.

- Legacy gateDelegation migration warnings are deduplicated per authority-file-path/shadowed-state pair in the process, rather than on every re-resolution. The downstream direct-leaf authority, ignored directExecutionEnabled input, configured policy precedence and host/readiness boundaries are unchanged. The provider-degradation parser's actual source owner is provider_degradation_settings.py; retained primitives do not restore removed provider tools.

## The host authority file

`paseo_authority.py` owns one file: the MCP settings file named by `configPath`. It reads that file's `paseoRuntime` block on every use and creates the block exactly once, publishing through a private temporary and rename, refusing a symlink and leaving an existing block byte-identical. `paseo_runtime_settings.py` holds the dedicated listen address and the dashboard origins a fresh block is built from. `runtime_config.py` reads the block from that same file, treats an absent one as no host configured, and no longer resolves a harness skill root.

- The once-only establishment of the host block.
- The default listen address a fresh block carries.

[1] mcp/src/agents_remember/kernel/primitives/checkout_coordination.py — symbol resolve_checkout_location; mcp/src/agents_remember/kernel/primitives/checkout_coordination.py — symbol require_durable_write_target
[2] mcp/test_support/agents_remember_test_support/code_quality/layering.py — symbol load_contract; mcp/test_support/agents_remember_test_support/code_quality/layering.py — lines 151-154; mcp/test_support/agents_remember_test_support/code_quality/layering.py — lines 229-244
[3] mcp/src/agents_remember/models/structural/gates.py — lines 8-13
[4] mcp/src/agents_remember/kernel/primitives/paseo_runtime_settings.py — code file
[5] mcp/src/agents_remember/kernel/primitives/runtime_config.py — code file
[6] mcp/src/agents_remember/kernel/_agentic_settings_core.py — code file
[7] mcp/src/agents_remember/kernel/_agentic_settings_sections.py — code file
[8] mcp/src/agents_remember/kernel/primitives/paseo_authority.py — symbol load_authority_paseo_runtime
[9] mcp/src/agents_remember/kernel/primitives/host_environment.py — symbol host_environment; mcp/src/agents_remember/kernel/primitives/host_environment.py — lines 13-26
[10] mcp/src/agents_remember/kernel/primitives/paseo_runtime_settings.py — symbol parse_paseo_runtime_settings
[11] mcp/src/agents_remember/kernel/primitives/checkout_coordination.py — lines 19-87; mcp/src/agents_remember/kernel/primitives/checkout_coordination.py — lines 111-129
[12] mcp/src/agents_remember/kernel/primitives/gate_policy.py — lines 1-149; mcp/src/agents_remember/kernel/primitives/gate_vocab.py — lines 1-49
[13] mcp/src/agents_remember/kernel/primitives/command_capture.py — lines 1-49; mcp/src/agents_remember/kernel/primitives/drift_snapshot.py — lines 1-55; mcp/src/agents_remember/kernel/primitives/observer_paths.py — lines 1-50; mcp/src/agents_remember/kernel/primitives/identity.py — lines 1-135
[14] mcp/src/agents_remember/kernel/primitives/memory_cap.py — code file; mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py — code file; mcp/src/agents_remember/kernel/primitives/tool_reports.py — code file; mcp/src/agents_remember/kernel/primitives/version.py — code file
[15] mcp/src/agents_remember/kernel/primitives/paseo_host_contract.py — lines 1-12; mcp/src/agents_remember/kernel/primitives/paseo_node_paths.py — lines 1-71; mcp/src/agents_remember/kernel/primitives/user_settings_location.py — lines 1-46
[16] mcp/src/agents_remember/worktrees/integration/configured_contract_authority.py — lines 1-258
[17] mcp/src/agents_remember/cli/paseo_launch.py — lines 371-448; mcp/src/agents_remember/cli/paseo_launch.py — lines 547-597; mcp/src/agents_remember/cli/paseo_catalog.py — lines 156-346; mcp/src/agents_remember/cli/paseo_catalog.py — lines 460-516; mcp/src/agents_remember/cli/paseo_catalog.py — lines 566-604
[18] mcp/src/agents_remember/kernel/primitives/runtime_config.py — lines 417-441; mcp/src/agents_remember/worktrees/modules/quality/certification_records.py — lines 192-235; mcp/src/agents_remember/worktrees/modules/quality/gate.py — lines 248-364
[19] mcp/src/agents_remember/kernel/primitives/runtime_config.py — code file; mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py — code file
[20] mcp/src/agents_remember/kernel/primitives/paseo_authority.py — symbol establish_authority_paseo_runtime
[21] mcp/src/agents_remember/kernel/primitives/paseo_runtime_settings.py — symbol DEFAULT_HOST_LISTEN
[22] mcp/src/agents_remember/kernel/primitives/fresh_host.py — symbol fresh_host_block


- Checkout policy derives from the loaded package path, separates coordination rows from enclosure reports, and centrally refuses targets outside both exact leaf-local roots. [1]
- The layering contract loader establishes package ranks; the checker enforces their order on imports between distinct packages. [2]
- Structural gate models import the producer-owned gate vocabulary from kernel. [3]
- Paseo settings own strict nested runtime fields and the explicit unconfigured-runtime refusal. [4]
- Runtime configuration owns repository/profile parsing and reads shared host authority per use. [5]
- Agentic settings keep model, effort and service tier separate and resolve role settings precedence; this file also contains the disclosed upward model import. [6]

- Role settings parsers shape-check independent fields; quality-gate caps remain optional. [7]

- The authority reader reads the block of the MCP settings file on each use. [8]

- The session environment filter delegates to named-variable and prefix predicates. [9]
- The five-fact settings parse accepts an optional non-selecting version key. [10]
- Checkout modes, leaf-local roots and daemon-role narrowing define the execution boundary. [11]
- Gate policy is human-first and rejects non-human delegation of pinned kinds; gate vocabulary is kernel-owned. [12]
- Command capture, snapshot removal, observer paths and provider naming are shared primitive operations. [13]
- Remaining opt-in memory-cap planning, provider-degradation settings parsing, report retention/redaction and package/source version resolution keep their primitive owners; removed inbox backoff supplies no current scheduler. [14]
- Packaged host pins, Linux x86_64 Node selection and the user-settings location supply shared host primitives. [15]
- Configured-contract authority checks repository identities, memory mode and canonical task/enclosure paths at its mutation boundary. [16]
- Native launch construction and replay belong to the CLI launch owner. Catalog selection refuses unsupported model, effort and feature values when the corresponding fresh or saved offering is known; unanswered parts pass configured values through unchecked. [17]

- The kernel validates the optional certification-profile path; requested certification loads that profile, freezes exact admission and executes the selected quality plan through its own owner, independently of ordinary closeout. [18]
- Legacy gateDelegation migration warnings are deduplicated per authority-file-path/shadowed-state pair in the process, rather than on every re-resolution. The downstream direct-leaf authority, ignored directExecutionEnabled input, configured policy precedence and host/readiness boundaries are unchanged. The provider-degradation parser's actual source owner is provider_degradation_settings.py; retained primitives do not restore removed provider tools. [19]
- The once-only establishment of the host block. [20]
- The default listen address a fresh block carries. [21]
- The five-key host block a cold settings file receives. [22]

- Control vocabulary is a zero-internal-import owner of receipt/store/log names and bridge outcome bytes shared by execution, application, explainer and serving seams. [23]

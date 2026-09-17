# mcp/src/agents_remember/install/experiment.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/install/experiment.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T10:20:31+00:00|
| lastVerifiedCommitHash | `58bf4cde0f5271bbe420ad8e045d18b433f11253` |
| lastVerifiedCommitDate | 2026-09-17T12:31:16+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`install/experiment.py` is the **experimental instruction cutover's** own module: it owns the
selection, the delivery decision and the run record for the capsule experiment, and nothing else. It
does not compile a capsule, does not decide a launch's instruction mode for a seat (that is
`serving/launch_capsule.py`, which records `instructionMode` per launch), and does not touch a
user-level harness configuration. It decides *what an installation is*, and it is the only place
that decides it.

This module is **new in 260915-CAPS-L9** and is **uncommitted on `ar/260915-caps-l9-ar`**; no commit
records it yet, so the verification metadata above names the leaf's base commit and stays
closeout-owned.

## Code Commentary

### The selection — one option, per run, never persisted

`EXPERIMENT_ENV = "AR_EXPERIMENT"` and `ROLE_CAPSULES = "role-capsules"` are the whole vocabulary
(`EXPERIMENTS`). `resolve_experiment_selection` reads the value from the run's own input — the
install request's `experiment` field, then this process's environment — and never from a settings
file, a user configuration; it is never written back anywhere. Precedence is **explicit request,
then this process's environment, then "not selected"**, and `ExperimentSelection` records which one
won so an operator can tell a per-invocation choice from a server-wide one.

**An unrecognised id raises `ExperimentError` naming it** rather than falling through to "not
selected", because a typo that silently runs the unmodified path is exactly the silent switch this
behaviour forbids. `unselected_experiment()` is the explicit "this run selected nothing" value: the
default of `RuntimeInstallScope.selection` in `install/runtime.py`, so the type — not caller
discipline — carries the distinction.

**The experiment has no persistent global switch, so there is none to leave on at the master's exit.**
An ambient `AR_EXPERIMENT` on a long-lived MCP server would be the global shape the traceability
register's X5 warns about, which is why the primary production input is the registered
`runtime_install` tool's own `experiment` parameter and the environment variable is the documented
fallback for a short-lived CLI/developer route.

### The delivery decision — three answers, and `legacy` is unreachable for a selected run

`decide_instruction_delivery(selection, capsule_available=…, capsule_failure=…)` answers exactly one
of `capsule`, `legacy` or `refused`:

| Input | Answer | Why |
| --- | --- | --- |
| not selected | `legacy` | the existing installation, unchanged |
| selected and able | `capsule` | the capsule path |
| selected and unable | `refused`, naming the failure | **never** `legacy` |

A runtime failure therefore reports itself and preserves the selected mode; it never quietly runs the
old startup chain. The installer turns `refused` into an `ExperimentError` **before its first
write**.

### The five probes, and which of them block

`probe_capabilities` produces a `CapabilityReport` of `Capability` rows. Three block: the
`canonical-corpus-anchor` (the `sha256` of `skills/l-01-agent-lifecycles/composition-manifest.json`
in the install source), the packaged eve application (`package.json` + `agent/agent.ts` in the
mirror), and the pinned dependency/lockfile pair read against `PINNED_DEPENDENCIES`
(`eve 0.56.0`, `ai 7.0.102`, `@ai-sdk/openai-compatible 3.0.49`, `zod 4.6.5`) plus each package's
non-empty `integrity`. Two do not: the PATH `node` (`MINIMUM_NODE_MAJOR = 24`, remedy `AR_EVE_NODE`,
because the launch path's own resolver stays the authority) and `node_modules` presence (remedy: the
exact `dependency_install_command`). A blocking failure is a refusal, and a refusal writes nothing.

### The record, the install targets, and the way back

`ExperimentRunRecord` is the packet's example run record (`experiment`, `source`, `harness`,
`instructionSource`, `eveVersion`) **plus** the delivery mode, the reason, the selection source and
the capability detail that produced it. `build_run_record` builds exactly one record for one run and
returns it to the caller that ran the install. `InstallTargets` and `source_identity` supply the
`<branch>@<commit>` source form when the install source is a checkout.
`dependency_install_command(application_root)` renders the one-line
`cd <root> && PATH=<node 24 bin>:$PATH npm ci --no-audit --no-fund` that the record carries.

`WITHHELD_STARTUP_TARGETS` names the coordinator `AGENTS.md` targets the capsule mode does not
install — the paths the install reports as withheld so a reader can see exactly what changed.

`experiment_rollback_plan` renders the exact undo rows (an `UndoRow` list) and `rollback_payload`
serialises them for the install payload: the experiment's own machine-local artifacts (the installed
application root, an `AR_EVE_STATE_ROOT` epoch when one is named) and the one command that restores
the legacy startup chain — **re-run the installer with no experiment selected**. Its row for an
`install_skills` destination root is labelled `created-by-skills_install` with an undo command that
says so, because a runtime install does not populate that root. The adopt / revise / discard decision
itself belongs to the developer and the owning seat; this module only makes the route back executable
and checkable.

### Invariants And Boundaries

- **The selection is a run input.** Never a settings key; never written anywhere. The run record
  names which input supplied it (`request` / `environment` / `unselected`).
- **A selected run never degrades to `legacy`**, and a refusal precedes the first write.
- **An unknown experiment id is refused by name**, never treated as "not selected".
- **The installed coordinator `skills/` tree is the authored copy the coordination root carries —
  not the compiler's input.** Production compiles from `packaged_source_root()/runtime/skills`
  through `application/skill_resources`. The installed copy is never injected and never compiled.
- **This module adds no configuration framework and no shared mutable ledger.** One record per run,
  written beside the run, is the whole durable output.
- The pinned versions and the corpus anchor are read from the install source, never from the
  product's own output.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The per-run selection input, its vocabulary, and the resolved value that records which input won. | `EXPERIMENT_ENV`; `EXPERIMENTS`; `ExperimentSelection`; `resolve_experiment_selection` | mcp/src/agents_remember/install/experiment.py:59-61; mcp/src/agents_remember/install/experiment.py:65-66; mcp/src/agents_remember/install/experiment.py:127-146; mcp/src/agents_remember/install/experiment.py:147-189 |
| The explicit "selected nothing" value the installer's scope defaults to. | `unselected_experiment` | mcp/src/agents_remember/install/experiment.py:190-200 |
| The three-answer delivery decision in which a selected-but-unable run is refused rather than degraded. | `decide_instruction_delivery`; `InstructionDelivery` | mcp/src/agents_remember/install/experiment.py:212-241; mcp/src/agents_remember/install/experiment.py:201-211 |
| The startup targets a capsule-mode installation withholds. | `WITHHELD_STARTUP_TARGETS` | mcp/src/agents_remember/install/experiment.py:103-118 |
| The pinned versions, the corpus anchor, the minimum node major, and the one-line dependency install command. | `PINNED_DEPENDENCIES`; `CORPUS_ANCHOR`; `MINIMUM_NODE_MAJOR`; `dependency_install_command` | mcp/src/agents_remember/install/experiment.py:83-98; mcp/src/agents_remember/install/experiment.py:320-333; mcp/src/agents_remember/install/experiment.py:537-566 |
| The capability report and the blocking/non-blocking probes. | `probe_capabilities`; `CapabilityReport` | mcp/src/agents_remember/install/experiment.py:479-566; mcp/src/agents_remember/install/experiment.py:262-294 |
| One run record per run, in the packet's shape plus the mode, reason, selection source and capability detail. | `ExperimentRunRecord`; `build_run_record` | mcp/src/agents_remember/install/experiment.py:568-609; mcp/src/agents_remember/install/experiment.py:633-665 |
| The rendered undo rows for the unmodified configuration, and the labelled skills-install row. | `experiment_rollback_plan`; `rollback_payload` | mcp/src/agents_remember/install/experiment.py:713-769; mcp/src/agents_remember/install/experiment.py:770-773 |
| The installer consumes an already-resolved selection and refuses an unselected scope. | `resolve_experiment_install`; `install_experimental_runtime` | mcp/src/agents_remember/install/runtime.py:564-614; mcp/src/agents_remember/install/runtime.py:654-670 |
| The compiler resolves its corpus from the packaged tree, not the coordination root's copy. | `packaged_source_root` | mcp/src/agents_remember/application/skill_resources/operation.py:1-120 |

## Update History

- 2026-09-17T10:20:31+00:00 — 260915-CAPS-L9 curator: **created.** This candidate adds the module
  (773 lines, untracked on `ar/260915-caps-l9-ar`), so the card documents the selection
  (`AR_EXPERIMENT`/`role-capsules`, request-then-environment precedence, unknown id refused by
  name, `unselected_experiment()` as the scope default), the three-answer delivery decision with
  `legacy` unreachable for a selected run, the five probes and which three block, the run record and
  its `selectionSource`, `WITHHELD_STARTUP_TARGETS`, and the run-produced rollback plan — plus the
  no-persistent-switch statement this module exists to make true. Verification metadata names the
  leaf's base commit because the candidate is uncommitted; the real stamp is closeout-owned.

# mcp/tests/test_platform_edge_refusals.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_platform_edge_refusals.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:32+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Provider-lifecycle, seed, task-document and dispatch **refusals**.

Everything here sits behind something the test suite cannot have: a docker daemon, a second
coordination root with a live provider stack, a ready hosted session. The code under test is
the part that decides *not* to proceed — the settings that disqualify a seed, the compose
command that came back non-zero, the edit that names an operation but carries no object to
apply. Those decisions are pure given their inputs, so the docker and compose seams are
doubled and the decision itself is asserted.

## What Is Being Asserted

The **payload or exception a caller acts on**: a benign skip that reports `ok` (nothing to
seed is not a failure), a hard failure that carries the failing command, an error message
naming the field the caller left out. Not "it ran".

## Classes

| Class | Refusal or decision |
| --- | --- |
| `CgcBackendPortsTests` | Which host ports the CGC backend reports, and where each number comes from. |
| `CgcBackendStartContextTests` / `CgcBackendStateTests` | Backend start context and state. |
| `ProviderComposeFailureTests` | A failing `docker compose up` is **reported, never raised**. |
| `GrepaiBackendStateTests` | Grepai backend state. |
| `GrepaiMismatchedContainerTests` | A container bound to the wrong data directory is removed; a failed removal is reported rather than silently treated as success. |
| `GrepaiWatcherStartPreconditionTests` | The watcher's image build must succeed before compose is asked to start it. |
| `GrepaiComposeFailureTests` | Each grepai service reports a failed `compose up` under its own action name. All three take the same shape, and the shape is the point: the caller is told which service failed and handed the failing command, so a partially-up stack reads off one payload rather than a traceback. |
| `SeedRefusalTests` | A seed clone that cannot be described is skipped **benignly**, naming the reason. |
| `WorktreeGrepaiSettingsTests` | A worktree's isolated grepai settings must actually describe the provider. |
| `ProviderWatcherStopTests` | The runtime install stops watchers before replacing their runtime tree. |
| `TaskDocEditRequirementTests` | Each edit operation names the object it needs when the caller omits it. |
| `DispatchTargetTests` | A dispatch-brief refuses before the durable inbox row exists. |
| `WorkspaceGateResponseWaitTests` | A gate raised with no lifecycle and no agent mailbox has no inbox to poll. |
| `BenchmarkRunCaseTests` | A real (non-preview) benchmark run picks its worker count and reports failures. |
| `RuntimeInstallFailureTests` | What a runtime install does when the copy fails, and where it installs from. |

## Invariants And Boundaries

- No docker daemon, no second coordination root, no hosted session is ever required.
- "Nothing to do" is `ok`, not a failure; a real failure carries the command that failed.
- Compose failures are payloads, not exceptions — the caller must be able to read which
  service failed from one result.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Provider lifecycle, backends and watchers. | [providers/](agents-remember/mcp/src/agents_remember/providers/) |
| Task-document edit operations and their required objects. | [task_document.py](agents-remember/mcp/src/agents_remember/task_document.py) |
| The sibling long-tail refusal collection. | [test_platform_long_tail.py](agents-remember/mcp/tests/test_platform_long_tail.py) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  platform-refusal suite. Verification metadata is pinned to the leaf's reformat commit
  until closeout stamps the code commit.

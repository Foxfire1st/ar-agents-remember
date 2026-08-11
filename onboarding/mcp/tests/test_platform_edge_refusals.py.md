# mcp/tests/test_platform_edge_refusals.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_platform_edge_refusals.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:32+02:00                     |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Provider lifecycle, backends and watchers. | "def cgc_backend_start("; "def cgc_watcher_running("; "def watchers_run(" | mcp/src/agents_remember/providers/cgc/lifecycle/backend.py:390-390; mcp/src/agents_remember/providers/cgc/lifecycle/runner.py:89-89; mcp/src/agents_remember/providers/lifecycle/watchers.py:186-186 |
| Task-document edit operations and their required objects. | "def task_doc_tool("; "class TaskEnclosureRef(_Doc):" | mcp/src/agents_remember/application/task_doc_tools.py:137-137; mcp/src/agents_remember/tasks/document.py:107-107 |
| The sibling long-tail refusal collection. | "class RequestedHarnessTests(unittest.TestCase):"; "class OpenTerminalRefusalTests(unittest.TestCase):" | mcp/tests/test_platform_long_tail.py:380-380; mcp/tests/test_platform_long_tail.py:414-414 |

## Update History

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_platform_edge_refusals.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: regenerated the task-doc row
  ranges via the scoped fixer; exact non-fixing check returns zero findings.

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 3 citation rows with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  platform-refusal suite. Verification metadata is pinned to the leaf's reformat commit
  until closeout stamps the code commit.

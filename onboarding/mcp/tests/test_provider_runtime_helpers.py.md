# mcp/tests/test_provider_runtime_helpers.py

| Field                  | Value                                       |
| ---------------------- | ------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/tests/test_provider_runtime_helpers.py` |
| doc_type               | `file-level-onboarding`                     |
| lastUpdated            | 2026-07-31T15:32+02:00                      |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`  |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                               |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural tests for provider runtime helpers **that no test previously reached**. Every
target is either a thin adapter over docker/compose or a settings writer, so each test
drives the real function and asserts the value it returns, the file it writes, or the error
it raises.

## Method

The subprocess seam these helpers already use — `run_command` and `docker_command` — is
replaced by a fake, so **no docker daemon is ever contacted** and no subprocess or file
handle is left open. `FakeClock` stands in for the `time` module: sleeping is what advances
the clock, which is what makes the retry-cadence assertions exact rather than timing-based.

## What Each Class Owns

| Class | Helper under test |
| --- | --- |
| `RenderTextTests` | `provider_setup.render_text` — the human-readable summary of a setup run: explicit state beats derived `ok`, an unwritten summary is omitted, a non-dict summary is ignored rather than crashing, missing fields fall back to placeholders, `reason` beats `stage` in the detail suffix. |
| `DockerRepoDigestTests` | `docker_runtime.docker_repo_digest` — the pinned digest of a local image. The exact inspect command is asserted; a missing image, unparseable stdout, a locally built image with no digests, and non-list JSON all return `None`; a non-string entry is coerced to text. |
| `DockerInspectNetworkTests` | `compose_runtime.docker_inspect_network` — inspect a compose network or admit it is not there. The result feeds the ownership check that guards removal, which is asserted too. |
| `DockerWaitForOllamaTests` | `embedder.docker_wait_for_ollama` — poll `ollama list` until the model store answers. Healthy returns without sleeping; transient failure retries after a two-second sleep; persistent failure raises with the last stderr (or stdout when stderr is empty); a zero timeout never polls. |
| `OllamaModelPresentTests` | `embedder.ollama_model_present` — exact tag, untagged request matching the `latest` alias, same family with a different tag, unrelated models, header-only output, empty output, blank lines. |
| `CgcRefreshPreflightTests` | `refresh.cgc_refresh_preflight` — the gate deciding whether an index run may start: dry run never touches backend or doctor; a failed backend short-circuits before the doctor; a failed doctor blocks but keeps the backend result; manual override skips the managed backend entirely. |
| `CgcRefreshTests` | `refresh.cgc_refresh` — one repo's forced reindex end to end minus docker: fan-out when settings name no repo id, dry run writes no state, a successful index records the run, indexing runs **without** a command timeout, a failed index still records its returncode, a failed doctor aborts before compose and leaves no state. |
| `CgcApplySettingsTests` | `core.cgc_apply_settings` — materialize every configured repo's runtime layout, record the workspace backend once, prune a runtime root settings no longer configure, and report a removal under dry run without deleting anything. |
| `WriteIsolatedCgcSettingsTests` | `cgc_setup.write_isolated_cgc_settings` — point a worktree at its own settings: source settings are not mutated, explicit path/container name honoured, dry run writes nothing, no isolated root clears a stale pointer, settings without a CGC provider produce no file, an isolated root without a target repo is rejected. |

## Invariants And Boundaries

- No container runtime, no network. The only doubles are the two command seams and the
  clock.
- Dry-run arms assert the *absence* of a side effect (no file written, no directory
  removed), not merely a returned plan.
- Failures are reported as payloads carrying the failing command, not raised — the caller
  reads which step failed off one result.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The provider runtime helpers under test (setup rendering, docker/compose adapters, embedder polling, CGC refresh/apply/isolation). | [providers/](agents-remember/mcp/src/agents_remember/providers/) |
| The lifecycle-level provider suites these helpers sit beneath. | [test_provider_lifecycle.py](agents-remember/mcp/tests/test_provider_lifecycle.py), [test_provider_setup.py](agents-remember/mcp/tests/test_provider_setup.py) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  provider-runtime helper suite. Verification metadata is pinned to the leaf's reformat
  commit until closeout stamps the code commit.

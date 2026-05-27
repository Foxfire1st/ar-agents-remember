# mcp/src/agents_remember/providers/cgc/lifecycle/installation.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/installation.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `f20f75e3e3c6da0c56a6ccfdedfa9d859d7329b7` |
| lastVerifiedCommitDate | 2026-05-27T18:11:35+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`installation.py` owns CodeGraphContext install, status, patch, and doctor
operations.

## Code Commentary

### Logic

The module installs the CGC Docker runner image, cleans old source artifacts,
reports Docker-image patch status, initializes runtime layout state, and runs
doctor checks through the runner image. Install-all also coordinates backend
installation and per-root install results from settings. The public `patch`
action is now a Docker-image no-op report because managed patches are baked
into the runner image during build.

### Invariants And Boundaries

- Patches are owned by the Docker runner image build; status should report the
  Docker-image patch mode rather than inspecting host site-packages.
- Runtime source artifacts under the code repository are cleanup targets; active
  provider runtime belongs under coordinator provider roots.
- Process start/stop and bounded CGC commands belong in sibling lifecycle
  modules and must use Docker runner commands.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC layout and backend settings come from the CGC core module. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/core.py) |
| CGC backend install/start behavior is delegated to the backend module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| Docker runner image build and command helpers live in the runner module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |

## Update History

- 2026-05-26T12:51+02:00: Updated after CGC install/status/doctor switched from host venvs to the Docker runner image.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from CGC install, status, patch, and doctor logic extracted out of provider lifecycle.

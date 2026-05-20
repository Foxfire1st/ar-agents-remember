# codegraphcontext.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/providers/requirements/codegraphcontext.txt` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-20T20:01+02:00                     |
| lastVerifiedCommitHash | `e4ae4955d888d3ce58b55b5ca99d20039cbcb214` |
| lastVerifiedCommitDate | 2026-05-20T20:01:26+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

This requirements file pins the CodeGraphContext provider dependency used by Agents Remember's provider lifecycle tooling.

## Code Commentary

### Logic

The file pins `codegraphcontext==0.4.10`. Runtime installation copies this package default into `ar-coordination/providers/requirements/codegraphcontext.txt`; the provider lifecycle manager installs or repairs the shared CGC provider venv from that installed requirements file.

### Conventions

Provider dependency pins live under `runtime/providers/requirements/` in the source checkout and install into `ar-coordination/providers/requirements/`. Live provider virtual environments live separately under `ar-coordination/providers/_venvs/` and are not package-owned source files.

### Invariants And Boundaries

Provider versions should stay pinned before patching so version-specific patch checks are meaningful. Do not point this file at user-global environments or unpinned package ranges.

## Docs References

No external documentation is needed for the pin itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The provider requirements file pins CodeGraphContext to version 0.4.10. | L1 | [codegraphcontext.txt](agents-remember-md/runtime/providers/requirements/codegraphcontext.txt) |
| The installer requires and copies `runtime/providers` into the coordination root. | L198-L208; L254-L258 | [installer](agents-remember-md/installer/install-runtime.py) |
| The shared provider helper writes this same pin when creating a missing CGC requirements file. | L13-L15; L162-L163 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |

## Cross-Repo References

No sibling repository evidence is needed for this provider pin.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-20T19:11+02:00: Created onboarding for the pinned CodeGraphContext provider requirement.

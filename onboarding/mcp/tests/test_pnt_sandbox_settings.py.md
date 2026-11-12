# mcp/tests/test_pnt_sandbox_settings.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Runs the PNT sandbox's own settings owner, which prepares and checks one installation's settings through the product rather than through a retired starter renderer (MIK-R196 rule 9).

## Code Commentary

The fixture builds a workspace with one repository and the settings file a template leaves there, and reaches the behaviour through `scripts/pnt_sandbox/settings_expectation.py`. The cases require prepared settings to differ from the template only in the recorded coordination root and dashboard port; an absent user settings file to stay absent while the sandbox's own file holds the host block; an existing shared host file to be untouched and recorded; and a repository outside the workspace to be refused. They further require existing native authority values to be preserved, an invalid existing authority to be refused without being replaced, an unapproved settings or host difference to be refused, and the old user settings location to be refused.

## Invariants And Boundaries

A sandbox is one ordinary installation: it writes its own settings file and treats the developer's user settings file as an input it never writes or creates. Nothing here imports the retired renderer, so the behaviour is the product's own.

## Evidence

### Repo-Internal References

- Prepared settings differ from the template only in the recorded coordination root and dashboard port. [1]

- The developer's user settings file is never written or created, and an invalid existing authority is refused rather than replaced. [2]

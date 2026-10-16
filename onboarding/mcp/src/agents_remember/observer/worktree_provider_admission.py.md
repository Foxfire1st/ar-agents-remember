# mcp/src/agents_remember/observer/worktree_provider_admission.py

## Governing Overview

[observer overview](overview.md)

## Purpose

Contract-derived provider/setup admission is stricter than active-enclosure membership; neither determines authored task stage.

Session-log phase demotion and series-retention clocks are removed.

## Code Commentary

### Logic

`admitted_worktree_groups` requires worktreeGroup, cleanup outside completed/abandoned/reopened, and neither completed closeout nor integration. `active_enclosure_worktree_groups` only requires the group and non-inactive cleanup; close/integration work can remain visible without paging providers. Both return basenames from supplied EnclosureNode facts, with no I/O, session fold or retention clock.

## Evidence

### Docs References

No relevant external documentation was found after checking the in-repo design docs.
This file implements repository-local worktree lifecycle admission policy.

No relevant external documentation found after checking in-repo design docs for active-enclosure admission.

### Repo-Internal References

- Provider admission returns nonempty worktreeGroup basenames from durable enclosures whose cleanup is not completed, abandoned or reopened and whose closeoutStatus and integrationStatus are both not completed. Admission has no lifecycle-log input or missing-log exception. [1]

- Active-enclosure membership returns nonempty worktreeGroup basenames from enclosures whose cleanup is not completed, abandoned or reopened. Unlike provider admission it does not additionally filter completed closeout/integration; lifecycle logs are not inputs. [3]

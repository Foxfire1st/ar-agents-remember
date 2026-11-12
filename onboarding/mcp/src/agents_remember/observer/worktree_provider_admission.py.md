# mcp/src/agents_remember/observer/worktree_provider_admission.py

## Governing Overview

[observer overview](overview.md)

## Purpose

Active-enclosure membership derives from durable worktree facts and does not determine authored task stage. The former provider/setup admission helper is removed.

Session-log phase demotion and series-retention clocks are removed.

## Code Commentary

### Logic

The retained `active_enclosure_worktree_groups` requires a nonempty worktreeGroup and cleanup outside completed/abandoned/reopened. It returns basenames from supplied EnclosureNode facts, with no I/O, session fold or retention clock. There is no current `admitted_worktree_groups` function or provider-paging policy in this module.

## Evidence

### Docs References

No relevant external documentation was found after checking the in-repo design docs.
This file implements repository-local worktree lifecycle admission policy.

No relevant external documentation found after checking in-repo design docs for active-enclosure admission.

### Repo-Internal References

- The complete current module only imports Path and EnclosureNode, declares the inactive-cleanup set and computes active-enclosure membership from supplied facts. It performs no I/O, session fold, retention-clock computation or provider-paging action. [4]
- The earlier current-callable provider-admission account is withdrawn: the complete current module has no admitted_worktree_groups function. Its only membership helper is active_enclosure_worktree_groups. [1]
- Active-enclosure membership returns nonempty worktreeGroup basenames from enclosures whose cleanup is not completed, abandoned or reopened. It adds no closeout/integration filter and reads no lifecycle log. [3]

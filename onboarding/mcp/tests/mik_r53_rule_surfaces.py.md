# mcp/tests/mik_r53_rule_surfaces.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Names the shipped skill workflow that states the ten merge and debt rules with their decision (MIK-R53), so the case reads the surface once instead of spelling out a path.

## Code Commentary

`QUALITY_CONTROL_WORKFLOW` resolves under the repository root to `skills/c-05-create-or-update-onboarding-files/workflows/memory-quality-control.md`, and `quality_control_workflow_text` returns it as UTF-8. The module's docstring records the other surface: the command help. The curated rule listing moved out of the retired c-02 skill into this c-05 workflow (MIK-R196 rule 6), which is why the path is here and not in the test body.

## Invariants And Boundaries

Reading only. The path is the shipped skill tree, not the packaged runtime copy, and an absent file raises rather than answering empty.

## Evidence

### Repo-Internal References

- The shipped workflow that lists the ten rules is named once, under the c-05 skill tree. [1]

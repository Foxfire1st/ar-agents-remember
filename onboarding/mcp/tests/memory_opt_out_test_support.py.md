# mcp/tests/memory_opt_out_test_support.py

## Governing Overview

[Onboarding overview](overview.md)

## Purpose

The one shared home for the MIK-R50 opt-out refusal worlds. The start-refusal module (rules 1-2) and the route-refusal module (rules 3-4) both build scratch coordinations and assert refusals through the helpers defined here, so every definition lives exactly once.

## Code Commentary

One scratch coordination builder covers the five memory shapes a refusal must distinguish: converted (layout marker committed on a branch), plain (a real repository with no converted knowledge), broken (a `.git` entry Git cannot answer), a plain directory, and no memory root at all. The shared assertion pins the refusal contract every case checks: the opt-out status, `requested` naming the removed mode, `supported` naming only external, the operation named in the summary, and never the removed internal-mode text nor a general invalid-mode text.

The on-disk legacy leaf helper writes a genuine external contract then rewrites its cells to the removed mode (or an unknown token), including stripping the memory section's pins so an unknown cell degrades to disabled only where the section it governs names no worktree and no ledger, and asserts the read-back mode. The live legacy leaf helper builds a genuine live enclosure — real code and memory worktrees descending from the parent series branch, both leaf and parent series carrying the removed mode, task documents filed, locator published against the final legacy bytes — shared by the attach route case and the no-mode start attach case.

## Evidence

- Shared-once contract between the two split refusal modules [1]
- Status, repo, and removal-reason constants [2]
- Scratch coordination with the five memory shapes [3]
- Common refusal assertions incl. the never-borrowed texts [4]
- On-disk legacy contract incl. unknown-cell degradation [5]
- Genuine live legacy leaf with disabled leaf and series [6]

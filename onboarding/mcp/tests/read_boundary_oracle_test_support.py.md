# mcp/tests/read_boundary_oracle_test_support.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The rule-6 read-boundary oracle: snapshots, findings and the classifying entry point.** Split whole from `test_knowledge_read_boundary.py`; every case, assertion and negative control is preserved and only the address changed. Tests import the names they touch; nothing here runs product code.

## Code Commentary

`_snapshot` inventories every file and directory under each root, plus per-checkout refs/HEAD, external admin dirs, and borrowed object stores through alternates-pointer chains with cycle protection (`_snapshot_alternates`, `_alternate_targets`; pointers are followed before the containment skip so an inside-root chain to an outside lender is inventoried). `_classify` is the single entry point: `_git_findings` plus `_file_findings`. `_bare_repo` builds hand-made world states for the controls.

## Evidence

- The oracle snapshots files, refs, admin dirs and alternates chains [1]
- Alternates pointers are followed before the containment skip [2]
- Pointer discovery accepts any store directory name [3]
- Classification is one entry point over Git and file findings [4]
- Hand-built world states for the controls [5]

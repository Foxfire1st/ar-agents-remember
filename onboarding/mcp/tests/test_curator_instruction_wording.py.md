# mcp/tests/test_curator_instruction_wording.py

## Governing Overview

[tests route overview](overview.md)

## Current source account — the moved Curator wording pins and the admitted writer

The module was split out of `test_role_instruction_wording.py` so that module stays under the size rail; it reads the same canonical `skills/l-01-agent-lifecycles` tree and the same built parser, and decides the same questions there. `test_current_coordination_and_curator_rules` matches each required clause against its source file after whitespace folding, and its Curator block fixes the authoring routes: `knowledge-ingest`, then the mounted `knowledge_write` "which runs the same writer with the same arguments", then "No other route writes knowledge", with `--commit` written as `commit: true`. The git-comparison scope of the skill tree is asserted once at the end of that case rather than per clause.

The writer-admission case pins the `{{detail:reference/curator-writer-details.md}}` include in the role text, the `knowledge-ingest` invocation and `--authorization-ref <ref> --commit --json` in the detail file, the operation's "source-bound command" wording and its refusal to bypass a refusal through another installation, and the parser accepting that invocation while exiting 2 with `unrecognized arguments` for `--baseline`, `--publish` and `--publish-to`. The remaining cases keep the coordination-default manifest descriptions and the rule that `role_start` is granted to starter roles only and no tool outside `PUBLIC_TOOLS` is listed.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- The Curator's role text names both authoring routes, says no other route writes knowledge, and writes `--commit` as `commit: true` [1]
- The writer admission is pinned in the role, detail and operation texts, and the parser refuses the removed options with exit 2 [2]

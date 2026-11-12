# mcp/tests/test_mik_r53_judgment_rows.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

This module protects the membership and decision/facet judgment contracts added by MIK-R53 Part B, their writer and reader paths, and regressions found in that implementation. It uses synthetic knowledge fixtures, temporary Git repositories and the real application functions. Source assertions are not evidence that this Curator ran the tests or changed the inherited membership-condition records.

## Code Commentary

### Logic

The membership group validates `no_family` rows, detects new and newly unlisted live invariants, excludes existing family members and old orphans, checks revision currency, and exercises the writer's admission/refusal cases. The record group validates disposition/effect combinations and exact JSON/Markdown change detection.

Later cases use real directory/Git snapshots for prose-only changes, preserve current-owner/open-file boundaries on the reconsideration exemption, normalize literal/bare/handoff aliases to stable row identities, reject malformed `considered` inputs, and preserve foreign evidence through later updates and reason-only rewrites. Reader fixtures check both the invariant's membership view and its timeline. The five writer-report cases construct actual refusing states, check the writer's reported reason, then exercise the commit refusal rather than treating a fabricated report as proof of the whole path.

### Invariants And Boundaries

- Newly retired status outranks revision growth in the record disposition contract.
- A closed attempt's raise must not exempt a later open attempt; foreign raises and additional prose/JSON changes likewise do not exempt.
- An unknown alias or malformed family list must refuse without writing the leaf history.
- Foreign record origin remains unchanged even when evidence is added to a later owner's row; a later reason rewrite must not discard retained evidence, including a value ending in the literal evidence marker.
- The reader-world repository and synthetic record IDs are test fixtures, not production memory or lifecycle acceptance. The source header's earlier rule-7 wording does not supersede the packet's later L54 deferral.

## Evidence

### Repo-Internal References

- Membership detection and revision-bound satisfaction distinguish new or newly unlisted invariants from inherited old orphans. [1]
- Record judgments validate effects and enforce changed/retired/no_impact according to revision and status. [2]
- Real Git/directory fixtures protect Markdown-only changes and the owner/open-file status-mark exemption. [3]
- Alias dispatch and strict considered-list parsing refuse invalid inputs without fabricated history. [4]
- Membership is visible in the invariant reader and history timeline. [5]
- Closed-attempt, alias and evidence-marker regressions exercise stable row IDs and preserved foreign evidence/origin. [6]
- Each of the five writer-reported rules is checked on a real writer run and at the commit route. [7]

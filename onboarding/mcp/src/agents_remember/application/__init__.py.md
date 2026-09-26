# mcp/src/agents_remember/application/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-21T22:40:00+02:00 |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`__init__.py` marks `agents_remember.application` as an importable package.

## Code Commentary

The file currently contains no exported application-layer facade. Public MCP payload
builders import application entry point functions directly from their domain modules such as
`provider_tools.py`, `worktree_tools.py`, `memory_tools.py`, and
`coordination_tools.py`.

## Invariants And Boundaries

- Keep this package initializer empty unless there is a concrete import-surface
  requirement.
- Do not use it to recreate the old `skill_tools.py` mass facade.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The overview hot path summarizes guarded commit-message and forwarding boundaries. | "## Hot Path Summary" | onboarding/mcp/src/agents_remember/application/overview.md:1088-1090 |
| Public payload builders import application entry points from their owning modules. | "from .benchmark import codex_benchmark_prepare_payload"; "from agents_remember.application.benchmark_tools import (" | mcp/src/agents_remember/mcp/tools/__init__.py:12-13; mcp/src/agents_remember/mcp/tools/benchmark.py:7-16 |

## Update History
- 2026-09-26T21:37:21Z — Reconciled the reference with the current source owner while retaining its scope and history.
- 2026-09-22T09:20:00+02:00 — 260921-ICR-L4 curator (gate repair pass on the merged line): **the duplicated Hot Path row is one row again, re-pointed at the heading.** The union had carried the claim twice (both citing `:669-669`, which holds neither the heading nor the layout paragraph after this leaf's and siblings' overview edits); the surviving row cites `:701-703`, the heading plus the paragraph it introduces. Wording unchanged; no stamp advanced.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the one enforced citation row was re-read and re-pointed at the heading the claim is about.** The claim — "The route overview documents the split application package layout" — names the anchor `"## Hot Path Summary"`, and its cited `application/overview.md:337-337` held neither the heading nor anything about the split layout. The heading the claim is about is the section heading of the route overview's own body, which the candidate carried at **612** when this row was written (`553` earlier in the same session — that document is being edited concurrently by other seats, and this range names the heading as read at this pass); the row now cites `612-614`, the heading plus the paragraph it introduces. The other occurrences of that text in the file are inside Update-History entries *describing* a past re-point, which is not what this claim is about — so the range names the heading, not a mention of it. Claim wording, the second row, both anchors and the two verification rows are unchanged; this is a citation-only repair and `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are deliberately **not** advanced, because nothing in this leaf is committed and the governed closeout owns the real stamp.
- 2026-09-21T15:14+02:00 — 260921-ICR-L19 curator (uncommitted change set on `ar/260921-icr-l19`, code base `0fca5c69`): re-derived the route-overview citation against the candidate rather than shifting it. The claim ("The route overview documents the split application package layout") and its literal anchor are unchanged; the `## Hot Path Summary` heading now stands at `overview.md:337`, so the cell reads `337-337` (it read `275-282`). Earlier leaves inserted sections above that heading, which is what moved it. No claim wording changed, no anchor was dropped, and no verification stamp was advanced — this card's source (`application/__init__.py`) is untouched by this leaf and its own metadata is retained as recorded.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "## Hot Path Summary" repointed to onboarding/mcp/src/agents_remember/application/overview.md:268-268. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "## Hot Path Summary" repointed to onboarding/mcp/src/agents_remember/application/overview.md:150-150. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T12:29:52+00:00: Generated citation repair: "## Hot Path Summary" repointed to onboarding/mcp/src/agents_remember/application/overview.md:128-128. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "## Hot Path Summary" repointed to onboarding/mcp/src/agents_remember/application/overview.md:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.
- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 curator: re-anchored the application-overview citation ("## Hot Path Summary" 48 → 52) after the application overview body gained the ambient-dispatch paragraph; no content impact. Verification metadata remains closeout-owned.

- 2026-08-13T07:53+02:00 — 260731-EFA-L23 super-line reconciliation: re-reviewed this card and its Repo-Internal citation targets after absorbing the super-integration memory line. Retained claims remain supported by the current tree. Verification is pinned to real code HEAD `1580f92715ff93c988f9a15439ad9bec60ef4c5d`; the new-line memory mapping remains closeout-owned.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 2 citation rows to plain
  sources; the route-overview row cites the memory-repo overview with a literal anchor ("Hot Path
  Summary") because `#`-heading anchors do not resolve against memory-repo targets. Zero findings
  remain.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-06T12:28+02:00: Corrected the public payload-builder reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-28T19:52+02:00: Created when the controllers route overview made the package initializer part of the explicit route coverage.

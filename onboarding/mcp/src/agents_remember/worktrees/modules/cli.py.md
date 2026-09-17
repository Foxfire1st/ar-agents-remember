# mcp/src/agents_remember/worktrees/modules/cli.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/cli.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

## Purpose

Owns command-line parsing and JSON print adapters for the worktree lifecycle.

## Code Commentary

### Logic

Closeout parsing accepts code and memory commit-message flags only; integrate accepts strategy and approval without a ledger-message flag. `command_closeout` normalizes those two messages before constructing the domain input. Synchronous apply still obeys the journal-required boundary.

The module builds the `start`, `attach`, `status`, `closeout`, `integrate`,
and `cleanup` subcommands (the `direct-closeout` subcommand was removed with
the direct-closeout surface, issue #62). Each command function
converts the raw `argparse.Namespace` into the typed `WorktreeArgs` DTO via
`WorktreeArgs.from_namespace(args)` before calling the result-returning service
functions, then prints payload JSON — keeping CLI transport concerns out of the
lifecycle operation modules.

260712-PTS-L1 adds the `heal-leaf-ids` subcommand (`--coordination-root`,
required; `--dry-run`) — the deliberate invocation seam for
`worktree_contract.heal_contract_leaf_ids`. `command_heal_leaf_ids` prints the
heal report as indented JSON and, unlike the lifecycle commands, deliberately
skips the `WorktreeArgs` DTO: healing legacy stem-shaped leaf ids is a one-shot
migration sweep, never a per-read side effect — run it once against a
coordination root (or at daemon startup) instead of relying on `load_contract`
to normalize, which it no longer does.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

The ledger is a computed consumer cache; it cannot supply an additional Git output or lifecycle prerequisite.

### Todos

None recorded for the ledger-retirement boundary.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `command_closeout` normalizes code/memory messages before the journal-bound closeout adapter. | `command_closeout` | mcp/src/agents_remember/worktrees/modules/cli.py:55-56 |
| `build_parser` exposes closeout/integration options without ledger-message flags. | `build_parser` | mcp/src/agents_remember/worktrees/modules/cli.py:130-131 |

| Finding | Anchor | Source |
| --- | --- | --- |
| The CLI module exposes the public main entry point for `python -m` execution. (`main`) | `main` | mcp/src/agents_remember/worktrees/modules/cli.py:189-190 |
| MCP startup enters the result-returning application owner without CLI parsing. (`worktree_start_tool`) | `worktree_start_tool` | mcp/src/agents_remember/application/worktree_tools.py:103-109 |
| MCP attachment enters the result-returning application owner without CLI parsing. (`worktree_attach_tool`) | `worktree_attach_tool` | mcp/src/agents_remember/application/worktree_tools.py:265-270 |
| MCP status enters the result-returning application owner without CLI parsing. (`worktree_status_tool`) | `worktree_status_tool` | mcp/src/agents_remember/application/worktree_tools.py:277-282 |
| Start or observe the exact contract-addressed integration operation. (`worktree_integrate_tool`) | `worktree_integrate_tool` | mcp/src/agents_remember/application/worktree_tools.py:371-377 |
| MCP cleanup enters the result-returning application owner without CLI parsing. (`worktree_cleanup_tool`) | `worktree_cleanup_tool` | mcp/src/agents_remember/application/worktree_tools.py:798-804 |
| The heal implementation this seam invokes (walk once, cheap-skip canonical ids, rewrite + report) lives in the contract module. (`heal_contract_leaf_ids`) | `heal_contract_leaf_ids` | mcp/src/agents_remember/worktrees/worktree_contract.py:487-488 |

## Series-Contract Notes

The common CLI contract-path help now names `series-contract.md`, aligning command-line usage with the root/leaf contract schema.

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## 260821-CLIVE-L1 Legacy CLI Boundary

The synchronous CLI closeout apply path now fails closed with `JOURNALED_CLOSEOUT_REQUIRED`. Dry-run loads the contract and uses the canonical normalizer, returning typed validation behavior without mutation. CLI flags are syntactically optional because enabledness is derived at runtime; enabled messages remain mandatory and explicit. The CLI does not provide a compatibility bypass around the lifecycle journal.

## 260821-CLIVE-L2 Current Contract

The current source seams include `parse_json_stdout`, `command_status`, `command_attach`. This module remains a public execution adapter over closed admission and exact mutation-owner reread; it does not duplicate reader exception families or lifecycle authority.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `parse_json_stdout`, `command_status`, `command_attach` at this ownership boundary. | `parse_json_stdout` | mcp/src/agents_remember/worktrees/modules/cli.py:27-28 |

## Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Governing Overview

[Governing route overview](overview.md)

## Update History

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=f5525c0b231cc8a1b471bd457621d8a2566f782f6d024966178ed01dfafdf642. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.

- 2026-09-13T17:20:55+00:00: Generated citation repair: "def worktree_cleanup_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:805-805. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "def worktree_cleanup_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:773-773. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:06:15+00:00: Generated citation repair: "def worktree_cleanup_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:769-769. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `command_attach`, `command_status`, `parse_json_stdout` repointed to mcp/src/agents_remember/worktrees/modules/cli.py:27-34, mcp/src/agents_remember/worktrees/modules/cli.py:37-40, mcp/src/agents_remember/worktrees/modules/cli.py:43-46. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def worktree_start_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:103-103. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def worktree_attach_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def worktree_status_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:277-277. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def worktree_integrate_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:371-371. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def worktree_cleanup_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:730-730. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "def worktree_start_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:111-111. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "def worktree_attach_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:273-273. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "def worktree_status_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:285-285. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "def worktree_integrate_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:461-461. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "def worktree_cleanup_tool" repointed to mcp/src/agents_remember/application/worktree_tools.py:811-811. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-08T16:45:00+02:00 — CCR-L38 final preparation repair: repointed frozen-source citations after the final contract diagnostic; no behavioral prose change, no verification or acceptance claim.

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout corrected-call model package relocation; CLI normalization and command routing are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-04T12:19:51+02:00 — 260731-EFA-L6 S18-B01 curator: reconciled the bounded worker ledger; source-clear citations were repaired, split, rewritten, or deleted as applicable, then the exact scoped fixer/check passed.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1: added the `heal-leaf-ids` subcommand and
  `command_heal_leaf_ids` (`--coordination-root`, `--dry-run`; prints the heal report JSON) — the
  explicit, one-shot invocation seam for `heal_contract_leaf_ids` now that contract loads are walk-free
  and never normalize. The command intentionally bypasses `WorktreeArgs` because the heal is a migration
  sweep, not a lifecycle operation. Verification metadata pinned until closeout stamps the 260712-PTS-L1
  commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: common CLI help now names `series-contract.md` for explicit contract paths, matching the retired `contract.md` schema. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-11T06:47+02:00 — Removed the `direct-closeout` subcommand, `command_direct_closeout`, and the `direct_closeout_result` import (issue #62 worktree-only closeout).
- 2026-05-31T12:50+02:00 — Command functions now wrap `args` in `WorktreeArgs.from_namespace(args)` (new import from `worktrees.modules.args`) before calling each result function; updated Code Commentary to name the `argparse.Namespace`-to-`WorktreeArgs` DTO conversion (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.

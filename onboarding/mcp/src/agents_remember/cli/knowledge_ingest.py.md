# mcp/src/agents_remember/cli/knowledge_ingest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_ingest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T17:30+02:00 |
| lastVerifiedCommitHash | `47570cd827428c171613c8cb01e01f0b1cb26f73` |
| lastVerifiedCommitDate | 2026-09-20T01:58:41+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

CLI adapter: ingest an orchestrator's curator hand-off list into a leaf's candidate — the knowledge
write plane's first production caller.

## Code Commentary

### Logic

Module-level surface:

- `add_arguments` (function, lines 50-87) — declares the operation's inputs: `--contract` (**required**),
  `--list`, `--candidate-directory`, `--authorization-ref` (**required**) and `--dry-run`.
- `run` (function, lines 88-115) — drives one ingest and prints its report; **the report IS the result**.
- `_summary` (function, lines 116-138) — the human-readable rendering of an `IngestReport`.
- `_targets` (function, lines 139-145) — how a resolved target (path plus its symbol or line range) is
  rendered per entry.
- `_payload` (function, lines 146-179) — the machine-readable report the caller actually consumes.
- `_counts` (function, lines 180-194) — the entry arithmetic: read, committed, refused, rulings.
- `_outcome` (function, lines 195-229) — one entry's typed outcome, including its refusal reason.

`--contract` is **REQUIRED and is the write guard**, exactly as `memory-citations` and `memory-backfill`
use it: the operation reads the code and memory repositories the contract names and writes into the
candidate directory the caller supplies, so **there is no argument list that can aim a knowledge write
at another leaf's line**. `--authorization-ref` is required for the same reason the underlying operation
requires one. The CLI adds no write path of its own — it calls
`application.knowledge_curator_ingest.ingest_curator_list` and reports what that closed write path did.

This module exists because the write plane had no production caller: at `e7998504` the ingest was
reachable only from its own tests, which is finding **M1-1** of this master's review round 1.

### Conventions

Module-level definitions follow the package conventions, matching its seven sibling CLI adapters; names
prefixed with `_` are private to this module. Argument declaration and dispatch are split the same way
they are in `memory_citations.py` and `memory_backfill.py`: `add_arguments` owns the parser surface and
`run` owns the behaviour, so the parser can be exercised without running the operation.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- **Every write is bounded by the contract.** The module cannot be pointed at another leaf's line: the
  repositories come from `--contract` and the destination from `--candidate-directory`, and
  `--authorization-ref` is mandatory.
- **The report is the result.** Nothing is inferred from exit status alone — the counts, the per-entry
  outcomes and the refusal reasons are the operation's evidence.
- **This adapter adds no knowledge behaviour.** It declares arguments and renders the operation's own
  report; every refusal, route resolution and row count originates in the application layer.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Declares the contract guard, the hand-off list, the candidate directory, the authorization ref and dry-run. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_ingest.py:50-87 |
| Drives one ingest and prints the report, which is the result. | `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:88-115 |
| The machine-readable report the caller consumes. | `_payload` | mcp/src/agents_remember/cli/knowledge_ingest.py:146-179 |
| The entry arithmetic: read, committed, refused, rulings. | `_counts` | mcp/src/agents_remember/cli/knowledge_ingest.py:180-194 |
| The production entry point this adapter calls — the closed write path. | `ingest_curator_list` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:681-780 |
| The subparser registration that makes this the ninth CLI subcommand. | "knowledge-ingest" | mcp/src/agents_remember/cli/__main__.py:35-36; mcp/src/agents_remember/cli/__main__.py:42-43 |

## Update History
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `knowledge_ingest.py.md:81` (knowledge-ingest) — re-read the claim against the current source: the construct moved, and the range was re-derived from its real extent in the file the claim already cites.
- 2026-09-19T22:38+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `knowledge_ingest.py.md:80` — re-read: the anchor resolves exactly once in the named file at 681-780; the source cell was a bare path with no range, which the grammar refuses. Range re-derived from the file.


- 2026-09-19T17:30+02:00 — 260915-KS-L28: created this file-level onboarding card for the new source file, closing the gap the governed closeout preview reported (`onboarding_metadata_refresh.missing`). This module is the production caller that repairs review finding **M1-1** — the write plane previously had no caller outside its own module and tests. Anchors and ranges derived from the current candidate source (229 lines); verification metadata is left at this leaf's base `e7998504`, because the candidate is deliberately uncommitted and the governed closeout stamps the real code commit.

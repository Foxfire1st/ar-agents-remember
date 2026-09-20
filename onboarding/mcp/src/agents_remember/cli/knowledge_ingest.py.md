# mcp/src/agents_remember/cli/knowledge_ingest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_ingest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T01:24+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l30-ar` uncommitted change set; base `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

CLI adapter: ingest an orchestrator's curator hand-off list into a leaf's candidate — the knowledge
write plane's first production caller, and, when the caller names a destination, the run that publishes
the committed candidate through the shipped publication owner.

## Code Commentary

### Logic

Module-level surface:

- `add_arguments` (function, lines 64-114) — declares the operation's inputs: `--contract` (**required**),
  `--list` (**required**), `--candidate-directory` (**required**), `--authorization-ref` (**required**),
  `--commit`, `--publish-to`, `--expected-destination` and `--json`.
- `_expected_destination` (function, lines 117-136) — the destination identity the caller admitted, read
  from its JSON object; a malformed value is refused by name rather than read as "absent".
- `_publication` (function, lines 139-147) — the publication this invocation selects, or `None` when it
  selected no destination.
- `run` (function, lines 150-178) — drives one ingest and prints its report; **the report IS the result**.
- `_summary` (function, lines 181-208) — the human-readable rendering of an `IngestReport`.
- `_targets` (function, lines 211-215) — how a resolved target (path plus its symbol or line range) is
  rendered per entry.
- `_payload` (function, lines 218-252) — the machine-readable report the caller actually consumes.
- `_counts` (function, lines 255-267) — the entry arithmetic: read, committed, refused, rulings.
- `_outcome` (function, lines 270-304) — one entry's typed outcome, including its refusal reason.

`--contract` is **REQUIRED and is the write guard**, exactly as `memory-citations` and `memory-backfill`
use it: the operation reads the code and memory repositories the contract names and writes into the
candidate directory the caller supplies, so **there is no argument list that can aim a knowledge write
at another leaf's line**. `--authorization-ref` is required for the same reason the underlying operation
requires one. `run` builds the one `IngestSelection(candidate_directory, authorization_ref,
dry_run=not args.commit, publication=_publication(args))` the operation now takes and passes it
positionally, so the adapter names exactly the selection the operation consumes — and the baseline the
operation may fork from is deliberately **not** a CLI input: a caller that selected none gets the
cold-start behaviour. `--publish-to` is the second half of the same act, reached from this surface
without a second write path: the committed candidate is published by the run that already holds it, and
`--expected-destination` is the exact identity the caller observed at that path. The CLI adds
no write path of its own — it calls
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
| Declares the contract guard, the hand-off list, the candidate directory, the authorization ref and dry-run. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_ingest.py:64-114 |
| Drives one ingest and prints the report, which is the result; it builds the one `IngestSelection` the operation takes. | `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:150-178 |
| The machine-readable report the caller consumes. | `_payload` | mcp/src/agents_remember/cli/knowledge_ingest.py:218-252 |
| The entry arithmetic: read, committed, refused, rulings. | `_counts` | mcp/src/agents_remember/cli/knowledge_ingest.py:255-267 |
| The production entry point this adapter calls — the closed write path. | `ingest_curator_list` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:806-911 |
| The subparser registration that makes this the ninth CLI subcommand. | "knowledge-ingest" | mcp/src/agents_remember/cli/__main__.py:35-43 |
| The production entry point this adapter calls — the closed write path — and the selection value it is handed. | `ingest_curator_list`; `IngestSelection` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:784-891; mcp/src/agents_remember/application/knowledge_curator_ingest.py:764-781 |

## Update History
- 2026-09-20T02:05:20+00:00: Generated citation repair: `ingest_curator_list` repointed to mcp/src/agents_remember/application/knowledge_curator_ingest.py:806-911. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `knowledge_ingest.py.md:81` (knowledge-ingest) — re-read the claim against the current source: the construct moved, and the range was re-derived from its real extent in the file the claim already cites.
- 2026-09-19T22:38+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `knowledge_ingest.py.md:80` — re-read: the anchor resolves exactly once in the named file at 681-780; the source cell was a bare path with no range, which the grammar refuses. Range re-derived from the file.


- 2026-09-20T01:24+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **the publication step reached this adapter, and the card was re-read against it.** The checklist reopened two claims in this card — `run` and `_payload` — and both were re-read at their current constructs: `run` (lines 150-178) still drives one ingest and prints the report, and `_payload` (lines 218-252) is still the machine-readable report the caller consumes, so both retain their wording and only their ranges moved (`:89-116`→`:150-178`, `:149-180`→`:218-252`). The remaining reference rows were re-cited to their construct's own extent for the same reason, so every (anchor, range) pair in the table holds its own anchor: `add_arguments` `:51-86`→`:64-114`, `_counts` `:183-195`→`:255-267`, and `ingest_curator_list`/`IngestSelection` `:741-843`/`:725-739`→`:784-891`/`:764-781` in the application module. The Logic section was corrected where the source now contradicts it: `add_arguments` declares `--commit`, `--publish-to`, `--expected-destination` and `--json` (the `--dry-run` this card named is not a flag the module has), `_expected_destination` and `_publication` are added to the module-level surface, and `run` builds the one `IngestSelection(candidate_directory, authorization_ref, dry_run=not args.commit, publication=_publication(args))` beside the baseline it still does not take from the CLI. No reference row, anchor or citation was deleted. Because this body now describes a working candidate no commit contains, the stale `lastVerifiedCommitHash` and `lastVerifiedCommitDate` rows were replaced by one `reviewedWorkingCandidate` row under the reopened-claim stamp rule: **no verification stamp was advanced and no commit hash was invented**; closeout owns the real code commit.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read this card against the CYCLE-01 repair. `ingest_curator_list` no longer accepts trailing keyword arguments: `run` now builds the one frozen `IngestSelection(candidate_directory, authorization_ref, dry_run=not args.commit)` and passes it positionally, and the baseline a run may fork from is deliberately not a CLI input, so `--dry-run` still means "report what the real run would write". The Logic paragraph records the selection value, and the reference row now cites `IngestSelection` beside `ingest_curator_list`. Three citation defects this checklist reported were also cleared: the `ingest_curator_list` row carried **no range at all** (it cited the file bare) and now cites `knowledge_curator_ingest.py:741-843`; the `knowledge-ingest` anchor was a backticked non-identifier, which is not an anchor, so it is now the double-quoted literal `"knowledge-ingest"` inside `cli/__main__.py:35-43`; and the `__main__.py:36,42,43` source was not a citation form at all and is replaced by that range. The remaining rows (`add_arguments`, `run`, `_payload`, `_counts`) were re-cited to their construct extents, which moved when this leaf's `IngestSelection` construction landed. No verification stamp was advanced.
- 2026-09-19T17:30+02:00 — 260915-KS-L28: created this file-level onboarding card for the new source file, closing the gap the governed closeout preview reported (`onboarding_metadata_refresh.missing`). This module is the production caller that repairs review finding **M1-1** — the write plane previously had no caller outside its own module and tests. Anchors and ranges derived from the current candidate source (229 lines); verification metadata is left at this leaf's base `e7998504`, because the candidate is deliberately uncommitted and the governed closeout stamps the real code commit.

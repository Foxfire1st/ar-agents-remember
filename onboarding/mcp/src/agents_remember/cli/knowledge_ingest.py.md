# mcp/src/agents_remember/cli/knowledge_ingest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_ingest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T18:45:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l47-ar`, uncommitted; base `be325216416326a66950c9e320ff8d08f41e5d66` |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a` |
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
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

- `add_arguments` (function, lines 93-153) — declares the operation's inputs: `--contract` (**required**),
  `--list` (**required**), `--candidate-directory` (**optional**), `--authorization-ref` (**required**),
  `--baseline`, `--commit`, `--publish-to`, `--expected-destination` and `--json`.
- `_expected_destination` (function) — the destination identity the caller admitted, read
  from its JSON object; a malformed value is refused by name rather than read as "absent".
- `_publication` (function, lines 178-186) — the publication this invocation selects, or `None` when it
  selected no destination.
- `_review_root` (function, lines 189-198) — the leaf's canonical review knowledge root, derived from
  the **contract's own recorded worktree group** rather than from the caller or the process's working
  directory.
- `_candidate_directory` (function, lines 201-210) — the directory this run writes into: the caller's
  if it named one, otherwise `<review root>/candidate`.
- `_place_review_baseline` (function, lines 213-245) — the run's **review handoff**: when a caller
  supplied `--baseline` and the batch committed, the fork-point dataset is **copied** into
  `<review root>/baseline`; otherwise the function returns a string saying why nothing was placed.
- `run` (function, lines 248-284) — drives one ingest and prints its report; **the report IS the result**.
- `_summary` (function, lines 287-316) — the human-readable rendering of an `IngestReport`.
- `_targets` (function) — how a resolved target (path plus its symbol or line range) is
  rendered per entry.
- `_payload` (function, lines 326-364) — the machine-readable report the caller actually consumes.
- `_counts` (function, lines 367-379) — the entry arithmetic: read, committed, refused, rulings.
- `_outcome` (function) — one entry's typed outcome, including its refusal reason.
- `COMMITTED_BATCH_STATES` (lines 85-90) — the two batch states that mean a candidate is on disk
  (`changed`, `no_change`), which is what decides whether the baseline half may be placed.

`--contract` is **REQUIRED and is the write guard**, exactly as `memory-citations` and `memory-backfill`
use it: the operation reads the code and memory repositories the contract names and writes into the
candidate directory the caller supplies, so **there is no argument list that can aim a knowledge write
at another leaf's line**. `--authorization-ref` is required for the same reason the underlying operation
requires one. `run` builds the one `IngestSelection(candidate_directory, authorization_ref,
dry_run=not args.commit, baseline=..., publication=_publication(args))` the operation now takes and passes
it positionally, so the adapter names exactly the selection the operation consumes.

**`--candidate-directory` is now OPTIONAL and defaults to the leaf's canonical review candidate root.**
That default is what connects the write side to the read side: the directory is
`<worktree-group>/provider-runtime/dev-ar-coordination/knowledge/candidate`, derived from the contract's
own recorded worktree group through **the same published constants the Intent Reviewer resolves with**
(`REVIEW_CANDIDATE_RELATIVE_ROOT`, `REVIEW_CANDIDATE_DIRECTORY`), so an ingest that names no directory
authors the candidate the review then opens — one spelling, not two conventions that happen to agree
today. Naming a directory still wins, because a caller that wants a scratch draft should get one; that
draft is then simply not the leaf's review candidate, and the report echoes the directory either way.
A contract that cannot be loaded is refused before the list is read, by name.

**The review handoff: a committing run that was given `--baseline` places the fork-point dataset in the
baseline half — from bytes read BEFORE the run publishes.** `_capture_baseline` runs at the top of
`run`, ahead of `ingest_curator_list`, and carries the bytes; `_place_review_baseline` writes those
bytes rather than re-reading `args.baseline`. That ordering is load-bearing and is this leaf's
`260915-KS-L47` repair: `--baseline` and `--publish-to` may name one path, publication replaces that
file **in place**, and a copy taken afterwards places the published candidate in the before half — so
the review compares a dataset against itself and reports a real addition as present on both sides with
an empty delta. Every way out is explicit rather than inferred: no `--baseline` → nothing is placed and
the half stays absent (where the review's `candidate_dataset_absent` is then the *truthful* answer); a
planning run (`--dry-run`) → `not-placed: planning run (the baseline is placed by the run that
commits)`; a batch that did not commit → `not-placed: the batch did not commit (<state>)`; a named
dataset that is not a file or cannot be read → `not-captured: …`; a destination already holding
byte-identical content → `present: <path>` and left alone, which is what makes a retry keep the fork
point it was first handed instead of restating it. Otherwise the bytes are **copied**, never moved and
never linked, because the review's own recorded decision is that both halves sit inside the leaf's
**disposable local root** "so a review reads no candidate out of the live coordination tree" — the
published dataset keeps serving its own lane while the leaf's review reads its own copy. The result
reaches the caller as the report's `reviewBaseline` field (and as a `review baseline:` line in the
human summary); it is a **string and not a boolean** because "not placed" has several reasons and a
caller that has to guess which one is being given a message rather than a result.

**`--baseline <published dataset>` is the continuity half of that one decision, and it is this leaf's
CYCLE-01 repair.** It names the published dataset the task forks FROM and reaches
`IngestSelection.baseline` as a `Path`, so the next task begins from the knowledge the repository already
published instead of from an empty candidate. Omitting it is not a failure but the other honest case — a
repository's first task has no prior dataset to select and still creates an empty candidate — which is
why the argument and the selection field are one pairing rather than an option and a default: a candidate
named without the baseline it starts from holds only this task's new entry, so the repository's existing
invariants are absent from it and the next task begins blind to what was already recorded. Nothing else
about the surface changed, and `--publish-to` remains the second half of the same act, reached from this
surface without a second write path: the committed candidate is published by the run that already holds
it, and `--expected-destination` is the exact identity the caller observed at that path. The CLI adds no
write path of its own — it calls
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
  repositories come from `--contract` and the destination is either the caller's directory or the
  canonical root derived from that same contract, and `--authorization-ref` is mandatory.
- **The write side and the read side name one directory.** The default candidate directory is derived
  from the contract through the review's own published constants, so an ingest that names nothing
  authors the candidate the Intent Reviewer resolves.
- **Nothing is placed on a way out that did not commit.** A planning run, a refused batch and a run with
  no `--baseline` each place nothing, and each says which case it was; no baseline is invented, there is
  no `HEAD` fallback and no coordination-tree resolution.
- **The fork-point dataset is copied, not moved and not linked.** The published dataset keeps serving its
  own lane; the leaf's disposable root gets its own bytes.
- **The report is the result.** Nothing is inferred from exit status alone — the counts, the per-entry
  outcomes, the refusal reasons and the `reviewBaseline` line are the operation's evidence.
- **This adapter adds no knowledge behaviour.** It declares arguments, derives one path from the contract
  and copies one file; every refusal, route resolution and row count originates in the application layer.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Declares the contract guard, the hand-off list, the optional candidate directory, the authorization ref, the baseline this task forks from, and dry-run. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_ingest.py:110-170 |
| Drives one ingest and prints the report, which is the result; it builds the one `IngestSelection` the operation takes, with `--baseline` reaching the selection it forks from. | `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:335-374 |
| **The canonical review root, derived from the contract's own recorded worktree group rather than from the caller, so the directory the review resolves and the directory this run writes are the same path by construction.** | `_review_root` | mcp/src/agents_remember/cli/knowledge_ingest.py:206-215 |
| **The candidate directory: the caller's when it named one, otherwise the canonical review candidate root.** | `_candidate_directory` | mcp/src/agents_remember/cli/knowledge_ingest.py:218-227 |
| **The review handoff: the captured fork-point dataset written into the baseline half on a committing run, with every not-placed reason stated as a string.** | `_place_review_baseline` | mcp/src/agents_remember/cli/knowledge_ingest.py:293-332 |
| **The before-snapshot capture, taken at the top of `run` before the ingest can publish over the file `--baseline` names (leaf `260915-KS-L47`).** | `_capture_baseline`; `_CapturedBaseline` | mcp/src/agents_remember/cli/knowledge_ingest.py:231-263 |
| The two batch states that mean the candidate is on disk, and the entry list that keeps an all-refused run from reading as one of them: `no_change` is a batch whose rows were already stored, but the batch-level state also falls back to it when the batch never ran, so a run whose every entry refused reports it too. The placement therefore also requires `report.committed` to be non-empty, because a run that committed no entry has no candidate of its own and must not touch the review's before half. | `COMMITTED_BATCH_STATES` | mcp/src/agents_remember/cli/knowledge_ingest.py:107-107; mcp/src/agents_remember/cli/knowledge_ingest.py:293-332 |
| **The one reason a placement did not happen, split so each branch states only what its own condition established.** The state half reports `the batch did not commit (<state>)`; the entry half reports `the batch committed no entry (<state>, refused N)`. They are two returns rather than one sentence because the single sentence served both halves and contradicted itself on the state-half branch -- a replayed run read `committed no entry (replayed, committed 1)`. | `_placement_refusal` | mcp/src/agents_remember/cli/knowledge_ingest.py:266-290 |
| The machine-readable report the caller consumes, including `reviewBaseline` beside `candidateDirectory`. | `_payload` | mcp/src/agents_remember/cli/knowledge_ingest.py:416-454 |
| The entry arithmetic: read, committed, refused, rulings. | `_counts` | mcp/src/agents_remember/cli/knowledge_ingest.py:457-469 |
| The production entry point this adapter calls — the closed write path. | `ingest_curator_list` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1023-1142 |
| **The two published directory constants this adapter derives its default from — one spelling shared with the reader, which is what connects the write side to the review.** | `REVIEW_CANDIDATE_RELATIVE_ROOT`; `REVIEW_CANDIDATE_DIRECTORY`; `REVIEW_BASELINE_DIRECTORY` | mcp/src/agents_remember/application/knowledge_review.py:132-132; mcp/src/agents_remember/application/knowledge_review.py:138-139 |
| The dataset name both halves take, so a placed baseline is the file the review opens. | `CANDIDATE_DATABASE_NAME` | mcp/src/agents_remember/models/knowledge/snapshot.py:52-52 |
| The production entry point this adapter calls — the closed write path — and the selection value it is handed, including the baseline a run forks from. | `ingest_curator_list`; `IngestSelection` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1023-1142; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1003-1020 |
| Declares the contract guard, the hand-off list, the candidate directory, the authorization ref, the baseline this task forks from, and dry-run. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_ingest.py:110-170 |
| The machine-readable report the caller consumes. | `_payload` | mcp/src/agents_remember/cli/knowledge_ingest.py:416-454 |
| The subparser registration that makes this the ninth CLI subcommand. | "knowledge-ingest" | mcp/src/agents_remember/cli/__main__.py:35-43 |
| The production entry point this adapter calls — the closed write path — and the selection value it is handed. | `ingest_curator_list`; `IngestSelection` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1023-1142; mcp/src/agents_remember/application/knowledge_curator_ingest.py:1003-1020 |

## Update History
- 2026-09-21T01:40+02:00 — 260915-KS-L47 curator (uncommitted change set on `ar/260915-ks-l47-ar`, code base `be325216416326a66950c9e320ff8d08f41e5d66`, memory base `2f415d930d1f8122ae0226bd296add3265600749`): **the refusal sentence was split, and every citation into this file was re-measured again rather than carried.** `_place_review_baseline`'s not-placed message served both halves of the placement condition in one sentence, so a replayed run reported `not-placed: the batch committed no entry (replayed, committed 1)` -- the gate was right and the sentence was wrong for the state-half branch. It is now two returns, `_placement_refusal` (`:266-288`), one per branch. The file grew 486 -> 505 lines, so this card's ranges were re-measured by AST extent: `_place_review_baseline` `:266-311` -> `:291-330`, `run` `:314-353` -> `:333-372`, `_payload` `:395-433` -> `:414-452`, `_counts` `:436-448` -> `:455-467`; `add_arguments` `:110-170`, `_review_root` `:206-215`, `_candidate_directory` `:218-227`, `_CapturedBaseline`/`_capture_baseline` `:231-263` and `COMMITTED_BATCH_STATES` `:107-107` are unchanged by the split and were re-verified rather than assumed. The same re-measurement was applied to the three other documents that cite this file. This is a body change and not a metadata-only refresh. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made.
- 2026-09-21T00:40+02:00 — 260915-KS-L47 curator (uncommitted change set on `ar/260915-ks-l47-ar`, code base `be325216416326a66950c9e320ff8d08f41e5d66`, memory base `2f415d930d1f8122ae0226bd296add3265600749`): **re-measured against the moved candidate, and the refusal-path defect this file's own repair opened is now stated and guarded.** The code worktree moved under this curation: `cli/knowledge_ingest.py` gained the `report.committed` requirement beside `COMMITTED_BATCH_STATES`, because an all-refused run also reports `no_change` — the batch-level state falls back to it when the batch never ran — so a changed request that the retry guard turns into a *refusal* re-placed the before half from the bytes captured at the top of the run, which after the leaf published over its own fork point are the PUBLISHED dataset, and the review showed the addition present on both sides with an empty delta. The file grew from 393 to 485 lines, so **every citation this card carries into it was re-measured rather than carried**: `add_arguments` `:93-153` → `:110-170`, `run` `:248-284` → `:314-353`, `_place_review_baseline` `:256-298` → `:266-311`, the two previously range-less cells now cite `:266-311` and `:231-263`, `COMMITTED_BATCH_STATES` `:97-97` → `:107-107`, `_payload` `:326-364` → `:395-433`, and `_counts` `:423-435` → `:436-448`. The same re-measurement was applied to the three other documents that cite this file — `mcp/overview.md`, `mcp/src/agents_remember/application/overview.md` and `mcp/tests/overview.md` — because a citation range is a measurement of the candidate, not a record that survives the candidate moving. The `COMMITTED_BATCH_STATES` row's own text was extended to state the entry-list requirement and why state alone cannot carry it. This is a body change, not a metadata-only refresh. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are retained exactly as recorded; no stamp was advanced or invented and no commit was made.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `COMMITTED_BATCH_STATES` repointed to mcp/src/agents_remember/cli/knowledge_ingest.py:97-97. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `_counts` repointed to mcp/src/agents_remember/cli/knowledge_ingest.py:423-435. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T17:17:10+00:00: Generated citation repair: `ingest_curator_list` repointed to mcp/src/agents_remember/application/knowledge_curator_ingest.py:1023-1142. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-20T18:45:00+02:00 — 260915-KS-L47 worker (uncommitted change set on `ar/260915-ks-l47-ar`, code base `be325216416326a66950c9e320ff8d08f41e5d66`): **the reviewer's before-snapshot is now captured before publication can overwrite it.** `_capture_baseline` reads `--baseline` at the top of `run`, ahead of `ingest_curator_list`, and `_place_review_baseline` writes those captured bytes. The defect this closes: `--baseline` and `--publish-to` may name one path, publication replaces that file **in place**, and the old post-ingest `shutil.copyfile(source, destination)` therefore copied the published candidate into the review's before half — the review then reported a real addition as present on both sides with `field_changes: []`, which is the rejected `KS-R22` Intent Reviewer comparison. Measured before the change on this base: the review's `before_snapshot_digest` equalled its `after_snapshot_digest` and the before statement read `present`; after the change the before half is byte-identical to the true fork point, the review answers before `absent` / after `present` over two different digests, and the retry preserves the half it was first handed. The surface table gained `_capture_baseline`/`_CapturedBaseline`; the two rows whose prose described the old copy-after-the-fact behaviour were rewritten rather than re-cited, and their ranges are dropped because those lines moved twice already. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate on base `be325216`, which is the candidate this reading was performed against, and `lastUpdated` moved with it; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains this body and no stamp was measured on it. No commit was made.
- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator, **memory-side sync conflict resolved as a UNION; no side dropped.** The memory source branch advanced to `92f444b04` (260915-KS-L45) while this leaf's curation was in flight, so the sync's re-apply conflicted in this file. Both sides were kept because both are true: 260915-KS-L45's landed additions (the Intent-review entry path, the two published half-names `REVIEW_BASELINE_DIRECTORY`/`REVIEW_CANDIDATE_DIRECTORY`, the `missing_dataset_half` pair preflight, the receipt-derived `review_namespace`, and the enumerating reads) and this leaf's 260915-KS-L43 edits (the allocated-identity/derived-citation split, the retry key and its journal, the explicit anchor reuse, and the recovery's journaled decisions with the bounded cycling refusal). Where the two sides carried the same row in different line numbers, the row was re-measured against the moved line rather than picked: L45 curated against `fb719f89` and this leaf's source moves every citation below `:306` of `knowledge_curator_ingest.py` and renumbers `cli/knowledge_ingest.py` entirely, so the surviving ranges are the post-merge measurement for both. One **contradiction** is recorded rather than silently resolved: the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` frontmatter pair is L45's (recorded against the moved line, the newest verification on record), while the `reviewedWorkingCandidate` row is this leaf's reading — two different claims, kept beside each other instead of one overwriting the other. No verification stamp was advanced by this leaf.
- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, code base `fb719f89`): **the run that authors the candidate is now the run that connects it to the review.** This card records the three facts a reader of this adapter needs. (1) `--candidate-directory` became **OPTIONAL**: omitting it derives `<worktree-group>/provider-runtime/dev-ar-coordination/knowledge/candidate` from the **contract's own recorded worktree group** through `_review_root` and the review's own **published** constants, which is what makes "the candidate this run authored" and "the candidate the review resolved" one directory instead of two conventions; naming a directory still wins and that draft is then simply not the leaf's review candidate. (2) `_place_review_baseline` is the review's other half: a committing run given `--baseline` **copies** that dataset into the baseline half, and every other outcome is a stated string (`not-placed: planning run…`, `not-placed: the batch did not commit (…)`, `not-placed: … is not a file`, `present: <path>` when the bytes already match) rather than an inferred boolean — the copy is deliberate, because the review's own recorded decision is that both halves sit in the leaf's disposable local root so a review reads nothing out of the live coordination tree. (3) The report gained `reviewBaseline` beside `candidateDirectory`, and `COMMITTED_BATCH_STATES` is the two-state set that decides whether placing is allowed at all. The module-level surface list was corrected where it had drifted (`_expected_destination`/`_outcome`/`_targets` now carry no line numbers, since those lines moved twice already) and the four reference rows whose constructs moved were re-cited. No anchor was renamed and no citation was dropped. No verification stamp was advanced, because no commit contains this body; `reviewedWorkingCandidate` now names this leaf's candidate on base `fb719f89`.
- 2026-09-20T05:16+02:00 — 260915-KS-L39 curator (uncommitted CYCLE-01 change set on `ar/260915-ks-l39-ar`, code base `756c47b37fa16324a836a44336655413d10fffaa`): **the public baseline selection reached this adapter, and the card's own statement that it had not was corrected.** This card said the baseline "is deliberately **not** a CLI input" and that "a caller that selected none gets the cold-start behaviour" — true when it was written, false now. `add_arguments` declares `--baseline <published dataset>` (default `None`) and `run` passes it into the one `IngestSelection` as `baseline=None if args.baseline is None else Path(args.baseline)`, so a next task can begin from a prior task's published knowledge instead of from an empty candidate; omitting it is still the correct cold start for a repository's first task, which is why the argument and the selection field are one pairing rather than an option and a default. Every construct extent on this card was re-measured in this candidate, because the declaration moved the whole module: `add_arguments` `:64-114`→`:71-129`, `run` `:150-178`→`:165-194`, `_payload` `:218-252`→`:234-268`, `_counts` `:255-267`→`:271-283`, `_expected_destination` `:117-136`→`:132-151`, `_publication` `:139-147`→`:154-162`, `_summary` `:181-208`→`:197-224`, `_targets` `:211-215`→`:227-231` and `_outcome` `:270-304`→`:286-320`; the `ingest_curator_list`/`IngestSelection` row now cites the application module at `:846-952` and `:827-843`. No anchor was renamed and no citation was dropped. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate `ar/260915-ks-l39-ar` on base `756c47b3`, which is the candidate this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains the body as it now stands and no stamp was measured on it. No commit was made.
- 2026-09-20T02:05:20+00:00: Generated citation repair: `ingest_curator_list` repointed to mcp/src/agents_remember/application/knowledge_curator_ingest.py:806-911. No content impact: mechanical anchor-range projection bound to citation source snapshot fe7fdbf3f561fa23007ac47565833928a7c74df1b4b028969d78a5b139bb65b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T01:24+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **the publication step reached this adapter, and the card was re-read against it.** The checklist reopened two claims in this card — `run` and `_payload` — and both were re-read at their current constructs: `run` (lines 150-178) still drives one ingest and prints the report, and `_payload` (lines 218-252) is still the machine-readable report the caller consumes, so both retain their wording and only their ranges moved (`:89-116`→`:150-178`, `:149-180`→`:218-252`). The remaining reference rows were re-cited to their construct's own extent for the same reason, so every (anchor, range) pair in the table holds its own anchor: `add_arguments` `:51-86`→`:64-114`, `_counts` `:183-195`→`:255-267`, and `ingest_curator_list`/`IngestSelection` `:741-843`/`:725-739`→`:784-891`/`:764-781` in the application module. The Logic section was corrected where the source now contradicts it: `add_arguments` declares `--commit`, `--publish-to`, `--expected-destination` and `--json` (the `--dry-run` this card named is not a flag the module has), `_expected_destination` and `_publication` are added to the module-level surface, and `run` builds the one `IngestSelection(candidate_directory, authorization_ref, dry_run=not args.commit, publication=_publication(args))` beside the baseline it still does not take from the CLI. No reference row, anchor or citation was deleted. Because this body now describes a working candidate no commit contains, the stale `lastVerifiedCommitHash` and `lastVerifiedCommitDate` rows were replaced by one `reviewedWorkingCandidate` row under the reopened-claim stamp rule: **no verification stamp was advanced and no commit hash was invented**; closeout owns the real code commit.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read this card against the CYCLE-01 repair. `ingest_curator_list` no longer accepts trailing keyword arguments: `run` now builds the one frozen `IngestSelection(candidate_directory, authorization_ref, dry_run=not args.commit)` and passes it positionally, and the baseline a run may fork from is deliberately not a CLI input, so `--dry-run` still means "report what the real run would write". The Logic paragraph records the selection value, and the reference row now cites `IngestSelection` beside `ingest_curator_list`. Three citation defects this checklist reported were also cleared: the `ingest_curator_list` row carried **no range at all** (it cited the file bare) and now cites `knowledge_curator_ingest.py:741-843`; the `knowledge-ingest` anchor was a backticked non-identifier, which is not an anchor, so it is now the double-quoted literal `"knowledge-ingest"` inside `cli/__main__.py:35-43`; and the `__main__.py:36,42,43` source was not a citation form at all and is replaced by that range. The remaining rows (`add_arguments`, `run`, `_payload`, `_counts`) were re-cited to their construct extents, which moved when this leaf's `IngestSelection` construction landed. No verification stamp was advanced.
- 2026-09-20T00:28+02:00 — 260918-TSIP-L11 closing seat (memory worktree `84152b9e`, code `79fa817f`): re-read and re-derived 1 claim row(s) on the merged tip. Every row was read against the construct it cites before its range was regenerated: the merged `mcp/tests/test-evidence-lanes.toml` was read at the line that carries each lane anchor, `pyproject.toml` was read at its declaration, and every renamed or consolidated case was re-anchored on the successor whose own docstring records the consolidation. No range was produced by adding a delta to an old number and the product's mechanical fixer was not run, so **no projection bullet is written and no claim is reopened on this edit's account**. Rows: `knowledge_ingest.py.md:81` (knowledge-ingest) — re-read the claim against the current source: the construct moved, and the range was re-derived from its real extent in the file the claim already cites.
- 2026-09-19T22:38+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): **re-read each claim below against the construct its range now covers, corrected the wording where the construct had moved, re-derived every range from the construct's real extent in the file the claim cites, and only then left the card's stamp to closeout.** No `Generated citation repair` bullet is written: these are curator edits, not a mechanical projection. `knowledge_ingest.py.md:80` — re-read: the anchor resolves exactly once in the named file at 681-780; the source cell was a bare path with no range, which the grammar refuses. Range re-derived from the file.


- 2026-09-19T17:30+02:00 — 260915-KS-L28: created this file-level onboarding card for the new source file, closing the gap the governed closeout preview reported (`onboarding_metadata_refresh.missing`). This module is the production caller that repairs review finding **M1-1** — the write plane previously had no caller outside its own module and tests. Anchors and ranges derived from the current candidate source (229 lines); verification metadata is left at this leaf's base `e7998504`, because the candidate is deliberately uncommitted and the governed closeout stamps the real code commit.

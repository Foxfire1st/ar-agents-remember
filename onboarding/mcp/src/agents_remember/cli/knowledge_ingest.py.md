# mcp/src/agents_remember/cli/knowledge_ingest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_ingest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T13:43:00+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l45-ar`, uncommitted; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| lastVerifiedCommitHash | `4a0442d62eb842661a3dd04686c376d0f0dbc61f` |
| lastVerifiedCommitDate | 2026-09-20T14:22:54+02:00|
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
baseline half.** `_place_review_baseline` is the whole of it, and every way out is explicit rather than
inferred: no `--baseline` → nothing is placed and the half stays absent (where the review's
`candidate_dataset_absent` is then the *truthful* answer); a planning run (`--dry-run`) → `not-placed:
planning run (the baseline is placed by the run that commits)`; a batch that did not commit → `not-placed:
the batch did not commit (<state>)`; a named dataset that is not a file → `not-placed: … is not a file`;
a destination already holding byte-identical content → `present: <path>` and left alone. Otherwise the
bytes are **copied**, never moved and never linked, because the review's own recorded decision is that
both halves sit inside the leaf's **disposable local root** "so a review reads no candidate out of the
live coordination tree" — the published dataset keeps serving its own lane while the leaf's review reads
its own copy. The result reaches the caller as the report's `reviewBaseline` field (and as a
`review baseline:` line in the human summary); it is a **string and not a boolean** because "not placed"
has several reasons and a caller that has to guess which one is being given a message rather than a
result.

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
| Declares the contract guard, the hand-off list, the optional candidate directory, the authorization ref, the baseline this task forks from, and dry-run. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_ingest.py:93-153 |
| Drives one ingest and prints the report, which is the result; it builds the one `IngestSelection` the operation takes, with `--baseline` reaching the selection it forks from. | `run` | mcp/src/agents_remember/cli/knowledge_ingest.py:248-284 |
| **The canonical review root, derived from the contract's own recorded worktree group rather than from the caller, so the directory the review resolves and the directory this run writes are the same path by construction.** | `_review_root` | mcp/src/agents_remember/cli/knowledge_ingest.py:189-198 |
| **The candidate directory: the caller's when it named one, otherwise the canonical review candidate root.** | `_candidate_directory` | mcp/src/agents_remember/cli/knowledge_ingest.py:201-210 |
| **The review handoff: the fork-point dataset copied into the baseline half on a committing run, with every not-placed reason stated as a string.** | `_place_review_baseline` | mcp/src/agents_remember/cli/knowledge_ingest.py:213-245 |
| The two batch states that mean the candidate is on disk, which is what decides whether the baseline half may be placed. | `COMMITTED_BATCH_STATES` | mcp/src/agents_remember/cli/knowledge_ingest.py:85-90 |
| The machine-readable report the caller consumes, including `reviewBaseline` beside `candidateDirectory`. | `_payload` | mcp/src/agents_remember/cli/knowledge_ingest.py:326-364 |
| The entry arithmetic: read, committed, refused, rulings. | `_counts` | mcp/src/agents_remember/cli/knowledge_ingest.py:367-379 |
| **The two published directory constants this adapter derives its default from — one spelling shared with the reader, which is what connects the write side to the review.** | `REVIEW_CANDIDATE_RELATIVE_ROOT`; `REVIEW_CANDIDATE_DIRECTORY`; `REVIEW_BASELINE_DIRECTORY` | mcp/src/agents_remember/application/knowledge_review.py:132-132; mcp/src/agents_remember/application/knowledge_review.py:138-139 |
| The dataset name both halves take, so a placed baseline is the file the review opens. | `CANDIDATE_DATABASE_NAME` | mcp/src/agents_remember/models/knowledge/snapshot.py:52-52 |
| The production entry point this adapter calls — the closed write path — and the selection value it is handed, including the baseline a run forks from. | `ingest_curator_list`; `IngestSelection` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:846-952; mcp/src/agents_remember/application/knowledge_curator_ingest.py:827-843 |
| The subparser registration that makes this the ninth CLI subcommand. | "knowledge-ingest" | mcp/src/agents_remember/cli/__main__.py:35-43 |

## Update History

- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, code base `fb719f89`): **the run that authors the candidate is now the run that connects it to the review.** This card records the three facts a reader of this adapter needs. (1) `--candidate-directory` became **OPTIONAL**: omitting it derives `<worktree-group>/provider-runtime/dev-ar-coordination/knowledge/candidate` from the **contract's own recorded worktree group** through `_review_root` and the review's own **published** constants, which is what makes "the candidate this run authored" and "the candidate the review resolved" one directory instead of two conventions; naming a directory still wins and that draft is then simply not the leaf's review candidate. (2) `_place_review_baseline` is the review's other half: a committing run given `--baseline` **copies** that dataset into the baseline half, and every other outcome is a stated string (`not-placed: planning run…`, `not-placed: the batch did not commit (…)`, `not-placed: … is not a file`, `present: <path>` when the bytes already match) rather than an inferred boolean — the copy is deliberate, because the review's own recorded decision is that both halves sit in the leaf's disposable local root so a review reads nothing out of the live coordination tree. (3) The report gained `reviewBaseline` beside `candidateDirectory`, and `COMMITTED_BATCH_STATES` is the two-state set that decides whether placing is allowed at all. The module-level surface list was corrected where it had drifted (`_expected_destination`/`_outcome`/`_targets` now carry no line numbers, since those lines moved twice already) and the four reference rows whose constructs moved were re-cited. No anchor was renamed and no citation was dropped. No verification stamp was advanced, because no commit contains this body; `reviewedWorkingCandidate` now names this leaf's candidate on base `fb719f89`.
- 2026-09-20T05:16+02:00 — 260915-KS-L39 curator (uncommitted CYCLE-01 change set on `ar/260915-ks-l39-ar`, code base `756c47b37fa16324a836a44336655413d10fffaa`): **the public baseline selection reached this adapter, and the card's own statement that it had not was corrected.** This card said the baseline "is deliberately **not** a CLI input" and that "a caller that selected none gets the cold-start behaviour" — true when it was written, false now. `add_arguments` declares `--baseline <published dataset>` (default `None`) and `run` passes it into the one `IngestSelection` as `baseline=None if args.baseline is None else Path(args.baseline)`, so a next task can begin from a prior task's published knowledge instead of from an empty candidate; omitting it is still the correct cold start for a repository's first task, which is why the argument and the selection field are one pairing rather than an option and a default. Every construct extent on this card was re-measured in this candidate, because the declaration moved the whole module: `add_arguments` `:64-114`→`:71-129`, `run` `:150-178`→`:165-194`, `_payload` `:218-252`→`:234-268`, `_counts` `:255-267`→`:271-283`, `_expected_destination` `:117-136`→`:132-151`, `_publication` `:139-147`→`:154-162`, `_summary` `:181-208`→`:197-224`, `_targets` `:211-215`→`:227-231` and `_outcome` `:270-304`→`:286-320`; the `ingest_curator_list`/`IngestSelection` row now cites the application module at `:846-952` and `:827-843`. No anchor was renamed and no citation was dropped. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate `ar/260915-ks-l39-ar` on base `756c47b3`, which is the candidate this reading was performed against; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains the body as it now stands and no stamp was measured on it. No commit was made.
- 2026-09-20T01:24+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **the publication step reached this adapter, and the card was re-read against it.** The checklist reopened two claims in this card — `run` and `_payload` — and both were re-read at their current constructs: `run` (lines 150-178) still drives one ingest and prints the report, and `_payload` (lines 218-252) is still the machine-readable report the caller consumes, so both retain their wording and only their ranges moved (`:89-116`→`:150-178`, `:149-180`→`:218-252`). The remaining reference rows were re-cited to their construct's own extent for the same reason, so every (anchor, range) pair in the table holds its own anchor: `add_arguments` `:51-86`→`:64-114`, `_counts` `:183-195`→`:255-267`, and `ingest_curator_list`/`IngestSelection` `:741-843`/`:725-739`→`:784-891`/`:764-781` in the application module. The Logic section was corrected where the source now contradicts it: `add_arguments` declares `--commit`, `--publish-to`, `--expected-destination` and `--json` (the `--dry-run` this card named is not a flag the module has), `_expected_destination` and `_publication` are added to the module-level surface, and `run` builds the one `IngestSelection(candidate_directory, authorization_ref, dry_run=not args.commit, publication=_publication(args))` beside the baseline it still does not take from the CLI. No reference row, anchor or citation was deleted. Because this body now describes a working candidate no commit contains, the stale `lastVerifiedCommitHash` and `lastVerifiedCommitDate` rows were replaced by one `reviewedWorkingCandidate` row under the reopened-claim stamp rule: **no verification stamp was advanced and no commit hash was invented**; closeout owns the real code commit.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read this card against the CYCLE-01 repair. `ingest_curator_list` no longer accepts trailing keyword arguments: `run` now builds the one frozen `IngestSelection(candidate_directory, authorization_ref, dry_run=not args.commit)` and passes it positionally, and the baseline a run may fork from is deliberately not a CLI input, so `--dry-run` still means "report what the real run would write". The Logic paragraph records the selection value, and the reference row now cites `IngestSelection` beside `ingest_curator_list`. Three citation defects this checklist reported were also cleared: the `ingest_curator_list` row carried **no range at all** (it cited the file bare) and now cites `knowledge_curator_ingest.py:741-843`; the `knowledge-ingest` anchor was a backticked non-identifier, which is not an anchor, so it is now the double-quoted literal `"knowledge-ingest"` inside `cli/__main__.py:35-43`; and the `__main__.py:36,42,43` source was not a citation form at all and is replaced by that range. The remaining rows (`add_arguments`, `run`, `_payload`, `_counts`) were re-cited to their construct extents, which moved when this leaf's `IngestSelection` construction landed. No verification stamp was advanced.
- 2026-09-19T17:30+02:00 — 260915-KS-L28: created this file-level onboarding card for the new source file, closing the gap the governed closeout preview reported (`onboarding_metadata_refresh.missing`). This module is the production caller that repairs review finding **M1-1** — the write plane previously had no caller outside its own module and tests. Anchors and ranges derived from the current candidate source (229 lines); verification metadata is left at this leaf's base `e7998504`, because the candidate is deliberately uncommitted and the governed closeout stamps the real code commit.

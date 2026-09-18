# mcp/src/agents_remember/kernel/memory_attribution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/memory_attribution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00 |
| governingOverview | `../../../overview.md` |

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Owns the shared `Code-Commit` key, memory-message renderer, and committed-attribution reader. The
attribution is part of the memory commit object; this module does not create commits or files.

## Code Commentary

### Logic

`render_memory_content_message` appends a separate final attribution block after the supplied
body. Keeping the writer beside the key prevents producer-local spellings from drifting away from
the reader. Carryover may receive a multi-paragraph public body; baseline uses its own adoption
subject, and closeout-shaped producers delegate through the effective input model.

`attributed_commits` reads Git's trailer values for every commit reachable from the requested tip,
optionally excluding another history. It uses the full ancestry rather than only first parents,
so a mapping introduced on a merged branch remains visible. NUL-delimited records preserve commit
boundaries. A readable commit with no matching attribution is returned with `code_commit=None`;
an unreadable history raises `MemoryAttributionError` instead of looking like empty attribution.

`_trailer_value_from` accepts the declared hash-shaped value and keeps the last matching value.
`parse_code_commit_trailer` is the message-level parser; it returns the last matching anchored
trailer line and ignores a mere in-line mention. `ledger_rows_from_attribution` preserves the Git
walk's ordering and omits unattributed commits. `AttributedCommit.row(code_repository=...)` optionally
checks that the named code commit exists.

The documentation correction removes the former runtime-table fallback story. This reader's
runtime implementation remains trailer-based. Explicit historical-table migration is owned by
`memory_backfill`, not activated by missing attribution in this module.

### Conventions

One frozen `AttributedCommit` value and module-level functions expose the reader. SHA-shaped text
is syntax; the optional code-repository check establishes object existence. The writer returns a
message string only and owns no publication or backfill policy.

### Invariants And Boundaries

- No cached or historical table is a runtime fallback for absent attribution.
- Unattributed commits and unreadable Git history remain different facts.
- The full reachable ancestry includes merge-side attribution.
- The shared key and renderer remain the only production spelling/format owner.
- Code-object validation applies when the caller supplies the code repository.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The single key, log format, renderer, and attribution value. | `CODE_COMMIT_TRAILER_KEY`; `_LOG_FORMAT` | mcp/src/agents_remember/kernel/memory_attribution.py:51; mcp/src/agents_remember/kernel/memory_attribution.py:56-56 |
| The history walk and message/value parsers define the actual read behavior. | `attributed_commits` | mcp/src/agents_remember/kernel/memory_attribution.py:143-174 |
| Row conversion and optional object validation. | `code_commit_exists` | mcp/src/agents_remember/kernel/memory_attribution.py:202-205 |
| Runtime ledger derivation never consults cache text. | `derive_memory_ledger` | mcp/src/agents_remember/kernel/memory_cache.py:22-41 |
| The source census and behavioral renderer case keep the producer seam visible. | `test_the_attribution_key_is_named_and_rendered_in_exactly_one_module`; `test_every_census_producer_reaches_the_shared_renderer` | mcp/tests/test_memory_attribution_producers.py:87-117; mcp/tests/test_memory_attribution_producers.py:120-138 |
| None | `attributed_commits`; `parse_code_commit_trailer`; `_trailer_value_from` | mcp/src/agents_remember/kernel/memory_attribution.py:127-140; mcp/src/agents_remember/kernel/memory_attribution.py:143-174; mcp/src/agents_remember/kernel/memory_attribution.py:186-199 |
| None | `AttributedCommit`; `code_commit_exists`; `ledger_rows_from_attribution` | mcp/src/agents_remember/kernel/memory_attribution.py:99-124; mcp/src/agents_remember/kernel/memory_attribution.py:202-205; mcp/src/agents_remember/kernel/memory_attribution.py:208-227 |
| None | `derive_memory_ledger`; "without consulting a cached file or a ledger commit" | mcp/src/agents_remember/kernel/memory_cache.py:22-41 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): stamped the untimestamped Update History entries with this document's own commit clock

- 2026-09-17T03:31:11+02:00 — 2026-09-15 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

- 2026-09-15T06:48:46+02:00 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

- 2026-09-14T23:55+02:00 — 260913-LCA completed-master review follow-up (same uncommitted change
  set, `ar/260913_ledger-commit-attribution`, base `bb65a207`): anchor repoint only, no claim
  change. The review's fix grew `worktrees/ledger_projection.py`, so this card's citations into that
  module and into the ledger test module moved: `worktrees/ledger_projection.code_commit_exists`
  483-486 → 496-499 (twice: the prose and the reference row), `read_ledger_source` 302-350 → 315-363
  (twice), `resolve_memory_source_commit` 274-299 → 287-312, and
  `test_the_rendered_trailer_is_the_one_the_reader_parses` 698-733 → 774-809. Every rewritten range
  was read back at its current position. Verification metadata remains closeout-owned; no acceptance
  claim and no verification stamp advanced.


- 2026-09-15T01:02 UTC — Corrected documentation to match the existing trailer-only runtime, removing transitional cached-table fallback and ledger-commit claims; preserved full-ancestry, last-match, shared-writer, and optional code-object semantics. No runtime change is claimed for this source-comment correction. Working candidate verified by source inspection; commit metadata records real committed history only.



- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of
  11 claim(s) whose anchor no longer sat in its cited range and normalised 8 further range(s) in
  this card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.

- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): this module stopped being read-only. `render_memory_content_message(body,
  code_commit)` (`:72-97`) is now the **one** writer of the trailer, placed beside the one key literal
  because both directions must agree on it; the module docstring, `Purpose` and a new `Logic` paragraph
  record it, and the appended-final-block shape is explained where it is defined (the body may be a
  public multi-paragraph argument of another tool, so the blank line is what keeps the caller's last
  paragraph out of the trailer block). The `Conventions` entry was rewritten from "the model imports
  the key" to "one literal, both directions": `models/closeout/input.py` no longer names the constant at
  all, so `grep -rn '"Code-Commit"' --include=*.py mcp/` still returns exactly one hit but that hit is
  now also the only interpolation. Added the one-literal/one-writer, appended-never-woven, no-fabricated-
  attribution, total-five-producer and rendered-message-is-not-evidence invariants with the measured
  producer sites, and repointed every citation to the grown file (`parse_code_commit_trailer` 103-116 →
  132-145, `attributed_commits` 119-150 → 148-179, `ledger_rows_from_attribution` 184-203 → 213-232,
  `AttributedCommit` 76-100 → 104-118, `code_commit_exists` 178-181 → 207-210, the constant 55 → 56).
  `Todos` keeps the residual gap the census cannot close: a producer building the string some third way
  is caught only by that route's behavioural case, and the prepared memory-content leg has none — the
  census case is what covers it. Verification metadata remains closeout-owned (no commit contains this
  candidate yet); no acceptance claim and no verification stamp advanced.


- 2026-09-13T23:18+02:00 — 260913-LCA-L2 curator (same uncommitted change set): **the two-literal
  defect this card first recorded is fixed, and the entry below stands as the record of what was
  true when it was found.** The L2 curator found it in this pass's first review — the module's
  docstring claimed an import that did not exist — and the owner fixed it in the same change set by
  wiring the direction the layering requires: the writing model now imports the key from here
  (`models/closeout/input.py:9`) and its own literal is deleted, so
  `grep -rn '"Code-Commit"' --include=*.py mcp/` returns exactly one hit — this module's
  declaration, which moved from `:49` to `:55` because the constant's comment block grew to carry the
  reasoning — and every other occurrence is prose. The rejected direction was checked on a concrete
  ground rather than a preference: `layers.toml` declares `order = [errors, kernel, models, ...]`
  with "a module in package P may import package Q only when rank(Q) < rank(P)", so a kernel module
  importing a model would break the declared contract, and a grep over
  `mcp/src/agents_remember/kernel/` finds zero imports of `agents_remember.models`. A new case,
  `test_the_rendered_trailer_is_the_one_the_reader_parses`, drives the real writer's rendered message
  through a real commit and back out through the real reader (the owner reports reintroducing the
  writer-side defect fails exactly that case and nothing else); the test modules keep literal
  `Code-Commit` text as independent oracles on purpose, so those must not be "corrected" to read the
  constant. `Conventions`, `Todos` and the reference rows above are rewritten to the resolved state —
  the history is where the defect stays visible. Every citation in this card was repointed to the
  grown file. Verification metadata remains intentionally empty (unstamped): closeout owns the stamp.


- 2026-09-13T23:06+02:00 — 260913-LCA-L2 curator (uncommitted change set on `ar/260913-lca-l2-ar`):
  created the one-to-one sidecar for this new kernel module. Records the attribution reader — the
  full-ancestry `git log` census, the last-trailer-wins rule in both the commit walk and the
  message parse, the one-row-per-attributed-commit map with the code-commit truth test applied at
  row creation, and the single `cat-file -e` definition the projection's `code_commit_exists` now
  delegates to. States the measured reason the walk is the whole ancestry (at tip `5e4899ea`: 442 of
  the table's 476 rows on the first-parent line, 34 off it, 21 of those still ancestors), the
  boundary that this module only reads and the tracked ledger commit is **not** retired here, and
  the one measured defect it carries: the module docstring says `models/closeout/input.py` imports
  `CODE_COMMIT_TRAILER_KEY` from here, and that import does not exist — the writer declares its own
  literal at `models/closeout/input.py:16`, so the two agree only by value. Verification metadata is
  intentionally empty (unstamped): the candidate is uncommitted and no commit contains this file
  yet, so closeout owns the stamp.

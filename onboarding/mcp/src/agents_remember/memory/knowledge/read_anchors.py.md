# mcp/src/agents_remember/memory/knowledge/read_anchors.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/read_anchors.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:55:00+02:00 |
| lastVerifiedCommitHash | `9b2f775f1ab0fca5f82b4f661785dd8216d4a8b3`|
| lastVerifiedCommitDate | 2026-09-28T17:43:09+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**Observe one recorded source anchor against the requested code tree.** An anchor is a *recorded* claim
about where an obligation is realized, so resolving it can end in several ways that are all facts, and
exactly one of them is "the recorded bytes are there". This module reports which one, and it never
converts an observation into a promotion.

**The rule this module exists to keep is about refusals: a refusal must describe the actual cause.** A
caller must never be told that a path is *absent* when the real reason is its *spelling*. Three outcomes
that used to collapse into one `None` are three genuinely different facts here:

| Outcome | The fact | Who answers it |
| --- | --- | --- |
| `path_absent` | **Git answered, and the requested tree holds nothing at that path.** | `_observed_entry`'s `entry is None` branch — a real absence, the only thing that reports one |
| `unsupported_locator` | **The spelling is not addressable as a confined tree path, so the tree was never asked.** The cause is in `detail`. | `_UnaddressableRecordedPath`, and the symbol-locator branch |
| `recorded_object_unavailable` | **The lookup did not answer**: the requested tree is not in the repository, or Git ran and failed, or Git could not be run at all. | the availability guard, and `_TreeLookupFailed` |

## Code Commentary

### Logic

`anchor_resolver_for(context)` returns the callable a context asks for, and the choice is itself a
statement:

- A context with **no exact code tree** gets `_UnrequestedAnchorResolver`: every anchor is reported
  `not_requested` **and still carries its recorded identity**. That is a supported state, not a degraded
  one — reading recorded knowledge does not require a Git object store, and inventing a resolution (or
  dropping the recorded attribution) would be worse than saying no tree was requested.
- A context naming **both** `repository_root` and `code_tree_id` gets `_TreeAnchorResolver`, whose
  `tree_is_available` is decided **once at construction** (`_tree_exists`, `git cat-file -e <tree>^{tree}`),
  so an unavailable tree is one failure named once instead of an identical per-item error on every page.
- `KnowledgeReadContext` refuses a *half-specified* resolution (tree without root, or root without tree)
  at construction, precisely so this module never has to report a caller's mistake as a fact about an
  anchor.

`observe_anchor` decides in one fixed order, and the order is the contract: `not_requested` →
symbol locator (`unsupported_locator`) → tree unavailable (`recorded_object_unavailable`) → the tree
lookup → the entry. Only the last step can report an absence.

`_observed_entry` turns one `ls-tree` entry into the observation it supports:

- **`None` means one thing only — Git looked and found no entry.** That is `path_absent`; the recorded
  claim and its blob identity are preserved and the obligation is not retired.
- **The entry kind is read from the Git entry *mode*, not the object kind.** Git reports a symlink as
  kind `blob` with mode `120000`, so a mode in `_TREE_ENTRY_MODES` (or a non-`blob` kind) is
  `entry_not_blob` and no path is followed to manufacture source bytes.
- Otherwise the observed object id is compared with the recorded one: `exact_recorded_blob` or
  `recorded_blob_mismatch`. The recorded identity stays on the observation either way, and a mismatch is
  never promoted to a realization of the current bytes.

**On the exact recorded blob the observation also carries the region, as structured values, and only
there.** `AnchorResolution.resolved_ranges` holds the one-based inclusive `LineRangeLocator`s the recorded
locator addresses in those exact bytes, and the model refuses ranges beside any other resolution:

| Locator kind | What `resolved_ranges` carries on `exact_recorded_blob` |
| --- | --- |
| `symbol` | **every** extent the shipped extractor finds defining the name, in order, de-duplicated (`_defining_extents` now returns `(start, end)` pairs; the `detail` sentence is spelled from them and reads exactly as before) |
| `line_range` | the recorded range itself **only if the blob holds those lines** — `_observed_line_range` reads the blob's lines once (`_recorded_lines`, the same call the symbol path makes) and compares the recorded `end_line` with `_line_count` |
| `file` | nothing: a file locator addresses the whole blob and names no range |

**A recorded range past the blob's end keeps `exact_recorded_blob` and carries no range.** Its `detail`
states how many lines the bytes hold and that no range is resolved; a blob whose lines cannot be read is
stated the same way. The resolution deliberately stays `exact_recorded_blob` — it is the blob-identity
fact, which is true, and attribution accounting and diff source-change signatures act on it — so a
consumer that wants the region must read `resolved_ranges`, never infer a region from the resolution
(reclassifying the case as `recorded_blob_mismatch` would change attribution and diff behaviour that
belongs to other owners). `_line_count` counts a final newline as the
end of the last line, not the start of another, and counts blank trailing lines. A recorded range is
never re-anchored, searched for or clipped.

**The path-refusal set, stated once because review corrected this leaf's first attempt at it.** A
recorded path or a path seed is an **address** handed to `git ls-tree`, and what makes such an argument
something other than an address is Git pathspec **magic** — the leading-`:` family (`:(exclude)…`,
`:!…`, `:(top)…`, `:/…`). `_confined_posix_relative` refuses a leading `:`, and also refuses an absolute
path, a `~`-prefixed path, a Windows drive or UNC spelling, a backslash, a NUL, and any empty, `.` or
`..` segment. **The glob characters `*`, `?` and `[` are admitted, not refused** — that refusal was
round 1's over-broad predicate, and it made a legitimate anchor un-authorable, un-seedable, and reported
as `path_absent` for a file the tree really holds.

The Git facts are measured, not reasoned about (`git 2.54.0`; the case at
`mcp/tests/test_knowledge_read_paths.py:256` reproduces them with its own subprocess calls):

| Argument to `git ls-tree <tree> -- <arg>` | rc | Output |
| --- | --- | --- |
| `src/a[1].py` (with `src/a1.py` also present) | 0 | **that** entry |
| `src/a?b.py`, `src/a*b.py` | 0 | **that** entry |
| `src/*.py` | 0 | *no output* — `ls-tree` does not glob |
| `:(exclude)src/x.py`, `:!src/x.py` | 128 | `pathspec magic not supported by this command` |
| `:(top)src/integration.py`, `:/src/integration.py` | 0 | the entry at a **different** location |

`git ls-files 'src/a[1].py'` **does** glob (it lists both `a1.py` and `a[1].py`), which is where the
opposite intuition comes from — but `ls-files` is not the command a stored anchor path is handed to.

**`_tree_entry`'s confinement is structural, not filesystem resolution, and that difference is
deliberate.** `kernel.sidecar_pairing.confine_rel` resolves a path against a real directory and therefore
*follows a symlink*: asked about a recorded path that happens to be a link, it answers with the link's
target, and the tree lookup would then describe the target instead of the entry the anchor recorded. An
anchor is a location inside a Git tree, so the needed check is that the stored spelling is a well-formed
confined POSIX relative path — which is also what the storage boundary applied when the anchor was
written. **A successor that "reuses the existing confinement primitive" here will silently resolve
symlinks.**

**Two producers of `recorded_object_unavailable`, and one branch that is honestly unasserted.** The
availability guard (`tree_is_available == False`) is one; a lookup that did not answer is the other, and
it covers both a non-zero exit and an `OSError` when the Git binary cannot be executed at all. Two rules
a reader must keep:

- The availability guard answers **before** `_tree_entry` is called, so a request pointed at a tree the
  repository does not hold never reaches the non-zero-exit branch. Measured on the frozen bytes: pointing
  the request at the *available* tree is what makes that branch's mutation kill.
- `_tree_entry`'s **non-zero-exit** branch is reachable by no input on this host and is an **explicitly
  disclosed unasserted defensive branch** (L9 ledger entry **A6**). It is *not* coverage; a published
  claim that a mutation made it reachable was withdrawn by the leaf's evidence erratum, because the
  kill that appeared to prove it also appears with the production line untouched. The `OSError` half has
  its own case (`mcp/tests/test_knowledge_read_paths.py:539`).

### Conventions

- A locator whose stored form decoded to a mapping is classified through one accessor
  (`_locator_kind`), so a mapping-decoded symbol locator is not silently reported as a resolved file.
- An identity that decoded as a mapping is read through one accessor (`_identity_object_id`), so the
  recorded identity is reported whatever shape the row took.
- `_parse_ls_tree` reads the first `-z` record; `len(fields) < 3` is treated the same as no record.
- **No content is ever published.** The observation carries identities, an entry kind, a status and, on
  the exact blob, structured line ranges; the bytes stay where they are, which is what keeps a read page a
  facts-only packet rather than a document dump. The blob's lines *are* read — for a `symbol` locator (to
  find its defining extents) and a `line_range` locator (to count lines) on the exact recorded blob only —
  and nothing from them but those numbers leaves this module.

### Invariants And Boundaries

- **`recorded_source_identity` is populated on every outcome, including every failure.** An older, moved,
  absent, unavailable or unresolvable anchor is reported *with* its recorded identity and is never
  promoted to a current realization.
- **No working tree, no `HEAD`, no branch name and no Markdown document is ever consulted.** The only
  object looked at is the exact tree the caller named. `path_absent` and `recorded_blob_mismatch`
  describe that tree and nothing about the working copy.
- **`AnchorResolutionState` still has the owner's seven members; none was added.** The
  unaddressable-spelling case is *mapped* onto `unsupported_locator`, whose `detail` states that the path
  was never addressed against the tree at all. If a distinct member is ever wanted for it, that is an
  owner decision and not a leaf edit.
- **`path_absent` is reported only for a real absence**, and every other refusal names its own cause.
- **Boundary.** This module observes. It does not decide which anchors a selection exposes (that is
  `read.py`'s `resolve_anchor` seam), does not select, does not page, does not refuse a read, and writes
  nothing.

### Todos

None recorded. Two carried observations belong to the owning seat rather than to a defect here: the
`unsupported_locator` mapping for an unaddressable spelling is documented rather than given its own
vocabulary member (an owner decision), and `_tree_entry`'s non-zero-exit branch is disclosed as an
unasserted defensive branch rather than presented as coverage (L9 ledger **A6**).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The three genuinely different facts, and the rule that a caller is never told "absent" for a spelling that was refused.** | `observe_anchor`; `_UnaddressableRecordedPath`; `_TreeLookupFailed` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:104-175; mcp/src/agents_remember/memory/knowledge/read_anchors.py:290-371 |
| **The path-refusal set: leading `:` (pathspec magic), absolute, `~`, drive/UNC, backslash, NUL and empty/`.`/`..` segments refused; `*`, `?` and `[` admitted as literal characters.** | `_confined_posix_relative` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:490-516 |
| **`None` means only "Git looked and found nothing"; the entry kind comes from the entry mode, not the object kind.** | `_tree_entry`; `_parse_ls_tree`; `_observed_entry`; `_TREE_ENTRY_MODES` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:432-463; mcp/src/agents_remember/memory/knowledge/read_anchors.py:519-529; mcp/src/agents_remember/memory/knowledge/read_anchors.py:171-224; mcp/src/agents_remember/memory/knowledge/read_anchors.py:40-44 |
| The shared rule the typed write and seed boundaries apply, with the measured Git table in its docstring. | `require_plain_git_path` | mcp/src/agents_remember/models/knowledge/base.py:59-92 |
| The two resolvers, and why an unrequested tree is a supported state rather than a degraded one. | `anchor_resolver_for`; `_UnrequestedAnchorResolver`; `_TreeAnchorResolver`; `_tree_exists` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:50-101; mcp/src/agents_remember/memory/knowledge/read_anchors.py:248-252 |
| The observation vocabulary this module reports into (seven members), declared in `read_anchor.py` and imported through `read.py`'s re-export, with the validator that refuses ranges beside any resolution other than the exact recorded blob. | `AnchorResolutionState`; `AnchorResolution`; `_require_ranges_only_on_the_recorded_bytes` | mcp/src/agents_remember/models/knowledge/read_anchor.py:27-35; mcp/src/agents_remember/models/knowledge/read_anchor.py:48-78 |
| **The dispatch that sends an exact-blob `symbol` or `line_range` locator to its range-measuring observer and answers a `file` locator with no range.** | `_observed_line_range`; `_observed_symbol` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:203-214; mcp/src/agents_remember/memory/knowledge/read_anchors.py:227-300; mcp/src/agents_remember/memory/knowledge/read_anchors.py:303-351 |
| **A symbol's every defining extent carried as structured ranges, with the unchanged `detail` sentence spelled from them.** | `_observed_symbol`; `resolved_ranges` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:227-300 |
| **A recorded line range published as a resolved range only when the exact blob holds those lines; past the end, or unreadable, it keeps `exact_recorded_blob` and carries none.** | `_observed_line_range` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:303-351 |
| How many lines a blob holds, where a final newline ends the last line. | `_line_count` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:354-357 |
| The extractor's defining extents as distinct `(start, end)` pairs rather than spelled strings. | `_defining_extents` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:379-392 |
| **The cases that pin the ranges: two members at distinct ranges in one file, a double definition carrying both ranges, a range past the blob end unresolved, and a mismatched blob carrying none.** | "test_a_recorded_range_past_the_blob_end_is_unresolved_with_no_range"; "test_a_symbol_defined_twice_carries_every_defining_range" | mcp/tests/test_review_family_member_sources.py:339-351; mcp/tests/test_review_family_member_sources.py:354-361 |
| **The case that pins the three facts apart: an unaddressable stored spelling refused rather than reported absent.** | "test_a_stored_path_that_cannot_be_addressed_is_refused_rather_than_reported_absent" | mcp/tests/test_knowledge_read_paths.py:370-444 |
| **The case that drives the second producer: a Git this process cannot run.** | "test_a_git_that_cannot_run_is_unavailable_rather_than_an_absent_path" | mcp/tests/test_knowledge_read_paths.py:539-644 |
| **The case that shows a failed lookup is unavailable rather than absent.** | "test_a_failed_tree_lookup_is_unavailable_rather_than_an_absent_path" | mcp/tests/test_knowledge_read_paths.py:445-538 |
| **The case that authors, stores, seeds and resolves a path holding glob characters to its own blob, and measures the Git facts itself.** | "test_a_path_holding_glob_characters_is_authorable_seedable_and_observed_as_its_blob" | mcp/tests/test_knowledge_read_paths.py:256-369 |
| The non-blob entry case, and the ordinary absent-path case. | "test_a_non_blob_tree_entry_is_reported_as_an_entry_and_never_read_as_source_bytes"; "test_a_path_absent_from_the_requested_tree_keeps_the_claim_and_reports_the_absence" | mcp/tests/test_knowledge_read_boundaries.py:375-464; mcp/tests/test_knowledge_read_boundaries.py:264-286 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Git is invoked as a subprocess against the
repository root the caller supplied; no second repository, ledger or coordination path is read.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): the resolver now reports the region an exact recorded blob supports as structured `resolved_ranges` (every defining extent of a symbol; a recorded line range only when the blob holds those lines; none for a file locator), with `detail` unchanged. Recorded the bound check (`_observed_line_range`, `_line_count`), that an out-of-range recorded range keeps `exact_recorded_blob` and carries no range, and corrected the convention that no content is read (the exact blob's lines are read to measure extents and bounds; nothing but numbers leaves the module). Re-pointed the vocabulary row to `read_anchor.py` and re-measured shifted ranges. No verification stamp was advanced.

- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-20T01:02:52+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): verified the 3 enforced citation rows this card carried (citation_anchor_absent_from_range ×3) by hand-reading `mcp/src/agents_remember/memory/knowledge/read_anchors.py`: `_observed_entry` is declared at 168 (range `:168-219`), `_tree_entry` at 368 (range `:368-399`) and `_parse_ls_tree` at 455 (range `:455-465`), so each named anchor sits inside a cited range and the earlier mechanical projection was correct; the claim wording, the anchors and every range are unchanged (including the extra `:37-41` cell), and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 3 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `_observed_entry`; `_parse_ls_tree`; `_tree_entry`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-19T22:28:52+00:00: Generated citation repair: `_confined_posix_relative` repointed to mcp/src/agents_remember/memory/knowledge/read_anchors.py:426-452. No content impact: mechanical anchor-range projection bound to citation source snapshot 440311ed835ff15c77271ad85c2bef2103d2b46ebe061b96476b211b3d19cd24; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `read_anchors.py.md:163` (`_tree_entry`, `_parse_ls_tree`, `_observed_entry`, `_TREE_ENTRY_MODES`).

- 2026-09-18T19:56:02+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the one enforced `citation_anchor_absent_from_range` row in this document.** The absent-path row cited `test_knowledge_read_boundaries.py:230-252`, an earlier node's body, for `test_a_path_absent_from_the_requested_tree_keeps_the_claim_and_reports_the_absence`; the case itself spans `264-286`, which is what that cell cites now. The non-blob range at `375-464` and the claim are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the recorded-anchor observation. It records the **three genuinely different facts** the read path distinguishes — `path_absent` (Git answered and the tree holds nothing there), `unsupported_locator` (the spelling is not addressable, with the cause in `detail`) and `recorded_object_unavailable` (the lookup did not answer) — and the rule behind them: **a refusal must describe the actual cause**, so a caller is never told a path is absent when the real reason is its spelling. That rule is also why the card states the corrected predicate explicitly: pathspec **magic** is the leading-`:` family plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and NUL, while `*`, `?` and `[` are **literal characters** to `ls-tree` and a legitimate anchor containing them must be authorable, seedable and resolvable — round 1's over-broad glob refusal is recorded as the thing the review corrected. The measured Git table (`git 2.54.0`) is carried with the case that reproduces it, together with the note that `git ls-files` is what globs and is not the command this path is handed to. The card also states the structural-confinement rule (never `confine_rel`, which follows a symlink), the entry-mode-versus-object-kind rule, and the honest limit: `_tree_entry`'s non-zero-exit branch is an explicitly disclosed unasserted defensive branch (L9 ledger **A6**) and is **not** coverage. Verification metadata remains empty until closeout stamps the code commit.

# mcp/src/agents_remember/memory/knowledge/read_anchors.py

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

**It also remembers, for the life of the process, the answers Git and the parser gave about complete
object ids** (tree entries, blob lines, per-blob definitions), so repeated observation of the same
anchors — every owner of one review, every subject of one comparison — costs one Git read and one parse
per object instead of one per observation. The tables live in
[`read_anchor_memo.py`](read_anchor_memo.py.md); **what may be remembered, and what never is, is decided
here** (see *The process-lifetime memo* below). Responses are byte-identical with and without it.

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
  **That probe is never remembered across resolvers**: every new resolver asks Git again, because whether
  a repository still *holds* a tree is a fact about the repository, not the id (review L56-R1-F1).
- `KnowledgeReadContext` refuses a *half-specified* resolution (tree without root, or root without tree)
  at construction, precisely so this module never has to report a caller's mistake as a fact about an
  anchor.

`observe_anchor` decides in one fixed order, and the order is the contract: `not_requested` →
tree unavailable (`recorded_object_unavailable`) → the tree lookup (an unaddressable spelling is
`unsupported_locator`, a lookup that did not answer is `recorded_object_unavailable`) → the entry, where
a `symbol` or `line_range` locator on the exact recorded blob is measured. Only the entry step can
report an absence. (An earlier account put a symbol-locator refusal before the tree check; since the
symbol observer landed, a symbol locator is resolved *after* the exact-blob match, in `_observed_symbol`,
and is `unsupported_locator` only when its path has no grammar or the grammar or blob cannot be read.)

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
| `symbol` | **every** extent the shipped extractor finds defining the name, in order, de-duplicated (`_blob_definitions` parses the blob once and keeps each defined name's distinct `(start, end)` pairs; `_defining_extents` looks the name up in that mapping; the `detail` sentence is spelled from them and reads exactly as before) |
| `line_range` | the recorded range itself **only if the blob holds those lines** — `_observed_line_range` reads the blob's lines once (`_recorded_lines`, the same read `_blob_definitions` makes for the symbol path) and compares the recorded `end_line` with `_line_count` |
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

**The process-lifetime memo (260921-ICR-L56, ICR-R24@v3).** A first visit to a family or invariant
subject used to spend most of its time re-observing the same anchors (hundreds of Git spawns and ~100
tree-sitter parses for ~20 tree paths and ~18 blobs). Three answers are now remembered in
[`read_anchor_memo.py`](read_anchor_memo.py.md), each keyed by the repository root Git runs against plus
the complete object id(s) the answer is a function of:

| Table | Key | Filled by | What is remembered |
| --- | --- | --- | --- |
| `TREE_ENTRIES` | (root, tree id, confined path) | `_tree_entry` | the parsed `ls-tree` entry **or `None`** — Git's own "no entry at this path" about an existing immutable tree is as permanent as a found entry |
| `BLOB_LINES` | (root, blob id) | `_recorded_lines` | the blob's lines as an immutable **tuple**, because one answer is shared by every later caller |
| `BLOB_DEFINITIONS` | (root, blob id, grammar of the path's suffix) | `_blob_definitions` | a read-only mapping of every defined name to its distinct `(start, end)` extents — one parse serves every symbol anchored in the blob, and one grammar's parse is never served for another's |

The rules a successor must keep, because each was either a review finding or is what makes "never
stale" true:

- **Only answers are remembered, and only for a complete id.** A value is put *after* Git or the parser
  answered; `OSError`, a non-zero exit, `_BlobUnreadable` and `GrammarUnavailableError` all leave the
  memo untouched, so a later success is observed. A question asked with a ref, `HEAD` or an abbreviation
  is never remembered (`is_complete_object_id` is the one admission test).
- **Whether the repository holds the tree is never remembered.** `_tree_exists` runs on every resolver
  construction and the remembered answers are consulted only behind a probe that succeeded, so a tree
  that was released and pruned, lost its alternate or became unreadable is reported
  `recorded_object_unavailable` for every anchor, exactly as before the memo. An earlier attempt
  remembered positive probes and was blocked for this (review L56-R1-F1).
- **Two documented residuals sit outside that guard** (they are in the module docstring, not defects to
  "fix" silently): a repository that still holds the tree but has lost one of its blobs (corruption, or
  a partial clone whose promisor never supplied it) is answered from memory for a blob read earlier in
  the same process; and a caller of `observe_anchor` that builds no resolver skips the probe altogether.
  The one such production caller is curator ingest (`knowledge_curator_ingest._observe`), which reads the
  tree's membership in the same run before it observes.
- **No invalidation exists and none is needed**: every key is an immutable object id. The bounds cap
  memory only (see the memo card for their approximate-weight semantics).
- **Nothing about the response changed.** Base and memo candidate served sha256-identical bodies on
  every review route measured (66 URLs); the memo is invisible to callers and no signature changed.

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
- **A remembered answer is only ever a content fact keyed by complete object ids**, never a failure,
  never an abbreviation or ref, and never the fact that a repository holds an object; the observation
  a caller receives is the one the unremembered path gives.
- **Boundary.** This module observes. It does not decide which anchors a selection exposes (that is
  `read.py`'s `resolve_anchor` seam), does not select, does not page, does not refuse a read, and writes
  nothing.

### Todos

None recorded. Two carried observations belong to the owning seat rather than to a defect here: the
`unsupported_locator` mapping for an unaddressable spelling is documented rather than given its own
vocabulary member (an owner decision), and `_tree_entry`'s non-zero-exit branch is disclosed as an
unasserted defensive branch rather than presented as coverage (L9 ledger **A6**).

The module is at 597 lines after 260921-ICR-L56, at the top of the 600-line healthy band, so the next
addition here should consider a split first.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The three genuinely different facts, and the rule that a caller is never told "absent" for a spelling that was refused.** [1]
- **The path-refusal set: leading `:` (pathspec magic), absolute, `~`, drive/UNC, backslash, NUL and empty/`.`/`..` segments refused; `*`, `?` and `[` admitted as literal characters.** [2]
- **`None` means only "Git looked and found nothing"; the entry kind comes from the entry mode, not the object kind.** [3]
- The shared rule the typed write and seed boundaries apply, with the measured Git table in its docstring. [4]
- The two resolvers, and why an unrequested tree is a supported state rather than a degraded one. [5]
- The observation vocabulary this module reports into (seven members), declared in `read_anchor.py` and imported through `read.py`'s re-export, with the validator that refuses ranges beside any resolution other than the exact recorded blob. [6]
- **The dispatch that sends an exact-blob `symbol` or `line_range` locator to its range-measuring observer and answers a `file` locator with no range.** [7]
- **A symbol's every defining extent carried as structured ranges, with the unchanged `detail` sentence spelled from them.** [8]
- **A recorded line range published as a resolved range only when the exact blob holds those lines; past the end, or unreadable, it keeps `exact_recorded_blob` and carries none.** [9]
- How many lines a blob holds, where a final newline ends the last line. [10]
- The extractor's defining extents as distinct `(start, end)` pairs rather than spelled strings, computed once per blob and grammar and looked up per name. [11]
- **The memo's three content answers: a tree entry (or its definite absence), a blob's lines as a tuple and a blob's definitions per grammar — each remembered only after Git or the parser answered, and only for a complete id.** [12]
- **The tree probe that is never remembered, run once per resolver, and the guard that serves remembered answers only behind it; the two residuals stated in the module docstring.** [13]
- The tables, their keys and the one admission test for a key. [14]
- **The cases that pin the memo: one read per object and identical answers, a failure asked again, an abbreviation never remembered, a pruned or revoked tree reported unavailable, no cross-repository or cross-grammar reuse.** [15]
- **The cases that pin the ranges: two members at distinct ranges in one file, a double definition carrying both ranges, a range past the blob end unresolved, and a mismatched blob carrying none.** [16]
- **The case that pins the three facts apart: an unaddressable stored spelling refused rather than reported absent.** [17]
- **The case that drives the second producer: a Git this process cannot run.** [18]
- **The case that shows a failed lookup is unavailable rather than absent.** [19]
- **The case that authors, stores, seeds and resolves a path holding glob characters to its own blob, and measures the Git facts itself.** [20]
- The non-blob entry case, and the ordinary absent-path case. [21]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Git is invoked as a subprocess against the
repository root the caller supplied; no second repository, ledger or coordination path is read.

No meaningful cross-repo references found.

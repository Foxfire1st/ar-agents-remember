# mcp/src/agents_remember/application/published_intent.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Select published text knowledge for the ordinary paired read. Its coordination context names the exact memory root; the route captures that tree and reads its derived index beside the requested source.

## Code Commentary

### Logic

`resolve_published_intent` selects a converted memory tree or reports `legacy-format`. `converted_memory_tree` accepts only a directory holding `knowledge/layout.json`; a `knowledge.sqlite` file and a parent inferred from its filename are not accepted tree inputs. Selection requires a coordination root for the derived cache, and partial indexes stay incomplete.

Source resolution is a root/tree pair or is unrequested, never half-invented. Path seeds prepare family-complete leaf selections; identity seeds use the scope walk. The whole knowledge block fits the shared threshold and resumes through `knowledge_read`.

### Invariants And Boundaries

Text in Git is the publication. No canonical published dataset path, database publication owner or read fallback remains. Unconverted memory is legacy format even before a database was published. A knowledge refusal does not erase returned source bytes. Currentness reports observations against the exact code tree without withholding stale content or changing intent.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository: `system/sources.md` carries no
`Domain Documentation` entries, so there is no live source to retrieve. The statements below are grounded in
repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- The selected index supplies its own identity; no canonical dataset or caller-asserted identity is selected. [4]

- **The source-resolution pair, resolved together or left unrequested because the read context refuses either half alone.** [6]

- The ordinary route selects converted text knowledge or reports legacy format without a database fallback. [7]

- **The read itself: the shipped taskless context constructor plus the shipped selective read, with `task_ref` left unset and identity seeds passed through; every page is then bound to the tree's index state.** [8]
- **The converted-tree route: which path names a converted tree, the one dataset resolution every knowledge read applies, the refusal without a coordination root, and the index selection that recomputes the tree key.** [9]
- **The ordinary read's converted-tree selection: `None` for an unconverted root, an `unusable` state when the tree cannot be indexed, and no authority-home check because the index is keyed by its tree alone.** [10]
- **MIK-R03: the `currentness` block at the resolved source tree, named with its `treeScope` and computed once inside the bounded block; with no pair, every realized invariant is unverifiable.** [12]

- The complete text-tree knowledge block is bounded by the shared threshold. [13]

- **MIK-R02: a memory-tree seed is prepared for the block, not read as a budgeted page; since MIK-R01 a path seed by the leaf read, an identity seed by the scope read.** [14]
- **MIK-R01: the block's currentness merges the leaf and scope subsets, and its top-level policy follows the seeds asked (rulings Q5 and N5).** [15]
- **MIK-R01: an index that is not the selected tree's is a named seed failure.** [16]
- **The module docstring paragraph for the family-complete leaf read.** [17]
- **MIK-R05: the docstring states the route-chain families after the leaf content, an entry-less path still returning them, and the refusal of a path with neither.** [18]
- **MIK-R05: a path seed's `registration_absent` refusal carries its route chain.** [19]
- **The module docstring paragraph for the bounded block and its continuation.** [20]
- **The module docstring paragraph for the currentness block.** [21]
- The published-intent case: the resolved tree and `treeScope`, an uncommitted edit that changes nothing, and no resolved tree. [22]
- **A page from a partial index is never presented as complete.** [23]
- **The two shipped owners this module delegates the read to, reused unchanged.** [24]
- **A path no recorded anchor could carry is refused as a seed instead of being answered with an absence this read never observed.** [27]
- **A value that is not one of the typed seeds is a named refusal naming its own Python type, never an `AttributeError` from inside the read.** [28]
- **One item exactly as the read selected it: dumped by its own model, excluding `None` without dropping a recorded value.** [29]
- **The recorded block that names the dataset, its snapshot, the source pair and — only for a converted memory tree — the `memoryTree` binding, and the block a publication that could not be read answers with.** [30]
- **The failure set modelled as input facts, so a paired read never aborts because a repository's knowledge file was foreign.** [31]
- The dataset identity reader reused here: it answers an identity or a reason, and never raises for a caller. [32]
- The one Git command this route runs, through the shared owner. [34]
- The scope-selection rule the read reports when a seed selects nothing, and the recorded-but-real selection it serves instead of refusing. [35]
- The typed seeds and budget this route constructs, and the policy version the recorded block carries. [36]
- The refusal and item shapes this route renders without re-spelling. [37]
- The storage failure class the input-fact set is built around. [38]
- **The resolver rule this card's memory-root paragraph states: the contract's memory worktree when one is in scope, the canonical external memory root otherwise.** [39]

- The ordinary route selects text-tree indexes, refuses malformed seeds, names absent registration and opens no unconverted canonical database. [40]

- **The mounted-route cases. Since MIK-R24 the ordinary `read_ar_files` call on an unconverted memory tree returns no knowledge section (`legacy-format`), so the two cases assert that; this module's block is measured directly by the route cases.** [41]
- The carrier-parity case that holds the retrieval instructions to the payload's real field spellings. [42]
- The route the ordinary read attaches this block from, the import it attaches it through, and the response field it travels on. [43]

- Unconverted roots refuse retired database selection and mounted tools open no legacy database. [44]



- Only a converted root directory is admitted as a knowledge selection; a database path is refused. [46]


### Cross-Repo References

No cross-repository behavior is implemented in this file. The read is addressed at one dataset inside the
memory layer this repository's own coordination declaration resolves, and reaches no sibling repository.

No meaningful cross-repo references found.

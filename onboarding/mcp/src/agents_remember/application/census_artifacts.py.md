# mcp/src/agents_remember/application/census_artifacts.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](overview.md)

## Purpose

**The census artifact store: an addressable digest, the measured pair identity, and a bounded, ledger-owned lifetime (MIK-R198 rules 1-2).** A whole-tree census is tens of megabytes, so `citation_census_tool` answers a bounded row window and hands the complete population here. This module owns the three obligations the census itself does not have: the artifact an answer advertises keeps resolving to the bytes and digest it named, its metadata names the trees that were actually measured rather than the directories a caller typed, and the store it lands in is bounded by an owner that reclaims it.

## Code Commentary

### Logic

- `write_census_artifact(config, full, artifact_path, *, repo_id, inputs)` serialises the whole population once (`json.dumps(..., indent=1, sort_keys=True, default=str)` plus a trailing newline) and digests that text with SHA-256, so the answered digest is the digest of the answered bytes. It returns `artifactPath`, `artifactSha256`, `artifactTargets`, `artifactInputIdentities`, `artifactPairStableDuringRead` and `artifactRetention`.
- A caller-named `artifact_path` must resolve inside the coordination root (`require_within_coordination`). Outside `temp/census/` it is written directly and answered with `_caller_retention()`: the store's ledger is never consulted, because the address belongs to the caller.
- Inside the store folder, or when no path is named, the write runs under `exclusive_file_lock` over the store's own ledger, so ownership transfer, writing and retirement are one transaction across threads and processes.
- A default artifact's name carries the digest of its own bytes (`<stamp>-<repo_id>-census-<digest[:12]>.json`): two populations measured in the same formatted second land at two addresses and neither can replace the other. An identical re-measurement that selects the same timestamp-and-digest address finds the file already holding its digest and answers that address instead of writing a twin. A measurement in a later formatted second selects a new timestamped address.
- Ownership is explicit. `_owned_ledger` reads the names this store wrote as defaults, and `_set_ownership` records or relinquishes one without rewriting an unchanged ledger. Reclamation may therefore delete only bytes this store wrote as a default: a caller-named file that happens to sit in the folder, even one whose name looks like a default's, is never deleted by a policy it never agreed to (L191-A3-04).
- `reclaim_census_artifacts(coordination_root, *, keep)` sorts the ledger's surviving files newest-first by mtime, keeps `CENSUS_ARTIFACT_KEEP`, unlinks the rest, and never unlinks the file just written. It rewrites the ledger only when something was reclaimed, and returns the names it pruned so the answer can state them.
- `tree_identity(root)` answers `{kind: git, commit, worktreeTree}` for a worktree, `{kind: directory, contentSha256}` for a plain directory, `{kind: absent}` for a missing root and `{kind: unreadable}` when Git cannot be run. The working-tree tree object is built through a throwaway index (`run_git_with_index`), so measuring a tree writes no index entry into the tree it measures and stages nothing. The root is resolved first, because a relative root reaches Git as a path it cannot enter and would silently degrade a Git identity to a content digest.
- `pair_identities` composes the two sides for the answer. `directory_files` captures a plain directory once, so hashing and census resolution consume the same bytes, and `directory_digest` hashes path, a NUL separator and each file's SHA-256 in sorted order.

### Conventions

- `CensusInputs` is the typed capture the answer's `artifactInputIdentities` and `artifactPairStableDuringRead` report; it is built in `application/census_inputs`, which reads the trees this module identifies.
- The retention answer carries its policy in words: the store folder, the keep count, the pruned names, and a `lifetime` of `"owned by the caller"` for a caller-named artifact, otherwise the stated keep-then-reclaim sentence.

### Invariants And Boundaries

- **An advertised digest always resolves.** A named path holding other bytes is replaced, and a default address is never overwritten by a different population.
- **Ownership comes from the ledger, never from the folder's contents.** A retention policy applies only to bytes this store wrote as a default, so the lifetime the answer states for a caller-named artifact stays true.
- **Measuring a tree does not touch it.** The index the identity stages into is temporary, so neither the worktree's index nor its contents change.

### Todos

None recorded.

## Evidence

- The entry point writes the whole population and answers its path, digest, target count, input identities, stability and retention. [1]
- The store retains twenty default artifacts before reclaiming the oldest. [2]
- The store's ownership ledger is its own file in the store folder. [3]
- The typed capture the answer reports as its input identities. [4]
- A caller-named path outside the coordination root is refused by name. [5]
- The retention answer a caller-named artifact receives. [6]
- The store write under the lock: digest-named address, identical-remeasurement reuse, refusal to overwrite a caller's still-valid receipt. [7]
- The ledger names only what this store wrote as a default. [8]
- Ownership is granted or relinquished without rewriting an unchanged ledger. [9]
- Reclamation keeps the newest owned artifacts, reclaims the rest and never the file just written. [10]
- The pair identity composes one identity per side. [11]
- A Git tree identity is built through a throwaway index; absent and unreadable roots are named kinds. [12]
- A plain directory is captured once into a path-keyed byte map. [13]
- The content digest covers each path and its bytes in sorted order. [14]
- Two populations measured in one second keep two retrievable addresses. [15]
- The bounded store names every retirement, under concurrent writes. [16]
- A relative root measures the same identity as an absolute one. [17]
- A named path holding other bytes is replaced so the advertised digest resolves. [18]
- A caller-named artifact in the store folder is never reclaimed, including a former default's transfer to the caller. [19]

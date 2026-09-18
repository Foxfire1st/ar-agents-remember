# mcp/tests/test_knowledge_read_paths.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_read_paths.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `65e3791bce458eb6265f752889435a1bcaac5f2e`|
| lastVerifiedCommitDate | 2026-09-18T06:16:59+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l07` uncommitted source; base `4eb2b1992f6183fba06e9f31aa664d9a93094c26` |
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**What a *path* is to this read: an address, not a pattern.** Five nodes in `integration` (row
`mcp/tests/test-evidence-lanes.toml:158`) covering the one contract the review corrected most sharply — the
predicate that decides which spellings are addressable, and the requirement that **a refusal describe the
actual cause**.

644 lines. This module exists because the path cases pushed `test_knowledge_read_boundaries.py` past the
repository's 1 200-line hard limit in fix round 2; the cases moved here rather than the limit being waived.

## Code Commentary

### Logic

**`test_a_pathspec_magic_spelling_is_refused_by_the_typed_path_and_never_answered_as_absence`** (`:178`) —
the boundary node. It refuses a leading-`:` spelling at **both** typed boundaries (`SourceAnchorDraft`'s
write path and `PathSeed`'s seed path) and measures the Git facts themselves with its own subprocess calls,
so the premise is evidence rather than prose.

**`test_a_path_holding_glob_characters_is_authorable_seedable_and_observed_as_its_blob`** (`:256`) — the
node the review's correction rests on. It commits its own tree holding **both** `src/a1.py` and
`src/a[1].py`, measures `git ls-tree` addressing `src/a[1].py` literally with `rc=0`, then (1) authors a
`SourceAnchorDraft` at that path through the typed write path, (2) stores the claim and anchor through the
ordinary store operation, (3) constructs `PathSeed(path="src/a[1].py")`, and (4) reads it back through
`read_knowledge_scope` asserting `exact_recorded_blob` with the observed blob equal to the tree's blob.
**The mutation that inverts this result is the read path re-admitting a glob refusal**, which flips the
outcome to `unsupported_locator` — the exact flip the reviewer measured on the pre-fix candidate.

**`test_a_stored_path_that_cannot_be_addressed_is_refused_rather_than_reported_absent`** (`:370`) — a row
written by something other than the typed API is reported `unsupported_locator` with the spelling refusal
in `detail`, **not** `path_absent`.

**`test_a_failed_tree_lookup_is_unavailable_rather_than_an_absent_path`** (`:445`) and
**`test_a_git_that_cannot_run_is_unavailable_rather_than_an_absent_path`** (`:539`) — the two producers of
`recorded_object_unavailable` pinned separately. The second drives the `OSError` producer by intercepting
the single `ls-tree` call while delegating every other command to the real runner; the first reads a real
stored anchor against a tree the repository does not hold and asserts the availability producer's own
`detail`, while the same claim against the fixture's real tree is a genuine `path_absent`.

**The rule, restated once:** Git pathspec **magic** is the leading-`:` family (`:(exclude)`, `:!`,
`:(top)`, `:/`) plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and NUL. The characters
`*`, `?` and `[` are **literal characters** to `ls-tree`, so a legitimate anchor containing them must be
authorable, seedable and resolvable — and **a caller must never be told a path is absent when the real
reason is its spelling.** `git ls-files` is the command that *does* glob those characters, and it is not the
command a stored anchor path is handed to.

### Conventions

- `pytestmark = pytest.mark.integration`; the module is registered in the integration lane, and it is one
  of the three declared consumers of `knowledge-read-scope-cases`.
- Every Git fact the module relies on is measured by the module itself with `subprocess`, against a tree it
  commits in `tmp_path`.
- A refusal node asserts the resolution state **and** the `detail`'s distinguishing content, because for
  this contract the code alone (`unsupported_locator`) is deliberately shared with the symbol-locator case.

### Invariants And Boundaries

- **The non-zero-exit branch of `_tree_entry` is not covered here or anywhere.** This module drives the
  `OSError` producer and the availability producer; the third branch is an explicitly disclosed unasserted
  defensive branch (L9 ledger **A6**). The erratum withdrew the claim that a mutation made it reachable.
- **A sibling node in the boundaries module carries a `detail` assertion at `:521-526`** which is a
  pre-existing node's extension, not a new case — a fact the round's own change summaries under-described.
  It is recorded here so a successor reading the change set sees four edits rather than three.
- **Boundary.** This is a test module. It declares one lane, asserts behaviour and owns no production
  contract.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The pathspec-magic boundary node: a leading-`:` spelling refused at both typed boundaries, with the Git facts measured by the module itself.** | "test_a_pathspec_magic_spelling_is_refused_by_the_typed_path_and_never_answered_as_absence" | mcp/tests/test_knowledge_read_paths.py:178-255 |
| **The glob-character node the review's correction rests on: authored, stored, seeded and resolved to its own blob.** | "test_a_path_holding_glob_characters_is_authorable_seedable_and_observed_as_its_blob" | mcp/tests/test_knowledge_read_paths.py:256-369 |
| **The unaddressable-stored-spelling node: a refusal of the spelling, never an absence from the tree.** | "test_a_stored_path_that_cannot_be_addressed_is_refused_rather_than_reported_absent" | mcp/tests/test_knowledge_read_paths.py:370-444 |
| **The lookup that ran and could not answer, refused as unavailable rather than absent.** | "test_a_failed_tree_lookup_is_unavailable_rather_than_an_absent_path" | mcp/tests/test_knowledge_read_paths.py:445-538 |
| **The lookup that could not be run at all, reported as the same fact.** | "test_a_git_that_cannot_run_is_unavailable_rather_than_an_absent_path" | mcp/tests/test_knowledge_read_paths.py:539-644 |
| **The corrected predicate this module measures: leading `:` refused; `*`, `?` and `[` admitted as literal characters.** | `_confined_posix_relative`; `require_plain_git_path` | mcp/src/agents_remember/memory/knowledge/read_anchors.py:308-334; mcp/src/agents_remember/models/knowledge/base.py:59-92 |
| **The write-path boundary that applies the shared rule, so a malformed anchor cannot be authored.** | `SourceAnchorDraft` | mcp/src/agents_remember/models/knowledge/source.py:82-127 |
| **The seed boundary that applies the same rule, so a refused spelling cannot be presented as a seed.** | `PathSeed` | mcp/src/agents_remember/models/knowledge/read.py:144-171 |
| **The pre-existing sibling node's `detail` assertion, which round 3 added (the fourth worktree edit).** | "the unavailable tree is the producer that answers here, and its detail says which fact it is" | mcp/tests/test_knowledge_read_paths.py:451-542 |
| The lane row this module occupies. | "mcp/tests/test_knowledge_read_paths.py" | mcp/tests/test-evidence-lanes.toml:167-167 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/test-evidence-lanes.toml:166-166` -> `mcp/tests/test-evidence-lanes.toml:167-167`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-18T02:37:44+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_paths.py" repointed to mcp/tests/test-evidence-lanes.toml:166-166. No content impact: mechanical anchor-range projection bound to citation source snapshot d211cfd02f11c0600198b11c621aa5574ac8743db6e0ca1d2c92936e561c5146; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T22:33:10+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_paths.py" repointed to mcp/tests/test-evidence-lanes.toml:164-164. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_read_paths.py" repointed to mcp/tests/test-evidence-lanes.toml:160-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the path-contract module. It records **the contract the review corrected**: pathspec **magic** is the leading-`:` family (`:(exclude)`, `:!`, `:(top)`, `:/`) plus `..`, absolute paths, `~`, drive/UNC spellings, backslashes and NUL, while `*`, `?` and `[` are **literal characters** to `ls-tree` and a legitimate anchor containing them must be authorable, seedable and resolvable; and the rule underneath it — **a caller must never be told a path is absent when the real reason is its spelling**, which is why the read path distinguishes `path_absent`, `unsupported_locator` (with the cause in `detail`) and `recorded_object_unavailable`. It records the two producers of `recorded_object_unavailable` pinned separately and, honestly, that `_tree_entry`'s non-zero-exit branch remains an **unasserted defensive branch** (L9 ledger `A6`) whose withdrawn mutation claim the erratum corrected. It also records the fourth worktree edit the round's own summaries under-described — the `detail` assertion added to the pre-existing sibling node at `:521-526`. Verification metadata remains empty until closeout stamps the code commit.

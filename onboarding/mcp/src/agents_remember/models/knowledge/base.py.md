# mcp/src/agents_remember/models/knowledge/base.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/base.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash |  `1ff1893f44d875073d58af863238501a6be35288`|
| lastVerifiedCommitDate |  2026-09-16T23:58:57+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The frozen base class and the shared identifier/length validators every persisted knowledge value inherits:
canonical UUID spelling, the SHA-256 and Git-object patterns, the prose/label/reference/path length ceilings,
the two authored origin states and the `KnowledgeState` union.

## Code Commentary

### Logic

`KnowledgeModel` is a Pydantic `BaseModel` with `ConfigDict(extra="forbid", frozen=True)`. `extra="forbid"`
makes an undeclared field a refusal rather than silently dropped input; `frozen=True` makes the process-local
value immutable.

Module constants: `UUID_PATTERN` (lowercase hyphenated UUID text), `SHA256_PATTERN` (`^[0-9a-f]{64}$`),
`GIT_OBJECT_PATTERN` (40- or 64-hex Git object identity), `PROSE_MAX_LENGTH` 20000, `LABEL_MAX_LENGTH` 512,
`REFERENCE_MAX_LENGTH` 1024, `PATH_MAX_LENGTH` 4096, and `PROPOSED_STATE`/`ACCEPTED_STATE` with the
`KnowledgeState` literal union that both name.

`normalized_uuid` accepts a `UUID` instance or UUID text and returns the canonical stored spelling. It strips
and lowercases, parses, and then compares `str(parsed)` against the canonical form, raising `ValueError` with the
non-canonical input when they differ.

`require_consistent_acceptance` is the shared authored-value rule for an origin state: accepted origin data is
accepted because a named authority accepted it, so a non-blank `acceptance_ref` is required; a proposed revision
that carried one would claim an acceptance that never happened. It is called by **both** revision aggregates at
construction — `InvariantRevision` (which previously inlined the same two checks) and `FamilyRevisionDraft` — so
the rule has one owner and a new revision kind inherits it instead of restating it.

`require_plain_git_path(value, *, what)` is the shared **pathspec rule**, added by 260915-KS-L7, and it is the one
place a Git-pathspell question is answered. A recorded path or a path seed is handed to `git ls-tree` as an
argument, and what makes such an argument something other than an address is pathspec **magic**: a spelling that
begins with `:` is read by Git as a pathspec — `:(exclude)…` and `:!…` make `ls-tree` exit non-zero, and
`:(top)…`/`:/…` are accepted and answer about a **different** location. The rule refuses a leading `:` and returns
the value unchanged otherwise; the surrounding absolute / `~` / drive / UNC / backslash / NUL / empty / `.` / `..`
refusals live at the two typed call sites (`SourceAnchorDraft` in `source.py`, `PathSeed` in
`models/knowledge/read.py`).

**The characters `*`, `?` and `[` are deliberately admitted, and that is the corrected half of this rule.** They
are *not* magic to `ls-tree`: measured against `git 2.54.0`, `git ls-tree <tree> -- 'src/a[1].py'` resolves exactly
that entry with `rc=0` even when `src/a1.py` also exists, and `src/a?b.py` / `src/a*b.py` behave the same way.
(`git ls-files` *does* glob them, which is where the opposite intuition comes from, but it is not the command this
path is handed to.) Round 1 refused them, which made a legitimate anchor un-authorable and un-seedable and —
through the read path's own confinement check — reported a file the tree really holds as `path_absent`: a false
statement about the repository rather than a refusal of a malformed spelling.

### Conventions

Two spellings of one identity never coexist: an identifier is validated into the canonical form at the model
boundary rather than normalized at the storage boundary. Length ceilings are generous for prose and far below any
SQLite limit; a legitimate value never approaches them.

### Invariants And Boundaries

- `frozen=True` is a property of the **value**, not of the row. Refusing an update to a stored revision is a
  storage rule enforced by schema triggers and the operation's preconditions — never by model immutability.
- A caller that supplies an identity supplies the identity that will be stored: non-canonical input is rejected,
  never quietly rewritten.
- `PROPOSED_STATE`/`ACCEPTED_STATE` live here because they decide something, so consumers import them rather than
  re-declaring their own literals.
- **A rule shared by two aggregates lives here, not in the first one that needed it.** A rule inlined in one
  revision kind is a rule the next kind will re-derive slightly differently; the accepted/proposed check was
  extracted for exactly that reason.
- **No model here gains a storage concern.** These are authored-value rules refused at construction, not
  substitutes for the storage boundary's checks.

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
| The frozen, extra-forbidding base every knowledge model inherits. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The shared accepted/proposed rule both revision aggregates apply at construction. | `require_consistent_acceptance` | mcp/src/agents_remember/models/knowledge/base.py:40-56 |
| **The shared pathspec rule, with the measured Git behavior in its docstring: a leading `:` is real pathspec magic and is refused; `*`, `?` and `[` are literal characters to `ls-tree` and are admitted.** | `require_plain_git_path` | mcp/src/agents_remember/models/knowledge/base.py:59-92 |
| **The write-path boundary that applies it, so a malformed anchor cannot be authored.** | `SourceAnchorDraft` | mcp/src/agents_remember/models/knowledge/source.py:82-127 |
| **The seed boundary that applies the same rule, so a refused spelling cannot be presented as a seed.** | `PathSeed` | mcp/src/agents_remember/models/knowledge/read.py:144-171 |
| The canonical-spelling identifier rule and its refusal of non-canonical input. | `normalized_uuid` | mcp/src/agents_remember/models/knowledge/base.py:95-109 |
| The declared length ceilings and identifier patterns used by every sibling model. | `PROSE_MAX_LENGTH`; `LABEL_MAX_LENGTH`; `UUID_PATTERN`; `SHA256_PATTERN`; `GIT_OBJECT_PATTERN` | mcp/src/agents_remember/models/knowledge/base.py:18-27 |
| The two authored origin states are declared once here. | `PROPOSED_STATE`; `ACCEPTED_STATE` | mcp/src/agents_remember/models/knowledge/base.py:29-31 |
| The two revision aggregates that apply the shared rule. | `InvariantRevision`; `FamilyRevisionDraft` | mcp/src/agents_remember/models/knowledge/invariant.py:33-115; mcp/src/agents_remember/models/knowledge/family.py:58-102 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded the one addition this leaf made — **`require_plain_git_path`, the shared Git-pathspec rule** — and, because review corrected this leaf's first attempt at it, recorded the corrected predicate explicitly: pathspec **magic** is the leading-`:` family (`:(exclude)`, `:!`, `:(top)`, `:/`), which is refused, while **`*`, `?` and `[` are admitted** because `ls-tree` addresses them as literal characters (measured on `git 2.54.0`, with the case that reproduces it). The card states why the refusal belongs at the typed boundaries rather than at the tree lookup — a spelling Git answers with an error or with a *different* location would otherwise be published as `path_absent`, a false statement about the repository — and names the two call sites that apply it. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): recorded the one addition this leaf made — `require_consistent_acceptance`, the accepted/proposed origin-state rule extracted from `InvariantRevision` so both revision aggregates apply one owner's rule at construction instead of the second kind re-deriving it — plus the boundary that no model here gains a storage concern. The identifier and length declarations are unchanged and are still the single source the siblings import. Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new frozen model base. It records that value immutability is distinct from row immutability and that identity spelling is validated rather than normalized. Verification metadata remains empty until closeout stamps the code commit.

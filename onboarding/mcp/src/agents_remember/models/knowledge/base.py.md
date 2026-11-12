# mcp/src/agents_remember/models/knowledge/base.py

## Governing Overview

[models route overview](../overview.md)

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

require_plain_git_path refuses a leading colon because Git reads it as pathspec magic and can answer about a different location. It admits literal glob characters that ls-tree addresses by name. Current PathSeed applies this shared rule alongside confined-path validation. The former SourceAnchorDraft write-path call site was retired by MIK-R26; no source-locator value is a replacement anchor authoring request.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The frozen, extra-forbidding base every knowledge model inherits. [1]
- The shared accepted/proposed rule both revision aggregates apply at construction. [2]
- **The shared pathspec rule, with the measured Git behavior in its docstring: a leading `:` is real pathspec magic and is refused; `*`, `?` and `[` are literal characters to `ls-tree` and are admitted.** [3]

- The retained PathSeed uses the shared plain-Git-path rule; the old stored-anchor writer boundary is retired. [4]

- **The seed boundary that applies the same rule, so a refused spelling cannot be presented as a seed.** [5]
- The canonical-spelling identifier rule and its refusal of non-canonical input. [6]
- The declared length ceilings and identifier patterns used by every sibling model. [7]
- The two authored origin states are declared once here. [8]
- The two revision aggregates that apply the shared rule. [9]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.

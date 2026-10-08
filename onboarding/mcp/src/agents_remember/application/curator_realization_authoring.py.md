# mcp/src/agents_remember/application/curator_realization_authoring.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Owns the **realization a curator hand-off target authors** — its role and its rationale — for the
ordinary curator writer (`knowledge_curator_ingest.py`). It resolves each target's role and rationale
(the target's own values first, then the entry's explicit default) and decides, before any identity is
minted, whether an entry that would write new realizations is admissible. The writer never generates
rationale text: an unexplained target refuses its entry by name. This module holds no I/O and writes
nothing; the ingest calls it.

## Code Commentary

### Logic

- **Keys.** At entry level the producer writes `realization_role` / `realization_rationale` (the
  historical spelling, kept); on a target the same facts are `role` / `rationale`, without the prefix,
  because the target is the realization being described. `governing_route` (target) and
  `authority.governing_route` (entry) are checked here too.
- **Resolution.** `EntryRealization.read` reads the entry-level default: the role validated against the
  shipped `RealizationRole` vocabulary (`get_args`, never a second copy), the rationale kept **verbatim**
  (the entry's content digest has always carried that spelling), and `problem`, the first refusal the
  entry-level values themselves earn. `EntryRealization.for_target` returns a `TargetRealization`: the
  target's own trimmed role/rationale win; what the target leaves unstated inherits the entry default;
  the two halves resolve independently; a role stated at neither level is `UNCLASSIFIED_ROLE`.
  `TargetRealization.stated` holds only the target's own keys, which is what the ingest's content
  digest adds — empty when the target inherits everything, so pre-existing lists digest unchanged.
- **Admission.** `realization_refusal(entry_id, entry, targets)` asks the entry-level problem first
  (every inheriting target would inherit its defect), then each target check in `_TARGET_CHECKS`
  order: `realization_value_not_text` → `realization_role_unknown` →
  `realization_governing_route_absent_literal` → `realization_rationale_absent` →
  `realization_rationale_too_long`. The first check any target fails decides the refusal, and the
  message names **every** target failing that same check by position, path and locator (`_describe`),
  plus a remedy, so the producer can correct them in one pass. A non-mapping target is skipped here;
  the ingest's target-shape check owns that defect.
- **Values.** `_stated` trims a string and reads a missing, null, blank or non-string value as `""`;
  it never calls `str()` on a value. `_field_problem` refuses a non-string (`realization_value_not_text`,
  naming the JSON type) and an unknown role word (`realization_role_unknown`, the string `"absent"`
  included). `_names_absent_route` matches the placeholder `absent` after `strip().casefold()`.
  `_authority_route_problem` applies the not-text and absent-literal rules to
  `authority.governing_route` and reports them as entry-level problems with a route-specific remedy.
  `_too_long` compares the effective per-target rationale with `PROSE_MAX_LENGTH` (20000).

### Conventions

- Refusal codes are module constants (`CODE_*`) and are the per-entry refusal codes the ingest report
  carries; the wording names where the value was written.
- The module is pure: it reads mappings and returns values or `(code, detail)` pairs; the ingest owns
  ordering relative to scope checks, allocation and planning.

### Invariants And Boundaries

- **No generated rationale.** Nothing here (or in the ingest) composes rationale text from a path; a
  target with no rationale at either level is refused `realization_rationale_absent`. This is the
  developer ruling "require rationale" recorded on leaf `260921-ICR-L45` (ICR-R20@v1 repair); the
  stored claim model requires non-blank text, so absence cannot be stored.
- **Per target wins.** A target's own `rationale` / `role` always beats the entry-level default; the
  entry default is an explicit authored value, never a fallback the writer invents.
- **Checked only on admission.** The caller (`knowledge_curator_ingest._resolve_creation`) does not ask
  these questions of an entry whose recorded allocation the candidate already stores: its exact retry
  writes nothing and replays as at base. A recorded-but-uncommitted allocation is still checked. This
  module does not itself know about allocations.
- **Not a quality judgment.** It checks that an explanation was *stated*, not that it is good.
- **History untouched.** Stored claims holding the old generated sentence "The statement is realized at
  <path>." are never re-read or rewritten here.
- **Route spelling.** Missing routes are spelled by omitting the key (or `null`); the word `absent` in
  any case is refused because the writer reads a route as a path and would author a route named
  `absent`.

### Todos

No additional work is asserted by this card. (Reviewer R4's optional note — rebasing the
recorded-but-uncommitted test on the real crash window — belongs to the test card and the Architect.)

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement: per target first, checked at admission, no route spelled by a placeholder, and what it does not cover.** [1]
- The five refusal codes and the producer-facing keys. [2]
- Values are trimmed text or nothing; a non-string is never rendered, and an unknown role is refused. [3]
- **The placeholder word `absent` is matched in any case once trimmed, at a target and at `authority.governing_route`, where a non-string route is also refused.** [4]
- **Resolution: target first, then the entry default, halves independent; only target-stated keys enter the digest.** [5]
- **The ordered target checks and the refusal that names every failing target.** [6]
- The shipped role vocabulary and the unassessed-edge member, and the stored prose limit. [7]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The hand-off template that tells producers
this shape is a same-repository skill file (`skills/l-01-agent-lifecycles/templates/curator-handoff-list.md`).

No meaningful cross-repo references found.

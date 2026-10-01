# mcp/src/agents_remember/models/knowledge/review_external_movement.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The value a review publishes about an identity a *raw* Git operation moved under it (ICR-R23@v1), and
the one implementation of the rule that keeps its state consistent with its own measurements.** A
comparison generation records the identities a review bound; managed work moves those identities
through exactly one route — `worktree_sync` — which *measures* what it moved and writes the measurement
beside the generation (ICR-R22@v1). Nothing obliges a repository to use that route. `git rebase`,
`git cherry-pick`, `git revert` and a branch or worktree switch are ordinary Git, they rewrite or
replace the very refs the sealed manifest names, and they leave no rebinding record behind because no
managed transaction ran.

The module's docstring states the design decision that makes this value honest: it is deliberately
**not** an attempt to classify the Git command a person ran, because Git leaves no such record and a
module that guessed one would be inventing a measurement. It reports what *was* measured — which
declared identities no longer appear in the repository, and which transition shape that is — beside the
reconciliation routes this system does and does not have.

**Four states, and only one of them claims the identities still stand.** `current` says every declared
identity that could be compared is still there, `stale` says a declared identity was replaced or the
worktree left its declared branch, `not-measured` says the comparison could not be taken at all, and
`unavailable` says the generation itself could not be read.

## Code Commentary

### Logic

**`reconciliation` is a field, not a tone of voice.** `GitTransitionReconciliation` (`:86`) is
`"supported" | "unsupported"`, and `supported` is earned by exactly the one recovery this system
performs — the successor generation the freeze owner publishes from the reviewed one. `unsupported`
repeats the matrix's unsupported verdicts in the value itself, so no reader can read this value and
conclude that an unsupported transition was handled, whatever sentence sits beside it.

**`unchanged` is the measured absence of a transition.** `ExternalGitTransition` (`:74-81`) carries six
members in the order the matrix publishes them, and `unchanged` is first because it is the commonest
state of all: naming it `ordinary-append` would assert an advance that did not happen. `transitions`
carries `unchanged` — and nothing else — exactly when every declared identity was compared and every one
still stands at its record; it is **empty** when no shape was observed and something could not be
compared, which is the honest answer for a boundary that measured nothing (`:111-119`).

**The per-channel evidence is what makes `advanced` distinguishable from `current` without reading a
sentence.** `GitMovementEvidence` (`:98`) is `current` / `advanced` / `replaced` / `unavailable`, where
`advanced` means the recorded identity is still an ancestor of the branch, so the branch moved forward
without replacing it. `transition_evidence` (`:130`) carries that per declared channel, and the three
channels are named by the thing that moved rather than by the command that moved it
(`GitMovementChannel`, `:92`).

**`observed_*` locate the replacement; they never substitute for the recorded identity.**
`observed_code_work_branch_head` (`:142`), `observed_declared_source_branch_head` (`:143-145`) and
`observed_memory_work_branch_head` (`:146`) exist to say where the branch is now; a channel that could
not be read reports `unavailable` in the evidence and carries no observed value at all (`:120-123`).

**The `after` validator is what makes a false movement unpublishable.**
`_the_state_follows_from_what_was_measured` (`:154-205`) checks every direction, and each wrong
combination is a different false claim: a named replacement must be `stale` (`:170-174`); a `stale`
report with nothing replaced asserts movement nobody observed (`:175-179`); the two absence states must
carry a non-blank reason while a measurement may carry none (`:180-190`); `generation_readable` cannot
be `True` beside `unavailable`, because only an unreadable generation is `unavailable` and every other
state was read (`:191-195`); and `unchanged` may travel only alone, in `current`, with nothing replaced
(`:196-204`).

### Conventions

`__all__` (`:60-66`) publishes the five names in one alphabetical list: the movement value, the
transition union, the channel union, the evidence union and the reconciliation union. The module imports
only what those need (`:45-58`): `Literal` from `typing`, `Field` and `model_validator` from pydantic,
five names from the knowledge base vocabulary — `GIT_OBJECT_PATTERN`, `PROSE_MAX_LENGTH`,
`SHA256_PATTERN`, `UUID_PATTERN`, `KnowledgeModel` — and `ReviewSyncMovementState` from
`models/knowledge/review_staleness.py`. Every constrained field names its bound from that shared
vocabulary rather than a local number: `generation_id` is `UUID_PATTERN` (`:138`), the binding digest is
`SHA256_PATTERN` (`:140`), the observed heads are `GIT_OBJECT_PATTERN` (`:142-146`) and every prose field
is `PROSE_MAX_LENGTH`. Cross-field rules are an `@model_validator(mode="after")` method returning
`self`, so no route can construct an invalid value — not even by `model_validate` on a dict, which is how
the cases forge one.

**The state vocabulary is reused, not re-minted.** `binding_state` is typed `ReviewSyncMovementState`
(`:128`), R22's four-member union, because a reader of either value must read the same four words the
same way — and because R15's currentness rules are the ones the packet's failure clause names, so
`stale` is the only state a replaced identity earns (`:104-109`). The module adds no fifth state; it adds
the *evidence* union beside it instead.

### Invariants And Boundaries

- **A movement never carries a reason; an absence always carries one.** `reason` (`:136`) is `None`
  exactly for the states that report a measurement, so an unreadable generation can never read as an
  unaffected repository, and a measurement never describes an absence that was not reported.
- **`stale` is a measurement, not a verdict.** It is reachable only with at least one named
  `channel:identity` in `moved_identities` (`:133`), which is what a reader acts on.
- **`unsupported` is repeated where the reader is.** `unsupported` (`:151`) carries the matrix's
  unsupported transitions on the value itself; empty means "this report has none to name", never "none
  exist" — the documented matrix is the authority on which transitions those are.
- **The value performs no recovery.** `recovery_action` (`:147`) is the step a person takes; the value
  itself writes nothing, reconciles nothing, re-freezes nothing and deletes nothing.
- **Boundary: this vocabulary is display-only.** No field holds a comparison verdict, a severity, a
  score or an approval; `successor_action` names the freeze owner's act and claims none of it.
- **Boundary: the recorded knowledge *dataset* identity is not restated here.** That identity is
  measured by the managed-sync rebinding (ICR-R22@v1) and this value carries only what a boundary
  compared about the three declared Git channels, so one measurement has one owner.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category — its whole content is the statement that
no entries are configured — so there is no external or domain documentation source to consult, and no
documentation row is recorded here. Every statement on this card is grounded in the repository's own
source, docstrings and cases, and the paragraphs above are backed by the table below.

### Repo-Internal References

Every claim on this card is checkable in the module's own declarations and validator, in the matrix the
labels come from, and in the cases that drive them. The three details a reader should carry: **the state
follows from what was measured, never from a two-way reading of the channel matches**; **`unsupported`
travels on the value, so the state alone cannot be read as "handled"**; and **`unchanged` is the measured
absence of a transition, published exactly when every declared identity still stands at its record.**

- **The module's own statement of why this is a measurement and not a command classifier, and what the four states mean.** [1]
- The shared bounds, the base model and the state vocabulary this value reuses. [2]
- The published surface: the value, the transition union, the channel union, the evidence union and the reconciliation union. [3]
- **The transition vocabulary, whose first member `unchanged` is the measured absence of a transition rather than an event.** [4]
- **Whether this system reconciles a transition at all, earned by the one recovery it performs.** [5]
- **The three declared channels, each named by the thing that moved rather than by the command that moved it.** [6]
- **What one channel's ancestry check found, with `advanced` as a measurement of its own.** [7]
- **The movement value: its four-state binding, the transition and evidence tuples, the moved identities and the reason rule.** [8]
- The field set, with `observed_*` present only for the channels that were read. [9]
- **The `after` validator that refuses every false shape — state against replaced identities, absence against reason, and `generation_readable` against `unavailable`.** [10]
- **The matrix these labels come from, and the recovery each row names.** [11]
- **The producer that publishes this value from what the repository shows.** [12]
- The closeout/integration statement, which repeats the unsupported verdicts whether or not a value was produced. [13]
- **The payload field this value travels on, and the re-export that keeps its import site.** [14]
- The payload module's own `__all__` entry for the value. [15]
- **The read path that carries the value from the measurement owner to the payload.** [16]
- The second review boundary that publishes the same value on the task-context path. [17]
- **The case that forges five false shapes, each departing from exactly one validator clause, with the real published value as the accepted control.** [18]
- The case that pins the control state as the value an untouched leaf publishes. [19]

### Cross-Repo References

No cross-repository behavior is implemented in this module. It declares value shapes only: it reads no
store, resolves no path, runs no Git command and touches no repository, and every identity its fields
carry — a generation id, a binding digest, a Git object id — is a value another owner in this same
repository resolved. No cross-repo reference row is recorded here because no cited range proves a
repository or external-system boundary.

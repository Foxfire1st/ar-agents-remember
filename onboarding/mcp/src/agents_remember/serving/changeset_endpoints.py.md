# mcp/src/agents_remember/serving/changeset_endpoints.py

## Governing Overview

[serving route overview](overview.md)

## Purpose

Which exact Git objects a **committed** change-set range binds, and what to say when one is absent.
The committed leaf views answer one question — "what did this leaf land?" — and that question has one
honest answer: the range between the two commits the enclosure contract **recorded**, the base it
forked from and the commit its closeout or integration wrote. Those two cell values are immutable task
facts; a branch tip and a worktree `HEAD` are not.

`HEAD` advances with every ordinary commit the task makes, so binding it would publish a range that is
not the leaf's landed delta under a label that says it is — and would answer differently on the next
poll of the same URL. A side whose recorded endpoint is absent is therefore reported as **absent, by
name**: nothing has recorded that side's landed commit yet, so the committed range does not exist yet.
No `HEAD`, no branch and no working tree is substituted for it.

The guard is a **kind**, not one flat failure, because a caller acts on the three reasons differently.
`not-recorded` is an endpoint nothing has written yet, and it is the *only* absence a half may degrade
to "nothing to show" for; `no-repository` (the contract names no repository for that side) and
`unresolvable` (a recorded commit this checkout does not hold) are broken state that no view may
report as an empty range, since that would publish a measurement the caller never made.

The module is deliberately narrow: it resolves the two recorded endpoints, checks that the repository
actually holds them, and raises. It renders no payload, opens no route and decides no degradation —
`serving/changeset.py` owns those, and its two sides call this resolver independently so that one
side's unrecorded endpoint never discards the other side's answer.

## Code Commentary

### Logic

**`recorded_committed_range(contract, *, memory)` is the whole operation.** It picks the side
(`code`/`memory`), the repository (`code_repo_path`/`memory_repo_path`) and the two recorded cells,
then refuses in a fixed order: no repository for this side (`no-repository`); no head or no base, with
the refusal naming which of the two is missing (`not-recorded`); a recorded commit the repository
cannot resolve (`unresolvable`). Only when all three pass does it return a `RecordedRange`.

**The two recorded cells are read through `_recorded_commits`, and either recorded cell is the
endpoint.** `code_commit` and `memory_content_commit` are written by closeout;
`integrated_code_commit` and `integrated_memory_content_commit` are written when the task's line lands
into its source branch. Either is *recorded*, and either therefore binds the range exactly; the
closeout cell is preferred only because it is the one a comparison against the working view is made
against. The base side is `code_base_commit`/`memory_base_commit` with no fallback at all.

**The `not-recorded` refusal is written for the reader who can still act.** It names the leaf, the
missing cell ("landed commit" or "base commit"), states that the committed view reads the two recorded
commits and substitutes no `HEAD`, branch or working tree for either, and gives two actions: read the
uncommitted view (`mode=working`) while the task is live, or reopen the view after closeout records
the range. The message therefore never leaks the worktree's `HEAD` into a committed answer even as
text — measured by the case module, which asserts the live head is absent from the message.

**`RecordedEndpointAbsent` is a `FileNotFoundError` because that is the type the change-set routes
already map to a 404 naming what could not be found.** It is its own type because the *reason* —
nothing has recorded this side's landed commit yet — is a fact about the task's progress rather than
about a path. `kind` is the payload that lets a caller with a second, independently resolved half
keep the two cases apart; it defaults to `NOT_RECORDED` so a caller that does not care about the
distinction still gets the one absence that is safe to degrade.

**`_unresolvable` asks the repository, not the caller.** It runs
`run_git(repository, ["cat-file", "-e", f"{commit}^{{commit}}"])` for each recorded commit and returns
the first one the repository does not hold. A recorded commit this checkout does not have is therefore
a named absence too, instead of an unhandled Git failure escaping the route.

**`RecordedRange` carries the repository beside the two ids** because a commit id without the
repository that holds it is not resolvable: the code side reads from the code repository and the
memory side from the memory repository, and the returned value states which one this range came from.
`_leaf` exists only so a refusal can name the leaf, falling back to the task id for a contract that
records no leaf id.

### Conventions

The side names are the words the change-set shape already publishes (`code`/`memory`), so a reader who
is told which side is missing reads the same word the payload uses for it. The absence kind is a
`Literal` alias with a named constant for the one degradable value, rather than a bare string at each
raise site. The module imports `run_git` from `kernel/git_command` and `WorktreeContract` from
`worktrees/worktree_contract` — the same two owners `serving/changeset.py` uses — and nothing else; it
holds no FastAPI import, so it cannot become a second route surface.

### Invariants And Boundaries

- **A committed range is two recorded commits or it is nothing.** No `HEAD`, no branch tip and no
  working tree is ever an endpoint of a committed range.
- **The three absences stay apart.** `not-recorded` is the only one a half may degrade to empty for;
  `no-repository` and `unresolvable` are broken state and stay refusals on both sides.
- **A recorded commit that this checkout cannot resolve is a named absence.** `git cat-file -e` is the
  check, and its failure never escapes as an unhandled error.
- **The repository travels with the ids.** A `RecordedRange` names the repository its two commits are
  read from.
- **The module renders nothing.** It raises values the routes already map, and the degradation policy
  belongs to the caller (`_leaf_range`), which is how the code half keeps its refusal while the memory
  half may degrade.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: this module's own docstring and
functions, the contract loader whose recorded cells it reads, the Git helper it probes with, the
caller that owns the two sides' independent degradation, and the case module that measures both the
bound range and the unrecorded-endpoint answer. Two details a reader should carry: the *closeout*
cell is preferred over the *integration* cell only because a comparison against the working view is
made against it, not because the integration cell is less recorded; and `kind` is the whole reason
the exception is a type rather than a message — the caller branches on `NOT_RECORDED` alone.

**260921-ICR-L25 changed what the caller does with that branch, not what this module does.** This
module still raises `RecordedEndpointAbsent(kind="not-recorded")` for a side whose landed commit is
not recorded yet — it owns *which* Git objects a range binds and has no view about HTTP. What changed
is one layer up: `serving/changeset.py`'s `_leaf_range` now **catches** that absence for the **code**
side and carries its sentence into the response body as `state="unrecorded"` / `stateDetail`, instead
of letting it reach the route as a `404` (register B6). The memory side's degradation and the
`no-repository`/`unresolvable` refusals are untouched.

- **The module's own statement of what a committed range is, why `HEAD` may not stand in for it, and why the three absences are separated.** [1]
- The published surface: the range value, the two absence types, the kind constant and the resolver. [2]
- The two side names, which are the words the change-set payload already uses for its halves. [3]
- The three absence kinds and the single degradable one. [4]
- **The range value: the two recorded ids plus the repository that holds them, because an id without its repository is not resolvable.** [5]
- **The absence type: a `FileNotFoundError`, with `kind` carrying the reason apart — the code side's `not-recorded` instance is caught by `_leaf_range` and published as the body's state rather than reaching the route as a 404 (260921-ICR-L25).** [6]
- **The whole resolver: the recorded-base precondition, the two missing-cell refusals, and the resolvability probe — in that order.** [7]
- The two recorded cells per side, with the closeout cell preferred over the integration cell and the base side having no fallback. [8]
- The leaf name a refusal carries, with the task id as the fallback for a contract that records no leaf. [9]
- **The resolvability probe: the repository is asked, per commit, and the first object it does not hold is named.** [10]
- The contract whose recorded cells this module reads, and the cells themselves. [11]
- **The caller that owns the degradation policy: the code half carries its own `not-recorded` absence into the body as `state`/`stateDetail` while only an unrecorded **memory** half may empty, and both sides resolve independently.** [12]
- **The case module that measures the bound range, the immovable endpoint, the state answered instead of a refusal, the route's own `200`, and the one-half degradation.** [13]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads recorded commits out of one code
repository and one memory repository named by the enclosure contract, and carries no identity that
ranges beyond them.

No meaningful cross-repo references found.

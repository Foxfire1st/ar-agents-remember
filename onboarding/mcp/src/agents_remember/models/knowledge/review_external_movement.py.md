# mcp/src/agents_remember/models/knowledge/review_external_movement.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The source-bound v2 report of raw Git ancestry on the complete retained review tree comparison. It reports which declared identities were observed current, advanced, replaced or unreadable; it does not guess which Git command ran or perform recovery.

## Code Commentary

### Logic

ExternalGitMovement carries the complete ReviewTreeComparisonRecord, its canonical digest and movement_version v2. A non-unavailable report must carry its source comparison, and a carried digest must identify that complete record. Missing comparison evidence carries no invented generation UUID or zero digest.

binding_state is current, stale, not-measured or unavailable. The per-channel transition_evidence distinguishes current ancestry, an ordinary advance retaining the recorded ancestor, replacement and unavailable observation. Commit identities can be checked for ancestry; an uncommitted candidate tree supplies no observed work-branch head, so that channel remains not-measured.

transitions names observed shapes. unchanged appears alone, in current, with no moved identities; naming an ordinary append on an untouched channel would invent an event. With no measured shape and incomplete observation, transitions is empty rather than a favorable unchanged claim.

observed_* values locate branch heads actually read and never replace recorded identity. A named moved input requires stale, and stale requires moved identities. not-measured and unavailable require a reason; a measured state carries none. unavailable cannot report generation_readable true. These are constructor rules, not wording conventions.

The application's support matrix owns supported and unsupported recovery routes. unsupported is repeated on the displayed value, while successor_action names a successor live review with exact code/memory tree comparison. Empty unsupported means no transitions named in this report, never that all transitions are supported.

### Invariants And Boundaries

- Source comparison and digest travel together and cannot be replaced by an unrelated record's identity.
- A movement is measured replacement; absence of evidence is neither an unaffected repository nor an inferred switch.
- Authored judgments remain readable at their original inputs; this report does not reinterpret them for replacement inputs.
- The value writes nothing, executes no Git operation and grants no approval or reconciliation.
- Raw ancestry observations and managed-sync exact tree-pair measurements are separate owner-produced facts.

### Historical boundary — MIK-R26

The former v1 value used dataset-generation identity. Historical shapes retain their own decoding constraints; v2 uses the complete tree comparison and invents no UUID or dataset coverage when that source is absent.

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


- The v2 raw movement report is bound to complete retained tree-comparison evidence. [1]

- The shared bounds, the base model and the state vocabulary this value reuses. [2]
- The published surface: the value, the transition union, the channel union, the evidence union and the reconciliation union. [3]

- Transitions describe measured shapes, with unchanged reserved for an untouched complete observation. [4]


- The reconciliation vocabulary distinguishes supported and unsupported recovery. [5]


- The three declared Git ancestry channels. [6]


- Ancestry distinguishes current, advanced, replaced and unavailable observations. [7]


- The measured report carries states, exact source and observed branch facts. [8]

- The field set, with `observed_*` present only for the channels that were read. [9]

- The validators enforce complete-source identity and state/observation consistency. [10]

- **The matrix these labels come from, and the recovery each row names.** [11]
- **The producer that publishes this value from what the repository shows.** [12]
- The closeout/integration statement, which repeats the unsupported verdicts whether or not a value was produced. [13]
- **The payload field this value travels on, and the re-export that keeps its import site.** [14]
- The payload module's own `__all__` entry for the value. [15]
- **The read path that carries the value from the measurement owner to the payload.** [16]
- The second review boundary that publishes the same value on the task-context path. [17]

- The current forgery sweep checks state consistency and complete source-comparison binding. [18]


- Untouched ancestry, advance, rewrite and uncommitted-tree nonmeasurement are distinct observed facts. [19]


### Cross-Repo References

No cross-repository behavior is implemented in this module. It declares value shapes only: it reads no
store, resolves no path, runs no Git command and touches no repository, and every identity its fields
carry — a generation id, a binding digest, a Git object id — is a value another owner in this same
repository resolved. No cross-repo reference row is recorded here because no cited range proves a
repository or external-system boundary.

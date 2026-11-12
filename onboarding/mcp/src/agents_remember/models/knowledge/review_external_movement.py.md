# mcp/src/agents_remember/models/knowledge/review_external_movement.py

## Governing Overview
[models route overview](../overview.md)

## Purpose
The source-bound v2 report of raw Git ancestry on the complete retained review tree comparison. It reports which declared identities were observed current, advanced, replaced or unreadable; it does not guess which Git command ran or perform recovery.

## Code Commentary
### Logic

ExternalGitMovement declares the complete ReviewTreeComparisonRecord, its canonical digest and movement_version v2. The local validator requires a comparison for a non-unavailable report and requires the digest to match whenever a comparison is present. It does not add a converse rule forbidding every digest when comparison is absent in an unavailable value. The current shape has no generation-UUID field; source authenticity and actual observation remain producer responsibilities.

binding_state is current, stale, not-measured or unavailable. The per-channel transition_evidence distinguishes current ancestry, an ordinary advance retaining the recorded ancestor, replacement and unavailable observation. Commit identities can be checked for ancestry; an uncommitted candidate tree supplies no observed work-branch head, so that channel remains not-measured.

ExternalGitTransition admits unchanged, ordinary-append, rebase and branch-switch; cherry-pick and revert are no longer constructible transition literals. These names describe ancestry shapes, not proof of which Git command ran. The validator permits unchanged only alone, in current, without moved identities. An empty transition tuple is representable; the value alone does not establish a complete observation or an unaffected repository.

This narrows the report's wire union, not the recovery matrix. `GitTransitionSupport`
separately admits cherry-pick/revert for documentation and recovery, and
`GIT_TRANSITION_SUPPORT` still contains those broader rows; they are not newly produced
wire transition values.

The optional observed_* fields are pattern-validated branch-object identities, not model-side evidence that I/O occurred or that every channel was supplied. The actual constructor rules are narrower: moved identities and stale agree in both directions; not-measured/unavailable require a nonblank reason and measured states carry none; unavailable cannot report generation_readable true; and unchanged is exclusive as described above. The reverse implication from generation_readable=false is not added by this validator.

The application's support matrix owns supported and unsupported recovery routes. unsupported is repeated on the displayed value, while successor_action names a successor live review with exact code/memory tree comparison. Empty unsupported means no transitions named in this report, never that all transitions are supported.

### Conventions

**The state vocabulary is reused, not re-minted.** `binding_state` is typed `ReviewSyncMovementState`, because a reader of either value must read the same four words the same way — and because R15's currentness rules are the ones the packet's failure clause names, so `stale` is the only state a replaced identity earns.

### Invariants And Boundaries

- A non-unavailable value requires its comparison; whenever a comparison is present its digest must match. This is constructor consistency, not an independent authenticity check.
- A movement is measured replacement; absence of evidence is neither an unaffected repository nor an inferred switch.
- This report supplies no authority to reinterpret an authored judgment at replacement inputs; historical judgments keep their original source attribution.
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

- The transition declaration now admits unchanged, ordinary-append, rebase and branch-switch, not cherry-pick/revert. [4]


- The reconciliation vocabulary distinguishes supported and unsupported recovery. [5]


- The three declared Git ancestry channels. [6]


- Ancestry distinguishes current, advanced, replaced and unavailable observations. [7]


- The measured report carries states, exact source and observed branch facts. [8]

- The field set declares optional pattern-validated observed branch identities and a nullable bounded reason; those declarations do not perform I/O or establish observed-channel completeness. [9]

- The validators enforce complete-source identity and state/observation consistency. [10]


- The support matrix retains recovery/documentation rows for cherry-pick and revert alongside observed shapes; its broader row type is not the four-member wire transition union. [11]


- The optional live-review entry point delegates to contract measurement and returns no boundary report for absent enclosure, closed leaf or non-live trees. [12]

- The closeout/integration statement, which repeats the unsupported verdicts whether or not a value was produced. [13]

- The payload carries the optional movement value, imports and publicly exports its type, whose own constructor lives in the focused model. [14]


- The payload module explicitly publishes ExternalGitMovement in its own export declaration. [15]



- Subject-review composition calls the measurement owner and carries its optional result onto the payload. [16]




- Task-context composition calls the same measurement owner and carries its optional result, not a separately inferred movement. [17]



- The current forgery sweep checks state consistency and complete source-comparison binding. [18]


- Untouched ancestry, advance, rewrite and uncommitted-tree nonmeasurement are distinct observed facts. [19]


- The four declared transition shapes include unchanged as the non-event spelling; cherry-pick/revert are removed. [20]
- The exported reconciliation vocabulary is supported/unsupported; choosing a value does not execute recovery. [21]
- Constructor guards couple stale and moved identities, absence and reasons, constrain unavailable readability in one direction, and keep unchanged exclusive. [25]

- **The three declared channels, each named by the thing that moved rather than by the command that moved it.** [22]
- **What one channel's ancestry check found, with `advanced` as a measurement of its own.** [23]
- **The movement value: its four-state binding, the transition and evidence tuples, the moved identities and the reason rule.** [24]
- The reused state vocabulary: `binding_state` carries the measured-currentness words, and `stale` is the only state a replaced identity earns. [26]

### Cross-Repo References

No cross-repository behavior is implemented in this value model. It reads no store,
resolves no path and runs no Git command. Its comparison, binding digest and Git-object
identities are values supplied by other owners in this repository; they do not establish
an external-system boundary. Same-repository evidence remains in the section above.

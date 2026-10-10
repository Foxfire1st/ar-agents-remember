# mcp/tests/test-evidence-lanes.toml

## Master Retirement And Abandoned-Row Cases

`mcp/tests/test_abandoned_series_closeout.py` is a `unit-regression` row (the first row of that list), and
`mcp/tests/test_master_retirement.py` and `mcp/tests/test_standalone_master_retirement.py` are
`integration`-lane rows. Each module appears in exactly one lane.
## Governing Overview

[tests route overview](overview.md)

## Purpose

The canonical evidence-lane catalog: which test modules belong to which lane, so a leaf's checks can
name the population they ran.

## Code Commentary

### Logic

The catalog assigns each current test module exactly one evidence lane. The dependency-facts
store controls and the Python load-independence scanner belong to `architecture-fitness`; the
existing knowledge reader coverage remains in `unit-regression`. Membership declares the selected
population, never that an invocation ran or passed.

### Conventions

TOML lists, one module path per row, kept sorted within the lane.

### Invariants And Boundaries

Both test catalogs stay in one canonical form; every loader refuses a duplicate or malformed entry.
A new test module that belongs to a lane is added here in the same pass.


### Registering a test module

A new test module is added to the list of its lane. `mcp/tests/test_reviewer_worklist_process.py` and
`mcp/tests/test_reviewer_worklist_reads.py` are in the `integration` list: they start real child
processes and Git repositories, and a default run with `not integration` skips them.

The L82 rule modules join their lanes: the sprint-archive, copies-rule, cache-rule, adoption,
no-remains, kept-line and refusal-guard test modules are `unit-regression` rows, and each module
appears in exactly one lane.

### Todos

No additional work is asserted by this card.

## Current verification scope

The existing reviewer-operation and copied-index capture rows remain unit-regression,
and their serving/public-preview operations remain integration. Imported runtime, bridge,
launch, message, status, sandbox and removal guards have explicit unit-regression rows.
The real tool-server start, role-handover binding and registered canonical-reader protocol
rows are integration. These lane declarations do not certify that a test ran.

## Current preview-proof registration

The registered public preview module is an integration-lane operation, alongside the two preserved L40 unit-regression rows. Curation does not move the public boundary into a helper-only lane or infer certification from the declaration.

## Current source account

New Paseo runtime, bridge, launch, messaging, sandbox and previous-host cases are registered in unit-regression. The real child tool-server, role-handover binding and registered canonical-reader protocol cases are in integration. Shared support modules collect no cases and gain no lane row.

## 260928-MIK-L114 River Tests Join Unit-Regression

`mcp/tests/test_f07_missing_lock_cursor.py`, `mcp/tests/test_f08_registered_handler_river.py`
and `mcp/tests/test_tool_event_river.py` are `unit-regression` rows in canonical byte
order; each module appears in exactly one lane.

## 260928-MIK-L101 Rule 6 budget test joins unit-regression

`mcp/tests/test_role_capsule_budgets.py` is a `unit-regression` row in canonical byte
order; each module appears in exactly one lane.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1`; it lives outside the code and memory repositories, so it is named
here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References


- The module the lane names. [20]

- **The manifest's own shape facts this account states: 450 lines, 432 entries for 432 modules on disk.** [783]
- **The manifest's own shape facts this account states: 450 lines, 299 unit-regression entries.** [784]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 401 now, after the L4, seal-removal, L5, L7, L8 and L3 plus L114 river insertions). [785]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 318 now, after the L4, L5, L7, L8 and L3 plus L114 river insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [786]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 363 now, after the L4, seal-removal, L5, L7, L8 and L3 plus L114 river insertions). [788]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it. [789]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 350 now, after the L4, L5, L7, L8 and L3 plus L114 river insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [790]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 347 now, after the L7, L8 and L3 plus L114 river insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [791]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 322 now, after the L8 and L3 plus L114 river insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [792]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (row 162 now, after the L4 plus L114 river insertions) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [793]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 401 now, after the L4, seal-removal, L5, L7, L8, L3, L01 and L17 plus L114 river insertions). [794]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 318 now, after the L4, L5, L7, L8, L3 and L01 plus L114 river insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [795]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 363 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 plus L114 river insertions). [797]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it. [798]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 350 now, after the L4, L5, L7, L8, L3 and L01 plus L114 river insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [799]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 347 now, after the L7, L8, L3 and L01 plus L114 river insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [800]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 322 now, after the L8, L3 and L01 plus L114 river insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [801]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 401 now, after the L4, seal-removal, L5, L7, L8 and L3 plus L114 river insertions). [802]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 318 now, after the L4, L5, L7, L8 and L3 plus L114 river insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [803]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 363 now, after the L4, seal-removal, L5, L7, L8 and L3 plus L114 river insertions). [805]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it. [806]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 350 now, after the L4, L5, L7, L8 and L3 plus L114 river insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [807]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 347 now, after the L7, L8 and L3 plus L114 river insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [808]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 322 now, after the L8 and L3 plus L114 river insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [809]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (row 162 now, after the L4 plus L114 river insertions) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [810]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 401 now, after the L4, seal-removal, L5, L7, L8, L3, L01 and L17 plus L114 river insertions). [811]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 318 now, after the L4, L5, L7, L8, L3 and L01 plus L114 river insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [812]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 363 now, after the L4, seal-removal, L5, L7, L8, L3 and L01 plus L114 river insertions). [814]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it. [815]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 350 now, after the L4, L5, L7, L8, L3 and L01 plus L114 river insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [816]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 347 now, after the L7, L8, L3 and L01 plus L114 river insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [817]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 322 now, after the L8, L3 and L01 plus L114 river insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [818]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 401 now, after the L4, seal-removal, L5, L7, L8 and L3 plus L114 river insertions). [819]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 318 now, after the L4, L5, L7, L8 and L3 plus L114 river insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [820]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 363 now, after the L4, seal-removal, L5, L7, L8 and L3 plus L114 river insertions). [822]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it. [823]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 350 now, after the L4, L5, L7, L8 and L3 plus L114 river insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [824]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 347 now, after the L7, L8 and L3 plus L114 river insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [825]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 322 now, after the L8 and L3 plus L114 river insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [826]
- The worktree surface's next-move enforcement suite is registered in the integration lane by the same leaf that created it (row 175 at that leaf; row 401 now, after the L4, seal-removal, L5, L7, L8, L3 and `260918-TSIP-L6` plus L114 river insertions). [827]
- The L34 boundary suite is registered in the integration lane by the same leaf that created it (row 132 at that leaf; row 318 now, after the L4, L5, L7, L8, L3 and `260918-TSIP-L6` plus L114 river insertions) — it drives the public checkpoint and closeout operations over real temporary Git repositories. [828]
- The L36 cross-master forcing module is registered in the integration lane by the same leaf that created it (row 143 at that leaf; row 331 now, after the L4, L5, L7, L8, L3 and `260918-TSIP-L6` plus L114 river insertions); it drives two sprint-commanded atomic masters plus the public checkpoint-landing and integration operations over one real temporary Git world. [829]
- The L37 stop boundary suite is registered in the integration lane by the same leaf that created it (row 158 at that leaf; row 363 now, after the L4, seal-removal, L5, L7, L8, L3 and `260918-TSIP-L6` plus L114 river insertions). [830]
- The L37 AST-only architecture guard is registered in architecture-fitness by the same leaf that created it. [831]
- The ordered lifecycle playthrough is registered in the integration lane by the same change set that created it (row 153 at that change set; row 350 now, after the L4, L5, L7, L8, L3 and `260918-TSIP-L6` plus L114 river insertions) — it plays master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf after the landing, over one real temporary Git world. [832]
- The L5 master-link binding suite is registered in the integration lane by the same change set that created it (entry row 347 now, after the L7, L8, L3 and `260918-TSIP-L6` plus L114 river insertions) — it drives the real public `worktree_start` over disposable code and external-memory repositories, so that is its behaviour-preserving lane. [833]
- The L7 capacity-refusal classification suite is registered in the integration lane by the same change set that created it (entry row 322 now, after the L8, L3 and `260918-TSIP-L6` plus L114 river insertions) — it composes the real `QueueFixture` over temporary Git repositories and drives the production graph admission and projection path, so that is its behaviour-preserving lane. [834]




### Cross-Repo References

No cross-repo boundary is crossed by this file.




## Refreshed current evidence

- The new module joins this lane. [19]
- The lane catalog with the host module rows. [21]
- The integration list includes the two reviewer worklist test modules. [240]
- Dependency-facts store controls belong to architecture fitness. [241]
- The bounded Python load-independence scanner belongs to architecture fitness. [242]

- The MIK-R33 row, after the unexplained-lane row and before the artifact-cleanup row. [619]
- The two MIK-R09 rows, after the onboarding-gate row and before the planned-effects row. [620]
- The MIK-R32 row, after the git-trees row and before the artifact-cleanup row. [621]
- The family route condition row, after the Eve protocol row (`:68`). [622]
- The two new rows, the index row they follow and the ingest row after them. [623]
- The two new rows, the validator row they follow and the index row after them. [624]
- The new row between its alphabetical neighbours. [625]
- The three rows and the census row they now follow. [626]
- The two new rows and the row they follow. [627]
- The new row and the row it follows. [628]
- The member-source locator cases' lane row. [629]
- The module's own lane marker. [630]
- The one new row in the unit-regression lane. [631]
- **The new lane row: the explicit-revision-comparison cases, in the unit-regression lane, mid-list in the knowledge run.** [632]
- The lane key the row is a member of. [633]
- The row immediately above the insertion, and the row it displaced. [634]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [635]
- What the module measures: the real comparison over real snapshot pairs plus the adapter's own head-selection function. [636]
- **The new lane row: the source-content cases, in the unit-regression lane, mid-list in the knowledge run.** [637]
- The lane key the row is a member of. [638]
- The row immediately above the insertion, and the row it displaced. [639]
- **The lane headers below the insertion, each one line lower than the previous account recorded.** [640]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [641]
- What the module measures, and why it needs a real repository rather than a stub: the real routes over the real owners, and the independent Git observation every text is asserted against. [642]
- The two catalog consumer rows the same module joined, and the counts they do not move. [643]
- **The new lane row: the durable-comparison-generation cases, in the unit-regression lane, mid-list in the knowledge run.** [644]
- The lane key the row is a member of. [645]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [646]
- The lane key the row is a member of, and the array header it sits inside. [647]
- **The row the merged line adds below this one, and the module it displaced — the second shift the merge applied.** [648]
- Retained unit-regression membership, including the R28 deferred-work and canonical terminal-evidence mapping proofs [651]
- Small actual integration file population [652]
- Retained structural detector classifications [653]
- Provider contract classifications [654]
- The registry retains separate stress-durability and migration lanes. [655]
- L38 registered public activation/admission and route-review transport ownership [656]
- The new parked-candidate suite is registered in the unit-regression lane. [657]
- The manifest still has no default classification for an unregistered test file. [658]
- LOCR-L09 boundary-delivery forcing module registered in the unit lane [659]
- The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. [660]
- The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. [669]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 162) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [670]
- The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. [671]
- **The knowledge block's current membership across all four KS leaves**, whose insertion order is why the rows are not contiguous by leaf. [673]
- The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. [674]
- Retained unit-regression membership, including the R28 deferred-work, canonical terminal-evidence mapping and L23 registration-order proofs [675]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 162) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [684]
- The L23 registration-order proof is registered in the unit-regression lane by the same change set that created it (entry row 288) — it drives the real catalog and sweeper over `tempfile` files with in-process registrar/compactor doubles, so it is hermetic and the default unit lane is its behaviour-preserving classification. [685]
- The L01 steady-state observation suite is registered in the unit-regression lane by the same change set that created it (entry row 256) — it drives the real lifespan finalizer, the real sweeper and the real catalog under a virtual event-loop clock and issues no HTTP request, so the default unit lane is its behaviour-preserving classification. [686]
- The L18 startup-prime proof is registered in the unit-regression lane by the same change set that created it (entry row 258), immediately below its sibling and sharing that sibling's fixture — it drives the real lifespan over a temporary catalog under a virtual clock with no HTTP request and no process, so the default unit lane is its behaviour-preserving classification. [687]
- The integration bracket at the L18 candidate measurement. [688]
- The L06 reviewer-relay proof is registered in the unit-regression lane by the same change set that created it (entry row 159) — it drives the real observer, the production terminal-evidence lift and the real notifier sweep over a temporary coordination root with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. Unlike the L17/L18 insertions this row lands inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate. [689]
- The registry retains separate stress-durability and migration lanes. [690]
- The registry retains separate stress-durability and migration lanes. [691]
- Small actual integration file population [692]
- Retained structural detector classifications [693]
- Provider contract classifications [694]
- L38 registered public activation/admission and route-review transport ownership [695]
- The new parked-candidate suite is registered in the unit-regression lane. [696]
- The manifest still has no default classification for an unregistered test file. [697]
- LOCR-L09 boundary-delivery forcing module registered in the unit lane [698]
- The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. [699]
- The L2 knowledge graph suite is registered in the unit-regression lane by the same change set that created it — all four modules are hermetic (temporary directories, in-process APSW databases, no integration marker, no repository or subprocess), so the default unit lane is each one's behaviour-preserving classification. [708]
- **The knowledge block's current membership across all four KS leaves**, whose insertion order is why the rows are not contiguous by leaf. [710]
- The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. [711]
- Retained unit-regression membership, including the R28 deferred-work, canonical terminal-evidence mapping and L23 registration-order proofs [712]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 162) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [721]
- The L23 registration-order proof is registered in the unit-regression lane by the same change set that created it (entry row 288) — it drives the real catalog and sweeper over `tempfile` files with in-process registrar/compactor doubles, so it is hermetic and the default unit lane is its behaviour-preserving classification. [722]
- The L01 steady-state observation suite is registered in the unit-regression lane by the same change set that created it (entry row 256) — it drives the real lifespan finalizer, the real sweeper and the real catalog under a virtual event-loop clock and issues no HTTP request, so the default unit lane is its behaviour-preserving classification. [723]
- The L18 startup-prime proof is registered in the unit-regression lane by the same change set that created it (entry row 258), immediately below its sibling and sharing that sibling's fixture — it drives the real lifespan over a temporary catalog under a virtual clock with no HTTP request and no process, so the default unit lane is its behaviour-preserving classification. [724]
- The integration bracket at the L18 candidate measurement. [725]
- The L06 reviewer-relay proof is registered in the unit-regression lane by the same change set that created it (entry row 159) — it drives the real observer, the production terminal-evidence lift and the real notifier sweep over a temporary coordination root with no HTTP request, no server and no process, so the default unit lane is its behaviour-preserving classification. Unlike the L17/L18 insertions this row lands inside the unit run above the rows this card cites, which is why every affected citation here was re-derived against the candidate. [726]
- Small actual integration file population [727]
- Retained structural detector classifications [728]
- Provider contract classifications [729]
- The registry retains separate stress-durability and migration lanes. [730]
- L38 registered public activation/admission and route-review transport ownership [731]
- The new parked-candidate suite is registered in the unit-regression lane. [732]
- The manifest still has no default classification for an unregistered test file. [733]
- LOCR-L09 boundary-delivery forcing module registered in the unit lane [734]
- The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. [735]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 162) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [744]
- Small actual integration file population [745]
- Retained structural detector classifications [746]
- Provider contract classifications [747]
- The registry retains separate stress-durability and migration lanes. [748]
- L38 registered public activation/admission and route-review transport ownership [749]
- The new parked-candidate suite is registered in the unit-regression lane. [750]
- The manifest still has no default classification for an unregistered test file. [751]
- LOCR-L09 boundary-delivery forcing module registered in the unit lane [752]
- The checkpoint landing forcing suite is registered in the unit-regression lane by the same leaf that created it. [753]
- The L3 memory-backfill suite is registered in the unit-regression lane by the same change set that created it (entry row 162) — its cases drive the backfill plan and apply paths against disposable `tempfile` repositories without an integration marker, so it is a unit-regression member. [762]
- The lane manifest is fail-closed: an unregistered tracked module makes loading refuse rather than classifying it by default. [763]
- The L4 capsule-and-skill-serving suite is registered in the unit-regression lane by the same change set that created it (entry row 19) — 19 of its 21 cases are hermetic over a disposable coordination root and a synthetic skills corpus and only its two real-process exchanges carry the integration marker, so that is its behaviour-preserving lane. [764]
- **The registered row itself, in the alphabetical knowledge run between the review-surface module and the requirement-reference contract.** [765]
- The lane key the population is counted from, and the key of the next occupied lane after the insertion. [766]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [767]
- The precedent for a `unit-regression` row whose cases really do create Git objects under a temporary root they own. [768]
- **The registered row itself, in the alphabetical knowledge run immediately after the review-surface module and before the source-endpoint module.** [769]
- The lane key the population is counted from, and the key of the next occupied lane after the insertion. [770]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [771]
- The row this insertion displaced by one line, itself a `260921-ICR-L1` mid-list registration. [772]
- **The three registered rows themselves, in the alphabetical knowledge run, and the neighbours they sit between.** [773]
- The lane key the population is counted from, and the key of the next occupied lane after the insertions. [774]
- The modules' own lane declarations, which make the classification their own rather than a budget convenience. [775]
- The row the insertions displaced, itself a mid-list registration. [776]
- The new lane row, directly below the sibling source-content module. [777]
- The new lane row, directly above its graph-projection sibling. [778]
- The new lane row, between its alphabetical neighbours. [779]
- The new lane row, between its alphabetical neighbours. [780]
- The three new lane rows, each directly below its sibling. [781]
- The two L37 rows, after the gate-routes row and before the planned-effects row. [782]
